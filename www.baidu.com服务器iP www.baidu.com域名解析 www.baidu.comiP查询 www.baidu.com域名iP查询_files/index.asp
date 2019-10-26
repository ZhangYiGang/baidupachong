(function () {
    var $link = document.getElementById('link');
    if ($link) {
        var text = '<p class="link-text"><a href="http://qpgyy6080.com/" target="_blank" rel="nofollow">青苹果电影视频</a><a href="http://wpa.qq.com/msgrd?v=3&uin=518733&site=qq&menu=yes" target="_blank" rel="nofollow">APP轻松百万流量</a><a href="http://www.cctv5mi.com/" target="_blank" rel="nofollow">体育赛事在线直播</a><a href="tencent://AddContact/?fromId=50&fromSubId=1&subcmd=all&uin=718126" target="_blank" rel="nofollow">老A实发国际短信</a><a href="http://wpa.qq.com/msgrd?v=3&uin=2230506948&site=qq&menu=yes" target="_blank"  rel="nofollow">OA,idc,正网出租</a><a href="http://wpa.qq.com/msgrd?v=3&uin=1073353388&site=qq&menu=yes" target="_blank" class="bold" rel="nofollow">广告QQ:1073353388</a></p>';

        var ua = navigator.userAgent.toLowerCase();
        var Mobile = ua.indexOf("mobi") > 0 || ua.indexOf("android") > 0 || ua.indexOf("linux") > 0 || window.screen.width <= 960;
        if (Mobile) {
            if (ua.indexOf("iphone") > 0 || ua.indexOf("ipad") > 0) {
                var img = '<div class="link-pic"><div class="left-pic"><a href="https://www.huashengdaili.com/" target="_blank" rel="nofollow"><img src="//site.liantu.cn/image/huashengdaili.png" width="240" height="60"/></a><span class="mark"></span></div><div class="right-pic"><a href="https://www.chajiechi.cn/" target="_blank" rel="nofollow"><img src="//site.liantu.cn/image/chajiechi.png" width="240" height="60"/></a><span class="mark"></span></div></div>';
            } else {
                var img = '<div class="link-pic"><a href="http://3915.douyou78.com/" target="_blank" rel="nofollow"><img src="//site.liantu.cn/image/douyou.png" width="490" height="60"/></a><span class="mark"></span></div>';
            }

        } else {
            var img = '<div class="link-pic"><div class="left-pic"><a href="https://www.huashengdaili.com/" target="_blank" rel="nofollow"><img src="//site.liantu.cn/image/huashengdaili.png" width="240" height="60"/></a><span class="mark"></span></div><div class="right-pic"><a href="https://www.chajiechi.cn/" target="_blank" rel="nofollow"><img src="//site.liantu.cn/image/chajiechi.png" width="240" height="60"/></a><span class="mark"></span></div></div>';
        }


        $link.innerHTML = text + img;

        var $banner1 = document.getElementById('banner1');
        if ($banner1) {
            $banner1.innerHTML = '';
        }

        var $banner2 = document.getElementById('banner2');
        if ($banner2) {
            $banner2.innerHTML = '';
        }
    }
})();