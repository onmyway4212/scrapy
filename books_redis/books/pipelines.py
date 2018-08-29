# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class BooksPipeline(object):
    def process_item(self, item, spider):
        return item


# 过滤重复数据,把书名相同的过滤掉
class DuplicatesPipeline(object):

    def __init__(self):
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['book_title']
        if name in self.book_set:
            raise DropItem("Duplicate book found:%s" %item)

        self.book_set.add(name)
        return item