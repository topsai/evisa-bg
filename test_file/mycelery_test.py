#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/4/28

from celery import Celery
from test_file import mycelery

app = Celery('hello', broker="redis://192.168.89.128", backend="redis://192.168.89.128")


@app.task(bind=True)
def hello(self):
    # for i in range(20):
    #     self.update_state(state='PROGRESS', meta={"progress": i}, )
    #     time.sleep(1)
    #     print(i)
    driv = mycelery.login()
    ticket_dict, dri = mycelery.tongcheng(driv, "北京", "天津")
    return "ok"
# ret = mycelery_test.hello.delay()
# ret1 = mycelery_test.hello.delay()
# ret2 = mycelery_test.hello.delay()
# ret.state
# ret1.state
# ret2.state
# ret._get_task_meta()
# ret._get_task_meta().get("result")
# ret._get_task_meta().get("status")
