# coding=gbk
import pymysql
def classInformation2(n,ID):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n == "1":  # �鿴���˽�ѧ��Ϣ
        ID_user=ID
        sql = "SELECT * FROM course WHERE ID='%s'" %(ID_user)
        cursor.execute(sql)
        results = cursor.fetchall()
        lentgh=len(results)
        a=[]
        print("��ʦ���  �γ̺�  �γ���   ��ʦ��    ��ʱ��    ѧ��    �γ̼�� ")
        for i in range(0,lentgh):
           a.append(results[i])
        for i in range(0,len(a)):
            print(a[i])
            # print("\n")

    elif n == "2":  #
        ID_user = ID
        sql = "SELECT count(cno) FROM course WHERE ID='%s'" % (ID_user)
        cursor.execute(sql)
        results = cursor.fetchone()
        results=str(results).replace("(","")
        results=results.replace(",)","")
        print("һ��%s��" %results)
    elif n == "3":
    # ���˵���һ��
        print("�ص���һ��")
#classInformation2("2","333")