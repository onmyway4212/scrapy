from scrapy import cmdline
cmdline.execute('scrapy crawl quotes_spider -o quotes.json'.split())