# coding=gbk
# from register_or_login import *
from classInformation import *
from YanjiuInformation import *
from selfInfomation import  *
def administrator(ID):
    #print("你现在是管理员了。")
    choose = input("请输入你要进行的操作，输入0退出程序，输入1进入个人信息界面，输入2进入教学情况查询界面，输入3进入科研信息界面：")
    str(choose)
    while choose != "0":
        if choose == "1":
            print("恭喜进入个人信息界面！你可以选择\n 1填写某个人信息，2更新某个人信息，3查看某个人信息，4删除某个人信息，5查看所有的教职工信息,6退到上一步\n")
            n = input("请输入：")
            n = str(n)
            selfInfomation(n)
        elif choose == "2":
            print("恭喜进入教学信息界面！你可以选择\n 1添加某个人教学信息，2查看某个人教学信息，3删除教学信息，4退到上一步,5查看所有课程的信息\n")
            n = input("请输入：")
            n = str(n)
            classInformation(n)
        elif choose == "3":
            print("恭喜进入科研信息界面！你可以选择\n 1查看某个人科研信息，2添加某个人科研信息，3删除科研信息，4退到上一步，5查看所有科研的信息\n")
            n = input("请输入：")
            n = str(n)
            YanjiuInformation(n)
        else:
            print("输入错误，请重新输入0~3")
        choose = input("请输入你要进行的操作，输入0退出程序，输入1进入个人信息界面，输入2进入教学情况查询界面，输入3进入科研信息界面：")
        str(choose)
    return 0