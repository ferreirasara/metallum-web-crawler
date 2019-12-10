# -*- coding: utf-8 -*-
import scrapy
from BandCrawler.items import BandDyscography


class BanddiscographySpider(scrapy.Spider):
    name = 'BandDiscography'
    def __init__(self, link='', *args, **kwargs):
        allowed_domains = ['metal-archives.com']
        super(BanddiscographySpider, self).__init__(*args, **kwargs)
        self.start_urls = [link]

    def parse(self, response):
        for td in response.css("tr"):
            title = td.css("td a::text").extract()
            disc_type = td.css("td:nth-child(2)::text").extract()
            year = td.css("td:nth-child(3)::text").extract()

            if (len(title) != 0):
                discography = BandDyscography(Title=title[0], Type=disc_type[0], Year=year[0])
                yield discography
