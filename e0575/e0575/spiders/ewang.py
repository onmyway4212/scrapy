# -*- coding: utf-8 -*-
import scrapy
from .. import items
'''
//*[@id="threadlist"]
.//table[@class='z']//tbody[@id='threadlist']
'''

class EwangSpider(scrapy.Spider):
    name = 'ewang'
    allowed_domains = ['www.e0575.cn']
    start_urls = ['http://www.e0575.cn/thread.php?fid=187']

    def parse(self, response):
        title_list = response.xpath("//*[@id='threadlist']/tr")
        for item in title_list:
            e0575_item = items.E0575Item()
            e0575_item['title'] = item.xpath(".//td[2]/a/text()").extract_first()
            e0575_item['author'] = item.xpath(".//td[3]/a/text()").extract_first()
            e0575_item['publish_time'] = item.xpath("//td[3]/p/text()").extract_first()
            e0575_item['replay'] = item.xpath(".//td[4]/text()").extract_first()
            e0575_item['last_author'] = item.xpath(".//td[5]/a/text()").extract_first()
            if item.xpath(".//td[2]/a/@href").extract_first():
                e0575_item['link'] = 'http://www.e0575.cn/' + item.xpath(".//td[2]/a/@href").extract_first()
            else:
                e0575_item['link'] = item.xpath(".//td[2]/a/@href").extract_first()

            yield e0575_item

        next_link = response.xpath(".//*[@id='c']/div[5]/div/div/a[@class='pages_next']/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("http://www.e0575.cn/" + next_link, callback=self.parse)




