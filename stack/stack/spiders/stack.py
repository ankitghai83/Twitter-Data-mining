import scrapy
from scrapy.spiders import Spider # This will tell the base web page that will on allowed doman for spider to crawl
from scrapy.selector import Selector # Used to capture Xpath that will tell from where to start capturing the  data from XML page

from stack.items import StackItem # import the StackItem class from stack to pull the filed we need to scrap

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="s-post-summary--content"]/h3')
        print("ques:",questions)

        for question in questions:
            print("Question:",question)
            item = StackItem()
            title = question.xpath('a[@class="s-link"]/text()').get(default='No Title Found')
            item['title'] = title
            print("Title:",title)
            item['url']=question.xpath('a[@class="s-link"]/@href').extract()
            yield item




             
