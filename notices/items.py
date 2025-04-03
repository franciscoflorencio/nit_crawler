# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CnpqItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    deadline = scrapy.Field()
    link = scrapy.Field()

class EacItem(scrapy.Item):
    title = scrapy.Field()
    day_deadline = scrapy.Field()
    time_deadline = scrapy.Field()
    deadline = scrapy.Field()
    link = scrapy.Field()

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    
class FaperjItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()

class UkriItem(scrapy.Item):
    title = scrapy.Field()
    opportunity_link = scrapy.Field()
    opportunity_status = scrapy.Field()
    funders = scrapy.Field()
    funders_url = scrapy.Field()
    funding_type = scrapy.Field()
    total_fund = scrapy.Field()
    award_range = scrapy.Field()
    publication_date = scrapy.Field()
    opening_date = scrapy.Field()
    closing_date = scrapy.Field()

class DaadItem(scrapy.Item):
    title = scrapy.Field()
    observation = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()

class FinepItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    deadline = scrapy.Field()
    date = scrapy.Field()

class FapespItem(scrapy.Item):
    title = scrapy.Field()
    institution = scrapy.Field()
    city = scrapy.Field()
    deadline = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    
