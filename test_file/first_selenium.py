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
# desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome()
driver.get(url)

# ele = driver.find_element_by_id("exampleFormControlSelect1")
# # Select.select_by_value()
# # 选择护照国家
# ele.find_element_by_xpath("//option[@value='chn']").click()
# next = Select.select_by_value("ui-btn-yellow")
# 点击下一步
print("next wait")
# is_click_byClass("ui-btn-yellow")
# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ui-btn-yellow'))).click()
# flag = True
# while flag:
#     try:
#         driver.find_element_by_class_name("ui-btn-yellow").click()
#         flag = False
#     except:
#         time.sleep(0.3)

# driver.find_element_by_class_name("ui-btn-yellow").click()
# 同意协议
# WebDriverWait(driver, 10, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)

# is_click_byClass("a-btn -primary")


flag = True
while flag:
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
        flag = False
    except Exception as e:
        print(e)
        time.sleep(0.3)

print("next ok")
# pd-nationality
time.sleep(1)
# 选择国籍
select = Select(driver.find_element_by_id('pd-nationality'))
select.select_by_value('chn')
# 选择机场
select = Select(driver.find_element_by_id('pd-airport'))
select.select_by_value('bkk')
# 选择称谓
select = Select(driver.find_element_by_id('pd-salutation'))
select.select_by_value('mr')
# 设置姓
driver.find_element_by_name("last_name").send_keys("last_name")
# 设置名
driver.find_element_by_name("first_name").send_keys("first_name")
# 选择性别
select = Select(driver.find_element_by_id('pd-gender'))
select.select_by_value('male')

# 设置出生日期
driver.execute_script('document.getElementById("js-datepicker-datebirth").value="ped"')
# driver.find_element_by_id("js-datepicker-datebirth").send_keys("js-datepicker-datebirth")
# 设置邮箱
driver.find_element_by_name("email").send_keys("email")

# 设置手机号
driver.find_element_by_id("pd-mobilenum").send_keys("186")

# 设置护照号码
driver.find_element_by_name("passport_number").send_keys("passport_number")

# 设置签发日期
# driver.find_element_by_id("js-datepicker-pid").send_keys("data")
driver.execute_script('document.getElementById("js-datepicker-pid").value="ped"')

# 设置有效期
# driver.find_element_by_id("js-datepicker-ped").send_keys("ped")
driver.execute_script('document.getElementById("js-datepicker-ped").value="ped"')

# 设置到达日期
# driver.find_element_by_id("js-datepicker-arrivaldate").send_keys("passport_number")
driver.execute_script('document.getElementById("js-datepicker-arrivaldate").value="ped"')
# 设置到达时间
driver.execute_script('document.getElementsByName("arrival_time")[0].value="ped"')
# driver.find_element_by_name("arrival_time").send_keys("time")
# 设置到达航班
driver.find_element_by_name("arrival_flightnum").send_keys("arrival_flightnum")
# 设置出发日期
driver.execute_script('document.getElementById("js-datepicker-departuredate").value="ped"')
# driver.find_element_by_id("js-datepicker-departuredate").send_keys("js-datepicker-departuredate")
# 设置出发时间
driver.execute_script('document.getElementsByName("departure_time")[0].value="ped"')
# driver.find_element_by_name("departure_time").send_keys("departure_time")
# 设置离开航班
driver.find_element_by_name("departure_flightnum").send_keys("departure_flightnum")
# 住宿类型
select = Select(driver.find_element_by_id('js-place-of-stay'))
select.select_by_value('hotel')
# 设置住宿名称

hotelname = driver.find_element_by_name("pos_name")
hotelname.clear()
hotelname.send_keys("sfsf")
# 选择省份
select = Select(driver.find_element_by_name('pos_city_province'))
select.select_by_index(1)

# 选择区
select = Select(driver.find_element_by_name('pos_district'))
select.select_by_index(1)
# 设置住址
driver.find_element_by_name("residential_address").send_keys("residential_address")


# is_click(driver.find_element_by_class_name("ui-btn-yellow"))
# driver.find_element_by_name("accepttc").click()

# driver.find_element_by_tag_name("button").click()
# 上传图片
file = driver.find_element_by_name("passportphoto[]")
f1 = os.path.join(BASE_DIR, "id.jpg")
f2 = os.path.join(BASE_DIR, "test_file/pass.jpg")
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
