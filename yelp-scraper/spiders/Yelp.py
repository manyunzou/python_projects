# -*- coding: utf-8 -*-
import scrapy
import requests
import csv
from lxml import etree
from fake_useragent import UserAgent
import numpy as  np
import pandas as pd
from pandas import Series, DataFrame

from scrapy import Spider, Request
#from scrapy.selector import Selector
from yelp.items import YelpItem

import os
import glob


class YelpSpider(scrapy.Spider):
    name = 'Yelp'
    allowed_domains = ['www.yelp.com']
    # start_urls =  ['https://www.yelp.com/biz/yummy-buffet-chicago-chicago?adjust_creative=s-obVb_6zMJew4cqQ57dUw&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=s-obVb_6zMJew4cqQ57dUw']

    # path = r'E:\\python\\04yelp\\Combined-Results\\under1000\\under1000-US'
    # all_files = glob.glob(path + "\\*.csv")

    pd.set_option('display.max_colwidth', 1000)

    #修改点1
    # for filename in all_files:
    url_list = pd.read_csv("Combined-Results/ny-all-locations1.csv", engine='python')['url']
    start_urls = [url for url in url_list]
    
    
    def parse(self, response):

        #店名
        try:
            res_name = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div[1]/h1/text()').extract()[0]
        except Exception as e:
            res_name = ""

        judget_text = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[1]/div[1]/div/h3/text()').extract()

        if judget_text == ['Popular Dishes']:

            for x in range(1, 10):
                if response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[1]/div/h3/text()').extract()  == ['Location & Hours']:

                        #地址
                        try:
                            address_1 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[1]/div/div/div/div[1]/address/p[1]/span/text()').extract()
                            address_1 = str(address_1).strip("['']")
                        except Exception as e:
                            address_1 = ""

                        try:
                            address_2 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[1]/div/div/div/div[1]/address/p[2]/span/text()').extract()
                            address_2 = str(address_2).strip("['']")
                        except Exception as e:
                            address_2 = ""

                        #营业时间1
                        try:
                            day1 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[1]/th/p/text()').extract()
                            day1 = str(day1).strip("['']")
                        except Exception as e:
                            day1 = ""

                        try:
                            day1_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[1]/td[1]/ul/li/p/text()').extract()
                            day1_time = str(day1_time).strip("['']")
                        except Exception as e:
                            day1_time = ""

                        #营业时间2
                        try:
                            day2 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[2]/th/p/text()').extract()
                            day2 = str(day2).strip("['']")
                        except Exception as e:
                            day2 = ""

                        try:
                            day2_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[2]/td[1]/ul/li/p/text()').extract()
                            day2_time = str(day2_time).strip("['']")
                        except Exception as e:
                            day2_time = ""

                        #营业时间3
                        try:
                            day3 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[3]/th/p/text()').extract()
                            day3 = str(day3).strip("['']")
                        except Exception as e:
                            day3 = ""

                        try:
                            day3_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[3]/td[1]/ul/li/p/text()').extract()
                            day3_time = str(day3_time).strip("['']")
                        except Exception as e:
                            day3_time = ""

                        #营业时间4
                        try:
                            day4 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[4]/th/p/text()').extract()
                            day4 = str(day4).strip("['']")
                        except Exception as e:
                            day4 = ""

                        try:
                            day4_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[4]/td[1]/ul/li/p/text()').extract()
                            day4_time = str(day4_time).strip("['']")
                        except Exception as e:
                            day4_time = ""

                        #营业时间5
                        try:
                            day5 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[5]/th/p/text()').extract()
                            day5 = str(day5).strip("['']")
                        except Exception as e:
                            day5 = ""

                        try:
                            day5_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[5]/td[1]/ul/li/p/text()').extract()
                            day5_time = str(day5_time).strip("['']")
                        except Exception as e:
                            day5_time = ""

                        #营业时间6
                        try:
                            day6 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[6]/th/p/text()').extract()
                            day6 = str(day6).strip("['']")
                        except Exception as e:
                            day6 = ""

                        try:
                            day6_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[6]/td[1]/ul/li/p/text()').extract()
                            day6_time = str(day6_time).strip("['']")
                        except Exception as e:
                            day6_time = ""

                        #营业时间7
                        try:
                            day7 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[7]/th/p/text()').extract()
                            day7 = str(day7).strip("['']")
                        except Exception as e:
                            day7 = ""

                        try:
                            day7_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[7]/td[1]/ul/li/p/text()').extract()
                            day7_time = str(day7_time).strip("['']")
                        except Exception as e:
                            day7_time = ""

                else:
                    continue

            #招牌菜 list
            dish_list = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[1]/div[2]/div[1]/div/div')

            for dish in dish_list:
                #菜名
                try:
                    dish_name = dish.xpath("div/div/a/div/div[2]/div/div/p/text()").extract()[0].strip()
                except Exception as e:
                    dish_name = ""

                #图片
                try:
                    dish_img = dish.xpath('div/div/a/div/div[1]/div/img/@src').extract()[0]
                except Exception as e:
                    dish_img = ""

                #评论数
                try:
                    dish_review = dish.xpath('div/div/a/div/div[2]/div/span[2]/text()').extract()[0]
                except Exception as e:
                    dish_review = ""

                #价格
                try:
                    dish_price = dish.xpath('div/div/a/div/div[1]/div/span/text()').extract()[0].strip()
                except Exception as e:
                    dish_price = ""

                item = YelpItem()

                item['res_url'] = response.request.url
                item['res_name'] = res_name
                
                item['address_1'] = address_1
                item['address_2'] = address_2

                item['day1'] = day1
                item['day1_time'] = day1_time
                item['day2'] = day2
                item['day2_time'] = day2_time
                item['day3'] = day3
                item['day3_time'] = day3_time
                item['day4'] = day4
                item['day4_time'] = day4_time
                item['day5'] = day5
                item['day5_time'] = day5_time
                item['day6'] = day6
                item['day6_time'] = day6_time
                item['day7'] = day7
                item['day7_time'] = day7_time

                item['dish_name'] = dish_name
                item['dish_img'] = dish_img
                item['dish_review'] = dish_review
                item['dish_price'] = dish_price

                yield item

        else:

            for x in range(1, 10):
                if response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[1]/div/h3/text()').extract()  == ['Location & Hours']:

                        #地址
                        try:
                            address_1 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[1]/div/div/div/div[1]/address/p[1]/span/text()').extract()
                            address_1 = str(address_1).strip("['']")
                        except Exception as e:
                            address_1 = ""

                        try:
                            address_2 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[1]/div/div/div/div[1]/address/p[2]/span/text()').extract()
                            address_2 = str(address_2).strip("['']")
                        except Exception as e:
                            address_2 = ""

                        #营业时间1
                        try:
                            day1 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[1]/th/p/text()').extract()
                            day1 = str(day1).strip("['']")
                        except Exception as e:
                            day1 = ""

                        try:
                            day1_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[1]/td[1]/ul/li/p/text()').extract()
                            day1_time = str(day1_time).strip("['']")
                        except Exception as e:
                            day1_time = ""

                        #营业时间2
                        try:
                            day2 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[2]/th/p/text()').extract()
                            day2 = str(day2).strip("['']")
                        except Exception as e:
                            day2 = ""

                        try:
                            day2_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[2]/td[1]/ul/li/p/text()').extract()
                            day2_time = str(day2_time).strip("['']")
                        except Exception as e:
                            day2_time = ""

                        #营业时间3
                        try:
                            day3 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[3]/th/p/text()').extract()
                            day3 = str(day3).strip("['']")
                        except Exception as e:
                            day3 = ""

                        try:
                            day3_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[3]/td[1]/ul/li/p/text()').extract()
                            day3_time = str(day3_time).strip("['']")
                        except Exception as e:
                            day3_time = ""

                        #营业时间4
                        try:
                            day4 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[4]/th/p/text()').extract()
                            day4 = str(day4).strip("['']")
                        except Exception as e:
                            day4 = ""

                        try:
                            day4_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[4]/td[1]/ul/li/p/text()').extract()
                            day4_time = str(day4_time).strip("['']")
                        except Exception as e:
                            day4_time = ""

                        #营业时间5
                        try:
                            day5 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[5]/th/p/text()').extract()
                            day5 = str(day5).strip("['']")
                        except Exception as e:
                            day5 = ""

                        try:
                            day5_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[5]/td[1]/ul/li/p/text()').extract()
                            day5_time = str(day5_time).strip("['']")
                        except Exception as e:
                            day5_time = ""

                        #营业时间6
                        try:
                            day6 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[6]/th/p/text()').extract()
                            day6 = str(day6).strip("['']")
                        except Exception as e:
                            day6 = ""

                        try:
                            day6_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[6]/td[1]/ul/li/p/text()').extract()
                            day6_time = str(day6_time).strip("['']")
                        except Exception as e:
                            day6_time = ""

                        #营业时间7
                        try:
                            day7 = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[7]/th/p/text()').extract()
                            day7 = str(day7).strip("['']")
                        except Exception as e:
                            day7 = ""

                        try:
                            day7_time = response.xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/section[' + str(x) + ']/div[2]/div[2]/div/div/table/tbody/tr[7]/td[1]/ul/li/p/text()').extract()
                            day7_time = str(day7_time).strip("['']")
                        except Exception as e:
                            day7_time = ""

                else:
                    continue


                dish_name = ""
                dish_img = ""
                dish_review = ""
                dish_price = ""

                item = YelpItem()

                item['res_url'] = response.request.url
                item['res_name'] = res_name
                
                item['address_1'] = address_1
                item['address_2'] = address_2

                item['day1'] = day1
                item['day1_time'] = day1_time
                item['day2'] = day2
                item['day2_time'] = day2_time
                item['day3'] = day3
                item['day3_time'] = day3_time
                item['day4'] = day4
                item['day4_time'] = day4_time
                item['day5'] = day5
                item['day5_time'] = day5_time
                item['day6'] = day6
                item['day6_time'] = day6_time
                item['day7'] = day7
                item['day7_time'] = day7_time

                item['dish_name'] = dish_name
                item['dish_img'] = dish_img
                item['dish_review'] = dish_review
                item['dish_price'] = dish_price

                yield item