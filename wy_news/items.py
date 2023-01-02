# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiproItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    url = scrapy.Field()  # 链接
    keywords = scrapy.Field()  # 关键词
    time = scrapy.Field()  # 时间
    hits = scrapy.Field()  # 热度