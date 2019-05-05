#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2019/4/3

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = "https://www.evisathailand.com/terms"

desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome()
driver.get(url)

print("next wait")

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

# 上传图片
file = driver.find_element_by_name("passportphoto[]")
f1 = os.path.join(BASE_DIR, "test_file/id.jpg")
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
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable(i))
    time.sleep(2)
    i.click()

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
driver.execute_script('document.getElementById("js-datepicker-datebirth").value="05/06/1990"')
# 设置邮箱
driver.find_element_by_name("email").send_keys("email@email.com")

# 设置手机号
driver.find_element_by_id("pd-mobilenum").send_keys("18612345678")

# 设置护照号码
driver.find_element_by_name("passport_number").send_keys("passport_number")

# 设置签发日期
driver.execute_script('document.getElementById("js-datepicker-pid").value="04/03/2019"')

# 设置有效期
driver.execute_script('document.getElementById("js-datepicker-ped").value="04/03/2024"')

# 设置到达日期
driver.execute_script('document.getElementById("js-datepicker-arrivaldate").value="09/04/2019"')
# 设置到达时间
driver.execute_script('document.getElementsByName("arrival_time")[0].value="0:00"')
# 设置到达航班
driver.find_element_by_name("arrival_flightnum").send_keys("arrival_flightnum")
# 设置出发日期
driver.execute_script('document.getElementById("js-datepicker-departuredate").value="19/04/2019"')
# 设置出发时间
driver.execute_script('document.getElementsByName("departure_time")[0].value="0:00"')
# 设置离开航班
driver.find_element_by_name("departure_flightnum").send_keys("departure_flightnum")
# 住宿类型
select = Select(driver.find_element_by_id('js-place-of-stay'))
select.select_by_value('hotel')
# 设置住宿名称
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, 'pos_name')))
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

upload = driver.find_elements_by_class_name("a-upload-btn")
# 等待图片上传
flag = 0
while flag == 3:
    for i in upload:
        if i.text == "✓ Uploaded":
            flag += 1
        else:
            print("等待图片上传")
            time.sleep(1)
# 提交 js-submitpd
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'js-submitpd'))).click()
# 等待数据处理
time.sleep(0.5)
alert = driver.find_element_by_class_name("m-alert")
if alert:
    print(alert.is_displayed())
    print(driver.find_element_by_class_name("m-alert__message").text)
else:
    print("alert 未弹出！")
