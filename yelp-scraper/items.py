# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YelpItem(scrapy.Item):
    # define the fields for your item here like:

    #url
    res_url = scrapy.Field()

    #店名
    res_name = scrapy.Field()

    #地址
    address_1 = scrapy.Field()
    address_2 = scrapy.Field()

    #营业时间
    day1 = scrapy.Field()
    day1_time = scrapy.Field()
    day2 = scrapy.Field()
    day2_time = scrapy.Field()
    day3 = scrapy.Field()
    day3_time = scrapy.Field()
    day4 = scrapy.Field()
    day4_time = scrapy.Field()
    day5 = scrapy.Field()
    day5_time = scrapy.Field()
    day6 = scrapy.Field()
    day6_time = scrapy.Field()
    day7 = scrapy.Field()
    day7_time = scrapy.Field()

    #招牌菜
    dish_name = scrapy.Field()
    dish_img = scrapy.Field()
    dish_review = scrapy.Field()
    dish_price = scrapy.Field()