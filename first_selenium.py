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
files = """C:/Users/john/Desktop/project/evisa/id.jpg
C:/Users/john/Desktop/project/evisa/pass.jpg"""
file.send_keys(files)
file1 = driver.find_element_by_name("ticketphoto[]")
file1.send_keys(files)
file2 = driver.find_element_by_name("accomodationphoto[]")
file2.send_keys(files)
# btn = driver.find_element_by_class_name("a-upload-btn")
btn = driver.find_elements_by_class_name("a-upload-btn")
for i in btn:
    i.click()
# 设置护照日期
date = driver.find_element_by_id("js-datepicker-pid").send_keys("20/03/2019")
driver.execute_script("arguments[0].value = '你猜一下';", date)

# 住宿类型
ele = driver.find_element_by_id("js-place-of-stay")
ele.find_element_by_xpath("//option[@value='hotel']").click()
# 住宿名称
driver.find_element_by_name("pos_name").send_keys("fasfasf")
driver.find_element_by_name("pos_city_province").get_attribute()
# 获取城市信息
driver.find_element_by_name("pos_city_province").find_elements_by_tag_name("option")[1].get_attribute("value")
# 区信息
driver.find_element_by_name("pos_district").find_elements_by_tag_name("option")[1].get_attribute("value")
'Amnat Charoen'

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# time.sleep(1)
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()