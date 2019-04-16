const app = getApp();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    ColorList: app.globalData.ColorList,
  },
  onLoad: function(e) {
    wx.getUserInfo({
      success(res) {
        
        // app.globalData.userInfo = res.rawData
        console.log('sfafs', app.globalData.userInfo)
        console.log('app.globalData.userInfo', app.globalData.userInfo)
      }
    })
  },
  onGetUserInfo: function(e) {
    console.log('e-->', e)
    console.log('this', this)
    console.log(e.detail.encryptedData)
    console.log(e.detail.iv)
    if (!this.logged && e.detail.userInfo) {
      app.globalData.userInfo = e.detail.userInfo;
      wx.login({
        success: function(res) {
          console.log('res:', res)
          //发送请求
          wx.request({
            url: 'http://127.0.0.1:8000/wxlogin/', //接口地址
            data: {
              code: res.code,

            },
            header: {
              'content-type': 'application/json', //默认值
            },
            success: function(res) {
              console.log(res.data)
              app.globalData.openid = res.data
              console.log('login-ok->app.globalData.openid:', app.globalData.openid)
              wx.switchTab({
                url: '/pages/home/index/index',
              })
            },
            fail: function(res) {
              console.log('login file->', res)
              wx.showToast({
                title: '失败',
                icon: 'cancel',
                duration: 1000,
                mask: true
              })
            }
          })
        }
      })
    }
  },



  //登录获取code
  login: function() {


  }


});