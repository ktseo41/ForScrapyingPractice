# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Crypitem(scrapy.Item):
    siteTitle = scrapy.Field()
    siteKeywords = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    titleTime = scrapy.Field()
    replyUrl = scrapy.Field()
    replauthor = scrapy.Field()
    replcontext = scrapy.Field()
    replTime = scrapy.Field()

class CrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
