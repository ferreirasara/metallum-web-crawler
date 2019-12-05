# -*- coding: utf-8 -*-
import scrapy


class BandinfoSpider(scrapy.Spider):
    name = 'BandInfo'
    allowed_domains = ['metal-archives.com']
    start_urls = ['http://metal-archives.com/']

    def parse(self, response):
        pass
