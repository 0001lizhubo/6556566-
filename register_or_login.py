# coding=gbk
from sha import *
import pymysql
import time
import getpass
#��¼����ע��
def register_or_login(choose):
    # �����ݿ�����
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if choose=="1":
        userID = input("����������˺ţ�")
        #password =getpass.getpass('������������룺')#����ʾ��������룬��IDE��������У�Ҫ����������
        password = input("�������룺")
        userID=str(userID)
        password=str(password)
        password = gethash(password)  # ���������hash����
        login(userID, password)

    elif choose=="2":
        userID = input("����������˺ţ�")
        password = input("������������룺")
        password2 = input("���ٴ������������ȷ�ϣ�")
        userID = str(userID)
        password = str(password)
        password2 = str(password2)
        if password==password2:
            password = gethash(password)  # ���������hash����
            register(userID,password)
        else:
            print("������������벻һ��")
            time.sleep(3)
    else:
        #print("���벻���ʣ�����������")
        c=input("���ȵ�¼����ע�ᡣ����1Ϊ��¼������2Ϊע�᣺")
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
            #print("����ʲô���͵��û�"+a[2])
            b=[a[0],a[2]]
            return b
            #print("����ʲô���͵��û�")
        if userID==a[0] and password!=a[1]:
            print("�������")
            time.sleep(3)
            return -1
        elif userID=="" or password=="":
            print("�û����������벻��Ϊ�գ�")
            time.sleep(3)
            return -1
    except:
        print("�û������ڣ�����ע��")
        time.sleep(3)
        register_or_login("2")

def register(username,password):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    sql = "SELECT ID FROM user WHERE ID='%s'" % (username)
    cursor.execute(sql)
    results = cursor.fetchone()
    #���Ԫ��Ϊ����ô��ʾ����û������û�,���Խ����������û�
    if not results:
        sql1 = 'insert into user(ID, password,role) values(%s, %s,%s)'
        cursor.execute(sql1,(username,password,"usr"))
        conn.commit()
        print("ע��ɹ���")
        time.sleep(3)
    else:
        print(results)
        print("����û����Ѿ����ڣ�������ѡһ���û�����¼��")
        time.sleep(3)

#register_or_login("1")