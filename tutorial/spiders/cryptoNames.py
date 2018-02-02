# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'cryptoNames'
    start_urls = ["https://coinmarketcap.com/"]


    def parse(self, response):

        next_page = response.css('ul[class="pagination top-paginator"]>li:contains("Next") a::attr(href)').extract()[0]
        currencyNames = response.css('td[class="no-wrap currency-name"]')

        for currencyname in currencyNames:
            symbol = currencyname.css('span[class="currency-symbol"]>a::text').extract()[0]
            nameOfCurrency = currencyname.css('a.currency-name-container::text').extract()[0]

            yield {
                'symbol' : symbol,
                'name' : nameOfCurrency,
                symbol : nameOfCurrency
            }


        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    # test
