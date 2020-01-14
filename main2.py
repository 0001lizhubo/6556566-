# coding=gbk
from register_or_login import *
# from classInformation import *
# from YanjiuInformation import *
# from selfInfomation import  *
import getpass
import time
from administrator import *
from user_hanshu import *
def main():
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    print("\t\t欢迎来到学校人事信息管理系统！")
    choose = input("请先登录或者注册。输入1为登录，输入2为注册：")
    if choose=="1":
        userID = input("请输入你的账号：")
        password = getpass.getpass('请输入你的密码：')  # 不显示输入的密码，在IDE中这个不行，要用下面的这个
        # password = input("输入密码：")
        userID = str(userID)
        password = str(password)
        password = gethash(password)  # 对密码进行hash加密
        try:
            a=login(userID, password)
            role=a[1]
            ID=a[0]
            if role is None:
                return -1
            if role == "admin":
                print("你现在是管理员了！")
                administrator(ID)
            elif role == "usr":
                user_hanshu(ID)
            else:
                print("你既不是用户又不是管理员！")
                return 0
        except:
            conn.rollback()
            choose="2"
        #a是返回的东西包括用户的ID和role
    elif choose=="2":
        userID = input("请输入你的账号：")
        password = input("请输入你的密码：")
        password2 = input("请再次输入密码进行确认：")
        userID = str(userID)
        password = str(password)
        password2 = str(password2)
        password = gethash(password)  # 对密码进行hash加密
        register(userID,password)
        #注册成功直接退出程序，让用户再打开程序进行登录
        return 0
    else:
        print("输入不合适，请重新输入，程序将关闭，如果要访问请选1进行登录，或者先进行注册")
        time.sleep(3)
        return -1
    return 0
main()

