# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

basepath=os.path.abspath(os.path.dirname(__file__))

starturl='http://alpha.wallhaven.cc/search?q='

baseurl='https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'

def genstartpage(tag):
    result=[]
    #default is 3 pages
    for i in range(1,4):
        result.append(starturl+tag+'&page='+str(i))
    return result