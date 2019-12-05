# -*- coding: utf-8 -*-
import scrapy


class BanddiscographySpider(scrapy.Spider):
    name = 'BandDiscography'
    allowed_domains = ['metal-archives.com']
    start_urls = ['http://metal-archives.com/']

    def parse(self, response):
        pass
