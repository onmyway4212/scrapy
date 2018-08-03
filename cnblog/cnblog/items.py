# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    publish_time = scrapy.Field()
    publish_title = scrapy.Field()
    abstract_content = scrapy.Field()
    title_link = scrapy.Field()


