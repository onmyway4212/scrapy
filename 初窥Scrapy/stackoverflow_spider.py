import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }


'''
Scrapy首先读取定义在 start_urls 属性中的URL(在本示例中，就是StackOverflow的top question页面的URL)， 创建请求，并且将接收到的
response作为参数调用默认的回调函数 parse ，来启动爬取。 在回调函数 parse 中，我们使用CSS Selector来提取链接。接着，我们产生
(yield)更多的请求， 注册 parse_question 作为这些请求完成时的回调函数。
'''