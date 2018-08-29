# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Sun0769Item


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=240']

    rules = (
        # 没有callback意味着follow为True
        # Rule(LinkExtractor(allow=r'report\?page=\d+'), process_links='deal_links', follow=True),
        # process_links = 函数名, 用来处理返回的链接错误,用函数来处理链接
        Rule(LinkExtractor(allow=r'report\?page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r"/question/\d+/\d+\.shtml"), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print(response.url)

        item = Sun0769Item()
        title = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract_first()
        item['title'] = title.split('\xa0')[0]
        item['num'] = title.split('\xa0')[2].split(':')[-1]
        content = response.xpath("//div[@class='c1 text14_2']//text() |//div[@class='c1 text14_2']/div[@class='contentext']/text() ").extract()
        item['content'] = "".join(content).replace('\xa0', '')
        item['url'] = response.url
        yield item



