# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re
import requests
import time

class LegislationScraperPipeline(object):

    def process_item(self, item, spider):
        url = item['url']
        bill_number = item['bill_number'][0]
        r = requests.get(url, stream = True)
        pdf_filename = 'data\\' + bill_number + '.pdf'
        txt_filename = 'data\\' + bill_number + '.txt'
        with open(pdf_filename, 'wb') as f:
            f.write(r.content)
        pdf2txt_path = 'legislation_scraper/pdf2txt.py'
        print("python " + pdf2txt_path + " -o " + txt_filename + " " + pdf_filename)
        os.system("python " + pdf2txt_path + " -o " + txt_filename + " " + pdf_filename)
        while not os.path.exists(txt_filename):
            time.sleep(0.001)
        file = open(txt_filename, 'r', encoding='utf8')
        filetext = file.read()
        filetext = filetext.replace('\n', '')
        filetext = filetext.replace('\r', '')
        filetext = ''.join(filetext)
        mat = re.search(r'(?=(FOR)).+?(?=( BY| (|\(1\)) SECTION 1.| WHEREAS| EXPLANATION))', filetext)
        if mat:
            item['purpose'] = ''.join(mat.group(0))
        else:
            item['purpose'] = ""
        file.close()
        os.remove(pdf_filename)
        os.remove(txt_filename)
        return item
