const app = getApp();
Page({
    data: {
        StatusBar: app.globalData.StatusBar + 6,
        TabbarBot: app.globalData.tabbar_bottom,
        swiperlist: [
            '../../../img/malaixiya.jpg'
        ],
    },
    onLoad: function (options) {
        let that = this;
    }
});
