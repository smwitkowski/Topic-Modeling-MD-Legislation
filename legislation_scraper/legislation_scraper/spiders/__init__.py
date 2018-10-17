import scrapy
from scrapy.spiders import CrawlSpider, Rule

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
    Rule(LinkExtractor(allow=('//table[@class = "grid"]//tr/td[1]/a[1]', callback = 'parse_item')))
    )

    def parse_item:
