# -*- encoding: utf-8 -*-

import scrapy
from urllib import unquote
from urlparse import urljoin
from dspbooks.items import BookItem

class DSPBooksSpider(scrapy.Spider):
    name = 'dspbooks'
    base_url = 'http://serv.yanchick.org/Books/dsp_books/'
    start_urls = ['http://serv.yanchick.org/Books/dsp_books/']

    def parse(self, response):
        quoted_links = response.xpath('//ul/li/a/@href').extract()[1:]
        rel_links = [urljoin(self.base_url, str(unquote(x)))
                for  x in quoted_links]
        for link in rel_links:
            if link.endswith('/'):
                yield scrapy.Request(url=link, callback=self.parse)
            else:
                yield BookItem(file_urls=[link,])
