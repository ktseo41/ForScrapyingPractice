# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'cryptoReddit'
    start_urls = ["https://www.reddit.com/r/CryptoCurrency/"]


    def fullitem(scrapy.Item):
        siteTitle = scrapy.Field()
        siteKeywords = scrapy.Field()
        title = scrapy.Field()
        url = scrapy.Field()
        replyAuthor = scrapy.Field()
        replyContext = scrapy.Field()


    def parse(self, response):

        # 사이트 페이지 타이틀
        siteTitle = response.css('head>title::text').extract()[0]

        # keyword, 사이트 자체 이름 찾기 위해.
        # 어떤 사이트에 keyword가 없으면?
        # siteKeywords = response.css('head>meta[name*=keyword]::attr(content)').extract()[0].split(',')
        siteKeywords = response.xpath('//head/meta[contains(@name,"keyword")]/@content').extract()[0].split(',')
        for keyword in siteKeywords:
            siteKeywords[siteKeywords.index(keyword)] = keyword.strip()

        top = response.xpath('//div[@class="top-matter"]')

        for topList in top :
            # 게시글 제목
            # 사이트마다 다를 것인데 어떻게 해야?
            title = topList.css("p.title>a.title::text").extract()[0]

            # 링크 따기 위해서
            href = topList.css('p.title>a::attr(href)').extract()[0]

            # href 를 url화 시키기, 레딧의 경우 레딧이 아니면 전체 주소가 나온다.
            if href[1] == 'r':
                url = 'https://www.reddit.com' + href
            else:
                url = href

            # replyurl 따오기, 왠일인지 href가 url이다.
            replyUrl = response.xpath('//li[@class="first"]/a/@href').extract()[0]

            # replyUrl is not None이 아니라 무조건 새로 parsing을 하게 해야할 것 같기는 하다.
            # 여기서 다해버리는 것은 새로운 url로 들어가야 하는 것이라서 안된다.
            # 아래처럼 Request를 할 때 인자들을 이런 식으로 넘기는 것은 안된다.
            # 왜냐면 이런 기능은 없음. item으로 만들어서 넘겨야하는 것 같다.
"""
            if replyUrl is not None:
                scrapy.Request(url = replyUrl, callback=self.parse_reply, siteTitle, siteKeywords, title, url)
"""

            # yield {'siteTitle' : siteTitle,
            # 'siteKeywords' : siteKeywords, 'title' : title, 'url' : url}



    def parse_reply(self, response):

        replys = response.xpath('//div[@class="sitetable nestedlisting"]//div[@class="entry unvoted"]')
        # replText = response.xpath('//form[@class="usertext warn-on-unload"]')
        # 위와같이하면 오른쪽 사이드바까지 포함되면서 지나치게 쓸데없이 많은 내용들이 포함되더라
        # sitetable nestedlisting은 하나다. 굿
        replTexts = response.xpath('//div[@class="sitetable nestedlisting"]//form[@class="usertext warn-on-unload"]')

        for reply in replys:
            author = reply.xpath('.//p[@class="tagline"]/a[contains(@class,"author")]/text()').extract()
            context = reply.xpath('.//form[@class="usertext warn-on-unload"]//div[@class="md"]/p/text()').extract()
