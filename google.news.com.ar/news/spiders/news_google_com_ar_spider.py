import scrapy

from news.items import NewsItem

from scrapy.selector import Selector

import datetime
import time

class NewsGoogleSpider(scrapy.Spider):
    name = "news_google_com_ar"
    allowed_domains = ["news.google.com.ar"]
    start_urls = ["https://news.google.com.ar/"]

    def parse(self, response):
        timeStr = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        for articleCell in response.xpath('//td[@class="esc-layout-article-cell"]'):
            item = NewsItem()
            item['title'] = articleCell.xpath('div/h2[@class="esc-lead-article-title"]/a/span/text()').extract()
            item['attribution'] = articleCell.xpath('div[@class="esc-lead-article-source-wrapper"]/table/tbody/tr/td/span[@class="al-attribution-source"]/text()').extract()
            item['snippet'] = articleCell.xpath('div[@class="esc-lead-snippet-wrapper"]/text()').extract()
            item['flags'] = []
            item['retrivalTime'] = timeStr
            yield item
        for popularCell in response.xpath('//div[@id="s_MOST_POPULAR"]/div[@class="contents"]/div//div[@cid]'):
            item=NewsItem()
            item['title'] = popularCell.xpath('div[@class="title"]/a/span/text()').extract()
            item['attribution'] = popularCell.xpath('div[@class="sub-title source"]/span[@class="source-pref"]/text()').extract()
            item['flags'] = ["popular"]
            item['retrivalTime'] = timeStr
            yield item
