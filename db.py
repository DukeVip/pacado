# -*- coding: utf-8 -*-
__auther__ = '35942'
from pymongo import MongoClient
from  tornado.options import options
import config
_meta_instance = None
_cnyb_instance = None


class DB(object):
    @classmethod
    def connect(cls,dbname):
        db = None
        config.init_config()
        options.parse_config_file('pacado.conf')
        if dbname == 'meta':
            db = MongoClient(options.mongo_meta_uri)['metadata']
        if dbname == 'cnyb':
            db = MongoClient(options.mongo_cnyb_uri)['cnyb']
        return db

    @classmethod
    def get_meta_db(cls,dbname):
        global _meta_instance
        if not _meta_instance:
            _meta_instance = cls.connect(dbname)
        return  _meta_instance

    @classmethod
    def get_cnyb_db(cls,dbname):
        global _cnyb_instance
        if not _cnyb_instance:
            _cnyb_instance = cls.connect(dbname)
        return _cnyb_instance

