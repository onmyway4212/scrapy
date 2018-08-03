import scrapy

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['book.douban.com']
    start_rul = [
        'https://book.douban.com/subject_search?search_text=python&cat=1001',
        # 'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/',
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
