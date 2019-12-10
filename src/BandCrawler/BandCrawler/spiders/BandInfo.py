# -*- coding: utf-8 -*-
import scrapy
from BandCrawler.items import BandInfo


class BandinfoSpider(scrapy.Spider):
    name = 'BandInfo'
    def __init__(self, link='', *args, **kwargs):
        allowed_domains = ['metal-archives.com']
        super(BandinfoSpider, self).__init__(*args, **kwargs)
        self.start_urls = [link]

    def parse(self, response):
        name = response.css(".band_name a::text").extract()[0]
        country = response.css("#band_stats dl.float_left dd:nth-child(2) a::text").extract()[0]
        genre = response.css("#band_stats dl.float_right dd:nth-child(2)::text").extract()[0]
        status = response.css("#band_stats dl.float_left dd:nth-child(6)::text").extract()[0]
        formed_in = response.css("#band_stats dl.float_left dd:nth-child(8)::text").extract()[0]
        lyrical_themes = response.css("#band_stats dl.float_right dd:nth-child(4)::text").extract()[0]
        current_label = response.css("#band_stats dl.float_right dd:nth-child(6) a::text").extract()[0]
        
        band = BandInfo(Name=name, Country=country, Genre=genre, Status=status, Formed_in=formed_in, Lyrical_themes=lyrical_themes, Current_label=current_label)
        
        yield band
