# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoticesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass 

class CnpqItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    deadline = scrapy.Field()
    link = scrapy.Field()

class MarieCurieItem(scrapy.Item):
    title = scrapy.Field()
    status = scrapy.Field()
    deadline = scrapy.Field()
    link = scrapy.Field()

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
