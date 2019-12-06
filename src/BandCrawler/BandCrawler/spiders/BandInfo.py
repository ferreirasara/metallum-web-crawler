# -*- coding: utf-8 -*-
import scrapy
from BandCrawler.items import BandcrawlerItem


class BandinfoSpider(scrapy.Spider):
    name = 'BandInfo'
    allowed_domains = ['metal-archives.com']
    start_urls = ['https://www.metal-archives.com/bands/Gormathon/3540310947'] # test with Gormathon band

    def parse(self, response):
        name = response.css(".band_name a::text").extract()
        country = response.css("#band_stats dl.float_left dd:nth-child(2) a::text").extract()
        genre = response.css("#band_stats dl.float_right dd:nth-child(2)::text").extract()
        status = response.css("#band_stats dl.float_left dd:nth-child(6)::text").extract()
        formed_in = response.css("#band_stats dl.float_left dd:nth-child(8)::text").extract()
        lyrical_themes = response.css("#band_stats dl.float_right dd:nth-child(4)::text").extract()
        current_label = response.css("#band_stats dl.float_right dd:nth-child(6) a::text").extract()
        
        band = BandInfo(name=name, country=country, genre=genre, status=status, formed_in=formed_in, lyrical_themes=lyrical_themes, current_label=current_label)
        
        yield band
