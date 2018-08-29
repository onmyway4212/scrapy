# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 3个文件图片和视频的特殊pipeline在文件的位置D:\Python\Python36\Lib\site-packages\scrapy\pipelines

import scrapy
# get_project_settings的作用是从settings文件中读取设置
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class ImagesPipeline(ImagesPipeline):
    #def process_item(self, item, spider):
    #    return item
    # 获取settings文件里设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imagelink"]
        yield scrapy.Request(image_url)

    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]

        # 把前面的名字改成后面的名字,用昵称命名的名字
        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["nickname"] + ".jpg")

        item["imagePath"] = self.IMAGES_STORE + "/" + item["nickname"]

        return item



