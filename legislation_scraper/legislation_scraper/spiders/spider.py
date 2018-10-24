import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from legislation_scraper.items import LegislationScraperItem


class LegislationSpider(CrawlSpider):
    name = 'legislation_spider'
    allowed_domains = ['http://mgaleg.maryland.gov']
    start_urls = [
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=app&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=b%26t&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=ecm&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=ehe&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=env&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=exn&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=fin&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=hgo&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=jpr&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=jud&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=sru&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=hru&stab=02&pid=cmtepage&tab=subject3&ys=2018RS',
        'http://mgaleg.maryland.gov/webmga/frmMain.aspx?id=w%26m&stab=02&pid=cmtepage&tab=subject3&ys=2018RS'
    ]

    rules = (
        Rule(LinkExtractor(allow=('//table[@class = "grid"]//tr/td[1]/a[1]/@href')), callback='parse_item', follow = True),
    )

    def parse_item(self, response):
        item = LegislationScraperItem()
        item['bill_name'] = response.xpath('//table[@class = "billheader"]//tr[1]/td[3]/h3/text()').extract()
        item['bill_number'] = response.xpath('//table[@class = "billheader"]//tr[2]/td[1]/h2/a/text()').extract()
        item['url'] = response.xpath('//table[@class = "billheader"]//tr[2]/td[1]/h2/a/@href').extract()
        item['sponsor'] = response.xpath('//table[@class = "billheader"]//tr[2]/td[3]/h3/a/text()').extract()
        item['status'] = response.xpath('//table[@class = "billheader"]//tr[3]/td[3]/h3/text()').extract()
        item['committee'] = response.xpath('//table[@class = "subcomm"]//td/a/text()').extract()
        item['broad_subjects'] = response.xpath('//table[@class = "billsum"]//tr[descendant::text()[contains(.,"Broad Subject")]]/td/a/text()')
        item['narrow_subjects'] = response.xpath('//table[@class = "billsum"]//tr[descendant::text()[contains(.,"Narrow Subject")]]/td/a/text()').extract()
        yield item