const app = getApp();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    ColorList: app.globalData.ColorList,
    nickName: null,
    avatarUrl: null
  },
  onLoad: function(e) {
    let that = this
    wx.getUserInfo({
      success(res) {
        console.log(res)
        wx.setStorage({
          key: 'userinfo',
          data: res.userInfo,
        })
        that.setData({
          nickName: res.userInfo.nickName,
          avatarUrl: res.userInfo.avatarUrl
        })
      }
    })
  },
  onGetUserInfo: function(e) {
    console.log('e-->', e)
    console.log('this', this)
    console.log(e.detail.encryptedData)
    console.log(e.detail.iv)
    wx.login({
      success: function (res) {
        console.log('res:', res)
        //发送请求
        wx.request({
          url: 'http://127.0.0.1:8000/wxlogin/', //接口地址
          data: {
            code: res.code,
          },
          success: function (res) {
            console.log(res.data)
            app.globalData.openid = res.data
            wx.setStorage({
              key: 'openid',
              data: res.data,
            })
            console.log('login-ok->app.globalData.openid:', app.globalData.openid)
            wx.switchTab({
              url: '/pages/home/index/index',
            })
          },
          fail: function (res) {
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
  },
});