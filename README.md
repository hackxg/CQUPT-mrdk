# CQUPT-mrdk
## CQUPT-每日打卡
因为疫情的变化 WE重邮再次开启了打卡模式
这里记录今天分析结果最后会附上使用方式

### 如果你只是想白嫖那就直接扫码吧

![Image text](https://raw.github.com/hackxg/CQUPT-mrdk/blob/master/QRcode.png)

### 1.反编译小程序包

在去年6月过后we重邮小程序子包分离（we重邮编写代码过于冗余）

这里正常操作反编译过后就能看到这里的请求地址和加密方式没有什么变化。

请求地址和加密方式

### 2.参数确定
通过抓包可以确定参数

结合源代码就可以确定参数含义了。

### 3.报文结构

{"key":"******"}
其中*为加密的json字段 具体可以看之前的帖子

注意字段变化

之前的字段

{
    "jbsks": "否",
    "jbsfl": "否",
    "jbsbs": "否",
    "jbslt": "否",
    "jbsyt": "否",
    "jbsfx": "否",
    "name": "无",
    "xh": "无",
    "xb": "无",
    "lxdh": "无",
    "szdq": "无",
    "xxdz": "无",
    "hjsfly": "是",
    "sfyfy": "否",
    "ywjchblj": "无",
    "ywjcqzbl": "无",
    "xjzdywqzbl": "无",
    "twsfzc": "是",
    "ywytdzz": "无",
    "brsfqz": "无",
    "brsfys": "无",
    "jbs": "无",
    "fyjtgj": "无",
    "fyddsj": "无",
    "sfbgsq": "无",
    "sfjjgl": "无",
    "jjglqssj": "无",
    "wjjglmqqx": "无",
    "beizhu": "无",
    "qtycqk": "无",
    "mrdkkey": "MfdugBGg",
    "timestamp": 1594963224
}
现在的字段

{
     "name":"**",
    "xh":"**",
    "xb":"**",
    "szdq":"**",
    "xxdz":"**",
    "ywjcqzbl":"低风险",
    "ywjchblj":"无",
    "xjzdywqzbl":"无",
    "twsfzc":"是",
    "ywytdzz":"无",
    "beizhu": "无",
    "openid": "***",
    "mrdkkey": "MfdugBGg",
    "timestamp": 1594963224
}
这里解释一些现在的字段

其中

openid字段为微信用户的某个唯一标识 其获取方式很简单 有需求的可以自行百度


mrdkkey字段 此字段是去年5月过后启用的校验字段

其加密方式为


 var o = new Object(), s = new Date(), l = s.getDate(), r = s.getHours();
                    o.key = i.keymrdk(l, r), console.log(l, r), console.log(o.key), a.setData({
                        "formData.mrdkkey": o.key
                    })

var r = [ "s9ZS", "jQkB", "RuQM", "O0_L", "Buxf", "LepV", "Ec6w", "zPLD", "eZry", "QjBF", "XPB0", "zlTr", "YDr2", "Mfdu", "HSoi", "frhT", "GOdB", "AEN0", "zX0T", "wJg1", "fCmn", "SM3z", "2U5I", "LI3u", "3rAY", "aoa4", "Jf9u", "M69T", "XCea", "63gc", "6_Kf" ], u = [ "89KC", "pzTS", "wgte", "29_3", "GpdG", "FDYl", "vsE9", "SPJk", "_buC", "GPHN", "OKax", "_Kk4", "hYxa", "1BC5", "oBk_", "JgUW", "0CPR", "jlEh", "gBGg", "frS6", "4ads", "Iwfk", "TCgR", "wbjP" ];

module.exports = {
    keymrdk: function(e, f) {
        return r[e] + u[f];
    }
};
函数意义为

获取当前的日期 例如今天则是20日

获取当前小时（24h制）例如当前为12.22 则为12

mrdkkey则等于 r[20]+u[12]=fCmnhYxa

timestamp为时间戳

编写好后通过base64加密塞入key中post请求即可

## 如果你想部署在自己的服务器上
准备工作：

1.编写一个脚本 根据你的喜好 带参发送post请求即可

2.当你能够准确的伪造数据包并进行加密

3.获取openid 或者 跟题主一样 伪造openid

（openid是微信官方对用户与公众号或小程序直接的某个唯一标识）

注意不同的公众号、用户的openid是不同的

提示：伪造openid的方法伪造 code短码（几乎不可能）伪造encryptedData（可能成功）用户绑定时上传openid伪造过程（成功）

4.发送报文

## 最后附上白嫖党使用方式
微信搜索

We重邮2021 小程序进行信息录入

[Link:https://www.longm.top/index.php/archives/55/](https://www.longm.top/index.php/archives/55/)


