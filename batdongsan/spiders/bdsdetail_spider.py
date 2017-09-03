#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2017 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""

"""
import scrapy


class BdsDetailSpider(scrapy.Spider):
    name = "bdsdetail"

    def start_requests(self):
        urls = [
            'https://batdongsan.com.vn/nha-dat-ban',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse_detail(self, response):
        body_detail = response.css('.pm-content').css('.pm-desc').extract_first()
        customeInfo = customerInfo = response.css('#divCustomerInfo')
        name = customerInfo.css('#LeftMainContent__productDetail_contactName').css('.right::text').extract_first()
        item = response.request.meta['item']
        item['bodyDetail'] = body_detail
        item['contactName'] = name
        yield item # full item


    def parse(self, response):
        for item in response.css('.search-productItem'):
            link = item.css('h3 a::attr(href)').extract_first()
            itemCrawl = {
                    'title': item.css('h3 a::attr(title)').extract_first(),
                    'link': link,    
                    'body': item.css('.p-main-text::text').extract_first(),
                    'price': item.css('.product-price::text').extract_first(),
                    'area': item.css('.product-area::text').extract_first(),
                    'city': item.css('.product-city-dist::text').extract_first(),
                    'date': item.css('.mar-right-10::text').extract_first()
                    }

            yield response.follow(link, callback=self.parse_detail,
                    meta={'item':itemCrawl}) # pass itemCrawl here to get more detail

        controller = response.css('.background-pager-controls').css('.background-pager-right-controls').css('a')
        next_page = controller[-2].css('::attr(href)').extract_first()
        button_content = controller[-2].css('::text').extract_first() # it must be ...
        if next_page is not None and button_content == '...':
            yield response.follow(next_page, callback=self.parse)


