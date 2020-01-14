# coding=gbk
# from register_or_login import *
from classInformation2 import *
from YanjiuInfomation2 import *
from selfinformation_user import  *
def user_hanshu(ID):
    print("你现在是用户了。\n")
    print("用户只能1.添加个人信息，2.更改个人信息，3.查询个人信息，4.查看个人教学信息，5.查看个人科研信息，6.添加个人研究信息\n")
    choose = input("请输入你要进行的操作，输入0退出程序，输入1进入个人信息界面，输入2进入教学情况查询界面，输入3进入科研信息界面：")
    str(choose)
    while choose != "0":
        if choose == "1":
            print("恭喜进入个人信息界面！你可以选择\n1填写个人信息，2更新个人的年龄或者部门，3查看个人信息，4退到上一步\n")
            n = input("请输入：")
            n = str(n)
            selfInfomation2(n,ID)
        elif choose == "2":
            print("恭喜进入教学信息界面！你可以选择\n1查看个人教学信息，2查看自己究竟任课几门，3退到上一步\n")
            n = input("请输入：")
            n = str(n)
            classInformation2(n,ID)
        elif choose == "3":
            print("恭喜进入教学信息界面！你可以选择\n1查看个人科研信息，2添加个人科研信息，3退到上一步 ，4增加论文的篇数\n")
            n = input("请输入：")
            n = str(n)
            YanjiuInformation2(n,ID)
        else:
            print("输入错误，请重新输入0~3")
        choose = input("请输入你要进行的操作，输入0退出程序，输入1进入个人信息界面，输入2进入教学情况查询界面，输入3进入科研信息界面：")
        str(choose)
    return 0