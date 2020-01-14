# coding=gbk
from sha import *
import pymysql
import time
import getpass
#登录或者注册
def register_or_login(choose):
    # 打开数据库连接
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if choose=="1":
        userID = input("请输入你的账号：")
        #password =getpass.getpass('请输入你的密码：')#不显示输入的密码，在IDE中这个不行，要用下面的这个
        password = input("输入密码：")
        userID=str(userID)
        password=str(password)
        password = gethash(password)  # 对密码进行hash加密
        login(userID, password)

    elif choose=="2":
        userID = input("请输入你的账号：")
        password = input("请输入你的密码：")
        password2 = input("请再次输入密码进行确认：")
        userID = str(userID)
        password = str(password)
        password2 = str(password2)
        if password==password2:
            password = gethash(password)  # 对密码进行hash加密
            register(userID,password)
        else:
            print("两次输入的密码不一样")
            time.sleep(3)
    else:
        #print("输入不合适，请重新输入")
        c=input("请先登录或者注册。输入1为登录，输入2为注册：")
        register_or_login(c)

def login(userID ,password):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    try:
        user_name=userID
        sql = "SELECT ID,password,role FROM user WHERE ID='%s'" % (user_name)
        cursor.execute(sql)
        results=cursor.fetchone()
        a=results
        if userID==a[0] and password==a[1]:
            print("welcome you!")
            #print("你是什么类型的用户"+a[2])
            b=[a[0],a[2]]
            return b
            #print("你是什么类型的用户")
        if userID==a[0] and password!=a[1]:
            print("密码错误")
            time.sleep(3)
            return -1
        elif userID=="" or password=="":
            print("用户名或者密码不能为空！")
            time.sleep(3)
            return -1
    except:
        print("用户不存在，请先注册")
        time.sleep(3)
        register_or_login("2")

def register(username,password):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    sql = "SELECT ID FROM user WHERE ID='%s'" % (username)
    cursor.execute(sql)
    results = cursor.fetchone()
    #如果元组为空那么表示里面没有这个用户,可以进行添加这个用户
    if not results:
        sql1 = 'insert into user(ID, password,role) values(%s, %s,%s)'
        cursor.execute(sql1,(username,password,"usr"))
        conn.commit()
        print("注册成功！")
        time.sleep(3)
    else:
        print(results)
        print("这个用户名已经存在，请重新选一个用户名登录！")
        time.sleep(3)

#register_or_login("1")