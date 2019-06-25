# -*- coding: utf-8 -*-
__auther__ = '35942'
import hashlib
import traceback
from functools import wraps
from  tornado.gen import BadYieldError
from  tornado.web import  RequestHandler
def hash(text):
    text = hashlib.md5(text.encode()).hexdigest() #给密码加密，用hashlib来算法加密，utf8不加的话就是默认utf8

    return text

USER_DATA = {
    'name':'user',
    'password':hash('1q2w3e4r')
}

def authenticate(username,password):#用户密码匹配判断函数
    if username and password:
        hash_pwd = hash(password)
        if username == USER_DATA['name'] and hash_pwd == USER_DATA['password']: #是否与保存的一致
            return True

    return False



# def catch(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print func,'----------'
#         RT = RequestHandler()
#         try:
#             return func(*args,**kwargs)
#         except TypeError:
#             traceback.print_exc()
#             msg = 'Json serislization error'
#             resp_status = 200
#             data = {'msg': msg, 'code': 0}
#             RT.write(data, resp_status)
#         except BadYieldError:
#             traceback.print_exc()
#             error = 'http status code 500'
#             resp_status = 200
#             data = {'msg': error, 'code': 0}
#             RT.write(data, resp_status)
#     return inner