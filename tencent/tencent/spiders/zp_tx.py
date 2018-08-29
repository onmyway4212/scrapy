# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem
from scrapy.linkextractors import LinkExtractor


class ZpTxSpider(scrapy.Spider):
    name = 'zp_tx'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?lid=&tid=&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start=0']

    def parse(self, response):
        position_list = response.css("table.tablelist tr:not(:first-child):not(:last-child)")
        for position in position_list:
            item = TencentItem()
            item['job_titile'] = position.css('td.l a::text').extract_first()
            item['link'] = response.urljoin(position.css('td.l a::attr(href)').extract_first())
            item['category'] = position.css('td:nth-child(2)::text').extract_first()
            item['number'] = position.css('td:nth-child(3)::text').extract_first()
            item['place'] = position.css('td:nth-child(4)::text').extract_first()
            item['time'] = position.css('td:nth-child(5)::text').extract_first()
            yield item

        '''
        next_url = response.css('table.tablelist tr.f div.pagenav a:nth-last-child(2)::attr(href)').extract_first()
        if next_url:
            next_page = response.urljoin(next_url)
            yield scrapy.Request(next_page, callback=self.parse)
        '''
        le = LinkExtractor(restrict_css='table.tablelist tr.f div.pagenav a:nth-last-child(2)')
        next_link = le.extract_links(response)
        if next_link:
            next_page = next_link[0].url
            yield scrapy.Request(next_page, callback=self.parse)
