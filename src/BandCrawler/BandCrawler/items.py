# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BandInfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    genre = scrapy.Field()
    status = scrapy.Field()
    formed_in = scrapy.Field()
    lyrical_themes = scrapy.Field()
    current_label = scrapy.Field()

class BandDyscography(scrapy.Item):
    main = scrapy.Field()
    lives = scrapy.Field()
    demos = scrapy.Field()
    misc = scrapy.Field()

class BandMembers(scrapy.Item):
    current = scrapy.Field()
    past = scrapy.Field()