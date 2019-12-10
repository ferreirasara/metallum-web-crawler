import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

link = sys.argv[1]
id_band = link.split('/')[5]
link_discography = 'https://www.metal-archives.com/band/discography/id/' + id_band + '/tab/all'

process.crawl('BandInfo', link)
process.crawl('BandMembers', link)
process.crawl('BandDiscography', link_discography)
process.start()