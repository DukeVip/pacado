# -*- coding: utf-8 -*-
__auther__ = '35942'

from tornado.options import define
def init_config():
    define('mongo_meta_uri', default="mongodb://test:read123abc@52.83.254.5:10026/admin",
           type=str, help='server listening port')
    define('mongo_cnyb_uri', default="mongodb://test:read123abc@52.83.254.5:10027/",
           type=str, help='server listening port')