# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# siteTitle, siteKeywords, title, url, titleTime, replyUrl, replauthor, replcontext, replTime
import datetime
import logging
import pymysql.cursors
from CR.items import Crypitem

class CrPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(user='root', passwd='tjqhgus11', db='cr', host='localhost')
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        """
        self.cursor.execute("select * from cr.cryptodb where siteTitle = %s and siteKeywords = %s and title = %s and url = %s and titleTime = %s and replyUrl = %s and replauthor = %s and replcontext = %s and replTime = %s", (item['siteTitle'][0].encode('utf-8'), item['siteKeywords'][0].encode('utf-8'), item['title'][0].encode('utf-8'), item['url'][0].encode('utf-8'), item['titleTime'][0].encode('utf-8'), item['replyUrl'][0].encode('utf-8'), item['replauthor'][0].encode('utf-8'), item['replcontext'][0].encode('utf-8'), item['replTime'][0].encode('utf-8')))
        result = self.cursor.fetchone()

        if result:
            print("data already exist")

        else:
            try:"""
        self.cursor.execute("insert into cr.cryptodb(siteTitle, siteKeywords, title, url, titleTime, replyUrl, replauthor, replcontext, replTime) values (%s %s %s %s %s %s %s %s %s)", (item['siteTitle'][0].encode('utf-8'), item['siteKeywords'][0].encode('utf-8'), item['title'][0].encode('utf-8'), item['url'][0].encode('utf-8'),
        item['titleTime'][0].encode('utf-8'), item['replyUrl'][0].encode('utf-8'), item['replauthor'][0].encode('utf-8'), item['replcontext'][0].encode('utf-8'), item['replTime'][0].encode('utf-8')))
        self.conn.commit()

        """
            except pymysql.Error as e:
                print ("Error %d: %s") % (e.args[0], e.args[1])
                return item
        """
