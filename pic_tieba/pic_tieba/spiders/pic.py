# -*- coding: utf-8 -*-
import scrapy


class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5821155632']

    def parse(self, response):
        pic_list = response.xpath("//img[@class='BDE_Image']/@src").extract()
        yield {
            'image_urls': [info for info in pic_list]
        }

        next_page = response.css("div#thread_theme_7 li.pb_list_pager a:nth-last-child(2)::attr(href)").extract()
        if next_page:
            next_url = response.urljoin(next_page[0])
            yield scrapy.Request(next_url, callback=self.parse)

