# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor


class WowSpider(scrapy.Spider):
    name = 'wow'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%AD%94%E5%85%BD%E4%B8%96%E7%95%8C/66392']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths="//div[@class='content-wrapper']")
        links = le.extract_links(response)
        for each in links:
            print(each.url)
