import json

import scrapy

from wy_news.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['news.163.com']
    start_urls = ['https://news.163.com/']

    def parse(self, response, *args, **kwargs):
        # self.models_urls = []
        # # with open("page.html", "w") as f:
        # #     f.write(str(response.text))
        # li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        # alist = [1,2]   # 国内，国际，军事板块在第2，3，5个li里面
        # for index in alist:
        #     model_url = li_list[index].xpath('./a/@href').extract_first()
        #     self.models_urls.append(model_url)
        #     # 依次对每一个板块对应的页面进行请求
        # print(f"url:{self.models_urls}")

        # 通过抓包工具查询到数据接口
        url_list = ["https://news.163.com/special/cm_guonei/?callback=data_callback",
            "https://news.163.com/special/cm_guonei_02/?callback=data_callback",
            "https://news.163.com/special/cm_guoji/?callback=data_callback",
            "https://news.163.com/special/cm_guoji_02/?callback=data_callback",
            "https://news.163.com/special/cm_war/?callback=data_callback",
            "https://news.163.com/special/cm_war_02/?callback=data_callback"]
        for url in url_list:  # 对每一个板块的url进行请求发送
            # 每一个板块对应的新闻标题相关的内容都是动态加载
            yield scrapy.Request(url, callback=self.parse_model, encoding="utf-8")

    def parse_model(self, response):  # 解析每一个板块页面中对应新闻的标题和新闻详情页的url
        data = response.text
        data = data.replace("data_callback(", "").replace(")", "")

        data = json.loads(data)
        # 数据解析
        for d in data:
            print(f"d:{d}")
            # csv格式这里不能使用','，要使用中文逗号
            title = d["title"].replace(',', '，')
            new_detail_url = d["docurl"].replace(',', '，')
            time = d["time"].replace(',', '，')
            hits = d["point"].replace(',', '，')
            keywords = ""
            for i in d["keywords"]:
                keywords += i["keyname"].replace(',', '，') + " "
            item = WangyiproItem()
            item['title'] = title
            item['url'] = new_detail_url
            item['keywords'] = keywords
            item['time'] = time
            item['hits'] = hits
            yield item
