# coding=gbk
import pymysql
def classInformation(n):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n == "2":  # �鿴��ѧ��Ϣ
        ID=input("�����ʦ��ţ�")
        sql = "SELECT * FROM course WHERE ID='%s'" %(ID)
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

    elif n == "1":  # ��Ӹ��˽�ѧ��Ϣ
        ID = input("�����ʦ�ı�ţ�")
        cno=input("�γ̺ţ�")
        cname=input("�γ�����")
        name=input("��ʦ������")
        times=input("��ʱ����")
        credit=input("ѧ�֣�")
        kechengxingzhi=input("�γ̸�Ҫ:")
        sql = 'insert into course(ID,cno,cname,name,times,credit,kechengxingzhi) values(%s, %s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (ID,cno,cname,name,times,credit,kechengxingzhi))
        conn.commit()

    elif n == "3":  #ɾ����Ϣ
        try:
            cno = input("����������ɾ���Ŀγ̺ţ� ")
            cursor = conn.cursor()
            sql = "DELETE FROM course where cno = %s "
            cursor.execute(sql, (cno))
            conn.commit()
            print("ɾ���ɹ�")
        except:
            # Rollback in case there is any error
            conn.rollback()
            print("��������ȷ�Ŀγ̺�")
    elif n == "4":
    # ���˵���һ��
        print("�ص���һ��")
    elif n=="5":
        sql = "SELECT * FROM course "
        cursor.execute(sql)
        results = cursor.fetchall()
        lentgh = len(results)
        a = []
        print("     ��ʦ���     �γ̺�      �γ���     ��ʦ��    ��ʱ��  ѧ��    �γ̼�� ")
        for i in range(0, lentgh):
            a.append(results[i])
        for i in range(0, len(a)):
            print(a[i])
            # print("\n")
#classInformation("5")