#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/4/2

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.evisathailand.com/")
ele = driver.find_element_by_id("exampleFormControlSelect1")
# Select.select_by_value()
# 选择护照国家
ele.find_element_by_xpath("//option[@value='chn']").click()
# next = Select.select_by_value("ui-btn-yellow")
# 点击下一步
next = driver.find_element_by_class_name("ui-btn-yellow")
next.click()
# 同意协议
accept = driver.find_element_by_name("accepttc")
accept.click()
# 上传图片
file = driver.find_element_by_name("passportphoto[]")
file.sendKeys("E:\testfile.jpg")


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# time.sleep(1)
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()