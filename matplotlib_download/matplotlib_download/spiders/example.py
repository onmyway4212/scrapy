# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MatplotlibDownloadItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        # LinkExtractor提取网页中所有的链接
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound', deny='/index.html$')
        print(len(le.extract_links(response)))
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_example)

    def parse_example(self, response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        example = MatplotlibDownloadItem()
        # 将所需下载文件的url地址组成的列表赋给item的file_urls字段,就会进行下载
        example['file_urls'] = [url]
        return example


