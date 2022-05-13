from flask import Flask,render_template
import os
import psutil
import time
import pickle

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    f=open('.\log\et.log','r')
    etime=int(f.read())
    f.close()
    etime=etime+1
    f=open('.\log\et.log','w')
    f.write(str(etime))
    f.close()
    print(etime)
    return render_template("错误.html",etime=etime), 404

@app.route("/")
def white():
    return render_template('跳转主页.html')

@app.route("/secret")
def secret():
    return "恭喜你发现了这个彩蛋页面，这个页面连html存放页面也没有！其实你发现了吗，反内卷协会才是最卷的（狗头）"

#反内卷

@app.route("/main/mainpage/")
def mainpage0():
    return render_template('0-主页.html')

@app.route("/main/member/")
def member0():
    return render_template('0-成员.html')

@app.route("/main/introduction/")
def introduction0():
    return render_template('0-介绍.html')

#反凡尔赛

@app.route("/branch1/mainpage/")
def mainpage1():
    return render_template('1-主页.html')

@app.route("/branch1/member/")
def member1():
    return render_template('1-成员.html')

@app.route("/branch1/introduction/")
def introduction1():
    return render_template('1-介绍.html')




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
            sys.exit()
        else:
            write_pid()
    else:
        write_pid()



if __name__ == "__main__":
    pidrun()
    app.run()
