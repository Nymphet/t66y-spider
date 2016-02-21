# -*- coding: utf-8 -*-

import scrapy


class T66YspiderDagaierItem(scrapy.Item):
    t_title         = scrapy.Field()
    t_image_list    = scrapy.Field()

class T66YspiderXinshidaiItem(scrapy.Item):
    t_title         = scrapy.Field()
    t_image_list    = scrapy.Field()
