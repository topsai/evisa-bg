from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from backstage import models
from django.contrib.auth import authenticate
import requests
# 导入requests_toolbelt库使用MultipartEncoder
from requests_toolbelt import MultipartEncoder
import json
import base64
import requests
import time
import random
import threading
import os
from evisa.settings import ImagePath
from backstage import mypool

url = 'https://www.evisathailand.com/images/upload'
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'www.evisathailand.com',
    'Origin': 'https://www.evisathailand.com',
    'Referer': 'https://www.evisathailand.com/ft',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.16 Safari/537.36'
}


# Create your views here.
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
        print("这是护照")
        try:
            # 阿里云ocr解析
            ret = json.loads(demo(filepath))
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


def ttt(request):
    if request.method == "GET":
        data = models.OrderList()
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
