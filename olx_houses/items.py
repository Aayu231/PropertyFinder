# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxHousesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    details = scrapy.Field()
    when = scrapy.Field()
    location = scrapy.Field()
    pass
