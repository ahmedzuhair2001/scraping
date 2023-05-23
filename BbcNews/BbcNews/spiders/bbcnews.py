from urllib import response

import scrapy
from scrapy import item


class BbcnewsSpider(scrapy.Spider):
    name = "bbcnews"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://www.bbc.com/news"]

    def parse(self, response):
        image_urls = response.css('img::attr(src)').getall()
        titles = response.css('.gs-c-promo-heading__title::text').getall()
        content = response.css('p::text').getall()

        for image_url in image_urls:
            yield {
                'image_url': image_url,
                'title': titles,
                'content' : content
            }
