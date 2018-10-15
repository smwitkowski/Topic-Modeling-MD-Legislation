# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests

class LegislationScraperPipeline(object):

    def process_item(self, item, spider):
        url = item.get('pdf_url')
        bill_number = item.get('bill_number')
        save_loc = "C:\\Users\\switkowski\\Documents\\Projects\\Topic - Model - MD - Legislation\\data\\"
        r = requests.get(url, stream = True)
        with open(save_loc + bill_number + '.pdf', 'wb') as f:
            f.write(r.conetnt)
        return item
