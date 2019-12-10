# -*- coding: utf-8 -*-
import scrapy
from BandCrawler.items import BandMembers


class BandmembersSpider(scrapy.Spider):
    name = 'BandMembers'
    def __init__(self, link='', *args, **kwargs):
        allowed_domains = ['metal-archives.com']
        super(BandmembersSpider, self).__init__(*args, **kwargs)
        self.start_urls = [link]

    def parse(self, response):
        for td in response.css("#band_tab_members_current div table tr.lineupRow"):
            name = td.css("a.bold::text").extract()[0]
            function = td.css("td::text").extract()[2].replace('\xa0', '').strip()
            status = 'Current'
            member = BandMembers(Name=name, Function=function, Status=status)
            yield member
        for td in response.css("#band_tab_members_past div table tr.lineupRow"):
            name = td.css("a.bold::text").extract()[0]
            function = td.css("td::text").extract()[2].replace('\xa0', '').strip()
            status = 'Past'
            member = BandMembers(Name=name, Function=function, Status=status)
            yield member