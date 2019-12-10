import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

if len(sys.argv) != 2:
    print("Invalid number of arguments")
else:
    link = sys.argv[1]

process.crawl('BandSpider', link)
process.start()