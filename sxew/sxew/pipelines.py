# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs


class E0575Pipeline(object):
    def __init__(self):
        self.filename = codecs.open("ew.json", "w", encoding='utf-8')

    def process_item(self, item, spider):
        # 如果没有ensure_ascii=False,输出的是中文的ascii码.加上ensure_ascii=False,输出的是中文.
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.close()