# -*- coding: utf-8 -*-

import scrapy
from CR.items import Testitem
#titleid, title, name, writer, date

class CryptoSpider(scrapy.Spider):
    name = 'testcrypt'
    start_urls = ["http://gall.dcinside.com/board/lists/?id=bitcoins"]

    def parse(self, response):
        onesets = response.xpath('//tr[@class="tb"]')

        for one in onesets :
            testitem = Testitem()

            if one.xpath('./td[@class="t_notice"]/text()').extract():
                testitem['titleid'] = one.xpath('./td[@class="t_notice"]/text()').extract()[0]
            else :
                testitem['titleid'] = ""

            if one.xpath('./td[@class="t_subject"]/a/text()').extract():
                testitem['title'] = one.xpath('./td[@class="t_subject"]/a/text()').extract()[0]
            else :
                testitem['title'] = ""


            if one.xpath('./td[contains(@class, "t_writer")]/@user_name').extract():
                testitem['writer'] = one.xpath('./td[contains(@class, "t_writer")]/@user_name').extract()[0]
            else :
                testitem['writer'] = ""



            if one.xpath('./td[@class="t_date"]/@title').extract():
                testitem['dateof'] = one.xpath('./td[@class="t_date"]/@title').extract()[0]
            else :
                testitem['dateof'] = ""

            yield testitem
