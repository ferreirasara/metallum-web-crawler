# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class BandInfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Country = scrapy.Field()
    Genre = scrapy.Field()
    Status = scrapy.Field()
    Formed_in = scrapy.Field()
    Lyrical_themes = scrapy.Field()
    Current_label = scrapy.Field()

class BandDyscography(scrapy.Item):
    Title = scrapy.Field()
    Type = scrapy.Field()
    Year = scrapy.Field()

class BandMembers(scrapy.Item):
    Name = scrapy.Field()
    Function = scrapy.Field()
    Status = scrapy.Field()