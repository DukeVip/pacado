# -*- coding: utf-8 -*-
__auther__ = '35942'
import os
import tornado
from  tornado.options import options, define
from  urls import handlers
BASE_DIR = os.path.dirname(__file__)

define("port", default=8888, help="run on the given port", type=int) #监听端口

settings = dict(
    debug=True,  # 调试模式，修改后自动重启服务，不需要自动重启，生产情况下切勿开启，安全性
    template_path= os.path.join(BASE_DIR, 'templates'),  # 模板文件目录,想要Tornado能够正确的找到html文件，需要在 Application 中指定文件的位置
    static_path=  os.path.join(BASE_DIR,'static'),  # 静态文件目录,可用于用于访问js,css,图片之类的添加此配置之后，tornado就能自己找到静态文件
    # static_url_prefix= '/stc/',
    login_url='/login',  # 没有登录则跳转至此
    cookie_secret='1q2w3e4r',  # 加密cookie的字符串
    pycket={  # 固定写法packet，用于保存用户登录信息
        'engine': 'redis',
        'storage': {
            'host': 'localhost',
            'port': 6379,
            'db_sessions': 5,
            'db_notifications': 11,
            'max_connections': 2 ** 33,
        },
        'cookie': {
            'expires_days': 38,
            'max_age': 100
        }
    }
)

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers=handlers, **settings)


if __name__ == '__main__':
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
