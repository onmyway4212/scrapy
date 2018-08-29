from scrapy import cmdline
# cmdline.execute('scrapy crawl dmoz'.split())
cmdline.execute('scrapy runspider myspider_redis.py'.split())