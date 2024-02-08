import scrapy
import w3lib


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        author_name = response.xpath('//span[@class="author-name"]/text()').get()
        subheading = response.xpath('//span[@class="subheading"]/text()').get()
        text = w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        return {"title": title,
                "author name": author_name,
                "subheading": subheading,
                "text": text}
        
