#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2019/4/7

import multiprocessing
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def func(msg):
    print(msg)
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
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


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=25)
    for i in "今天在帮一个兄弟找bug的时候发现了一个与理论知识":
        msg = "hello %s" % (i)

        pool.apply_async(func, (i,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("Sub-process(es) done.")
