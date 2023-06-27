import scrapy
import w3lib

# xpath selectors:
# /html/body/div/h1
# //h1
# //div/h1
# //div//h1
# //span[@class="title"]/text()
# //span[@class="title"]/@id

class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        # title = response.css('span.title::text').get()
        # title = response.xpath('//span[@class="title"]/text()').get()
        title = response.xpath('//meta[@name="DC.Title"]/@content').get()
        author_name = response.xpath('//span[@class="author-name"]/text()').get()
        author_cmpny = response.xpath('//span[@class="author-company"]/text()').get()
        author_date = response.xpath('//span[@class="date"]/text()').get()
        text = w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        address = response.xpath('//span[@class="address"]/text()').get()
        phone = response.xpath('//span[@class="phone"]/text()').get()
        email = response.xpath('//span[@class="email"]/text()').get()
        return {"title": title, "author_name": author_name, "author_cmpny": author_cmpny, "author_date": author_date, "text": text, "address": address, "phone": phone, "email": email}
