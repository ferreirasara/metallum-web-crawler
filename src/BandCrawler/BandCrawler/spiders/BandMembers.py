# -*- coding: utf-8 -*-
import scrapy
from BandCrawler.items import BandMembers


class BandmembersSpider(scrapy.Spider):
    name = 'BandMembers'
    allowed_domains = ['metal-archives.com']
    start_urls = ['https://www.metal-archives.com/bands/Gormathon/3540310947']

    def parse(self, response):
        current = response.css("#band_tab_members_current div table tr a::text").extract()
        past = []

        members = BandMembers(current=current, past=past)
        yield members