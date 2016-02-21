# -*- coding: utf-8 -*-

import scrapy

from t66ySpider.items import T66YspiderDagaierItem


class t66yDagaierSpider(scrapy.Spider):
    name = 'DaGaiEr'
    allowed_domains = ['t66y.com']
    start_urls = ["http://t66y.com/thread0806.php?fid=16&search=&page=1"]
    unicode_next_page = u'\u4e0b\u4e00\u9801'

    def parse(self, response):
        thread_hrefs = response.selector.xpath('//h3/a/@href')

        for thread_href in thread_hrefs:
            thread_url = response.urljoin(thread_href.extract())
            yield scrapy.Request(thread_url, callback=self.parse_thread)

        next_page_href = response.selector.xpath(
            "//a[text()='%s']/@href" % self.unicode_next_page)[0]
        next_page_url = response.urljoin(next_page_href.extract())

        yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_thread(self, response):
        item = T66YspiderDagaierItem()
        item['t_title'] = response.selector.xpath(
            'string(//title)')[0].extract()
        item['t_image_list'] = response.selector.xpath(
            '//input/@src').extract()
        yield item
