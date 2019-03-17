#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import base64
import requests

data = {
    "authority": "公安部出入境管理局",
    "birth_date": "19831220",
    "birth_day": "",
    "birth_place": "陕西",
    "birth_place_raw": "陕西/SHAANXI",
    "country": "QKL",
    "expiry_date": "20200107",
    "expiry_day": "",
    "issue_date": "20100108",
    "issue_place": "陕西",
    "issue_place_raw": "陕西/SHAANXI",
    "line0": "PBQKLMUZ<REI<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",
    "line1": "G55770289CHN8312206F200107819206101<<<<<<80",
    "name": "MUZ<REI",
    "name_cn": "穆锐",
    "name_cn_raw": "穆/MU锐/RUI",
    "passport_no": "",
    "person_id": "",
    "request_id": "20190313104729_95ec900d65171545982fc4e970500e90",
    "sex": "F", "src_country": "",
    "success": "true",
    "type": "PB"
}


def get_img_base64(img_file):
    with open(img_file, 'rb') as infile:
        s = infile.read()
        return base64.b64encode(s).decode()


def predict(url, appcode, img_base64, kv_configure):
    param = {}
    param['image'] = img_base64
    if kv_configure is not None:
        param['configure'] = json.dumps(kv_configure)
    body = json.dumps(param)
    headers = {'Authorization': 'APPCODE %s' % appcode}
    # request = urllib.Request(url=url, headers=headers, data=body)
    r = requests.post(url=url, headers=headers, data=body)
    # try:
    #     response = urllib.urlopen(request, timeout=10)
    #     return response.code, response.headers, response.read()
    # except urllib.HTTPError as e:
    #     return e.code, e.headers, e.read()
    try:
        r = requests.post(url=url, headers=headers, data=body)
        return r.status_code, r.headers, r.text
    except Exception as e:
        print(e)


def demo(img):
    appcode = '080fdbbfde1f4a829ed4988ea90a2fa5'
    url = 'http://ocrhz.market.alicloudapi.com/rest/160601/ocr/ocr_passport.json'
    img_file = img
    configure = None
    # configure = {'side': 'face'}
    # 如果没有configure字段，configure设为None
    # configure = None

    img_base64data = get_img_base64(img_file)
    stat, header, content = predict(url, appcode, img_base64data, configure)
    if stat != 200:
        print('Http status code: ', stat)
        print('Error msg in header: ', header['x-ca-error-message'] if 'x-ca-error-message' in header else '')
        print('Error msg in body: ', content)
        exit()
    result_str = content

    print(result_str)
    # result = json.loads(result_str)


if __name__ == '__main__':
    demo()
