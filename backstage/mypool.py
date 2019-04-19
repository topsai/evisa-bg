#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2019/4/7


from selenium.webdriver.support.select import Select
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from backstage import models
from evisa.settings import ImagePath

ret = {
    "url": None,
    "err": None
}


def func(msg):
    print(msg)
    chrome_options = Options()
    # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--no-sandbox')
    # 指定浏览器分辨率
    chrome_options.add_argument('window-size=1920x3000')
    # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--disable-gpu')
    # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('--hide-scrollbars')
    # 不加载图片, 提升速度
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('--headless')
    # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(msg)
    driver.find_element_by_id("su").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'h3')))
    print(driver.find_element_by_tag_name("h3").text)
    # print('hao123' in driver.page_source)
    print("end", msg)
    driver.close()  # 切记关闭浏览器，回收资源


def process(data):
    url = "https://www.evisathailand.com/terms"

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # driver = webdriver.Chrome()
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

    # 上传护照图片
    passport = driver.find_element_by_name("passportphoto[]")
    passportphoto = """{}\n{}""".format(os.path.join(ImagePath, data.passport_img1),
                                        os.path.join(ImagePath, data.passport_img2))
    print("passportphoto", passportphoto)
    passport.send_keys(passportphoto)
    # 上传机票图片
    ticket = driver.find_element_by_name("ticketphoto[]")
    ticketphoto = """{}\n{}""".format(os.path.join(ImagePath, data.airimg1), os.path.join(ImagePath, data.airimg2))
    print(ticketphoto)
    ticket.send_keys(ticketphoto)
    # 上传行程单图片
    file2 = driver.find_element_by_name("accomodationphoto[]")
    file2.send_keys(os.path.join(ImagePath, data.hotelimg))
    # btn = driver.find_element_by_class_name("a-upload-btn")
    btn = driver.find_elements_by_class_name("a-upload-btn")
    for i in btn:
        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable(i))
        time.sleep(1)
        i.click()

    # 选择国籍
    select = Select(driver.find_element_by_id('pd-nationality'))
    select.select_by_value(data.nationality)
    # 选择机场
    select = Select(driver.find_element_by_id('pd-airport'))
    select.select_by_value(data.airport)
    # 选择称谓
    select = Select(driver.find_element_by_id('pd-salutation'))
    if data.salutation == "M":
        select.select_by_value('mr')
    else:
        select.select_by_value('ms')
    # 设置姓
    driver.find_element_by_name("last_name").send_keys(data.last_name)
    # 设置名
    driver.find_element_by_name("first_name").send_keys(data.first_name)
    # 选择性别
    select = Select(driver.find_element_by_id('pd-gender'))
    if data.gender == "M":
        select.select_by_value('male')
    else:
        select.select_by_value('female')

    # 设置出生日期
    driver.execute_script('document.getElementById("js-datepicker-datebirth").value="{}"'.format(data.birth_date))
    # 设置邮箱
    driver.find_element_by_name("email").send_keys(data.email)

    # 设置手机号
    driver.find_element_by_id("pd-mobilenum").send_keys(data.mobile_number)

    # 设置护照号码
    driver.find_element_by_name("passport_number").send_keys(data.passport_number)

    # 设置签发日期
    driver.execute_script('document.getElementById("js-datepicker-pid").value="{}"'.format(data.passport_issue))

    # 设置有效期
    driver.execute_script('document.getElementById("js-datepicker-ped").value="{}"'.format(data.passport_expiry))

    # 设置到达日期
    driver.execute_script('document.getElementById("js-datepicker-arrivaldate").value="{}"'.format(data.arrival_date))
    # 设置到达时间
    driver.execute_script('document.getElementsByName("arrival_time")[0].value="{}"'.format(data.arrival_time))
    # 设置到达航班
    driver.find_element_by_name("arrival_flightnum").send_keys(data.arrival_flightnum)
    # 设置出发日期
    driver.execute_script(
        'document.getElementById("js-datepicker-departuredate").value="{}"'.format(data.departure_date))
    # 设置出发时间
    driver.execute_script('document.getElementsByName("departure_time")[0].value="{}"'.format(data.departure_time))
    # 设置离开航班
    driver.find_element_by_name("departure_flightnum").send_keys(data.departure_flightnum)
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
    while flag != 3:
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
    try:
        alert = driver.find_element_by_class_name("m-alert")
        if alert:
            print(alert.is_displayed())
            err = driver.find_element_by_class_name("m-alert__message").text
            ret["err"] = err
        else:
            print("alert 未弹出！")
    except Exception as e:
        print(e)

    # "https://www.evisathailand.com/confirm/4ae0a91b254c0eb11b6c2157b5c6b47bc53071af"

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "js-ap-contpayment")))
    pay_url = driver.current_url
    ret["url"] = pay_url
    driver.close()
    return ret


if __name__ == "__main__":
    # pool = multiprocessing.Pool(processes=25)  # 线程数量
    # data = models.Order.objects.filter(state=1).all()[:10]
    data = models.Order.objects.filter(state=1).first()
    process(data)
    #
    # for i in data:
    #     msg = "hello {}".format(i.id)
    #     pool.apply_async(process, (i,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    #
    # print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    # pool.close()
    # pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    # print("Sub-process(es) done.")
