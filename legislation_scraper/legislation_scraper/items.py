# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LegislationScraperItem(scrapy.Item):
    #define the fields for your item here like:
    bill_name = scrapy.Field()
    bill_number = scrapy.Field()
    url = scrapy.Field()
    sponsor = scrapy.Field()
    status = scrapy.Field()
    committee = scrapy.Field()
    broad_subjects = scrapy.Field()
    narrow_subjects = scrapy.Field()
    pass
