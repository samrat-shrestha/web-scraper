import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from article_scraper.items import Article

class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Kevin_Bacon"]

    #This defines the rule for crawling the web page. Defined regex in the link extractor to browse any pages with /wiki/... and skip pages with /wiki/:... 
    #follow param means that we have specified to crawl the pages until we run at the end of the site.
    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)]

    #Any settings we want to override for this specific spider from the ones we specify in the settings.py file.
    custom_settings = {
        'FEED_URI' : 'articles.xml',
        'FEED_FORMAT' : 'xml'
    }

    def parse_info(self, response):
        article = Article()
        article['title'] = response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get(),
        article['url'] = response.url,
        article['last_edited'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()     
        
        return article
