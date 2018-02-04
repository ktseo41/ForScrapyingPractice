# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'cryptoReply'
    start_urls = ["https://www.reddit.com/r/CryptoCurrency/comments/7uxnja/the_state_of_rcryptocurrency_rn/"]


    def parse(self, response):
        replys = response.xpath('//div[@class="sitetable nestedlisting"]//div[@class="entry unvoted"]')
        # replText = response.xpath('//form[@class="usertext warn-on-unload"]')
        # 위와같이하면 오른쪽 사이드바까지 포함되면서 지나치게 쓸데없이 많은 내용들이 포함되더라
        # sitetable nestedlisting은 하나다. 굿
        replTexts = response.xpath('//div[@class="sitetable nestedlisting"]//form[@class="usertext warn-on-unload"]')

        for reply in replys:
            author = reply.xpath('.//p[@class="tagline"]/a[contains(@class,"author")]/text()').extract()
            context = reply.xpath('.//form[@class="usertext warn-on-unload"]//div[@class="md"]/p/text()').extract()

            if author is not None or context is not None:
                yield {
                    "author" : author,
                    "context" : context
                }

            # 위와같이 했을 때 이유는 모르겠는데 몇몇 author들이 있음에도 빈칸으로 표시된다.
            # 확인한건 리플말고 본문도 entry unvoted 라서 , 그리고 그글에도 author가 있어서 찾아지는데
            # 막상 author는 없다고 나오게 됐다.
