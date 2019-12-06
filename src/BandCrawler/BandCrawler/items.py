# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BandcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    genre = scrapy.Field()
    status = scrapy.Field()
    formed_in = scrapy.Field()
    lyrical_themes = scrapy.Field()
    current_label = scrapy.Field()