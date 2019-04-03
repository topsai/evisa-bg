#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/4/2

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
url = "https://www.evisathailand.com/terms"

# 实例化一个启动参数对象
chrome_options = Options()
# 设置浏览器窗口大小
chrome_options.add_argument('--window-size=1366,768')
# 启动浏览器
# browser = webdriver.Chrome(chrome_options=chrome_options)


def is_click_byClass(ele):
    flag = True
    while flag:
        try:
            driver.find_element_by_class_name(ele).click()
            flag = False
        except Exception as e:
            print(e)
            time.sleep(0.3)


def is_click_byName(ele):
    flag = True
    while flag:
        try:
            driver.find_element_by_name(ele).click()
            flag = False
        except Exception as e:
            time.sleep(0.3)


desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome()
driver.get(url)

jquery = open("jquery.min.js", "r").read()

driver.execute_script(jquery)
request_type = "post"
data = '{"nationality": "chn", "airport": "BKK+-+Suvarnabhumi+International+Airport", "arrivaldate":"", "accepttc": "true"}'
ajax_query = '''
            $.ajax('%s', {
            type: %s,
            data: %s, 
            headers: { "User-Agent": "Mozilla/5.0" },
            crossDomain: true,
            xhrFields: {
             withCredentials: true
            },
            success: function(){}
            });
            ''' % (url, request_type, data)

ajax_query = ajax_query.replace(" ", "").replace("\n", "")
resp = driver.execute_script("return " + ajax_query)











# ele = driver.find_element_by_id("exampleFormControlSelect1")
# # Select.select_by_value()
# # 选择护照国家
# ele.find_element_by_xpath("//option[@value='chn']").click()
# next = Select.select_by_value("ui-btn-yellow")
# 点击下一步
print("next wait")
# is_click_byClass("ui-btn-yellow")
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ui-btn-yellow'))).click()
# flag = True
# while flag:
#     try:
#         driver.find_element_by_class_name("ui-btn-yellow").click()
#         flag = False
#     except:
#         time.sleep(0.3)
print("next ok")
# driver.find_element_by_class_name("ui-btn-yellow").click()
# 同意协议
# WebDriverWait(driver, 10, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)

# is_click_byClass("a-btn -primary")
EC.
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
# is_click(driver.find_element_by_class_name("ui-btn-yellow"))
# driver.find_element_by_name("accepttc").click()

# driver.find_element_by_tag_name("button").click()
# 上传图片
file = driver.find_element_by_name("passportphoto[]")
f1 = os.path.join(BASE_DIR, "id.jpg")
f2 = os.path.join(BASE_DIR, "pass.jpg")
files = """{}
{}""".format(f1, f2)
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
# ele = driver.find_element_by_id("js-place-of-stay")
# ele.find_element_by_xpath("//option[@value='hotel']").click()
select = Select(driver.find_element_by_id('js-place-of-stay'))
select.select_by_value('hotel')
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
