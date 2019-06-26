# -*- coding: utf-8 -*-
__auther__ = '35942'


from handlers import *

handlers = [
    (r"/", IndexHandlers),
    (r"/acc", Acc),
    (r"/generic", Generic),
    (r"/visitormsg", VisitorMessage),
    (r"/elements", Elements)

]

