# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SxewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    user = scrapy.Field()
    datetime = scrapy.Field()
    page_content = scrapy.Field()
    page_link = scrapy.Field()
