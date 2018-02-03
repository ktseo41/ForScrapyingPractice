# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'cryptoReddit'
    start_urls = ["https://www.reddit.com/r/CryptoCurrency/"]


    def parse(self, response):
        top = response.css('div.top-matter')
        # 사이트 페이지 타이틀
        siteTitle = response.css('head>title::text').extract()[0]

        # 사이트 자체 이름 찾기 위해.
        # keyword가 없으면?
        siteKeywords = response.css('head>meta[name*=keyword]::attr(content)').extract()[0].split(',')
        for keyword in siteKeywords:
            siteKeywords[siteKeywords.index(keyword)] = keyword.strip()


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

            yield {'siteTitle' : siteTitle,
            'siteKeywords' : siteKeywords, 'title' : title, 'url' : url}
