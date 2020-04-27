# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import CarBrandsItem


class QczjSpider(scrapy.Spider):
    name = 'qczj'
    allowed_domains = ['car.m.autohome.com.cn']
    start_urls = ['http://car.m.autohome.com.cn/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.MySQLPipeline': 300
        }
    }

    def parse(self, response):
        brands = response.css('section#div_ListBrand li')
        item = CarBrandsItem()
        for brand in brands:
            item['text'] = brand.css('span::text').get()
            item['img_url'] = brand.css('img::attr(data-src)').get()
            item['qczj_id'] = int(brand.css('div::attr(v)').get())
            yield item
