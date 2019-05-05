#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/4/18

# 用webdriver登录并获取cookies，并用requests发送请求，以豆瓣为例
from selenium import webdriver
import requests
import time
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import sys


def main():
    # 从命令行参数获取登录用户名和密码
    user_name = "*"
    password = "*"
    main_cookie = None

    # 豆瓣登录页面URL
    login_url = 'https://user.qunar.com/passport/login.jsp'

    # 获取chrome的配置
    opt = webdriver.ChromeOptions()
    # 在运行的时候不弹出浏览器窗口
    # opt.set_headless()
    # from selenium.webdriver import ActionChains
    # 获取driver对象
    driver = webdriver.Chrome(chrome_options=opt)
    # 当前页面句柄
    main_handle = driver.current_window_handle
    # 所有页面句柄
    driver.window_handles
    # 打开新标签
    driver.execute_script("window.open('', '_blank');")
    # 打开登录页面
    driver.get(login_url)
    print('opened login page...')
    # 向浏览器发送用户名、密码，并点击登录按钮
    driver.find_element_by_class_name("pwd-login").click()
    time.sleep(1)
    driver.find_element_by_class_name("login_qq").click()
    time.sleep(1)
    driver.switch_to.frame('ptlogin_iframe')
    driver.find_element_by_id("img_out_474295701").click()

    # driver.find_element_by_name('username').send_keys(user_name)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id("x_btn_login").click()
    # 获取验证码焦点，且对本元素截图
    ele = driver.find_element_by_id("vcodeImg")
    ele.screenshot("C:\\Users\\Public\\ele.png")
    img = Image.open("C:\\Users\\Public\\ele.png")
    img.show()
    img.close()
    # 获取 cookie 列表
    main_cookie = driver.get_cookies()
    # # 验证码
    # driver.find_element_by_name('vcode').send_keys(password)
    # # 多次登录需要输入验证码，这里给一个手工输入验证码的时间
    # time.sleep(6)
    # driver.find_element_by_class_name('btn-submit').submit()
    # print('submited...')
    # # 等待2秒钟
    # time.sleep(2)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'm-uf-userinfo-name')))
    print(driver.find_element_by_class_name('m-uf-userinfo-name').text)

    ticket_info = {
        "train": "G109",
        "fromstation": "北京南",
        "tostation": "上海虹桥",
        "seat": "二等座",
        "starttime": "20190420"
    }
    """
    
    """
    "https://tieyo.trade.qunar.com/site/booking/purchase.jsp?train=G109&dptHm=08%3A15&fromstation=%E5%8C%97%E4%BA%AC%E5%8D%97&tostation=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&starttime=20190420&seat=%E4%BA%8C%E7%AD%89%E5%BA%A7"
    "https://tieyo.trade.qunar.com/site/booking/purchase.jsp?train=G109&fromstation=%E5%8C%97%E4%BA%AC%E5%8D%97&tostation=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&seat=%E4%BA%8C%E7%AD%89%E5%BA%A7&starttime=20190420"

    train, fromstation, tostation, seat, starttime = None
    ticket_url = "https://tieyo.trade.qunar.com/site/booking/purchase.jsp?train={}&fromstation={}&tostation={}&seat={}&starttime={}".format(
        train, fromstation, tostation, seat, starttime)
    driver.get(ticket_url)
    # # 创建一个requests session对象
    # s = requests.Session()
    # # 从driver中获取cookie列表（是一个列表，列表的每个元素都是一个字典）
    # cookies = driver.get_cookies()
    # # 把cookies设置到session中
    # for cookie in cookies:
    #     s.cookies.set(cookie['name'], cookie['value'])
    # # 关闭driver
    # driver.close()
    #
    # # 需要登录才能看到的页面URL
    # page_url = 'https://www.douban.com/accounts/'
    # # 获取该页面的HTML
    # resp = s.get(page_url)
    # resp.encoding = 'utf-8'
    # print('status_code = {0}'.format(resp.status_code))
    # # 将网页内容存入文件
    # with open('html.txt', 'w+') as  fout:
    #     fout.write(resp.text)
    #
    # print('end')
    # 跳转页面
    driver.switch_to.window()
    # 当前打开的标签列表
    driver.window_handles


if __name__ == '__main__':
    main()
