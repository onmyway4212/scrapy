# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/profile?_next=/places/default/index']

    def parse(self, response):
        keys = response.css('table label::text').re('(.+):')
        values = response.css('table td.w2p_fw::text').extract()
        yield dict(zip(keys, values))

    login_url = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'

    def start_requests(self):
        yield Request(self.login_url, callback=self.login)

    def login(self, response):
        fd = {
            'email': '88186161@qq.com',
            'password': 'zh12345',
        }
        yield FormRequest.from_response(response, formdata=fd, callback=self.parse_login)

    def parse_login(self, response):
        if '飞' in response.text:
            yield from super().start_requests()