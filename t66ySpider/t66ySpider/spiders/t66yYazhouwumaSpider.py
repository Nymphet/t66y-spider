# -*- coding: utf-8 -*-

import scrapy
import re

from t66ySpider.items import T66YspiderYazhouwumaItem


class t66yYazhouwumaSpider(scrapy.Spider):
    name = 'YaZhouWuMa'
    allowed_domains = ['t66y.com']
    start_urls = ["http://t66y.com/thread0806.php?fid=2"]
    unicode_next_page = u'\u4e0b\u4e00\u9801'
    imgchili_net = re.compile(r'''imgchili''')
    imagetwist_com = re.compile(r'''imagetwist''')

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
        item = T66YspiderYazhouwumaItem()
        item['t_title']         = response.selector.xpath('string(//title)')[0].extract()
        item['t_url']           = response.url

        t_img_l = []
        for link in response.selector.xpath('//input/@src').extract() + response.selector.xpath('//img/@src').extract():
            if self.imgchili_net.search(link):
                t_img_l.append(link.replace('http://t','http://i'))
            elif self.imagetwist_com.search(link):
                t_img_l.append(link.replace('/th/','/i/'))
            else:
                t_img_l.append(link)

        item['t_image_list']    = t_img_l
        item['t_torrent_list']  = response.selector.xpath('//a[contains(text(),"rmdown")]/text()').extract()
        yield item
