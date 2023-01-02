# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WyNewsPipeline:
    def open_spider(self, spider):
        # self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        # self.cursor = self.db.cursor()
        with open("data/data.csv", "a+") as f:
            f.write("title,url,keywords,time,point\n")
        pass

    def close_spider(self, spider):
        # self.db.close()
        pass

    def process_item(self, item, spider):
        print(f"item: {item}")
        with open("data/data.csv", "a+") as f:
            f.write(f"{item['title']},{item['url']}url,{item['keywords']},{item['time']},{item['hits']}\n")
        return item

