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
    print("\t\t��ӭ����ѧУ������Ϣ����ϵͳ��")
    choose = input("���ȵ�¼����ע�ᡣ����1Ϊ��¼������2Ϊע�᣺")
    if choose=="1":
        userID = input("����������˺ţ�")
        password = getpass.getpass('������������룺')  # ����ʾ��������룬��IDE��������У�Ҫ����������
        # password = input("�������룺")
        userID = str(userID)
        password = str(password)
        password = gethash(password)  # ���������hash����
        try:
            a=login(userID, password)
            role=a[1]
            ID=a[0]
            if role is None:
                return -1
            if role == "admin":
                print("�������ǹ���Ա�ˣ�")
                administrator(ID)
            elif role == "usr":
                user_hanshu(ID)
            else:
                print("��Ȳ����û��ֲ��ǹ���Ա��")
                return 0
        except:
            conn.rollback()
            choose="2"
        #a�Ƿ��صĶ��������û���ID��role
    elif choose=="2":
        userID = input("����������˺ţ�")
        password = input("������������룺")
        password2 = input("���ٴ������������ȷ�ϣ�")
        userID = str(userID)
        password = str(password)
        password2 = str(password2)
        password = gethash(password)  # ���������hash����
        register(userID,password)
        #ע��ɹ�ֱ���˳��������û��ٴ򿪳�����е�¼
        return 0
    else:
        print("���벻���ʣ����������룬���򽫹رգ����Ҫ������ѡ1���е�¼�������Ƚ���ע��")
        time.sleep(3)
        return -1
    return 0
main()

