# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CarBrandsItem(scrapy.Item):
    text = scrapy.Field()
    img_url = scrapy.Field()
    qczj_id = scrapy.Field()


class CarBrandsCategoryItem(scrapy.Item):
    fctname = scrapy.Field()
    qczj_fctid = scrapy.Field()
    seriesplace = scrapy.Field()
    seriesplacenum = scrapy.Field()
    brandsid = scrapy.Field()
    qczj_brandsid = scrapy.Field()


class CarListItem(scrapy.Item):
    brands_category = scrapy.Field()
    qczj_fctid = scrapy.Field()
    containbookedspec = scrapy.Field()
    fctname = scrapy.Field()
    newenergy = scrapy.Field()
    newenergySeriesId = scrapy.Field()
    pnglogo = scrapy.Field()
    rank = scrapy.Field()
    seriesImg = scrapy.Field()
    seriesName = scrapy.Field()
    seriesPriceMax = scrapy.Field()
    seriesPriceMin = scrapy.Field()
    seriesState = scrapy.Field()
    seriesid = scrapy.Field()
    seriesplace = scrapy.Field()
