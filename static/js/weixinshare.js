function configWechat(shareData) {
    $.get('http://slide.cm/wechat/config', {
            url: location.href.split('#')[0]
    }).done(function(data) {
            if (data.code !== 0) {
                        return false;
                    }
            wx.config({
                debug: true,
                appId: 'wx82a5d90838b461ba',
                timestamp: data.config.timestamp,
                nonceStr: data.config.nonceStr,
                signature: data.config.signature,
                jsApiList: [
                    'onMenuShareTimeline',
                    'onMenuShareAppMessage',
                    'onMenuShareQQ',
                    'onMenuShareWeibo',
                    'previewImage'
                    ]
                 });
             wx.ready(function() {
                        configContent(shareData);
             });
                    
             wx.error(function(res) {});
        }).fail(function(e) {
                console.log('wechatshare config failure');
       });
}

function configContent(shareData) {
    var title = '厘米脚印邀请您对我们在项目中的表现进行评价';
    var link = 'http://' + window.location.hostname;
    var imgUrl = 'http://' + window.location.hostname + '/static/images/wechatshare.jpg';
    var desc = ' ';
    
    if (shareData) {
            if (shareData.title) {
                     title = shareData.title;
                    }
            if (shareData.link) {
                     link = shareData.link;
                    }
            if (shareData.imgUrl) {
                     imgUrl = shareData.imgUrl;
                    }
            if (shareData.desc) {
                     desc = shareData.desc;
                    }
            }

    wx.onMenuShareTimeline({
            title: title,
            link: link,
            imgUrl: imgUrl
        });
    wx.onMenuShareAppMessage({
            title: title,
            desc: desc,
            link: link,
            imgUrl: imgUrl
        });
    wx.onMenuShareQQ({
            title: title,
            desc: desc,
            link: link,
            imgUrl: imgUrl
        });
    wx.onMenuShareWeibo({
            title: title,
            desc: desc,
            link: link,
            imgUrl: imgUrl
        });
}
