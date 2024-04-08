# 导入需要的库
import requests
from bs4 import BeautifulSoup as bs
import json
import csv
import re
import time

# 宏变量存储目标js的URL列表
COMMENT_PAGE_URL = []

#接入代理池并自动索取IP


# 生成链接列表
def Get_Url(num):
    urlFront = 'https://rate.tmall.com/list_detail_rate.htm?itemId=522900342691&spuId=418624783&sellerId=1707225666&order=1&currentPage='

    urlRear = '&append=0&content=0&tagId=&posi=&picture=&groupId=&ua=098%23E1hvFvvbvnpvU9CkvvvvvjiPnLMWAjnjnLSwzjnEPmPv1jnjPLcUzj1URFdygjECR2oCvpvW7Dt3vRFw7Di4cdcN3QhvCvvhvvm5vpvhvvmv9FyCvvpvvvvv2QhvCvvvvvvEvpCWmvLlvvaFDfeU%2Bb8ramegKO7l%2BigDN%2BBl%2BE7re16s3wjCDLwAv0KD%2BXV9%2Bul684oQD76Xd56OfaCl%2BboJayb96b2XrqpyCW2%2BFO7t%2BdyCvm9vvvvHphvwxQvvvqivpCvhvvm2phCvhRvvvUnvphvpgvvvvGEvpCClkphvC99vvOCgoTyCvv9vvUvtKcqB6phCvvOvCvvvphvtvpvhvvvvvv%3D%3D&needFold=0&_ksTS=1593328499128_2853&callback=jsonp2854'





    for i in range(0, num):
        COMMENT_PAGE_URL.append(urlFront + str(1 + i) + urlRear)


# 获取评论数据
def GetInfo(num):
    # 定义需要的字段
    #交易时间
    # tradeendtime = []
    #用户id 和 用户名
    # user_id=[]
    displayUserNick = []
    #购买款式
    auctionSku = []
    #评价内容
    ratecontent = []
    #评价时间
    ratedate = []
    #评价图片
    # pics = []


    # 循环获取每一页评论
    for i in range(num):
        # 头文件，没有头文件会返回错误的js
        headers = {
            'cookie': 'cna=qMU/EQh0JGoCAW5QEUJ1/zZm; enc=DUb9Egln3%2Fi4NrDfzfMsGHcMim6HWdN%2Bb4ljtnJs6MOO3H3xZsVcAs0nFao0I2uau%2FbmB031ZJRvrul7DmICSw%3D%3D; lid=%E5%90%91%E6%97%A5%E8%91%B5%E7%9B%9B%E5%BC%80%E7%9A%84%E5%A4%8F%E5%A4%A9941020; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; hng=CN%7Czh-CN%7CCNY%7C156; x=__ll%3D-1%26_ato%3D0; t=2c579f9538646ca269e2128bced5672a; _m_h5_tk=86d64a702eea3035e5d5a6024012bd40_1551170172203; _m_h5_tk_enc=c10fd504aded0dc94f111b0e77781314; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bI3949Xhg%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzZ1MVSremcx%2BQ%3D&id2=UNcPuUTqrGd03w%3D%3D&nk2=F5RAQ19thpZO8A%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=tb51552614; _l_g_=Ug%3D%3D; ck1=""; unb=3778730506; lgc=tb51552614; cookie1=UUBZRT7oNe6%2BVDtyYKPVM4xfPcfYgF87KLfWMNP70Sc%3D; login=true; cookie17=UNcPuUTqrGd03w%3D%3D; cookie2=1843a4afaaa91d93ab0ab37c3b769be9; _nk_=tb51552614; uss=""; csg=b1ecc171; skt=503cb41f4134d19c; _tb_token_=e13935353f76e; x5sec=7b22726174656d616e616765723b32223a22393031623565643538663331616465613937336130636238633935313935363043493362302b4d46454e76646c7243692b34364c54426f4d4d7a63334f44637a4d4455774e6a7378227d; l=bBIHrB-nvFBuM0pFBOCNVQhjb_QOSIRYjuSJco3Wi_5Bp1T1Zv7OlzBs4e96Vj5R_xYB4KzBhYe9-etui; isg=BDY2WCV-dvURoAZdBw3uwj0Oh2yUQwE5YzQQ9qAfIpm149Z9COfKoZwV-_8q0HKp',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'referer': 'https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-17205939323.51.30156440Aer569&id=41212119204&rn=06f66c024f3726f8520bb678398053d8&abbucket=19&on_comment=1&sku_properties=134942334:3226348',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9'
        }

        # 解析JS文件内容
        proxy={"http" : "http://121.232.164.232:43853"}

        content = requests.get(COMMENT_PAGE_URL[i], headers=headers, proxies=proxy).text
        print(i)

        # 交易时间
        # tradeendtime.extend(re.findall('"tradeEndTime":"(.*?)"', content))
        # print( tradeendtime)
        # 用户id 和 用户名
        # userid = re.findall('"id":"(.*?)"', content)
        # user_id.extend(userid)
        # print(userid)

        nk = re.findall('"displayUserNick":"(.*?)"', content)
        displayUserNick.extend(nk)
        print(nk)
        # 购买款式
        auctionSku.extend(re.findall('"auctionSku":"(.*?)"', content))
        # print(auctionSku)
        # 评价内容
        ratecontent.extend(re.findall('"rateContent":"(.*?)"', content))
        # print(ratecontent)
        # 评价时间
        ratedate.extend(re.findall('"rateDate":"(.*?)"', content))
        # print(ratedate)
        # 评价图片
        # pics.extend(re.findall("\'pics\':\'(.*?)\'", content))
        # print(pics)


    # 将数据写入TEXT文件中
    for i in list(range(0, len(displayUserNick))):
        # text = ','.join(( tradeendtime[i], user_id[i], displayUserNick[i], auctionSku[i], ratecontent[i], ratedate[i], pics[i] )) + '\n'
        text = '@@@'.join((displayUserNick[i], auctionSku[i], ratecontent[i], ratedate[i])) + '\n'

        with open(r"update-data/01不一定有内偶人+时间顺序.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            print(i + 1, ":写入成功")


# 主函数
if __name__ == "__main__":
    Page_Num = 100
    Get_Url(Page_Num)
    GetInfo(100)


#参考链接
#https://mp.weixin.qq.com/s?__biz=MzU4MzQyODAyNg==&mid=2247483777&idx=1&sn=e12d0485a4d1b59aa4f9dcce46c62360&chksm=fda87354cadffa4285e39f04c863c94a0797baed1667d977f0a16272bffb8bb8682b671866d8&scene=126&sessionid=1592810907&key=15bfe6e62683f695c69a5a25439a59bf9c71c56de819212ed94a8b67f0ec00514285fd1af1d7ed6e2ba8ab7cfd1107d5fbcc996def2cf410e4217154c08f748e6f38fcaae180834cc10eebda1c712bba&ascene=1&uin=MTk5NzMyMTkyMg%3D%3D&devicetype=Windows+7+x64&version=62090070&lang=zh_CN&exportkey=A4ocpZC3PfwJ0X7rVuJiVV0%3D&pass_ticket=ppGa6D86gvZvqOQ1sya9rAuTsPHwcYCrd0U7DuQvc7sneKpyssovsz3acZxu%2FyIY
#https://bbs.csdn.net/topics/392570708
