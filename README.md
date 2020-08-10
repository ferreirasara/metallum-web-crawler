# metallum-web-crawler

This is a crawler that uses get information about bands from [Metal Archives](https://www.metal-archives.com).

in this project, it was used:
* Python 3.8
* Scrapy 2.3


## To run the crawler:
In `metallum-web-crawler\src\BandCrawler` run:
```
python StartBandCrawler [link]
```

Where `[link]` is the Metal Archives link to a band page.
after crawling the page, the band information will be in `metallum-web-crawler\src\BandCrawler\band.xml`
