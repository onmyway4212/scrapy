# -*- coding: utf-8 -*-
import scrapy
from ..items import CnblogItem


class QiyeSpider(scrapy.Spider):
    name = 'qiye'
    allowed_domains = ['www.cnblogs.com']
    start_urls = [
                  'http://www.cnblogs.com/qiyeboy/default.html?page=2',
                  'http://www.cnblogs.com/qiyeboy/default.html?page=1',
    ]

    def parse(self, response):
        title_list = response.xpath("//div[@class='forFlow']//div[@class='day']")
        for q_item in title_list:
            qy_item = CnblogItem()
            # extract()序列化该节点为Unicode字符串并返回list列表.
            qy_item['publish_time'] = q_item.xpath(".//div[@class='dayTitle']/a/text()").extract_first()
            qy_item['publish_title'] = q_item.xpath(".//div[@class='postTitle']/a/text()").extract_first()
            qy_item['abstract_content'] = q_item.xpath(".//div[@class='postCon']/div[@class='c_b_p_desc']/text()").extract_first()
            qy_item['title_link'] = q_item.xpath(".//div[@class='postTitle']/a/@href").extract_first()
            yield qy_item

        next_link = response.xpath("//div[@class='topicListFooter']/div[@class='pager']/a[7]/@href").extract()
        # 正则表达式版本
        # next_page = Selector(response).re(u'<a href="(\s*)">下一页</a>')
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request(next_link, callback=self.parse)




