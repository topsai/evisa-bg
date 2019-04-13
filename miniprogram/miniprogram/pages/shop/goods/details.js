import WxValidate from '../../../utils/WxValidate.js'
const app = getApp();

Page({
  data: {
    airport: {
      index: "",
      option: [
        ['bkk', 'BKK - Suvarnabhumi'],
        ['dmk', 'DMK - Don Mueang'],
        ['hkt', 'HKT - Phuket'],
        ['cnx', 'CNX - Chiang'],
      ]
    },
    pos_select: {
      index: "",
      option: [
        ['hotel', 'Hotel'],
        ['hostel', 'Hostel'],
        ['guesthouse', 'Guesthouse'],
        ['private_property', 'Private Property'],
      ]
    },
    images: {
      mode: 'scaleToFill',
      text: 'scaleToFill：不保持纵横比缩放图片，使图片完全适应',
    },

    StatusBar: app.globalData.StatusBar + 6,
    TabbarBot: app.globalData.tabbar_bottom,
    swiperlist: [
      '../../../img/malaixiya.jpg'
    ],
  },
  formSubmit: function(e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
  },
  PickerChange(e) {
    let that = this;
    let dic = e.currentTarget.id + ".index"
    console.log(dic)
    this.setData({
      [dic]: e.detail.value,
    })
  },
  bindDateChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value, e.currentTarget, e.currentTarget.id)
    let d = e.detail.value.split("-")[2] + "/" + e.detail.value.split("-")[1] + "/" + e.detail.value.split("-")[0]
    let dd;
    if (e.currentTarget.id == 'id_arrival_date') {
      dd = {
        arrival_date: d
      }
    } else if (e.currentTarget.id == 'id_departure_date') {
      dd = {
        departure_date: d
      }
    }
    this.setData(dd)
  },
  chooseImage(e) {
    console.log(e.currentTarget.dataset.name);
    let classname = e.currentTarget.dataset.name
    let passport = e.currentTarget.dataset.passport
    if (!passport) {
      passport = ""
    }
    let that = this;
    wx.chooseImage({
      // 图片数量
      count: 1,
      sizeType: ['original', 'compressed'], //可选择原图或压缩后的图片
      sourceType: ['album', 'camera'], //可选择性开放访问相册、相机
      success: res => {
        const tempFilePaths = res.tempFilePaths
        // const images = this.data.images.concat(res.tempFilePaths)
        // 限制最多只能留下3张照片
        // this.data.images = images.length <= 3 ? images : images.slice(0, 3)
        console.log(tempFilePaths);
        let dd = classname + ".src"
        this.setData({
          [dd]: tempFilePaths
        })
        // TODO 上传图片
        wx.uploadFile({
          url: 'http://138.128.220.228:8000/upload/', // 仅为示例，非真实的接口地址
          filePath: tempFilePaths[0],
          name: 'file',
          formData: {
            name: 'name',
            passport: passport
          },
          success(res) {
            console.log(res.data);
            let data = JSON.parse(res.data);
            console.log(data);
            console.log(data.filename);
            // do something
            if (classname == 'passport_img2') {
              that.setData({
                'passinfo.nationality': data.country.toLowerCase(),
                'passinfo.last_name': data.last_name,
                'passinfo.first_name': data.first_name,
                'passinfo.salutation': data.sex,
                'passinfo.gender': data.sex,
                'passinfo.passport_type': 'ordinary',
                'passinfo.birth_date': data.birth_date,
                'passinfo.passport_number': data.passport_no,
                'passinfo.passport_issue': data.issue_date.slice(6, 8) + "/" + data.issue_date.slice(4, 6) + "/" + data.issue_date.slice(0, 4),
                'passinfo.passport_expiry': data.expiry_date.slice(6, 8) + "/" + data.expiry_date.slice(4, 6) + "/" + data.expiry_date.slice(0, 4),
              })
            }
            // 设置文件预览
            let dd = "passinfo."+ classname
            console.log("dd--->",dd)
            that.setData({
              [dd]: data.filename,
            })
            
          }
        })
      }
    })
  },
  bindTimeChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    let dd;
    if (e.currentTarget.id == 'departure_time') {
      dd = {
        departure_time: e.detail.value
      }
    } else if (e.currentTarget.id == 'arrival_time') {
      dd = {
        arrival_time: e.detail.value
      }
    }
    this.setData(dd)
  },
  onLoad: function(options) {
    let that = this;
  },
  passinfo: {
    // 目的地
    'destination': '',
    'passport_img1': '',
    'passport_img2': '',
    'airimg1': '',
    'airimg2': '',
    'hotelimg': '',
    'passport_type': '',
    'nationality': '',
    'airport': '',
    'salutation': '',
    'last_name': '',
    'first_name': '',
    'gender': '',
    'birth_date': '',
    'email': '',
    'mobile_number': '',
    'passport_number': '',
    'passport_type': 'ordinary',
    'passport_issue': '',
    'passport_expiry': '',
    'arrival_date': '',
    'arrival_time': '',
    'arrival_flightnum': '',
    'departure_date': '',
    'departure_time': '',
    'departure_flightnum': '',
    'pos_name': '',
    'pos_select': '',
    'pos_city_province': '',
    'pos_district': '',
    'pos_postcode': '',
    'residential_address': '',
  },

















  
});