import scrapy
from scrapy.spiders import Spider # This will tell the base web page that will on allowed doman for spider to crawl
from scrapy.selector import Selector # Used to capture Xpath that will tell from where to start capturing the  data from XML page

from stack.items import StackItem # import the StackItem class from stack to pull the filed we need to scrap


class ExampleSpider(Spider):
    name = "stack" # Name of the spider
    allowed_domains = ["stackoverflow.com"] # Base url for the allowed domain for spider to crawl
    start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"] # scrapy starts crawling from here

    def parse(self, response):
        questions=Selector(response).xpath('//div[@class="s-post-summary--content"]/h3')

        for question in questions:
            item=StackItem()
            item['title']=question.xpath('a[@class="s-post-summary--content-title"]/text()').extract()[0]
            item['url=']=question.xpath('a[@class="s-post-summary--content-title"]/href').extract()[0]
            yield item

#We are iterating through the `questions` and assigning the `title` and `url` values from the scraped data. Be sure to test out the
#  XPath selectors in the JavaScript Console within Chrome Developer Tools - e.g., `$x('//div[@class="summary"]/h3/a[@class="question-hyperlink"]/text()')` and `$x('//div[@class="summary"]/h3/a[@class="question-hyperlink"]/@href')`.



## Test : Ready for the first test? Simply run the following command within the "stack" directory:



             
