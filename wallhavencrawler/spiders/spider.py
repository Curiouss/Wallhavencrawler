#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from wallhavencrawler.params import tag
from . import headers,basepath,baseurl,genstartpage
import os,requests


class BackgroundSpider(CrawlSpider):
    name = 'havenspider'
    download_delay = 2
    allowed_domains = ['wallhaven.cc']
    start_urls = genstartpage(tag)
    rules = (
        Rule(LinkExtractor(allow=('https://alpha.wallhaven.cc/wallpaper/\d{1,6}'),\
                           deny=('https://alpha.wallhaven.cc/wallpaper/\d{1,6}/[^ ]+')),\
             callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        if response:
            imagenum=baseurl+str(response.url)[-6:]+'.jpg'
            page=requests.get(imagenum,headers=headers)
            with open(os.path.join(basepath,tag,'{}.jpg'.format(str(response.url)[-6:])), 'wb') as f:
                f.write(page.content)
