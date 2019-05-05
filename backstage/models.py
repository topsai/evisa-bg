from django.db import models
from django.forms import ModelForm
from django.forms import widgets as wid  # 因为重名，所以起个别名

# Create your models here.
state_choise = (
    (0, "未处理"),
    (1, "待支付"),
    (2, "已支付"),
    (3, "待上传"),
    (4, "待审核"),
    (5, "成功"),
    (6, "失败"),
)
order_method_choise = {
    (0, "小程序"),
    (1, "门店办理"),
}


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField(auto_now_add=True)
    # 目的地
    destination = models.CharField(max_length=256, default="泰国")
    passport_img1 = models.CharField(max_length=256)
    passport_img2 = models.CharField(max_length=256)
    airimg1 = models.CharField(max_length=256)
    airimg2 = models.CharField(max_length=256)
    hotelimg = models.CharField(max_length=256)
    # 订单时间
    # order_info = models.ForeignKey("OrderInfo", on_delete=True)
    passport_type = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    airport = models.CharField(max_length=256)
    salutation = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    birth_date = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    mobile_number = models.CharField(max_length=256)
    passport_number = models.CharField(max_length=256)
    passport_issue = models.CharField(max_length=256)
    passport_expiry = models.CharField(max_length=256)
    arrival_date = models.CharField(max_length=256)
    arrival_time = models.CharField(max_length=256)
    arrival_flightnum = models.CharField(max_length=256)
    departure_date = models.CharField(max_length=256)
    departure_time = models.CharField(max_length=256)
    departure_flightnum = models.CharField(max_length=256)
    pos_name = models.CharField(max_length=256)
    pos_select = models.CharField(max_length=256)
    pos_city_province = models.CharField(max_length=256)
    pos_district = models.CharField(max_length=256)
    pos_postcode = models.CharField(max_length=256)
    residential_address = models.CharField(max_length=256)
    # 订单状态（是否支付）
    state = models.IntegerField(choices=state_choise, default=0)
    # 订单渠道（微信、店面）
    order_method = models.IntegerField(choices=order_method_choise, default=1)
    # 支付地址
    pay_addr = models.CharField(max_length=256, blank=True, null=True)


class OrderInfo(models.Model):
    passport_img1 = models.CharField(max_length=256)
    passport_img2 = models.CharField(max_length=256)
    airimg1 = models.CharField(max_length=256)
    airimg2 = models.CharField(max_length=256)
    hotelimg = models.CharField(max_length=256)
    userdata = models.ForeignKey("UserData", on_delete=models.CASCADE)


class UserData(models.Model):
    pass


class OrderList(ModelForm):
    class Meta:
        airport_choises = (
            ("bkk", "BKK - Suvarnabhumi"),
            ("dmk", "DMK - Don Mueang"),
            ("hkt", "HKT - Phuket"),
            ("cnx", "CNX - Chiang"),
        )
        hotel_choises = (
            ("hotel", "Hostel"),
            ("guesthouse", "Guesthouse"),
            ("private_property", "Private Property"),
            ("dormitory", "Dormitory"),
        )
        model = Order  # 对应的Model中的类
        fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段
        # exclude = None  # 排除的字段
        # labels = None  # 提示信息
        help_texts = None  # 帮助提示信息
        # widgets = None  # 自定义插件
        # 自定义错误信息
        # error_messages用法：
        exclude = ["state", "order_method", "destination"]
        error_messages = {
            'name': {'required': "用户名不能为空", },
            'age': {'required': "年龄不能为空", },
            "passport_type": {'required': "不能为空"},
            "nationality": {'required': "不能为空"},
            "airport": {'required': "不能为空"},
            "salutation": {'required': "不能为空"},
            "last_name": {'required': "不能为空"},
            "first_name": {'required': "不能为空"},
            "gender": {'required': "不能为空"},
            "birth_date": {'required': "不能为空"},
            "email": {'required': "不能为空"},
            "mobile_number": {'required': "不能为空"},
            "passport_number": {'required': "不能为空"},
            "passport_issue": {'required': "不能为空"},
            "passport_expiry": {'required': "不能为空"},
            "arrival_date": {'required': "不能为空"},
            "arrival_time": {'required': "不能为空"},
            "arrival_flightnum": {'required': "不能为空"},
            "departure_date": {'required': "不能为空"},
            "departure_time": {'required': "不能为空"},
            "departure_flightnum": {'required': "不能为空"},
            "pos_select": {'required': "不能为空"},
            "pos_name": {'required': "不能为空"},
            "pos_city_province": {'required': "不能为空"},
            "pos_district": {'required': "不能为空"},
            "pos_postcode": {'required': "不能为空"},
            "residential_address": {'required': "不能为空"},
        }
        # widgets用法,比如把输入用户名的input框给为Textarea
        # 首先得导入模块
        widgets = {
            "id": wid.TextInput(),
            # 还可以自定义属性class="filepath"
            "passport_img1": wid.TextInput(attrs={"class": "filepath", "required": "true"}),
            "passport_img2": wid.TextInput(attrs={"class": "filepath", "passport": "true", "required": "true"}),
            "airimg1": wid.TextInput(attrs={"class": "filepath", "required": "true"}),
            "airimg2": wid.TextInput(attrs={"class": "filepath", "required": "true"}),
            "hotelimg": wid.TextInput(attrs={"class": "filepath", "required": "true"}),
            "passport_type": wid.TextInput(attrs={"class": "form-control up", "required": "true"}),
            "nationality": wid.TextInput(attrs={"class": "form-control up", "required": "true"}),
            # "airport": wid.TextInput(attrs={"class": "form-control up"}),
            # "airport": wid.ChoiceWidget(choices=(("a",1), ("b", 2))),
            "airport": wid.Select(choices=airport_choises, attrs={"class": "form-control up"}),
            "salutation": wid.TextInput(attrs={"class": "form-control up"}),
            "last_name": wid.TextInput(attrs={"class": "form-control up"}),
            "first_name": wid.TextInput(attrs={"class": "form-control up"}),
            "gender": wid.TextInput(attrs={"class": "form-control up"}),
            "birth_date": wid.TextInput(attrs={"class": "form-control up"}),
            "email": wid.TextInput(attrs={"class": "form-control up"}),
            "mobile_number": wid.TextInput(attrs={"class": "form-control up"}),
            "passport_number": wid.TextInput(attrs={"class": "form-control up"}),
            "passport_issue": wid.TextInput(attrs={"class": "form-control up"}),
            "passport_expiry": wid.TextInput(attrs={"class": "form-control up"}),
            "arrival_date": wid.TextInput(attrs={"class": "form-control datepicker up", "placeholder": "到达日期"}),
            "arrival_time": wid.TextInput(attrs={"class": "form-control up", "placeholder": "到达时间"}),
            "arrival_flightnum": wid.TextInput(attrs={"class": "form-control up", "placeholder": "到达航班号"}),
            "departure_date": wid.TextInput(attrs={"class": "form-control datepicker up", "placeholder": "离开日期"}),
            "departure_time": wid.TextInput(attrs={"class": "form-control up", "placeholder": "离开时间"}),
            "departure_flightnum": wid.TextInput(attrs={"class": "form-control up", "placeholder": "离开航班号"}),
            # "pos_select": wid.TextInput(attrs={"class": "form-control up"}),
            "pos_name": wid.TextInput(attrs={"class": "form-control up", "placeholder": "住宿名称"}),
            "pos_select": wid.Select(choices=hotel_choises, attrs={"class": "form-control up"}),
            "pos_city_province": wid.TextInput(attrs={"class": "form-control up"}),
            "pos_district": wid.TextInput(attrs={"class": "form-control up"}),
            "pos_postcode": wid.TextInput(attrs={"class": "form-control up"}),
            # "residential_address": wid.TextInput(attrs={"class": "form-control up"}),
            "residential_address": wid.Textarea(attrs={"class": "form-control up", "rows": 3}),
        }
        # labels，自定义在前端显示的名字
        labels = {
            "passport_type": "护照类型",
            "nationality": "国籍",
            "airport": "到达机场",
            "salutation": "称谓",
            "last_name": "姓",
            "first_name": "名",
            "gender": "性别",
            "birth_date": "出生日期",
            "email": "邮箱地址",
            "mobile_number": "手机号",
            "passport_number": "护照号",
            "passport_issue": "护照签发日期",
            "passport_expiry": "护照有效期",
            "arrival_date": "到达日期",
            "arrival_time": "到达时间",
            "arrival_flightnum": "到达航班",
            "departure_date": "离开日期",
            "departure_time": "离开时间",
            "departure_flightnum": "离开航班",
            "pos_select": "住宿类型",
            "pos_name": "住宿名称",
            "pos_city_province": "城市",
            "pos_district": "区",
            "pos_postcode": "邮政编码",
            "residential_address": "住宿信息",
        }


train_state_choise = (
    (0, "未处理"),
    (1, "待支付"),
    (2, "已支付"),
    (3, "成功"),
    (4, "失败"),
)


class TrainOrderId(models.Model):
    # 订单创建时间
    time = models.TimeField(auto_now_add=True)
    train_order_id = models.CharField(max_length=256)
    user_info = models.ForeignKey("TrainUserInfo", on_delete=models.CASCADE)


class TrainUserInfo(models.Model):
    time = models.TimeField(auto_now_add=True)
    # 身份证号
    id_card = models.CharField(max_length=18)
    # 姓名
    name = models.CharField(max_length=256)
    # 出发站
    fromstation = models.CharField(max_length=256)
    # 到达站
    tostation = models.CharField(max_length=256)
    # 车次
    train = models.CharField(max_length=256)
    # 座次
    seat = models.CharField(max_length=256)
    # 乘车日期
    starttime = models.CharField(max_length=256)
    # 联系电话
    phone = models.CharField(max_length=18)
    # 我自定义的id
    order_id = models.AutoField(primary_key=True)
    # qunaer id
    qunaer_id = models.CharField(max_length=256, blank=True)
    # 12306 id
    real_id = models.CharField(max_length=256, blank=True)
    # 订单状态
    state = models.SmallIntegerField(choices=train_state_choise, default=0, blank=False)
    # 价格
    price = models.IntegerField(blank=True, default=0)


class TrainUserInfoModelForm(ModelForm):
    class Meta:
        model = TrainUserInfo
        fields = "__all__"
        help_texts = None
        exclude = ['order_id', 'qunaer_id', 'real_id', 'state', 'price']
        error_messages = {}
        labels = {
            "id_card": "身份证号",
            "name": "姓名",
            "fromstation": "出发站",
            "tostation": "到达站",
            "train": "车次",
            "seat": "座次",
            "starttime": "乘车日期",
            "phone": "联系电话",
            "order_id": "我自定义的id",
            "车次": "train",
        }
        widgets = {
            "id_card": wid.TextInput(),
            "name": wid.TextInput(),
            "fromstation": wid.TextInput(),
            "tostation": wid.TextInput(),
            "train": wid.TextInput(),
            "seat": wid.TextInput(),
            "starttime": wid.TextInput(),
            "phone": wid.TextInput(),
            "order_id": wid.TextInput(),
            "车次": wid.TextInput(),
        }


from django.forms import modelformset_factory

TrainUserInfoFormSet = modelformset_factory(
    TrainUserInfo,
    form=TrainUserInfoModelForm,
)


class TrainOrderIdModelForm(ModelForm):
    class Meta:
        model = TrainOrderId
        fields = "__all__"
        help_texts = None
        exclude = []
        error_messages = {}
        labels = {}
