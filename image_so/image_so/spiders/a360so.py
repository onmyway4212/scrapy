# -*- coding: utf-8 -*-
import scrapy
import json


class A360soSpider(scrapy.Spider):
    BASE_URL = 'http://image.so.com/zj?ch=beauty&sn=%s&listtype=new&temp=1'
    start_index = 0

    # 限制最大下载数量,防止磁盘用量过大
    MAX_DOWNLOAD_NUM = 1000

    name = '360so'
    start_urls = [BASE_URL % 0]

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        # infos['list']是一个列表, info['qhimg_url']是迭代出所有图片的url地址
        # 提取所有图片下载url到一个列表, 赋给item的'image_urls'字段
        # (图片下载的ImagePipeline的item字段是image_urls或者images)
        yield {
            'image_urls': [info['qhimg_url'] for info in infos['list']]
        }

        # 获取下一页的下载信息.
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(self.BASE_URL % self.start_index)
