# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Tx2Item


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?lid=&tid=&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start=0']

    rules = (
        Rule(LinkExtractor(allow=("start=\d+")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        position_list = response.css("table.tablelist tr:not(:first-child):not(:last-child)")
        for position in position_list:
            item = Tx2Item()
            item['job_titile'] = position.css('td.l a::text').extract_first()
            item['link'] = response.urljoin(position.css('td.l a::attr(href)').extract_first())
            item['category'] = position.css('td:nth-child(2)::text').extract_first()
            item['number'] = position.css('td:nth-child(3)::text').extract_first()
            item['place'] = position.css('td:nth-child(4)::text').extract_first()
            item['time'] = position.css('td:nth-child(5)::text').extract_first()
            yield item
