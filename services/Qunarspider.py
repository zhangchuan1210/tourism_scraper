import time  # 引入time库，降低访问频率
import scrapy  # 引入爬虫框架scrapy库
from scrapy.selector import Selector  # 引用Selector方法，对目标response进行解析

class QunarItem(scrapy.Item):
    Title = scrapy.Field() # Title：文章标题
    Comment = scrapy.Field()# Comment：作者名称
    TravelLink = scrapy.Field()# TravelLink：标题的链接
    Date = scrapy.Field()# Date：出发日期
    Days = scrapy.Field() # Days：旅游共几天
    Photo_Nums = scrapy.Field()# Photo_Nums：照片数量
    Fee = scrapy.Field()# Fee：人均消费
    People = scrapy.Field()# People：适合人数
    Places = scrapy.Field()# Places：途径地点
    Views = scrapy.Field()# Views：评论人数


class QunarSpider(scrapy.Spider):  # 编写QunarSpider类
    name = 'Qunarspider'  # 唯一名字
    # allowed_domains = ['travel.qunar.com']
    start_urls = ['https://travel.qunar.com/travelbook/list.htm?page=1&order=hot_heat']  # 基地址

    def parse(self, response):
        selector = Selector(response)  # 对目标返回的response进行解析
        item = QunarItem()  # 将在items.py定义好的相关字段赋值给变量item
        infos = selector.xpath('//li[starts-with(@class,"list_item")]')  # 找到循环点，此处为记录每一条游记的标签
        for info in infos:  # 进行循环
            # 经过大量实验可知，某些游记也许存在空值，为了程序的正常运行，则进行抛出异常处理

            # 以获取标题为例：
            try:
                Title = info.xpath('.//h2[@class="tit"]/a/text()').extract()[0]  # 返回利用xpath已获取Title列表中的第一个元素
                item['Title'] = Title  # 赋值

                time.sleep(1)  # 休息一秒
                # 回调item，对items.py中的字段进行赋值
                yield item
            except IndexError:
                pass
            urls = ['https://travel.qunar.com/travelbook/list.htm?page={}&order=hot_heat'.format(str(i)) for i in
                    range(2, 201)]  # 对目标网站进行字符串格式化
            for url in urls:  # 循环
                yield scrapy.Request(url)  # 利用循环的urlparse回调函数