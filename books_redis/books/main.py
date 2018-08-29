from scrapy import cmdline
# cmdline.execute('scrapy crawl books_scrape -o books2.csv'.split())
cmdline.execute('scrapy crawl books_scrape'.split())
# cmdline.execute("scrapy crawl books_scrape -o'export_data/%(name)s/%(time)s.csv'".split())
# cmdline.execute("scrapy crawl books_scrape -o %(time)s.csv".split())

'''
%(name)s会被替换为spider的名字
%(time)s会被替换为文件创建时间.
'''