# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrPipeline(object):
    def __init(self):
        try:
            self.conn = MySQLdb.connect(user='root', passwd='tjqhgus11', db='', host='')
            print ("1")
            self.cursor = self.conn.cursor()
        except MySQLdb.error, e:
            print ("Error %d: %s") % (e.args[0], e.args[1])
            sys.exit(1)

    def process_item(self, item, spider):
        self.cursor.execute("select * from cryptodb.cr where")
        return item
