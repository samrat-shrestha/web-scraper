"Project created to learn some basic web scraping using Scrapy.

#NOTE: (Some Commands)
    scrapy startproject project_name
    scrapy genspider name_of_spider_file site_to_scrape
    scrapy runspider spider_file
    scrapy runspider spider_file -o output_file.csv -t csv -s CLOSESPIDER_PAGECOUNT=3
    scrapy runspider spider_file -s FEED_URI='output_file.csv' -s FEED_FORMAT='csv'" 
