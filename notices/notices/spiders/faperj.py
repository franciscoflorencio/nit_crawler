import scrapy


class FaperjSpider(scrapy.Spider):
    name = "faperj"
    allowed_domains = ["www.faperj.br"]
    start_urls = ["https://www.faperj.br/?id=28.5.7"]

    def parse(self, response):
        pass
