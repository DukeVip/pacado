# -*- coding: utf-8 -*-
__auther__ = '35942'
import tornado.web
import os
from pycket.session import SessionMixin
# from  tools import  catch

class BaseHandlers(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        return  self.session.get('uid', None)


class IndexHandlers(BaseHandlers):
    def initialize(self):
        pass


    # @tornado.web.authenticated
    def get(self):
        a = 'a'
        self.write( a/ 10)

