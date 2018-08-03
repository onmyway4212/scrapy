# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


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


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.setting.get('MONGO_URI'),
            mongo_db = crawler.setting.get('MONGO_DB')
        )
