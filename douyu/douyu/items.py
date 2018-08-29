# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # 主播昵称
    nickname = scrapy.Field()
    # 图片地址
    imagelink = scrapy.Field()
    # 保存路径
    imagePath = scrapy.Field()
    #pass
