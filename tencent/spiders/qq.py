# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem

class QqSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['tencent.com']
    baseUrl = 'http://hr.tencent.com/'
    offSet = 0
    start_urls = ['http://hr.tencent.com/position.php?keywords=&tid=0&lid=2268&start=#a0']

    def parse(self, response):
        node_lists = response.xpath('//*[@class="even" or @class="odd"]')
        positionName = node_lists.xpath('./td[1]/a/text()').extract()
        positionType = node_lists.xpath('./td[2]/text()').extract()
        peopleNum = node_lists.xpath('./td[3]/text()').extract()
        workLocation = node_lists.xpath('./td[4]/text()').extract()
        publishTime = node_lists.xpath('./td[5]/text()').extract()
        next_url = response.xpath('//*[@id="next"]/@href').extract()[0]

        item = TencentItem()
        for positionName, positionType, peopleNum, workLocation, publishTime in zip(positionName, positionType, peopleNum, workLocation, publishTime):
            item['positionName'] = positionName
            item['positionType'] = positionType
            item['peopleNum'] = peopleNum
            item['workLocation'] = workLocation
            item['publishTime'] = publishTime
            yield item

        if next_url != "javascript:;":
            request_url = self.baseUrl + next_url
            print(request_url)
            yield scrapy.Request(request_url, callback=self.parse)

        #pass
