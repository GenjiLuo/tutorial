# -*- coding: utf-8 -*-
import json

import scrapy

from tutorial.db.dbhelper import DBHelper
from tutorial.items import CarListItem


class CarListSpider(scrapy.Spider):
    name = 'car_list'
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.CarListSpider': 400
        }
    }
    def start_requests(self):
        db = DBHelper()
        sql = 'select `id`, `qczj_id` from car_brands'
        infos = db.select_db(sql)
        for info in infos:
            url_init = 'https://car.m.autohome.com.cn/ajax/GetSeriesByBrandId1?r=9&brandid={}'.format(info[1])
            yield scrapy.Request(url_init, meta={'id': info[0]}, callback=self.parse)
        # url_init = 'https://car.m.autohome.com.cn/ajax/GetSeriesByBrandId1?r=9&brandid=33'
        # yield scrapy.Request(url_init, meta={'id': infos[0][0]}, callback=self.parse)


    def parse(self, response):
        data = json.loads(response.text)
        item = CarListItem()
        for row in data['fctlist']:
            for res in row['serieslist']:
                db = DBHelper()
                sql = 'select `id` from car_brands_category where `qczj_fctid`={}'.format(row['fctid'])
                fctids = db.select_db(sql)
                item['brands_category'] = fctids[0][0]  # brands_id
                item['qczj_fctid'] = res['fctid']
                item['containbookedspec'] = res['containbookedspec']
                item['fctname'] = res['fctname']
                item['newenergy'] = res['newenergy']
                item['newenergySeriesId'] = res['newenergySeriesId']
                item['pnglogo'] = res['pnglogo']
                item['rank'] = res['rank']
                item['seriesImg'] = res['seriesImg']
                item['seriesName'] = res['seriesName']
                item['seriesPriceMax'] = res['seriesPriceMax']
                item['seriesPriceMin'] = res['seriesPriceMin']
                item['seriesState'] = res['seriesState']
                item['seriesid'] = res['seriesid']
                item['seriesplace'] = res['seriesplace']
                yield item
