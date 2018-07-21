# -*- coding: utf-8 -*-
import scrapy


class GooglescholarSpider(scrapy.Spider):
    name = 'googlescholar'
    allowed_domains = ['scholar.google.com']
    topic='description_logic'
    start_urls = ['https://scholar.google.com.eg/citations?view_op=search_authors&hl=en&mauthors=label:'+topic,]
    
    def getURL(self,Prev_Next_url):
        url=Prev_Next_url
        url=url.replace("\\x3d","=")
        url=url.replace("\\x26","&")
        url=url.replace("&oe=ASCII","")
        url=url.replace("window.location='","https://scholar.google.com.eg")
        url=url.replace("'","")
        return url
    			
    def parse(self, response):
        authors=response.xpath('//*[@class="gsc_1usr gs_scl"]')
        for author in authors:
            name= author.xpath('.//h3[@class="gsc_oai_name"]/a/text()').extract_first()
            link= author.xpath('.//h3[@class="gsc_oai_name"]/a/@href').extract_first()
            aff= author.xpath('.//*[@class="gsc_oai_aff"]/text()').extract_first()
            email= author.xpath('.//*[@class="gsc_oai_eml"]/text()').extract_first()
            citedby=str(author.xpath('.//*[@class="gsc_oai_cby"]/text()').extract_first()).replace('Cited by ', '')
            topics=author.xpath('.//*[@class="gsc_oai_one_int"]/text()').extract()
            yield{'Name':name,'Link':'https://scholar.google.com'+link, 'Affiliation':aff,'Email':str(email).replace('Verified email at ', ''),'CitedBy':str(citedby).replace('Cited by ', ''),'Topics':topics}
			
        Prev_Next =response.xpath("//button[@type='button'][@aria-label='Next']/@onclick").extract()
        if(len(Prev_Next)>0):
            Prev_Next_url=str(Prev_Next[0])
            Prev_Next_url=self.getURL(Prev_Next_url)
            yield scrapy.Request(url=Prev_Next_url, dont_filter=True)
        
            			
			
