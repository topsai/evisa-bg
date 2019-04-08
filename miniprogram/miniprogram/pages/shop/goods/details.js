const app = getApp();

Page({
  data: {
    array: [
      ['bkk', 'BKK - Suvarnabhumi'],
      ['dmk', 'DMK - Don Mueang'],
      ['hkt', 'HKT - Phuket'],
      ['cnx', 'CNX - Chiang]'],
    ],
    images: {
      mode: 'scaleToFill',
      text: 'scaleToFill：不保持纵横比缩放图片，使图片完全适应',
      src: ''
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
      'passport_type': '',
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
    StatusBar: app.globalData.StatusBar + 6,
    TabbarBot: app.globalData.tabbar_bottom,
    swiperlist: [
      '../../../img/malaixiya.jpg'
    ],
  },
  formSubmit: function(e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
  },
  bindPickerChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index: e.detail.value
    })
  },
  bindDateChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    let d = e.detail.value.split("-")[2] + "/" + e.detail.value.split("-")[1] + "/" + e.detail.value.split("-")[0]
    this.setData({
      date: d
    })
  },
  chooseImage(e) {
    console.log(e.currentTarget.dataset.name);
    let classname = e.currentTarget.dataset.name
    let passport = e.currentTarget.dataset.passport
    if(!passport){
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
        this.setData({
          'images.src': tempFilePaths
        })

        // TODO 上传图片
        wx.uploadFile({
          url: 'http://127.0.0.1:8000/upload/', // 仅为示例，非真实的接口地址
          filePath: tempFilePaths[0],
          name: 'file',
          formData: {
            name: 'name',
            passport: passport
          },
          success(res) {
            console.log(res.data);
            const data = JSON.parse(res.data);
            console.log(data);
            console.log(data.filename);
            // do something
            if (classname == 'passport_img1') {
              that.setData({
                'passinfo.passport_img1': data.filename,
              })
            } else if (classname == 'passport_img2') {
              that.setData({
                'passinfo.passport_img2': data.filename,
                'passinfo.nationality': data.country,
                'passinfo.last_name': data.last_name,
                'passinfo.first_name': data.first_name,
                'passinfo.salutation': data.filename,
                'passinfo.gender': data.filename,
                'passinfo.birth_date': data.filename,
                'passinfo.passport_number': data.filename,
                'passinfo.passport_type': data.filename,
                'passinfo.passport_issue': data.filename,
                'passinfo.passport_expiry': data.filename,
              })

            } else if (classname == 'airimg1') {
              that.setData({
                'passinfo.airimg1': data.filename,
              })

            } else if (classname == 'airimg2') {
              that.setData({
                'passinfo.airimg2': data.filename,
              })

            } else if (classname == 'hotelimg') {
              that.setData({
                'passinfo.hotelimg': data.filename,
              })
            }

          }
        })
      }
    })
  },
  bindTimeChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      time: e.detail.value
    })
  },
  onLoad: function(options) {
    let that = this;
  }
});