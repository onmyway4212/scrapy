# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotesItem


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            saying = QuotesItem()
            saying['wisdom'] = quote.css('.text::text').extract_first()
            saying['celebrity'] = quote.css('.author::text').extract_first()
            content = quote.css('.tags .tag::text').extract()
            saying['tags'] = '/'.join(content)
            yield saying

        next_page = response.css('.pager .next a::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request('http://quotes.toscrape.com'+next_page, callback=self.parse)
