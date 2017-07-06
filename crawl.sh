#!/bin/sh

#  crawl.sh
#  
#
#  Created on 7/6/17.
#

echo "tag=\"$1\"" >./wallhavencrawler/params.py
mkdir ./wallhavencrawler/spiders/$1
scrapy crawl havenspider
