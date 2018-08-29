# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tx2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_titile = scrapy.Field()
    category = scrapy.Field()
    number = scrapy.Field()
    place = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()
