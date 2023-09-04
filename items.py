# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SlackscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SlackAppItem(scrapy.Item):
    category = scrapy.Field()
    ranking = scrapy.Field()
    app_name = scrapy.Field()
    app_description = scrapy.Field()
    scraped_date = scrapy.Field()
