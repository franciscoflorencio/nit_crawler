import scrapy


class MscaSpider(scrapy.Spider):
    name = "msca"
    allowed_domains = ["marie-sklodowska-curie-actions.ec.europa.eu"]
    start_urls = ["https://marie-sklodowska-curie-actions.ec.europa.eu/funding"]

    def parse(self, response):
        pass
