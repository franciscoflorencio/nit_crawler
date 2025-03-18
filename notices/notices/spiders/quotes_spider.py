import scrapy
from notices.items import QuoteItem
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'https://quotes.toscrape.com/js/'
        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('span small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall() 
            yield quote_item
