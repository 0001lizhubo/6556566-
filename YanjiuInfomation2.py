# coding=gbk
import pymysql
def YanjiuInformation2(n,ID):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    ID_user = ID
    if n == "1":  # �鿴���˿�����Ϣ
        try:
            #��Ȼ���ӵĹ�����ѯ
            sql = "SELECT * FROM keyan natural join teacher WHERE ID='%s'" % (ID_user)
            # ִ��SQL���
            cursor.execute(sql)
            # ��ȡ���м�¼�б�
            results = cursor.fetchall()
            #print(results)
            for row in results:
                ID_user = row[0]
                Proname = row[1]
                direction = row[2]
                station=row[3]
                papers = row[4]
                xingming=row[5]
                # ��ӡ���
                print("����û��ű�ţ�%s,����:%s  ��Ŀ���ƣ� %s,���з���%s,�о���� %s��������������� %s" % (ID,xingming, Proname, direction,station, papers))
        except:
            conn.rollback()
            print("û����Ŀ�����Ϣ")
    elif n == "2":  # ����Լ��Ŀ�����Ϣ
        try:
            ID_user = ID
            Proname = input("�����������Ŀ���ƣ� ")
            direction = input("��������Ŀ��з��� ")
            station=input("���ڵ��о�״��:")
            papers = input("�������������� ")
            #cursor = conn.cursor()
            # ִ��sql���
            sql = "INSERT INTO keyan(ID, Proname, direction,station, papers) VALUES(%s, %s, %s,%s,%s)"
            cursor.execute(sql,(ID_user,Proname, direction,station, papers))
            # �ύ�����ݿ�ִ��
            conn.commit()
        except:
            # Rollback in case there is any error
            conn.rollback()
    elif n == "3":
    # ���˵���һ��
        print("�ص���һ��")
    elif n=="4":
        print("ѡ��4����ƪ����1")
        sql = "UPDATE keyan set papers=papers+1 where ID='%s'"% (ID)
        cursor.execute(sql)
        conn.commit()
# YanjiuInformation2("1","100002")