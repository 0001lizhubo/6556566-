# coding=gbk
import pymysql
def YanjiuInformation(n):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n == "1":  # �鿴���˿�����Ϣ
        try:
            ID = input("�����ʦ�Ŀ��кţ�")
            cursor = conn.cursor()
            sql = "SELECT * FROM keyan WHERE ID='%s'" % (ID)
            # ִ��SQL���
            cursor.execute(sql)
            # ��ȡ���м�¼�б�
            results = cursor.fetchall()
            for row in results:
                ID = row[0]
                name = row[1]
                direction = row[2]
                station=row[3]
                papers = row[4]
                # ��ӡ���
                print("�ý�ʦ�Ŀ��б�ţ�%s,��Ŀ���ƣ� %s,���з���%s,�о���� %s��������������� %s" % (ID, name, direction,station, papers))
        except:
            print("Error: unable to fecth data")
    elif n == "2":  # ��ӿ�����Ϣ
        try:
            ID = input("��������п�������ʦ��ID�ţ�")
            Proname = input("��������Ŀ���ƣ� ")
            direction = input("��������з��� ")
            station=input("���ڵ��о�״��:")
            papers = input("�������������� ")
            # ִ��sql���
            sql = "INSERT INTO keyan(ID, Proname, direction,station, papers) VALUES(%s, %s, %s,%s,%s)"
            cursor.execute(sql,(ID,Proname, direction,station, papers))
            # �ύ�����ݿ�ִ��
            conn.commit()
        except:
            # Rollback in case there is any error
            conn.rollback()
    elif n == "3":  #ɾ����Ϣ
        try:
            ID = input("����������ɾ���Ŀ�����Ŀ��Ӧ��ʦ��ID�� ")
            cursor = conn.cursor()
            sql = "DELETE FROM keyan where ID = %s "
            cursor.execute(sql, (ID))
            conn.commit()
            print("ɾ���ɹ�")
        except:
            # Rollback in case there is any error
            print("��������ȷ��ID")
            conn.rollback()
    elif n == "4":
    # ���˵���һ��
        print("�ص���һ��")
    elif n=="5":
        try:
            #sql = "SELECT * FROM keyan natural join teacher WHERE ID='%s'" % (ID_user)
            # ִ��SQL���
            #cursor.execute(sql)
            # ��ȡ���м�¼�б�
            #results = cursor.fetchall()
            # print(results)
            sql = "SELECT * FROM keyan natural join teacher"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                ID_user = row[0]
                Proname = row[1]
                direction = row[2]
                station = row[3]
                papers = row[4]
                xingming = row[5]
                # ��ӡ���
                print("�û���ţ�%s,����:%s  ��Ŀ���ƣ� %s,���з���%s,�о���� %s����������ƪ���� %s" % (
                ID_user, xingming, Proname, direction, station, papers))
            # lentgh = len(results)
            # a = []
            # print("���н�ʦ���     ���п�����      ���з���     �ֽ׶��о��ɹ�    �������������")
            # for i in range(0, lentgh):
            #     a.append(results[i])
            # for i in range(0, len(a)):
            #     print(a[i])
        except:
            conn.rollback()
# YanjiuInformation("5")