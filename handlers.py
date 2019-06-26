# -*- coding: utf-8 -*-
__auther__ = '35942'
import json
import tornado.web
from db import DB

from pycket.session import SessionMixin

from tools import authenticate
# from  tools import  catch

class BaseHandlers(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        return  self.session.get('uid', None)

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        # self.set_header('Content-type', 'application/json')

class IndexHandlers(BaseHandlers):
    def initialize(self):
        pass


    # @tornado.web.authenticated
    def get(self):

        self.render('index.html')


class VisitorMessage(BaseHandlers):
    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        email = self.get_argument('email')
        text = self.get_argument('message')
        self.redirect('/')


class Generic(BaseHandlers):
    def get(self):

        self.render('generic.html')

class Elements(BaseHandlers):
    def get(self):

        self.render('elements.html')

class Acc(BaseHandlers):
    def get(self):
        db = DB.get_cnyb_db('cnyb')
        data = list(db.predict_data.find({
            "dtime":{'$gte':'2019-07-01 00:00:00', '$lte':'2019-07-10 00:00:00'} ,
            'index':7},
            {'_id':0}))
        values = {'predict_data':data}
        self.set_header('Content-type', 'application/json')
        self.write(json.dumps(values).replace('NaN', 'null'))


class RegisterHandler(BaseHandlers):
    def get(self, *args, **kwargs):
        print('register')
        self.render('register.html')

    def post(self, *args, **kwargs):
        print('registerpost')

        username = self.get_argument('username','')
        password1 = self.get_argument('password1','')
        password2 = self.get_argument('password2','')

        if username and password1 and (password1 == password2):
            pass
        else:
            self.write({'msg':'register fail'})


class LoginHandler(BaseHandlers):
    def get(self,*args,**kwargs):
        if self.current_user: #若用户已登录
            self.redirect('/') #那么直接跳转到主页
        else:
            nextname = self.get_argument('next','') #将原来的路由赋值给nextname
            self.render('login.html',nextname = nextname) #否则去登录界面

    def post(self,*args,**kwargs):
        username = self.get_argument('username',None)
        password = self.get_argument('password',None)

        passed = authenticate(username,password)

        if passed:
            self.session.set('user_info',username) #将前面设置的cookie设置为username，保存用户登录信息
            next_url = self.get_argument('next', '')  # 获取之前页面的路由

            if next_url:
                self.redirect(next_url) #跳转主页路由
            else:
                self.redirect('/')
        else:
            self.write({'msg':'login fail'}) #不通过，有问题

class LogoutHandler(BaseHandlers):
    def get(self, *args, **kwargs):
        #self.session.set('user_info','') #将用户的cookie清除
        self.session.delete('user_info')
        self.redirect('/login')