# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class YelpPipeline(object):
    def __init__(self):
        columns = ['res_url','res_name','address_1','address_2','day1','day1_time','day2','day2_time','day3','day3_time',
                    'day4','day4_time','day5','day5_time','day6','day6_time','day7','day7_time',
                    'dish_name','dish_img','dish_review','dish_price']
        file_name = 'US/NY-METRO-AREA1.csv'
        file = open(file_name, 'w', newline='', encoding = 'utf-8')
        self.writer = csv.DictWriter(file, columns)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item