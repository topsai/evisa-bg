#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/4/3
from selenium import webdriver
import os
driver = webdriver.Chrome()
url = "http://cn.evisathailand.com/ft"
# driver.get(url)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
jquery = open(os.path.join(BASE_DIR, "static/vendor/jquery/../static/vendor/jquery/jquery.js"), "r").read()

driver.execute_script(jquery)
request_type = "post"
data = '{"nationality": "chn", "airport": "BKK+-+Suvarnabhumi+International+Airport", "arrivaldate":"", "accepttc": "true"}'
ajax_query = '''
            $.ajax({
            url:%s,
            type: %s,
            data: %s, 
            crossDomain: true,
            xhrFields: {
             withCredentials: true
            },
            success: function(){}
            });
            ''' % (url, request_type, data)

ajax_query = ajax_query.replace(" ", "").replace("\n", "")
resp = driver.execute_script("return " + ajax_query)
