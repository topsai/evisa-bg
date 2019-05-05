from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib.auth.models import User
from backstage import models
from django.contrib.auth import authenticate
import requests
# 导入requests_toolbelt库使用MultipartEncoder
# from requests_toolbelt import MultipartEncoder
import requests
import time
import random
import base64
import json
import threading
import os
from evisa.settings import ImagePath
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from evisa.settings import BASE_DIR

# from backstage import mypool

url = 'https://www.evisathailand.com/images/upload'
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'www.evisathailand.com',
    'Origin': 'https://www.evisathailand.com',
    'Referer': 'https://www.evisathailand.com/ft',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.16 Safari/537.36'
}
driver = None
chrome_state = 0


def open_chrome():
    opt = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=opt)
    login_url = 'https://user.qunar.com/passport/login.jsp'
    # 打开登录页面
    driver.get(login_url)
    print('opened login page...')
    # 向浏览器发送用户名、密码，并点击登录按钮
    driver.find_element_by_class_name("pwd-login").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'login_qq')))
    driver.find_element_by_class_name("login_qq").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'ptlogin_iframe')))
    driver.switch_to.frame('ptlogin_iframe')
    driver.find_element_by_id("img_out_474295701").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, 'password')))
    # driver.find_element_by_name('username').send_keys(user_name)
    driver.find_element_by_name('password').send_keys("cai@521131")
    driver.find_element_by_id("x_btn_login").click()


# open_chrome()
[{'domain': '.qunar.com', 'expiry': 2145916559.817546, 'httpOnly': False, 'name': 'QN1', 'path': '/', 'secure': False,
  'value': 'dXrgkVzD0JlWBUZYpE0lAg=='},
 {'domain': '.qunar.com', 'expiry': 3703820534.986593, 'httpOnly': False, 'name': '_i', 'path': '/', 'secure': False,
  'value': 'RBTKSaSKJHHqy2Wx6nHJSleNT2bx'},
 {'domain': '.qunar.com', 'expiry': 1556941676, 'httpOnly': False, 'name': 'QN205', 'path': '/', 'secure': False,
  'value': 'organic'}, {'domain': '.qunar.com', 'httpOnly': True, 'name': '_o', 'path': '/', 'secure': False,
                        'value': 'B1nbA5cXprIKRzqys4srNchU94NJ7hm-gph70OkFLgqUkCNII-kCTyDznb6dOT9H82XQOQkxzL5wOYzTwK0PJdlJmdFGjum6WfxRWDtc_AJG08WQtyifXHQbQScRh2xQmZZDoJggcjLOkHROhoSWJbYMYO4MXeP8-8zpvOZiJlMr'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN25', 'path': '/', 'secure': False,
  'value': '3cd141c5-c914-439c-9d63-e386e44c8658-9f992f90'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN28', 'path': '/', 'secure': False, 'value': 'qq'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN19', 'path': '/', 'secure': False,
  'value': 'x-cHNMrr1pC0StgmY8Ptzm8yXjpeapQkUurxFGYZu3nGNCedyA4QH3wCxWQLoze_9Owrnwh4IFeV4UbY3NHShfo3r9mfMLt3tbf39534edded1f920d70f29b26fe50a991922611321'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN16', 'path': '/', 'secure': False, 'value': '1'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN15', 'path': '/', 'secure': False, 'value': '6572256%40qq'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN21', 'path': '/', 'secure': False,
  'value': '%E5%BE%80%E4%BA%8B%40qq'},
 {'domain': '.qunar.com', 'expiry': 1558928877, 'httpOnly': False, 'name': 'QN269', 'path': '/', 'secure': False,
  'value': '3BE98800689F11E9AAEFFA163E642F8B'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN42', 'path': '/', 'secure': False, 'value': 'iosm6549'},
 {'domain': '.qunar.com', 'expiry': 3703820524.043566, 'httpOnly': False, 'name': 'fid', 'path': '/', 'secure': False,
  'value': 'c2c71498-f4d8-4967-a7d8-af28b5d3ecc9'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN43', 'path': '/', 'secure': False, 'value': '4'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': '_q', 'path': '/', 'secure': False, 'value': 'U.ryfoaho4347'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': '_t', 'path': '/', 'secure': False, 'value': '26180868'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'csrfToken', 'path': '/', 'secure': False,
  'value': 'FAKCr2MpVdKpRQVytqHqEpnQbesPuppi'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': '_s', 'path': '/', 'secure': False,
  'value': 's_CKESNOCQGIOYOOAGVCPBHNXMDI'},
 {'domain': '.qunar.com', 'httpOnly': True, 'name': '_v', 'path': '/', 'secure': False,
  'value': 'RyTYTyM3isS_FR4I7yQ6_Q2xFW__yt8x47S0FlNSpEOmXILuMCk-GsOJrLS3e9UDZjXCzedEkfps7pW0l4suQfR7VanvZ5ILGY24iJM2N84X73GjExaxu6oMO_9gmnVcUTDt4ZM3UfMGF9YuY1IbqELY3DPF-OBNphSjnN5QeHSp'},
 {'domain': '.qunar.com', 'expiry': 1564112887.986646, 'httpOnly': True, 'name': '_vi', 'path': '/', 'secure': False,
  'value': 'RQ1l6DZI15SPiljpUA_O6JI9W1P0UaLbQovJMJfDyftu_JsJeNtZyl72wTck5HaONR00IEjqVHw-dmbNilHeepHtxj6FHR3gNc54H7-BsRn3szIe9HAO_jDH8jizpgb5xnVA53yVpPNpaRFD6nkZ5w_-uftgOP81kVJZbjMftthO'},
 {'domain': 'user.qunar.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False,
  'value': '71330E8DB64BD92DA0F82AB353487DEA'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN44', 'path': '/', 'secure': False, 'value': 'ryfoaho4347'},
 {'domain': '.qunar.com', 'expiry': 2345341688.012183, 'httpOnly': False, 'name': 'QN48', 'path': '/', 'secure': False,
  'value': 'tc_95bc89a444fa227c_16a5ce8377b_5fc6'},
 {'domain': '.qunar.com', 'httpOnly': False, 'name': 'QN271', 'path': '/', 'secure': False,
  'value': 'cce87517-7e4b-4118-bd54-86d76656457d'}]


# from Crypto.Cipher import AES


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))
        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')
        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]


def jiemi(appId, sessionKey, encryptedData):
    # appId = 'wx4f4bc4dec97d474b'
    # sessionKey = 'tiihtNczf5v6AKRyjwEUhQ=='
    # encryptedData = 'CiyLU1Aw2KjvrjMdj8YKliAjtP4gsMZMQmRzooG2xrDcvSnxIMXFufNstNGTyaGS9uT5geRa0W4oTOb1WT7fJlAC+oNPdbB+3hVbJSRgv+4lGOETKUQz6OYStslQ142dNCuabNPGBzlooOmB231qMM85d2/fV6ChevvXvQP8Hkue1poOFtnEtpyxVLW1zAo6/1Xx1COxFvrc2d7UL/lmHInNlxuacJXwu0fjpXfz/YqYzBIBzD6WUfTIF9GRHpOn/Hz7saL8xz+W//FRAUid1OksQaQx4CMs8LOddcQhULW4ucetDf96JcR3g0gfRK4PC7E/r7Z6xNrXd2UIeorGj5Ef7b1pJAYB6Y5anaHqZ9J6nKEBvB4DnNLIVWSgARns/8wR2SiRS7MNACwTyrGvt9ts8p12PKFdlqYTopNHR1Vf7XjfhQlVsAJdNiKdYmYVoKlaRv85IfVunYzO0IKXsyl7JCUjCpoG20f0a04COwfneQAGGwd5oa+T8yO5hzuyDb/XcxxmK01EpqOyuxINew=='
    iv = 'r7BXXKkLb8qrSNn05n0qiA=='
    pc = WXBizDataCrypt(appId, sessionKey)
    print(pc.decrypt(encryptedData, iv))


# Create your views here.
def get_img_base64(img_file):
    with open(img_file, 'rb') as infile:
        s = infile.read()
        return base64.b64encode(s).decode('UTF-8')


def predict(u, appcode, img_base64, kv_configure):
    param = {}
    param['image'] = img_base64
    if kv_configure is not None:
        param['configure'] = json.dumps(kv_configure)
    body = json.dumps(param)
    headers = {'Authorization': 'APPCODE %s' % appcode}
    # request = urllib.Request(url=url, headers=headers, data=body)
    # r = requests.post(url=url, headers=headers, data=body)
    # try:
    #     response = urllib.urlopen(request, timeout=10)
    #     return response.code, response.headers, response.read()
    # except urllib.HTTPError as e:
    #     return e.code, e.headers, e.read()
    try:
        print('try predict')
        r = requests.post(url=u, headers=headers, data=body)
        print(r.status_code, r.headers, r.text)
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
        content = None
    result_str = content

    print(result_str)
    return result_str


def cookie_auth(func):
    def weaper(request, *args, **kwargs):
        cookies = request.session.get('name')
        if cookies:
            return func(request)
        else:
            return redirect('/login/')

    return weaper


def login(request):
    if request.method == 'GET':
        return render(request, 'sb2/login.html')
    else:
        name = request.POST.get('username')
        pwd = request.POST.get('pwd')
        print(name, pwd)
        # obj=models.Girl.objects.filter(username=name,passwprd=pwd).first()
        # obj = User.objects.filter(username=name, password=pwd).first()
        user = authenticate(username=name, password=pwd)
        # obj = models.Boy.objects.filter(username=name, passwprd=pwd).first()
        if user:
            # 1、生成随机字符串（sessionID）
            # 2、通过cookie发送给客户端
            # 3、服务端保存{zhanggen随机字符串:{'name':'fan'.'email':'hurte@foxmail.com'}}
            request.session['name'] = user.username  # 在Django 中一句话搞定
            print(request.session)
            return redirect('/index')
        else:
            print("err")
            return render(request, 'sb2/login.html', {'msg': "用户名/密码错误"})


@cookie_auth
def index(request):
    # 1、获取客户端的 sessionID
    # 2、在服务端查找是否存在 这个sessionID
    # 3、在服务端查看对应的key sessionID键的值中是否有name（有值就是登录过了！！）
    return render(request, 'sb2/index.html', {})


@cookie_auth
def country(request):
    return render(request, 'sb2/country.html', {})


@cookie_auth
def process(request):
    return render(request, 'sb2/country.html')


@cookie_auth
def Thailand(request):
    obj = ""
    if request.method == "GET":
        obj = models.OrderList()

    elif request.method == "POST":
        obj = models.OrderList(request.POST)  # 修改数据
        # obj.state = 0
        # obj.order_method = 1
        # obj.destination = "泰国"
        if obj.is_valid():
            a = obj.save()
            print("ok")
            print(a.id)
            return redirect("/progress/")
        else:
            print(obj.errors)
    return render(request, 'sb2/process.html', {"obj": obj})
    # return render(request, 'sb2/none.html', {"obj": obj})


# @cookie_auth
def upload(request):
    passport = request.POST.get("passport")
    file = request.FILES.get("file")
    name = request.POST.get("name")
    data = {}
    print(file, name)
    # save images
    # 处理文件名
    date = time.strftime('%Y%m%d-%H%M%S-', time.localtime(time.time())) + str(random.randint(100, 999)) + "-"
    filename = date + name + "." + file.name.split(".")[-1]
    filepath = os.path.join(ImagePath, filename)
    with open(filepath, "wb+") as f:
        for chunk in file.chunks():  # 分块写入文件
            f.write(chunk)
    if passport:
        print("passport")
        try:
            # 阿里云ocr解析
            ret = json.loads(demo(filepath))
            print('ali-ok')
            firstname, lastname = ret.get("name").split(".")
        except Exception as e:
            print(e)
            return HttpResponse("1")
        # print(ret.get("country"), ret.get("name"), ret.get("sex"), ret.get("birth_date"), ret.get("passport_no"),
        #       ret.get("issue_date"),
        #       ret.get("expiry_date"))

        # data = [ret.get("country"), firstname, lastname, ret.get("sex"), ret.get("birth_date"), ret.get("passport_no")
        #         ret.get("issue_date"),
        #         ret.get("expiry_date")]
        data = {
            "country": ret.get("country"),
            "sex": ret.get("sex"),
            "birth_date": ret.get("birth_date"),
            "passport_no": ret.get("passport_no"),
            "issue_date": ret.get("issue_date"),
            "expiry_date": ret.get("expiry_date"),
            "type": ret.get("type"),
            "first_name": firstname,
            "last_name": lastname,
            "name": ret.get("name"),
        }
        print(json.dumps(data))
    # # 上传泰国evisa官网
    # file_payload = {name: (file.name, open(file.name, 'rb'), "image/jpeg")}
    # # file_payload = {'name':'': open('timg.jpg', 'rb')}
    # # 生成可用于multipart/form-data上传的数据
    # m = MultipartEncoder(file_payload)
    # # 自动生成Content-Type类型和随机码
    # headers['Content-Type'] = m.content_type
    # # 使用data上传文件
    # html = requests.post(url, headers=headers, data=m)
    # data.update(html.json())
    # print("----->:", data)
    data["filename"] = filename
    return HttpResponse(json.dumps(data))


from backstage.tasks import add
from evisa.celery import add1


def ttt(request):
    res = add1.delay()
    print(res.state)
    if request.method == "GET":
        data = models.TrainUserInfoFormSet(queryset=models.TrainUserInfo.objects.none())
        return render(request, "test.html", {"data": data})


# "country":"CHN" 国籍
# "name":"MIERAILI.YUSUFU", 姓名
# "sex":"M" 性别、称谓
# "birth_date": "19891001" 出生日期
# "passport_no": "E21160222", 护照号
# "issue_date": "20130520", 签发日期
# "expiry_date": "20230519",  有效期


a = {"authority": "公安部出入境管理局", "birth_date": "19891001", "birth_day": "891001", "birth_place": "新疆",
     "birth_place_raw": "新疆/XINJIANG", "country": "CHN", "expiry_date": "20230519", "expiry_day": "230519",
     "issue_date": "20130520", "issue_place": "新疆", "issue_place_raw": "新疆/XINJIANG",
     "line0": "POCHNMIERAILI<<YUSUFU<<<<<<<<<<<<<<<<<<<<<<<", "line1": "E211602222CHN8910015M2305190MDNHLGPAXF2",
     "name": "MIERAILI.YUSUFU", "name_cn": "米尔力杰薇国", "name_cn_raw": "米尔力杰薇T国ALUSUEU", "passport_no": "E21160222",
     "person_id": "", "request_id": "20190322151243_011b84df9f9247023236a1e12dd02bc9", "sex": "M", "src_country": "CHN",
     "success": 1, "type": "PO"}


def test(request):
    print(request.body)
    return HttpResponse("ok")


def progress(request):
    obj = models.Order.objects.all()
    return render(request, 'sb2/progress.html', {"obj": obj})


def pay(request):
    print(request.GET.get("id"))
    # 这是将数据库数据提交官网
    # data = models.Order.objects.filter(state=0).first()
    # ret = mypool.process(data)
    # if ret.get("url"):
    #     print(ret.get("url"))
    #     data.state = 1
    #     data.pay_addr = ret.get("url")
    #     data.save()
    # else:
    #     print(ret.get("err"))
    # time.sleep(1000)
    obj = models.Order.objects.get(id=request.GET.get("id"))
    return render(request, 'sb2/pay.html', {"obj": obj})


from django.core import serializers


# data1 = serializers.serialize("json", SomeModel.objects.filter(myfield1=myvalue))

def shapcar(request):
    obj = models.Order.objects.all()
    data = serializers.serialize("json", obj)
    return HttpResponse(data)


def trainticket(request):
    return render(request, 'sb2/trainticket.html', {'show': "show"})


def buy_ticket(train, fromstation, tostation, seat, starttime, name, id_card, phone, ret):
    ticket_url = "https://tieyo.trade.qunar.com/site/booking/purchase.jsp?train={}&fromstation={}&tostation={}&seat={}&starttime={}".format(
        train, fromstation, tostation, seat, starttime)
    driver.get(ticket_url)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, 'pName_0')))
    # 姓名
    driver.find_element_by_name('pName_0').send_keys(name)
    # 身份证号
    driver.find_element_by_name('pCertNo_0').send_keys(id_card)
    # 联系人
    driver.find_element_by_name('contact_name').send_keys(name)
    # 联系电话
    driver.find_element_by_name('contact_phone').send_keys(phone)
    # 确认
    driver.find_element_by_id("fillOrder_eTicketNormalSubmit").submit()
    # 点击选择取票联系人
    # driver.find_element_by_id("contact208499259").click()  class="order_code" # 坐席class="robOptionSeats"
    # 生成时间+随机数的字符串
    # '{0:%Y%%d%H%M%S%f}'.format(datetime.datetime.now())+''.join([str(random.randint(0,9)) for i in range(9)])

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'order_code')))
    # qunaer订单号
    order_num = driver.find_element_by_name("orderNo").get_attribute("value").rstrip("PAY1_multiPay")
    print(order_num)
    # 价格
    price = float(driver.find_element_by_class_name("js-reduce-orderAmount").text)
    print(price)
    ret.qunaer_id = order_num
    ret.price = price

    # pay
    driver.find_element_by_name('balance').click()
    # pwdpay
    if driver.find_element_by_class_name('use_which').text == '使用交易密码':
        driver.find_element_by_class_name('use_which').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, 'payPwd')))
        # TODO 交易密码
        driver.find_element_by_name('payPwd').send_keys('*')
        driver.find_element_by_class_name("js_pay_amount_full_dlg_btn").submit()
    # 支付完成
    ret.state = 2
    ret.save()


# 身份证计算所需list
id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]


# 字符串转为时间
# date_string = "2016-11-30 13:53:59"
# print(time.strptime(date_string, "%Y-%m-%d %H:%M:%S"))


def trainticket_team(request):
    if request.method == "GET":
        # data = models.TrainUserInfoFormSet(models.TrainUserInfo.objects.none())
        return render(request, 'sb2/trainticket_team.html', {'show': "show"})

    if request.method == "POST":
        # info = json.loads(request.POST.get('info'))
        # 订单号
        train_order_id = 'yidian' + '{0:%Y%M%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join(
            [str(random.randint(0, 9)) for i in range(9)])
        # all_info = []
        # ret_list = []
        # 验证信息合法性
        # for i in info:
        #     print(i)
        #     name = i.get("姓名")
        #     id_card = i.get("身份证号")
        #     fromstation = i.get("出发站")
        #     tostation = i.get("到达站")
        #     train = i.get("车次")
        #     seat = i.get("座次")
        #     try:
        #         time.strptime(i.get("乘车日期"), "%Y/%m/%d")
        #         starttime = i.get("乘车日期").replace('/', '')
        #         phone = i.get("联系电话")
        #         order_id = '{0:%Y%M%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join(
        #             [str(random.randint(0, 9)) for i in range(9)])
        #         # 检测身份证是否合法
        #         result = id_card[:-1]
        #         idcard = result + str(
        #             check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in result])]) % 11])
        #         if len(id_card) != 18 or not isinstance(id_card, str) or id_card != idcard:
        #             raise Exception("身份证格式不正确")
        #         if not name: raise Exception("没有名字")
        #         if not id_card: raise Exception("没有身份证")
        #         if not fromstation: raise Exception("没有始发站")
        #         if not tostation: raise Exception("没有终点站")
        #         if not train: raise Exception("没有车次")
        #         if not seat: raise Exception("没有座次")
        #         if not starttime: raise Exception("没有出发日期")
        #         if not phone: raise Exception("没有联系方式")
        #         user_info = {
        #             "name": name,
        #             "id_card": id_card,
        #             "fromstation": fromstation,
        #             "tostation": tostation,
        #             "train": train,
        #             "seat": seat,
        #             "starttime": starttime,
        #             "phone": phone,
        #             "state": 0,
        #             'order_id': order_id
        #         }
        #         all_info.append(user_info)
        #     except Exception as e:
        #         print(str(e))
        #         return HttpResponse("{},{},{}".format(name, id_card, str(e)))
        # print(all_info)

        # print(request.POST.get("form-TOTAL_FORMS"))

        data = models.TrainUserInfoFormSet(request.POST)
        # data.order_id = train_order_id
        if data.is_valid():
            a = data.save()
            user_info_list = []
            for i in a:
                user_info_list.append(
                    models.TrainOrderId(train_order_id=train_order_id, user_info=i)
                )
            ret = models.TrainOrderId.objects.bulk_create(user_info_list)
            print("ok", a, ret)
            # TODO 这里应该调用celery异步执行任务
            return HttpResponse(train_order_id)
        else:
            print(data.errors)
            return render(request, 'sb2/trainticket_team.html', {'show': "show", 'obj': data.errors})
        # BlogList = [Blog(title=line.split('****')[0], content=line.split('****')[1]) for line in f]
        #
        # Blog.objects.bulk_create(BlogList)
        # 信息验证成功 返回订单号

        # obj = models.TrainUserInfoModelForm(user_info)
        # if obj.is_valid():
        #     ret = obj.save()
        #     print(ret)
        #     print("买票")
        #     # buy_ticket(train, fromstation, tostation, seat, starttime, name, id_card, phone, ret)
        #
        # else:
        #     print(obj.errors)
        # 买票
        # ticket(name, id_card, fromstation, tostation, train, seat, starttime, phone)
        # {'': '王雪', '': '110526198512041000', '': '北京', '': '上海', '': 'G129', '': '二等座', '': '2019/06/01'}
    # return render(request, 'sb2/trainticket_team.html', {'show': "show"})


def trainticket_refund(request):
    return render(request, 'sb2/trainticket_refund.html', {'show': "show"})


def trainticket_report(request):
    return render(request, 'sb2/trainticket_report.html', {'show': "show"})


def trainticket_search(request):
    obj = None
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('name')
        id_card = request.POST.get('id_card')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        search_info = {}
        if name:
            search_info['name'] = name
        if id_card:
            search_info['id_card'] = id_card

        obj = models.TrainUserInfo.objects.filter(**search_info)
        print(obj)
    return render(request, 'sb2/trainticket_search.html', {'obj': obj, 'show': "show"})


wxloginapi = "https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code"


# 获取openid
def wxlogin(request):
    print(request.body)
    print(request.GET.get('code'))
    code = request.GET.get("code")
    openid = request.GET.get("openid")
    r = requests.post(
        wxloginapi,
        data={
            'appid': 'wxb11c8642b5007e82',
            'secret': '41035b5dc2c09eb18123ddd0c90d3be3',
            'js_code': code,
            'grant_type': 'authorization_code',
        }
    )
    open_id = r.json().get('openid')
    print(open_id)
    return HttpResponse(open_id)


# 验证是否登陆
def wx_auth(func):
    def weaper(request, *args, **kwargs):
        openid = request.GET.get("openid")
        if openid:
            return func(request)
        else:
            return Http404('no login')

    return weaper


# appid string  是   小程序 appId
# secret    string  是   小程序 appSecret
# js_code   string  是   登录时获取的 code
# grant_type    string  是   授权类型，此处只需填写 authorization_code


# 处理后台数据
def forever():
    while True:
        # 这是将数据库数据提交官网
        data = models.Order.objects.filter(state=0).first()
        if data:
            try:
                print("有任务")
                ret = mypool.process(data)
                if ret.get("url"):
                    print(ret.get("url"))
                    data.state = 1
                    data.pay_addr = ret.get("url")
                    data.save()
                else:
                    print(ret.get("err"))
            except Exception as e:
                print(e)
        else:
            print("全部任务已经完成")
        time.sleep(1)


t = threading.Thread(target=forever)


# t.start()


# 购票
def ticket(name, idcard, fromstation, tostation, train, seat, starttime, phone):
    ticket_url = "https://tieyo.trade.qunar.com/site/booking/purchase.jsp?train={}&fromstation={}&tostation={}&seat={}&starttime={}".format(
        train, fromstation, tostation, seat, starttime)
    driver.get(ticket_url)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, 'pName_0')))
    # 姓名
    driver.find_element_by_name('pName_0').send_keys(name)
    # 身份证号
    driver.find_element_by_name('pCertNo_0').send_keys(idcard)
    # 联系人
    driver.find_element_by_name('contact_name').send_keys(name)
    # 联系电话
    driver.find_element_by_name('contact_phone').send_keys(phone)
    # 确认
    driver.find_element_by_id("fillOrder_eTicketNormalSubmit").submit()
    # 点击选择取票联系人
    # driver.find_element_by_id("contact208499259").click()  class="order_code" # 坐席class="robOptionSeats"
    # 生成时间+随机数的字符串
    # '{0:%Y%%d%H%M%S%f}'.format(datetime.datetime.now())+''.join([str(random.randint(0,9)) for i in range(9)])

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'order_code')))
    # 订单号
    order_num = driver.find_element_by_class_name('order_code').text
    print(order_num)
    time.sleep(6000)
