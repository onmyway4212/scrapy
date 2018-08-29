# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import Item
from .settings import mongo_host, mongo_db_name, mongo_port, mongo_db_collection
import sqlite3
import pymysql
import pymongo
import redis


class QuotesPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['wisdom']:
            if len(item['wisdom']) > self.limit:
                item['wisdom'] = item['wisdom'][0:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Miss Text')


# mongo数据库
class MongoPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item


# SQLite3数据库
class SQLitePipeline(object):
    def open_spider(self, spider):
        # get的第二个参数是一个默认的数据库,如果settings中没有指定SQLITE_DB_NAME,就会使用默认的数据库
        db_name = spider.settings.get('SQLITE_DB_NAME', 'quotes.db')

        self.db_conn = sqlite3.connect(db_name)
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)

        return item

    def insert_db(self, item):
        values = (
            item['wisdom'],
            item['celebrity'],
            item['tags'],
        )
        sql = 'INSERT INTO famous VALUES(?,?,?)'
        self.db_cur.execute(sql, values)
        self.db_conn.commit()


# mysql数据库
class MySQLPipeline(object):
    def open_spider(self, spider):
        # get的第二个参数是一个默认的数据库,如果settings中没有指定SQLITE_DB_NAME,就会使用默认的数据库
        db_name = spider.settings.get('MYSQL_DB_NAME', 'quotes')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'root')

        self.db_conn = pymysql.connect(host=host, port=port, db=db_name, user=user, passwd=passwd)
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)

        return item

    def insert_db(self, item):
        values = (
            item['wisdom'],
            item['celebrity'],
            item['tags'],
        )
        sql = 'INSERT INTO famous VALUES(%s,%s,%s)'
        self.db_cur.execute(sql, values)
        self.db_conn.commit()


# redis数据库
class RedisPipeline(object):
    # 建立数据库链接,将得到的对象赋值给self.db_conn
    def open_spider(self, spider):
        db_host = spider.settings.get('REDIS_HOST', 'localhost')
        db_port = spider.settings.get('REDIS_PORT', 6379)
        db_index = spider.settings.get('REDIS_DB_INDEX', 0)

        self.db_conn = redis.StrictRedis(host=db_host, port=db_port, db=db_index)
        self.item_i = 0

    # 方法在爬去完全部数据后被调用,关闭与数据库的链接
    def close_spider(self, spider):
        self.db_conn.connection_pool.disconnect()

    # 处理爬去到的每一项数据,调用insert_db()方法
    def process_item(self, item, spider):
        self.insert_db(item)

        return item

    # 将一项数据转化为字典,然后调用hmset方法将数据以hash类型存入redis数据库
    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)

        self.item_i += 1
        self.db_conn.hmset('book:%s' % self.item_i, item)
