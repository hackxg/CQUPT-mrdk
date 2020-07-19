#coding=utf-8
import tornado.ioloop
import tornado.web
import os
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
class postHandler(tornado.web.RequestHandler):

    def post(self):
        name=self.get_argument("username")
        if(name==None):
            self.write('信息不全')
        else:
            xh=self.get_argument("id")
            if(xh==None):
                self.write('信息不全')
            else:
                sexy=self.get_argument("sexy")
                if (sexy == None):
                    self.write('信息不全')
                else:
                    lxdh=self.get_argument("lxdh")
                    if (lxdh == None):
                        self.write('信息不全')
                    else:
                        szdq = self.get_argument("szdq")
                        if (szdq == None):
                            self.write('信息不全')
                        else:
                            xxdz = self.get_argument("xxdz")
                            if (xxdz == None):
                                self.write('信息不全')
                            else:
                                hjsfly = self.get_argument("hjsfly")
                                if (hjsfly == None):
                                    self.write('信息不全')
                                else:
                                    sfyfy = self.get_argument("sfyfy")
                                    if (sfyfy == None):
                                        self.write('信息不全')
                                    else:
                                        email = self.get_argument("email")
                                        if (email == None):
                                            self.write('信息不全')
                                        else:
                                            password = self.get_argument("password")
                                            if (password == None):
                                                self.write('信息不全')
                                            else:
                                                code = self.get_argument("testcode")
                                                if (code == None):
                                                    self.write('信息不全')
                                                else:
                                                    if getkey(code) == True:
                                                        if pd(xh,password)==True:
                                                            temp= '''{"name":"xx"}'''
                                                            temp=json.loads(temp)
                                                            temp["name"]=name
                                                            temp["xh"]=xh
                                                            temp["xb"]=sexy
                                                            temp["lxdh"]=lxdh
                                                            temp["szdq"]=szdq
                                                            temp["xxdz"]=xxdz
                                                            temp["hjsfly"]=hjsfly
                                                            temp["sfyfy"]=sfyfy
                                                            temp["email"]=email
                                                            temp["password"]=password
                                                            set(temp,xh,email)
                                                            self.write('操作成功')
                                                        else:
                                                            self.write('操作失败如果需要更改信息请输入正确的超级密码。')
                                                            self.write('如果需要关闭每日打卡 请前往指定页面')
                                                    else:
                                                        self.write('操作失败测试码无效或已达使用上限~')
def getkey(code):
    bait_type_path = os.path.dirname(__file__)
    f = open(os.path.join(bait_type_path, r'key.json'), encoding='utf-8-sig')
    temp = json.load(f)
    f.close()
    if temp['key']==code and int(temp["times"])>0:
        temp["times"]=int(temp["times"])-1
        f = open(os.path.join(bait_type_path, r'key.json'), 'w', encoding='utf-8-sig')
        f.write(json.dumps(temp, ensure_ascii=False))
        f.close()
        return True
    else:
            return False
    return False

def set(text,usr_id,email):
    bait_type_path = os.path.dirname(__file__)
    f = open(os.path.join(bait_type_path, r'data/' + usr_id + '.json'),'w', encoding='utf-8-sig')
    f.write(json.dumps(text,ensure_ascii=False))
    f.close()
    sendemail(email,"\n"+"再次声明：此软件仅供学习使用，如果你的行程或身体状况发送转变"+"\n"+"请前往http://www.longm.top/mrdk/ 修改你的信息或关闭本服务")
def pd(xh,password):
    bait_type_path = os.path.dirname(__file__)
    task = os.listdir(os.path.join(bait_type_path, r'data'))
    for i in task:
        if i.split('.')[0]==xh:
            bait_type_path = os.path.dirname(__file__)
            f = open(os.path.join(bait_type_path, r'data/' + i.split('.')[0] + '.json'), encoding='utf-8-sig')
            temp = json.load(f)
            f.close()
            if temp['password']==password:
                return True
            else:
                return False
    return True
def sendemail(email,text):
    # 发送邮箱服务器
    # 发送邮箱用户/密码
    from_addr = ''#email
    password = ''#key
    # 发送邮箱
    # 收信方邮箱
    to_addr = email
    # 发信服务器
    smtp_server = 'smtp.163.com'
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    temp='系统已经收到你的反馈！\n'+str(text)
    msg = MIMEText(temp, 'plain', 'utf-8')
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
def edit(xh,oldpassword,password):
    bait_type_path = os.path.dirname(__file__)
    task = os.listdir(os.path.join(bait_type_path, r'data'))
    for i in task:
        if i.split('.')[0]==xh:
            bait_type_path = os.path.dirname(__file__)
            f = open(os.path.join(bait_type_path, r'data/' + i.split('.')[0] + '.json'),'r', encoding='utf-8-sig')
            temp = json.load(f)
            f.close()
            if temp['password']==oldpassword:
                temp['password']=password
                f = open(os.path.join(bait_type_path, r'data/' + i.split('.')[0] + '.json'), 'w', encoding='utf-8-sig')
                f.write(json.dumps(temp,ensure_ascii=False))
                f.close()
                return True
            else:
                f.close()
                return False

    return False
class changeHandler(tornado.web.RequestHandler):
    def post(self):
        xh = self.get_argument("id")
        if xh==None:
            self.write('信息不完整')
        else:
            email=self.get_argument("email")
            if email==None:
                self.write('信息不完整')
            else:
                password=self.get_argument("password")
                if password==None:
                    self.write('信息不完整')
                else:
                    if pd(xh,password)==True:
                        bait_type_path = os.path.dirname(__file__)
                        os.remove(os.path.join(bait_type_path, r'data/' + xh + '.json'))
                        self.write("删除成功!")
                        sendemail(email,"你刚才通过超级密码关闭了本服务。")
                    else:
                        self.write("删除失败请检查信息后重试!")
class passHandler(tornado.web.RequestHandler):
    def post(self):
        xh = self.get_argument("id")
        if xh==None:
            self.write('信息不完整')
        else:
            email=self.get_argument("email")
            if email==None:
                self.write('信息不完整')
            else:
                oldpassword=self.get_argument("oldpassword")
                if oldpassword==None:
                    self.write('信息不完整')
                else:
                    password = self.get_argument("password")
                    if password == None:
                        self.write('信息不完整')
                    else:
                        if edit(xh,oldpassword,password)==True:
                            sendemail(email, "你刚才修改了超级密码！")
                            self.write("修改成功!")
                        else:
                            self.write("修改失败请检查信息后重试!")
app = tornado.web.Application(
        handlers = [
            (r"/mrdk/api",postHandler),
            (r"/mrdk/change",changeHandler),
            (r"/mrdk/edit",passHandler)
        ],debug = False
)
application = tornado.httpserver.HTTPServer(app)

if __name__ == "__main__":
    print("服务已启动")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
