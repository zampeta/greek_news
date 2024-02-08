import scrapy


class TitlesSpider(scrapy.Spider):
    name = "titles"
    allowed_domains = ["kathimerini.gr"]
    start_urls = ["https://kathimerini.gr"]

    def parse(self, response):
        side_title = response.xpath('//*[@class="title is-2 medium_title nx-title"]/text()').get()
        return {'side title': side_title}
