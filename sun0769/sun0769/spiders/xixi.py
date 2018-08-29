# -*- coding: utf-8 -*-
import scrapy
from ..items import Sun0769Item


class XixiSpider(scrapy.Spider):
    name = 'xixi'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    url = 'http://wz.sun0769.com/index.php/question/report?page='
    start_urls = [url + str(offset)]

    def parse_link(self, response):
        links = response.xpath("//table[@width='98%']//tr//a[2]//@href").extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse)

        if self.offset < 126100:
            self.offset += 30
            yield scrapy.Request((self.url+str(self.offset)), callback=self.parse_link)

    def parse(self, response):
        item = Sun0769Item()
        title = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract_first()
        item['title'] = title.split('\xa0')[0]
        item['num'] = title.split('\xa0')[2].split(':')[-1]
        content = response.xpath("//div[@class='c1 text14_2']//text() |//div[@class='c1 text14_2']/div[@class='contentext']/text() ").extract()
        item['content'] = "".join(content).replace('\xa0', '')
        item['url'] = response.url
        yield item
