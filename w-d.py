from flask import Flask,render_template,session
import os
import psutil
import time
import requests
import bs4

oldv="0.1.3"
newv="NONE"
new=1
def get_v():
    try:
        # 请求网页
        # 设置请求头、降低请求频率，防止反爬虫
        head = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
        }
        time.sleep(1)

        #TODO 修改下方需要爬取的网址
        url = "https://github.com/Wangxy666/wd-no-neijuan-for-Windows/blob/master/README.md"
        # 解析网页、选取数据
        res = requests.get(url, headers=head,timeout=5)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        #TODO 修改下方爬取条件中的标签名、属性
        data = soup.find_all("p", dir="auto")
        newv=data[0].text
        #判断当前版本是否最新
        if newv!=oldv:
            new=0
        else:
            new=1
    except:
        newv = "NONE"


app = Flask(__name__)
app.secret_key='wdfanneijuan'

#报错处理

@app.errorhandler(404)
def page_not_found(error):
    f=open('.\log\et.log','r')
    etime=int(f.read())
    f.close()
    etime=etime+1
    f=open('.\log\et.log','w')
    f.write(str(etime))
    f.close()
    session['et'] = str(etime)
    return render_template("错误.html",etime=etime), 404

#其他页面

@app.route("/")
def white():
    return render_template('跳转主页.html')
    
@app.route("/secret")
def secret():
    return "恭喜你发现了这个彩蛋页面，这个页面连html存放页面也没有！其实你发现了吗，反内卷协会才是最卷的（狗头）"

@app.route("/reget/v/")
def reget_v():
    get_v()

#反内卷

@app.route("/main/mainpage/")
def mainpage0():
    return render_template('0-主页.html',oldv=oldv,newv=newv,new=new)
    
@app.route("/main/member/")
def member0():
    return render_template('0-成员.html',oldv=oldv,newv=newv,new=new)
    
@app.route("/main/introduction/")
def introduction0():
    return render_template('0-介绍.html',oldv=oldv,newv=newv,new=new)
    
#反凡尔赛
    
@app.route("/branch1/mainpage/")
def mainpage1():
    return render_template('1-主页.html',oldv=oldv,newv=newv,new=new)
    
@app.route("/branch1/member/")
def member1():
    return render_template('1-成员.html',oldv=oldv,newv=newv,new=new)
    
@app.route("/branch1/introduction/")
def introduction1():
    return render_template('1-介绍.html',oldv=oldv,newv=newv,new=new)

    
    
def write_pid():
    pid = os.getpid()
    fp = open(".\log\pid.log",'w')
    fp.write(str(pid))
    fp.close()
        
def read_pid():
    if os.path.exists(".\log\pid.log"):
        fp = open(".\log\pid.log",'r')
        pid = fp.read()
        fp.close()
        return pid
    else:
        return False

def pidrun():
    pid = read_pid()
    pid = int(pid)
    if pid:
        running_pid = psutil.pids()
        if pid in running_pid:
            os.system("start http://127.0.0.1:5000/")
            sys.exit()
        else:
            write_pid()
    else:
        write_pid()



if __name__ == "__main__":
    pidrun()
    get_v()
    os.system("start http://127.0.0.1:5000/")
    app.run(host="0.0.0.0")
    #app.run(debug=True,use_reloader=False)
