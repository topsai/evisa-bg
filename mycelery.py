#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2019/4/26


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

qunaer_cookie = [{'domain': '.ctrip.com', 'expiry': 1558935740, 'httpOnly': False, 'name': 'appFloatCnt', 'path': '/',
                  'secure': False, 'value': '2'},
                 {'domain': '.ctrip.com', 'httpOnly': False, 'name': '_bfi', 'path': '/', 'secure': False,
                  'value': 'p1%3D10320670296%26p2%3D0%26v1%3D1%26v2%3D0'},
                 {'domain': '.ctrip.com', 'expiry': 4042022400, 'httpOnly': False, 'name': '_RDG', 'path': '/',
                  'secure': False, 'value': '28f772448e212b211b3d4df12adcb93e07'},
                 {'domain': '.ctrip.com', 'expiry': 1619415367, 'httpOnly': False, 'name': '_bfa', 'path': '/',
                  'secure': False, 'value': '1.1556343367507.49uh1o.1.1556343367507.1556343367507.1.1'},
                 {'domain': '.ctrip.com', 'expiry': 4042022400, 'httpOnly': False, 'name': '_RF1', 'path': '/',
                  'secure': False, 'value': '123.116.229.199'},
                 {'domain': '.ctrip.com', 'expiry': 1556345167, 'httpOnly': False, 'name': '_bfs', 'path': '/',
                  'secure': False, 'value': '1.1'},
                 {'domain': '.ctrip.com', 'expiry': 1556429766.731, 'httpOnly': False, 'name': 'gad_city', 'path': '/',
                  'secure': False, 'value': '96617ee7af8aedd02bbece8583e0066e'},
                 {'domain': '.ctrip.com', 'expiry': 1556948540, 'httpOnly': False, 'name': 'MKT_Pagesource',
                  'path': '/',
                  'secure': False, 'value': 'PC'},
                 {'domain': '.ctrip.com', 'expiry': 1556430140, 'httpOnly': False, 'name': '_gid', 'path': '/',
                  'secure': False, 'value': 'GA1.2.1103865373.1556343734'},
                 {'domain': '.ctrip.com', 'httpOnly': True, 'name': 'cticket', 'path': '/', 'secure': False,
                  'value': '45137DCB2FAFCB6EF8E943A5501003FCCB6AEAE72C2976E6CCC459461BADAEBC'},
                 {'domain': '.ctrip.com', 'expiry': 4042022400, 'httpOnly': False, 'name': '_RSG', 'path': '/',
                  'secure': False, 'value': '.iaxLlLyoW9W0lN5tP4nqA'},
                 {'domain': '.ctrip.com', 'expiry': 4042022400, 'httpOnly': False, 'name': '_RGUID', 'path': '/',
                  'secure': False, 'value': '9832f15b-d5ee-4b3e-ad31-119dc55ef020'},
                 {'domain': '.ctrip.com', 'httpOnly': False, 'name': 'DUID', 'path': '/', 'secure': False,
                  'value': 'u=D1ABE5C37FB224228FF26B9F20071D9165EF7F96F3E58E2AEA6081721283C327&v=0'},
                 {'domain': '.ctrip.com', 'httpOnly': False, 'name': 'IsNonUser', 'path': '/', 'secure': False,
                  'value': 'F'},
                 {'domain': '.ctrip.com', 'httpOnly': True, 'name': 'ticket_ctrip', 'path': '/', 'secure': False,
                  'value': 'uoeOwviAJ6VQEgTNwLuTqSV9j/bS+aOP3Riia1P+kyQbgkQZsD2gic9pphJTvHJCEY+O6HpnATIDu5IkKYSiUfKiWE9FiRBzp+h/j5CkUwj3OTkomR7l0rAEm6XZT8M6Vya2i/UGKk1wWxFPCJ1bnYfOQnDmWbbgtgrUXVWj1xxtSKKEFHl1FktUPbO5uzeQb0LNIgkGpvw9h4Ki//4HqDkb6HuaIZ8j3d0TRnomH8kdqzGCEIgMv9mXl8rHGjWg/i1e9/OzyV+9sBY3xcgSPc38+DCnPNHO5M18XhwsqIwlsEjBAWnJfKJ+QOq9d6KYeITl7PK4bfM='},
                 {'domain': '.ctrip.com', 'httpOnly': False, 'name': 'corpid', 'path': '/', 'secure': False,
                  'value': ''},
                 {'domain': '.ctrip.com', 'httpOnly': False, 'name': 'corpname', 'path': '/', 'secure': False,
                  'value': ''},
                 {'domain': '.ctrip.com', 'httpOnly': False, 'name': 'AHeadUserInfo', 'path': '/', 'secure': False,
                  'value': 'VipGrade=0&UserName=&NoReadMessageCount=1&U=6EC36BB6F8E289EAAFA0AA93D4BCF59E8793CC616EF1AD24'},
                 {'domain': '.ctrip.com', 'expiry': 1556948530.498521, 'httpOnly': False, 'name': 'Union', 'path': '/',
                  'secure': False,
                  'value': 'AllianceID=1881&SID=2209&OUID=72EA79890E37DA146F1E605D5EAC31D6%7c100.1030.00.000.00'},
                 {'domain': '.ctrip.com', 'expiry': 1558935730.498698, 'httpOnly': False, 'name': 'Session',
                  'path': '/',
                  'secure': False,
                  'value': 'SmartLinkCode=U2209&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh'},
                 {'domain': 'my.ctrip.com', 'httpOnly': True, 'name': 'ASP.NET_SessionSvc', 'path': '/',
                  'secure': False,
                  'value': 'MTAuOC4xODkuNTh8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTU1NjAzMTMxNzE2NA'},
                 {'domain': 'my.ctrip.com', 'httpOnly': True, 'name': 'ASP.NET_SessionId', 'path': '/', 'secure': False,
                  'value': 'efigxipgrzftsq21g4xlkq50'},
                 {'domain': 'my.ctrip.com', 'httpOnly': False, 'name': 'MyCtripDescription', 'path': '/',
                  'secure': False,
                  'value': 'UID=6EC36BB6F8E289EAAFA0AA93D4BCF59E88982A0DC5AE1C07&IsClub140=F&IsHoliday=F&CorpMileage=F'},
                 {'domain': '.ctrip.com', 'expiry': 1619415740, 'httpOnly': False, 'name': '_ga', 'path': '/',
                  'secure': False, 'value': 'GA1.2.1316613482.1556343734'}]
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


def login():
    # qunaer
    # url = "https://my.ctrip.com/home/myinfo.aspx"
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
        print("ok")
    else:
        print("err")
    return driver
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
    return ticket_dict, driver

    # for i in train_info:
    #     print(i)

    # 余票


# ticket_dict, dri = tongcheng(driv, "北京", "天津")


def buy_ticket(seat, data, driver):
    price, balance, btn = data.get(seat)
    print(seat, price, balance)
    btn.click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'nameValue')))
    driver.find_element_by_class_name("nameValue").send_keys("xingming")
    driver.find_element_by_class_name("cardNoValue").send_keys("130102199105139235")
    driver.find_element_by_class_name("phoneNum").send_keys("18612345678")
    driver.find_element_by_class_name("post_order_btn").click()


# buy_ticket("硬卧", ticket_dict, dri)
from celery import Celery

app = Celery('hello', broker='redis://10.0.0.14', backend='redis://10.0.0.14')


@app.task
def hello():
    ret = login()
    return ret


"https://www.ly.com/huochepiao/Pages/Order.aspx?trainType=Z&TrainNo=Z157&SeatType=hardseat&FromCity=%E5%8C%97%E4%BA%AC&ToCity=%E9%95%BF%E6%98%A5"

'''
trainType: Z
TrainNo: Z157
SeatType: hardseat
FromCity: 北京
ToCity: 长春
'''
