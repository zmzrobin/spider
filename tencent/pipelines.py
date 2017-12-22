# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class TencentPipeline(object):

    def open_spider(self, spider):
        self.con = sqlite3.connect("tencent.sqlite")
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        insert_sql = "insert into qqwork (positionname, positiontype, peoplenum, worklocation, publishtiome) VALUES ('{}', '{}', '{}', '{}', '{}')".format(item['positionName'], item['positionType'], item['peopleNum'], item['workLocation'], item['publishTime'])
        print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()

        return item

    def spider_close(self, spider):
        self.con.close()