from tutorial.db.dbhelper import DBHelper


class MySQLPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        self.db = DBHelper()


    # 关闭数据库
    def close_spider(self, spider):
        self.db.close_db(self)

    # 对数据进行处理
    def process_item(self, item, spider):
        values = (
            item['text'],
            item['qczj_id'],
            item['img_url'],
        )
        sql = "INSERT INTO car_brands VALUES(NULL, %s,%s,%s)"
        self.db.insert_db(sql, values)
        return item


class BrandCategorySpider(object):

    # 打开数据库
    def open_spider(self, spider):
        self.db = DBHelper()


    # 关闭数据库
    def close_spider(self, spider):
        self.db.close_db(self)

    # 对数据进行处理
    def process_item(self, item, spider):
        values = (
            item['fctname'],
            item['qczj_fctid'],
            item['seriesplace'],
            item['seriesplacenum'],
            item['brandsid'],
            item['qczj_brandsid'],
        )
        sql = "INSERT INTO car_brands_category VALUES(NULL, %s,%s,%s,%s,%s,%s)"
        self.db.insert_db(sql, values)
        return item


class CarListSpider(object):
    # 打开数据库
    def open_spider(self, spider):
        self.db = DBHelper()

    # 关闭数据库
    def close_spider(self, spider):
        self.db.close_db(self)

    # 对数据进行处理
    def process_item(self, item, spider):
        values = (
            item['brands_category'],
            item['qczj_fctid'],
            item['containbookedspec'],
            item['fctname'],
            item['newenergy'],
            item['newenergySeriesId'],
            item['pnglogo'],
            item['rank'],
            item['seriesImg'],
            item['seriesName'],
            item['seriesPriceMax'],
            item['seriesPriceMin'],
            item['seriesState'],
            item['seriesid'],
            item['seriesplace'],
        )
        sql = "INSERT INTO car_list VALUES(NULL, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.db.insert_db(sql, values)
        return item


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
