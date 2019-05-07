#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/5/5

from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
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

xiecheng_cookies = [
    {'domain': '.ly.com', 'expiry': 1587910564, 'httpOnly': False, 'name': 'Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5',
     'path': '/', 'secure': False, 'value': '1556374536'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': '__tctmu', 'path': '/', 'secure': False, 'value': '144323752.0.0'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': '__tccgd', 'path': '/', 'secure': False, 'value': '144323752.0'},
    {'domain': 'member.ly.com', 'httpOnly': False, 'name': 'route', 'path': '/', 'secure': False,
     'value': '47050ac27666c09cd98dad27fee75141'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'longKey', 'path': '/', 'secure': False,
     'value': '1556374555305678'},
    {'domain': 'member.ly.com', 'httpOnly': True, 'name': 'ASP.NET_SessionId', 'path': '/', 'secure': False,
     'value': 'qnpbnoswlikuz2iipstrlvy1'},
    {'domain': '.ly.com', 'expiry': 1619446564, 'httpOnly': False, 'name': '__tctma', 'path': '/', 'secure': False,
     'value': '144323752.1556374555305678.1556374555207.1556374555207.1556374555207.1'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': '__tctmz', 'path': '/', 'secure': False,
     'value': '144323752.1556374555207.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none)'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': '__tctrack', 'path': '/', 'secure': False, 'value': '0'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'NewProvinceId', 'path': '/', 'secure': False, 'value': '3'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'NCid', 'path': '/', 'secure': False, 'value': '53'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'NewProvinceName', 'path': '/', 'secure': False,
     'value': '%E5%8C%97%E4%BA%AC'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'NCName', 'path': '/', 'secure': False,
     'value': '%E5%8C%97%E4%BA%AC'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'passport_login_state', 'path': '/', 'secure': False,
     'value': 'pageurl=&loginfrom=6281871&partner_loginname=%e5%be%80%e4%ba%8b&aloneid=5993425&OpenId=7E1F6585C152E8A00C1071D3185B292D&uid=5993425&memberid=30649624'},
    {'domain': '.ly.com', 'expiry': 1558966564.626421, 'httpOnly': True, 'name': 'cnUser', 'path': '/', 'secure': False,
     'value': 'userid=30649624&token=106106046195065029085079135032052105084246209011225251116187255042044033026207119162157200247167189252123209023125041202031189109067189228091111117168059187023057039131147139019058115113155097220153146158107162122106&loginType=passport'},
    {'domain': '.ly.com', 'expiry': 1558966564.626364, 'httpOnly': False, 'name': 'us', 'path': '/', 'secure': False,
     'value': 'userid=30649624&nickName=%e8%8c%83%e6%96%af%e7%89%b9%e7%bd%97%e5%a4%ab%e6%96%af%e5%9f%ba&level=1&isUpgrade=true'},
    {'domain': '.ly.com', 'expiry': 1556376364, 'httpOnly': False, 'name': '__tctmb', 'path': '/', 'secure': False,
     'value': '144323752.1676347613610322.1556374539476.1556374560347.2'},
    {'domain': '.ly.com', 'expiry': 1587996964.166961, 'httpOnly': False, 'name': 'nus', 'path': '/', 'secure': False,
     'value': 'userid=30649624&nickName=%e8%8c%83%e6%96%af%e7%89%b9%e7%bd%97%e5%a4%ab%e6%96%af%e5%9f%ba&level=1'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5', 'path': '/',
     'secure': False, 'value': '1556374565'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'qdid', 'path': '/', 'secure': False, 'value': '-9999'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': '17uCNRefId', 'path': '/', 'secure': False,
     'value': 'RefId=0&SEFrom=&SEKeyWords='},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'TicketSEInfo', 'path': '/', 'secure': False,
     'value': 'RefId=0&SEFrom=&SEKeyWords='},
    {'domain': '.ly.com', 'httpOnly': False, 'name': 'CNSEInfo', 'path': '/', 'secure': False,
     'value': 'RefId=0&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl='},
    {'domain': '.ly.com', 'httpOnly': False, 'name': '__tctmc', 'path': '/', 'secure': False,
     'value': '144323752.114854299'},
    {'domain': '.ly.com', 'httpOnly': False, 'name': '__tctmd', 'path': '/', 'secure': False,
     'value': '144323752.737325'}]


@shared_task
def login():
    # 同程
    url = 'https://member.ly.com/'

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
    # chrome_options.add_argument('--headless')
    # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    # 手动指定使用的浏览器位置
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get(url)
    ret = {"driver": driver, "state": None}
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'showName')))
    try:
        uname = driver.find_element_by_id("showName").text
    except:
        uname = None
    if uname == "范斯特罗夫斯基":
        print("登陆未失效")
        ret["state"] = "login_ok"
        return ret
    else:
        print("登陆失效")
        print("继续登陆")

    driver.delete_all_cookies()
    for i in xiecheng_cookies:
        driver.add_cookie(i)
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'showName')))
    uname = driver.find_element_by_id("showName").text
    ###
    # driver.find_elements_by_class_name()
    ###
    if uname == "范斯特罗夫斯基":
        print("登陆成功")
        ret["state"] = "login_ok"
        print("ok")
    else:
        print("err")
        ret["state"] = "login_err"
    # print(ret)
    return ret
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'member-id')))
    # uname = driver.find_element_by_class_name("member-id").text
    # print(uname)
    # if uname == "范先生":
    #     print("登陆成功")
    #     return "ok"
    # return "err"


# driv = login()


# name, id_card, train, seat, starttime, phone
def tongcheng(driver, fromstation, tostation, ):
    # 查询余票及价格
    url = "https://www.ly.com/huochepiao/"
    driver.get(url)
    # 出发站
    driver.execute_script('document.getElementById("txtLeaveCity").value ="{}"'.format(fromstation))
    # driver.find_element_by_id("txtLeaveCity").send_keys(fromstation)
    # 到达站
    driver.execute_script('document.getElementById("txtArriveCity").value ="{}"'.format(tostation))
    # driver.find_element_by_id("txtArriveCity").send_keys(tostation)
    # driver.execute_script('document.getElementsByClassName("calendar-panel")[0].style.display="none"')
    # 关闭所有弹出框
    driver.find_element_by_id("seach_title").click()
    # 搜索
    driver.find_element_by_id("trainSearchSubmit").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'list_item')))
    # 定位车次
    train_info = driver.find_element_by_xpath("//*[text()='2601']/../..")
    train_info = train_info.find_elements_by_tag_name("td")
    # 车次
    # train_info[0].text
    # 出发到达时间
    # train_info[1].text
    # 出发到达站点
    # train_info[2].text
    # 耗时
    # train_info[3].text
    # 座次/票价 seat_item  seat_name
    seat_item = train_info[4].find_elements_by_class_name("seat_item")
    seat_item_list = []
    for i in seat_item:
        # 座次
        wseat = i.find_element_by_class_name("seat_name").text
        print(wseat)
        # 价格
        count = i.find_element_by_class_name("v_middle").text
        print(count)
        seat_item_list.append([wseat, count])

    # 余票 ticket_num
    ticket_num = train_info[5].find_elements_by_class_name("ticket_num")
    ticket_num_list = []
    for i in ticket_num:
        # 余票数量
        ticket_num_list.append(i.find_element_by_class_name("color_1th").text)

    # 购买按钮 order_btn
    order_btn = train_info[6].find_elements_by_tag_name("button")
    order_btn_list = []
    for i in order_btn:
        order_btn_list.append(i)
    # 座次，价格，购买按钮整合为字典
    i = 0
    ticket_dict = {}
    while i < len(seat_item_list):
        dic = {seat_item_list[i][0]: [seat_item_list[i][1], ticket_num_list[i], order_btn_list[i]]}
        ticket_dict.update(dic)
        i += 1
    print(ticket_dict)
    return driver, ticket_dict


def buy_ticket(driver, seat, data):
    price, balance, btn = data.get(seat)
    print(seat, price, balance)
    btn.click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'nameValue')))
    driver.find_element_by_class_name("nameValue").send_keys("xingming")
    driver.find_element_by_class_name("cardNoValue").send_keys("130102199105139235")
    driver.find_element_by_class_name("phoneNum").send_keys("18612345678")
    driver.find_element_by_class_name("post_order_btn").click()
    flag = True
    i = 0
    while flag:
        try:
            tongcheng_order_id = driver.find_element_by_xpath("//span[contains(text(),'同程火车票支付')]")
            print(tongcheng_order_id.text)
            print("跳转成功，退出循环")
            flag = False
        except Exception as e:
            print(e)

        time.sleep(1)
        i += 1
        print("sleep", i)
        assert i < 60, print("支付跳转超时", i)

    return driver


def pay(driver):
    # $("#alipaySubmitBtn span").click()
    pay_tab = driver.find_element_by_id("alipaySubmitBtn")
    pay_tab.find_element_by_tag_name("span").click()
    print("支付完成")


@shared_task(bind=True)
def buysome(self):
    self.update_state(state='opening', meta={"progress": "open"}, )
    ret = login()
    # ret = {"driver": driver, "state": None}
    if ret.get("state") == "login_ok":
        self.update_state(state='buy', meta={"progress": "login"}, )
    else:
        print("login_file")

    driver = ret.get("driver")
    driver, ticket_dict = tongcheng(driver, "北京", "天津")
    try:
        # 提交个人信息
        driver = buy_ticket(driver, "硬座", ticket_dict)
    except Exception as e:
        print(e)
        self.update_state(state='err', meta={"progress": "err"}, )
        time.sleep(10)
        driver.close()
        return "个人信息有误"

    pay(driver)
    time.sleep(10)
    driver.close()


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
