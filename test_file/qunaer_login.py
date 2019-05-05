#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/4/18

import requests
import re

"""

此代码共分为4部分：初始化模块，获取添加cookies模块，验证码模块，登录模块

"""


def start_get_session():
    session_ = requests.session()  # 得到一个session
    return session_


def get_base_cookies(session_):
    session_.get('https://user.qunar.com/passport/login.jsp')  # 获得cookie参数，原始的QN1
    get_image(session_)  # 通过调用get_image函数，得到验证码图片，同时获得cookie参数QN1，QN25
    session_.get('https://user.qunar.com/passport/addICK.jsp?ssl')  # 获得cookie参数_i，_vi

    """
    由于获取fid参数的url需要cookie参数SESSIONID得到，所以没办法直接得到fid，需要先得到SESSIONID这个参数，再得到fid参数

    """
    # 经过查找发现SESSIONID在这个js文件中，所以先得到它
    response = session_.get('https://rmcsdf.qunar.com/js/df.js?org_id=ucenter.login&js_type=0')
    # 查找SESSIONID
    cookie_SE = re.findall(r'&sessionId=(.*?)&', response.text)[0]  # 通过正则得到SESSIONID

    # 获取fid
    session_.get('https://rmcsdf.qunar.com/api/device/challenge.json?callback=callback_1511693290383&'
                 'sessionId={}&domain=qunar.com&orgId=ucenter.login'.format(cookie_SE))


"""
https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a&t=1555581397624
"""
session_.cookies.update({'QN271': cookie_SE})  # 通过比对发现参数QN271和SESSIONID相同，所以直接加入cookies中


def get_image(session_):
    response = session_.get(
        'https://user.qunar.com/captcha/api/image?k={en7mni(z&'
        'p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a')  # 获得二维码的response

    with open('files/img/code.png', 'wb') as f:
        f.write(response.content)  # 把二维码存进同级img文件夹下命名为code


def login(session_, username, password, vcode):
    data = {
        'loginType': 0,
        'username': username,
        'password': password,
        'remember': 1,
        'vcode': vcode,
    }

    url = 'https://user.qunar.com/passport/loginx.jsp'
    response = session_.post(url, data)  # 通过post请求方式，模拟登录
    print(response.text)


if __name__ == '__main__':  # 主程序，程序入口
    session = start_get_session()  # 实例化一个session
    get_base_cookies(session)  # 调用函数，在session中添加cookie
    username = "hurte@foxmail.com"
    password = "cai@521131"
    vcode = input('请输入验证码：')
    login(session, username, password, vcode)  # 调用登录函数
