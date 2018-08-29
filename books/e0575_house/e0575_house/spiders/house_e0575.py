# -*- coding: utf-8 -*-
import scrapy


class HouseE0575Spider(scrapy.Spider):
    name = 'house_e0575'
    allowed_domains = ['house.e0575.com']
    start_urls = ['http://house.e0575.com/']

    def parse(self, response):
        pass
