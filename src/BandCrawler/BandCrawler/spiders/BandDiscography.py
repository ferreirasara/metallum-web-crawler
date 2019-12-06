# -*- coding: utf-8 -*-
import scrapy
from BandCrawler.items import BandDyscography


class BanddiscographySpider(scrapy.Spider):
    name = 'BandDiscography'
    allowed_domains = ['metal-archives.com']
    start_urls = ['http://metal-archives.com/']

    def parse(self, response):
        main = ''
        lives = ''
        demos = ''
        misc = ''

        discography = BandDyscography(main=main, lives=lives, demos=demos, misc=misc)

        yield discography
