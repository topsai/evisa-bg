from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from backstage import models
from django.contrib.auth import authenticate
import json
import base64
import requests


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
        exit()
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
def process(request):
    return render(request, 'sb2/process.html')


@cookie_auth
def upload(request):
    passport = request.FILES.get("passport")
    if passport:
        # save images
        with open(passport.name, "wb+") as f:
            for chunk in passport.chunks():  # 分块写入文件
                f.write(chunk)
        ret = demo(passport.name)
        return HttpResponse(ret)
