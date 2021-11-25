from os import write
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import csv 


class MydivSpider(CrawlSpider):
    name = 'myseries'
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@id="main"]/div/span/div/div/div[3]/table/tbody'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1/text()').extract()
        item['date'] = response.xpath('///*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[2]/span/text()').extract()
        item['public'] = response.xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/ul/li[3]/span/text()").extract()
        item['duration'] = response.xpath('//li[@class="ipc-inline-list__item"]/text()').extract()
        item['note'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()').extract()
        item['synopsis'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[1]/text()').extract()
        item['genre'] = response.xpath('//li[@data-testid="storyline-genres"]/div/ul/li/a/text()').extract()
        item['actors'] = response.xpath('//section[@data-testid="title-cast"]/div/div/div/div/a/text()').extract()
        item['Origin language'] = response.xpath('//li[@data-testid="title-details-languages"]/div/ul/li/a/text()').extract()
        item['Origin country'] = response.xpath('//li[@data-testid="title-details-origin"]/div/ul/li/a/text()').extract()
        item['Origin title'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div[2]/div/text()').extract()
        item['number saison'] = response.xpath('//label[@for="browse-episodes-season"]/text()').extract()
        item['number episode'] = response.xpath('//div[@data-testid="episodes-header"]/a/h3/span/text()').extract()



        return item