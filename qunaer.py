#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/4/18


import requests

url = "https://tieyo.trade.qunar.com/site/booking/purchase.jsp"
data = {
    "train": "Z175",
    "dptHm": "00:03",
    "fromstation": "南京",
    "tostation": "杭州",
    "starttime": "20190419",
    "seat": "无座"
}

# r = requests.get(url, params=data)
# print(r.text)

posturl = "https://tieyo.trade.qunar.com/site/booking/purchaseCheck.jsp"
postdata = {
    "insuranceCorpCode": "TK",
    "trainSeat": "无座",
    "ticketCount": 1,
    "trainFrom": "南京",
    "trainTo": "杭州",
    "trainStartTime": "201904190003",
    "trainEndTime": "201904190554",
    "trainDistance": 936,
    "trainDuration": 351,
    "trainNo": "Z175",
    "ex_track": "noextrack",
    "pricesInformation": "无座:69",
    "isCheckPrice": 1,
    "needCheckHistoryOrder": "true",
    "pTicketType_0": 1,
    "pName_0": "发送",
    'pCertType_0': 0,
    'pCertNo_0': '370304199110131615',
    'pGender_0': 1,
    'pBirthDate_0': '19911013',
    'contact_name': '发送',
    'contact_phone': '18612365482',
    'expressPrice': 0,
    'license': 'on',
    'isPackageService': 'false',
    'packagePrice': 0,
    'packageId': -1,
    'isRecommendPaper': 'false',
    'passenger_member': 'nfm',
    'isNeedPaper': 'false',
    'acceptOtherSeat': 'false',
    'ticketToStationSelected': 'false',
    # paperProvinceCode:
    # paperCityCode:
    # paperDistrictCode:
    # mailcode:
    # receiptType:
    # receiptTitle:
    # taxNumber:
    # hasKnown:
    # paperProvinceName:
    # paperCityName:
    # paperDistrictName:
    # paperType:
    # seatCodeList:
    # seatSpecifiedCount:
    # fromCity:
    # toCity:
    # refuseAir:

}

r = requests.get(posturl, params=postdata)
print(r.text)
{
    "orderDetailUrl": "/site/order/detail.jsp?orderNo=tieyo190418170453db7&md5=8aefd117eeb80772fa834d7cd34b02368d95c9c60afa46fc133367b6f19a1cca95cd7bf28327b979f099a07707d539b2",
    "status": 0, "cburl": "/site/booking/payment.jsp",
    "params": {"orderNo": "tieyo190418170453db7", "ex_track": "noextrack", "sig": "7407ccfc4c19e2f7e01f13d1ac38eb08"}}

'https://tieyo.trade.qunar.com/site/Occupy/trainServerJudge.jsp'

# judgeType: 2
# orderNo: tieyo190418165957ddb
# contactPhone: 15171661471
# useNewOccupyConf: true

# 支付页面
# https://tieyo.trade.qunar.com/site/booking/payment.jsp?orderNo=tieyo190418165957ddb&ex_track=noextrack&sig=c1f87b64e84bd93a75bdc293fd76591a
# https://tieyo.trade.qunar.com/site/booking/payment.jsp?orderNo=tieyo190418170453db7&ex_track=noextrack&sig=7407ccfc4c19e2f7e01f13d1ac38eb08


# orderNo: tieyo190418165957ddb
# ex_track: noextrack
# sig: c1f87b64e84bd93a75bdc293fd76591a