import pymysql

from tutorial import settings


class DBHelper:
    def __init__(self):
        dbparams = dict(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_NAME,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            charset='utf8'
        )

        self.db_conn = pymysql.connect(**dbparams)
        self.db_cur = self.db_conn.cursor()

    def close_db(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

        # 插入数据
    def insert_db(self, sql, values):
        self.db_cur.execute(sql, values)

    def select_db(self, sql):
        self.db_cur.execute(sql)
        info = self.db_cur.fetchall()
        self.close_db(self)
        return info
