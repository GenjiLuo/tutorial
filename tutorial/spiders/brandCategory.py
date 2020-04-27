# -*- coding: utf-8 -*-
import json

import scrapy

from tutorial.db.dbhelper import DBHelper
from tutorial.items import CarBrandsCategoryItem


class BrandCategorySpider(scrapy.Spider):
    name = 'brandCategory'
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.BrandCategorySpider': 400
        }
    }

    def start_requests(self):
        db = DBHelper()
        sql = 'select `id`, `qczj_id` from car_brands'
        infos = db.select_db(sql)
        for info in infos:
            url_init = 'https://car.m.autohome.com.cn/ajax/GetSeriesByBrandId1?r=9&brandid={}'.format(info[1])
            yield scrapy.Request(url_init, meta={'id': info[0]}, callback=self.parse)


    def parse(self, response):
        id = response.meta['id']
        data = json.loads(response.text)
        item = CarBrandsCategoryItem()
        for row in data['fctlist']:
            item['fctname'] = row['fctname']
            item['qczj_fctid'] = row['fctid']
            item['seriesplace'] = row['seriesplace']
            item['seriesplacenum'] = row['seriesplacenum']
            item['brandsid'] = id
            item['qczj_brandsid'] = row['fctid']
            yield item

