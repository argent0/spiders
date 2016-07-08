# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    attribution = scrapy.Field()
    snippet = scrapy.Field()
    classification = scrapy.Field()
    flags = scrapy.Field()
    retrivalTime = scrapy.Field()
