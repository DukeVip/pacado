# -*- coding: utf-8 -*-
__auther__ = '35942'
from pymongo import MongoClient
from  tornado.options import options
import pacado.config
_DbInstance = None



class DB(object):
    @classmethod
    def connect(cls):
        options.parse_config_file('pacado.conf')
        # db_meta = MongoClient(options.mongo_meta_uri)
        db_cnyb = MongoClient(options.mongo_cnyb_uri)
        return  db_cnyb

    @classmethod
    def get_db(cls):
        global _DbInstance
        if not _DbInstance:
            _DbInstance = cls.connect()
        return  _DbInstance



pacado.config.init_config()
options.parse_config_file("pacado.conf")
print  options.mongo_meta_uri