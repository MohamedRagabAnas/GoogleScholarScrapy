# -*- coding: utf-8 -*-
import scrapy


class GscholarSpider(scrapy.Spider):
    name = 'gscholar'
    allowed_domains = ['scholar.google.com']
    Topic='cloud_computing'
    start_urls = ['https://scholar.google.com.eg/citations?view_op=search_authors&hl=en&mauthors=label:'+Topic,]

    def getURL(self,Prev_Next_url):
        url=Prev_Next_url
        url=url.replace("\\x3d","=")
        url=url.replace("\\x26","&")
        url=url.replace("&oe=ASCII","")
        url=url.replace("window.location='","https://scholar.google.com.eg")
        url=url.replace("'","")
        return url

    def parse2(self, response):
        authors=response.xpath('//*[@class="gsc_1usr gs_scl"]')
        for author in authors:
            name= author.xpath('.//h3[@class="gsc_oai_name"]/a/text()').extract_first()
            aff= author.xpath('.//*[@class="gsc_oai_aff"]/text()').extract_first()
            email= author.xpath('.//*[@class="gsc_oai_eml"]/text()').extract_first()
            citedby=author.xpath('.//*[@class="gsc_oai_cby"]/text()').extract_first()
            yield{'Name':name, 'Affiliation':aff, 'email':email,'citedby':citedby}
        
			
    def parse(self, response):
        authors=response.xpath('//*[@class="gsc_1usr gs_scl"]')
        for author in authors:
            name= author.xpath('.//h3[@class="gsc_oai_name"]/a/text()').extract_first()
            aff= author.xpath('.//*[@class="gsc_oai_aff"]/text()').extract_first()
            email= author.xpath('.//*[@class="gsc_oai_eml"]/text()').extract_first()
            citedby=author.xpath('.//*[@class="gsc_oai_cby"]/text()').extract_first()
            yield{'Name':name, 'Affiliation':aff, 'email':email,'citedby':citedby}
        Pre_Next=response.xpath("//button[@type='button']/@onclick").extract_first()
        Prev_Next_url=str(Pre_Next)
        Prev_Next_url=self.getURL(Prev_Next_url)
        yield scrapy.Request(url=Prev_Next_url, callback=self.parse2,dont_filter=True)	
