# -*- coding: utf-8 -*-

import scrapy


class Crypitem(scrapy.Item):
    siteTitle = scrapy.Field()
    siteKeywords = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    replyUrl = scrapy.Field()
    replauthor = scrapy.Field()
    replcontext = scrapy.Field()


class CryptoSpider(scrapy.Spider):
    name = 'subcrypt'
    start_urls = ["https://www.reddit.com/r/CryptoCurrency/"]


    def parse(self, response):

        siteTitle = response.xpath('//head/title/text()').extract()[0]

        siteKeywords = response.xpath('//head/meta[contains(@name,"keyword")]/@content').extract()[0].split(',')
        for keyword in siteKeywords:
            siteKeywords[siteKeywords.index(keyword)] = keyword.strip()

        top = response.xpath('//div[@class="top-matter"]')

        for topList in top :
            # title = topList.css("p.title>a.title::text").extract()[0]
            title = topList.xpath('//p[@class="title"]/a[@class="title"]/text()').extract()[0]

            href = topList.css('p.title>a::attr(href)').extract()[0]
            if href[1] == 'r':
                url = 'https://www.reddit.com' + href
            else:
                url = href

            replyUrl = response.xpath('//li[@class="first"]/a/@href').extract()[0]


            crypitem = Crypitem()

            crypitem['siteTitle'] = siteTitle
            crypitem['siteKeywords'] = siteKeywords
            crypitem['title'] = title
            crypitem['url'] = url
            crypitem['replyUrl'] = replyUrl


            yield scrapy.Request(url = replyUrl, callback=self.parse_reply, meta={'item' : crypitem })


    def parse_reply(self, response):

        crypitem = response.meta['item']

        replys = response.xpath('//div[@class="sitetable nestedlisting"]//div[@class="entry unvoted"]')
        # replText = response.xpath('//form[@class="usertext warn-on-unload"]')
        # 위와같이하면 오른쪽 사이드바까지 포함되면서 지나치게 쓸데없이 많은 내용들이 포함되더라
        # sitetable nestedlisting은 하나다. 굿
        replTexts = response.xpath('//div[@class="sitetable nestedlisting"]//form[@class="usertext warn-on-unload"]')

        for reply in replys:
            author = reply.xpath('.//p[@class="tagline"]/a[contains(@class,"author")]/text()').extract()
            context = reply.xpath('.//form[@class="usertext warn-on-unload"]//div[@class="md"]/p/text()').extract()

            crypitem['replauthor'] = author
            crypitem['replcontext'] = context

            yield crypitem
