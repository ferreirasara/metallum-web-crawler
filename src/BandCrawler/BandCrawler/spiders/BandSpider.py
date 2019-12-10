# -*- coding: utf-8 -*-
import scrapy
from BandCrawler.items import BandInfo, BandMembers, BandDiscography

class BandSpider(scrapy.Spider):
    name = 'BandSpider'
    def __init__(self, link='', *args, **kwargs):
        allowed_domains = ['metal-archives.com']
        super(BandSpider, self).__init__(*args, **kwargs)
        id_band = link.split('/')[5]
        link_discography = 'https://www.metal-archives.com/band/discography/id/' + id_band + '/tab/all'
        self.start_urls = [link, link_discography]

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], self.parseInfo)
        yield scrapy.Request(self.start_urls[1], self.parseDisco)

    def parseInfo(self, response):
        name = response.css(".band_name a::text").extract()[0]
        country = response.css("#band_stats dl.float_left dd:nth-child(2) a::text").extract()[0]
        genre = response.css("#band_stats dl.float_right dd:nth-child(2)::text").extract()[0]
        status = response.css("#band_stats dl.float_left dd:nth-child(6)::text").extract()[0]
        formed_in = response.css("#band_stats dl.float_left dd:nth-child(8)::text").extract()[0]
        lyrical_themes = response.css("#band_stats dl.float_right dd:nth-child(4)::text").extract()[0]
        current_label = response.css("#band_stats dl.float_right dd:nth-child(6) a::text").extract()[0]
        members = []
        for td in response.css("#band_tab_members_current div table tr.lineupRow"):
            name = td.css("a.bold::text").extract()[0]
            function = td.css("td::text").extract()[2].replace('\xa0', '').strip()
            status = 'Current'
            member = BandMembers(Name=name, Function=function, Status=status)
            members.append(member)

        for td in response.css("#band_tab_members_past div table tr.lineupRow"):
            name = td.css("a.bold::text").extract()[0]
            function = td.css("td::text").extract()[2].replace('\xa0', '').strip()
            status = 'Past'
            member = BandMembers(Name=name, Function=function, Status=status)
            members.append(member)
        band = BandInfo(Name=name, Country=country, Genre=genre, Status=status, Formed_in=formed_in, Lyrical_themes=lyrical_themes, Current_label=current_label)
        
        yield {"Info":band, "Members":members}
    
    def parseDisco(self, response):
        discography_list = []
        for td in response.css("tr"):
            title = td.css("td a::text").extract()
            disc_type = td.css("td:nth-child(2)::text").extract()
            year = td.css("td:nth-child(3)::text").extract()

            if (len(title) != 0):
                discography = BandDiscography(Title=title[0], Type=disc_type[0], Year=year[0])
                discography_list.append(discography)
                
        yield {"Discography":discography_list}