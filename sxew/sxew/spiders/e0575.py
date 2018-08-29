# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SxewItem


class E0575Spider(CrawlSpider):
    name = 'e0575'
    allowed_domains = ['www.e0575.cn']
    start_urls = ['http://www.e0575.cn/thread.php?fid=13&page=1']

    rule_page = LinkExtractor(allow=r'thread\.php\?fid=\d+&page=\d+')
    rule_content = LinkExtractor(allow=r'read\.php\?tid=\d+$')

    rules = (
        Rule(rule_page, follow=True),
        Rule(rule_content, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = SxewItem()
        response.xpath("//div[@class='tpc_content']/div[@id='read_tpc']/text()").extract_first()
        item['title'] = response.xpath("//div[@class='readTop']//h1/text()").extract_first()
        item['user'] = response.xpath("//div[@class='readName b']//a/text()").extract_first()
        item['datetime'] = response.xpath("//div[@class='tipTop s6']/span[2]/text()").extract_first()
        content = response.xpath("//div[@class='tpc_content']/div[@id='read_tpc']//text()").extract()
        if len(content) == 0:
            item['page_content'] = ''
        else:
            item['page_content'] = ''.join(content).replace('\xa0', '').replace('\n', '')
        item['page_link'] = response.url
        yield item
