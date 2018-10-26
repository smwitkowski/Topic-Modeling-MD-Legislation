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
        save_loc = "C:\\Users\\switkowski\\Documents\\Projects\\Topic-Model-MD-Legislation\\data\\"
        r = requests.get(url, stream = True)
        pdf_filename = save_loc + bill_number + '.pdf'
        txt_filename = save_loc + bill_number + '.txt'
        with open(pdf_filename, 'wb') as f:
            f.write(r.content)
        pdf2txt_path = 'pdf2txt.py'
        print("python " + pdf2txt_path + " -o " + txt_filename + " " + pdf_filename)
        os.system("python " + pdf2txt_path + " -o " + txt_filename + " " + pdf_filename)
        file = open(txt_filename, 'r', encoding='utf8')
        filetext = file.read()
        filetext = filetext.replace('\n', '')
        filetext = filetext.replace('\r', '')
        filetext = ''.join(filetext)
        mat = re.search(r'(?=(FOR)).+?(?=( BY| (1) SECTION 1.))', filetext)
        if mat:
            item['purpose'] = ''.join(mat.group(0))
        else:
            item['purpose'] = ""
        del pdf_filename
        del txt_filename
        return item
