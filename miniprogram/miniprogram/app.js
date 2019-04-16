//app.js
App({
  globalData: {
    userinfo: '',
    openid: ''
  },
  onLaunch: function() {
    let that = this
    wx.getSystemInfo({
      success: e => {
        this.globalData.StatusBar = e.statusBarHeight;
        let custom = wx.getMenuButtonBoundingClientRect();
        this.globalData.Custom = custom;
        let CustomBar = custom.bottom + custom.top - e.statusBarHeight;
        this.globalData.CustomBar = CustomBar;
        //适配全面屏底部距离
        if (CustomBar > 75) {
          this.globalData.tabbar_bottom = "y"
        }
      }
    })
    wx.getStorage({
      key: 'userinfo',
      success: function(res) {
        console.log('userinfo', res.data)
        that.globalData.userinfo = res.data
      },
    })
    wx.getStorage({
      key: 'openid',
      success: function(res) {
        console.log('openid', res.data)
        that.globalData.openid = res.data
      },
    })
    console.log('app-userinfo', )
  }

});