# -*- coding: utf-8 -*-
import scrapy


class AuthorpageSpider(scrapy.Spider):
    name = 'authorPage'
    allowed_domains = ['scholar.google.com']
    start_urls = ['http://scholar.google.com/citations?user=zqzNbPIAAAAJ']

    def parse(self, response):
        name=response.xpath('//*[@id="gsc_prf_in"]/text()').extract_first()
        print '\n'
        print name
        print '\n'

        yield{'Name':name}
