#coding=utf-8
import requests as req
import base64
import time
import json
import os
import smtplib
import sys
from email.mime.text import MIMEText
from email.header import Header
def get(usr_id):
    bait_type_path = os.path.dirname(__file__)
    f=open(os.path.join(bait_type_path, r'data/'+usr_id+'.json'),encoding='utf-8-sig')
    data=json.load(f)
    f.close()
    return data
def init(usr_id):
    data=get(usr_id)
    name = data['name']
    xh = data['xh']
    xb = data['xb']
    lxdh = data['lxdh']
    szdq = data['szdq']
    xxdz = data['xxdz']
    hjsfly = data['hjsfly']
    sfyfy = data['sfyfy']
    email=data['email']
    data=json.dumps(get_mrdk(name,xb,xh,lxdh,szdq,xxdz,hjsfly,sfyfy),ensure_ascii=False)
    mima = base(data)
    return [post('https://we.cqu.pt/api/mrdk/post_mrdk_info.php','{"key": "' + mima + '"}'),email]
def get_mrdk(name,xb,xh,lxdh,szdq,xxdz,hjsfly,sfyfy):
    bait_type_path = os.path.dirname(__file__)
    file=open(os.path.join(bait_type_path, 'data.json'),encoding='utf-8-sig')
    f=json.load(file)
    file.close()
    f['name']=name
    f['xb']=xb
    f['xh'] = xh
    f['lxdh']=lxdh
    f['szdq']=szdq
    f['xxdz']=xxdz
    f['hjsfly']=hjsfly
    f['sfyfy']=sfyfy
    f['timestamp']=int(time.time())
    f['locationBig']=szdq
    f['locationSmall']=szdq+xxdz
    xy=getxy(szdq+xxdz)
    f['latitude']=xy[0]
    f['longitude']=xy[1]
    return f
def getxy(place):
    url='https://apis.map.qq.com/jsapi?qt=geoc&addr='+place
    res=req.get(url)
    temp=res.text
    temp=json.loads(temp)
    return [temp["detail"]["pointy"],temp["detail"]["pointx"]]
def get_mrdk_list(user_id):
    t=time.time()
    text=r'{"openid": "'+''+'", "xh":"'+str(user_id)+'", "timestamp": '+str(int(t))+'}'
    mima=base(text)
    return '{"key": "'+mima+'"}'
def base(code):
    code = code.encode()
    str_url = base64.b64encode(code)
    mima=str(str_url,'utf-8')
    return mima
def post(url,data):
    url=url
    head={
        'Host':'we.cqu.pt',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.15.1680(0x27000F34) Process/appbrand0 WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32',
        'charset':'utf-8',
        'Accept-Encoding': 'gzip,compress,br,deflate,',
        'content-type':'application/json'}
    res=req.post(url=url,data=data,headers=head)
    return res

def sendemail(email,success=""):
    text='放心睡觉！系统已为你打卡哦！'
    from_addr = ''
    password = ''
    # 发送邮箱
    # 收信方邮箱
    to_addr = email
    # 发信服务器
    smtp_server = 'smtp.163.com'
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    temp=str(text)
    msg = MIMEText(temp+'\n'+str(success), 'plain', 'utf-8')
    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('每日打卡系统通知')
    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL('smtp.163.com')
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()
def start(userid):
    i=0
    while(i<3):
        code = init(userid)
        if code[0].status_code == 200:
            sendemail(code[1])
            print("成功")
            break
        i+=1
        print('失败'+str(i)+'次')
        time.sleep(60)

bait_type_path = os.path.dirname(__file__)
task=os.listdir(os.path.join(bait_type_path, r'data'))
for i in task:
    start(i.split('.')[0])
    time.sleep(20)
sys.exit()

