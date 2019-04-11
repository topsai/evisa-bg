const app = getApp();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    ColorList: app.globalData.ColorList,
  },
  onGetUserInfo: function(e) {
    if (!this.logged && e.detail.userInfo) {
      app.globalData.userInfo = e.detail.userInfo;
      wx.login({
        success: function (res) {
          console.log(res.code)
          //发送请求
          wx.request({
            url: 'http://127.0.0.1:8000/wxlogin/', //接口地址
            data: {
              code: res.code
            },
            header: {
              'content-type': 'application/json' //默认值
            },
            success: function (res) {
              console.log(res.data)
            }
          })
        }
      })
      wx.switchTab({
        url: '/pages/home/index/index',
      })
    }
  },



  //登录获取code
  login: function() {
    

  }


});