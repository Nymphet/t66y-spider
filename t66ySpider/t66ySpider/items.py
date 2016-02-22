# -*- coding: utf-8 -*-

import scrapy


class T66YspiderDagaierItem(scrapy.Item):
    t_title         = scrapy.Field()
    t_image_list    = scrapy.Field()

class T66YspiderXinshidaiItem(scrapy.Item):
    t_title         = scrapy.Field()
    t_image_list    = scrapy.Field()

class T66YspiderYazhouwumaItem(scrapy.Item):
    t_title         = scrapy.Field()
    t_url           = scrapy.Field()
    t_image_list    = scrapy.Field()
    t_torrent_list  = scrapy.Field()

class T66YspiderYazhouyoumaItem(scrapy.Item):
    t_title         = scrapy.Field()
    t_url           = scrapy.Field()
    t_image_list    = scrapy.Field()
    t_torrent_list  = scrapy.Field()

class T66YspiderDongmanItem(scrapy.Item):
    t_title         = scrapy.Field()
    t_url           = scrapy.Field()
    t_image_list    = scrapy.Field()
    t_torrent_list  = scrapy.Field()
