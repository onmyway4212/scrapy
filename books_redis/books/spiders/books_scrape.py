# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import BooksItem
from scrapy.linkextractor import LinkExtractor


class BooksScrapeSpider(RedisSpider):
    name = 'books_scrape'
    allowed_domains = ['books.toscrape.com']
    # start_urls = [
    #     'http://books.toscrape.com',
    #     'http://books.toscrape.com/catalogue/page-2.html', ]

    def parse(self, response):
        book_list = response.xpath("//ol[@class='row']//li")
        for books in book_list:
            book_message = BooksItem()
            book_message['book_title'] = books.xpath('.//h3/a/@title').extract_first()
            book_message['price'] = books.xpath(".//div[@class='product_price']/p/text()").extract_first()
            book_message['book_link'] = 'http://books.toscrape.com/' + books.xpath(
                "./article/div/a/@href").extract_first()
            yield book_message
        '''
        # 使用selector提取下一页的链接
        next_url = response.xpath("//ul[@class='pager']/li[@class='next']/a/@href").extract()
        if next_url:
            next_page = response.urljoin(next_url[0])
            yield scrapy.Request(next_page, callback=self.parse)
        '''

        # 使用linkExtractor提取下一页的链接
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)
