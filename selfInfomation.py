# coding=gbk
import pymysql
def selfInfomation(n):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n=="1":#��д�����룩������Ϣ
        ID=input("������ı�ţ�")
        name=input("����������֣�")
        age=input("������䣨����20~75֮������֣���")
        sex=input("����Ա�����1Ϊ�У�����2ΪŮ��Ĭ��Ϊ�У���")
        if sex=="1":
            sex="��"
        elif sex=="2":
            sex="Ů"
        else:
            sex="��"
        education = input("���ѧ����")
        department=input("�������Ĳ��ţ�01Ϊ��ѧ����02Ϊ��ѧ����03Ϊũҵ����04Ϊ��Ϣѧ����05Ϊ��ѧ����06Ϊҽѧ������")
        school=input("��ı�ҵѧУ��")
        health=input("��Ľ���״����")
        title=input("���ְ�ƣ�")#ְ��
        post=input("���ְ��")#ְ��
        #rewards=input("��Ĺ��ʣ�")
        sql = 'insert into teacher(ID, name, age, sex, education, department, school, health,title,post) values(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)'
        # sql = "INSERT INTO teacher(ID ,name,age,sex, education, department, school, health,title,post,rewards) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s);"
        cursor.execute(sql,(ID, name, age, sex, education, department, school, health,title,post))
        conn.commit()
        print("������Ϣ�ɹ�")
    elif n=="2":#���¸�����Ϣ���ȴ�ӡ���˵���Ϣ��Ȼ�����ѡ���޸��Ǹ���Ϣ
        try:
            name = input("���Ҫ������Ϣ���˵����֣�")
            sql = "SELECT * FROM teacher WHERE name='%s'" % (name)
            list = ['ID', "name", "age", "sex", "education", "department", "school", "health", "title", "post"]
            cursor.execute(sql)
            results = cursor.fetchall()
            a = results[0]
            b = 0
            while b < len(a):
                list = ['ID', "name", "age", "sex", "education", "department", "school", "health", "title", "post"]
                print(list[b] + ": " + a[b])
                b = b + 1
            newinput=input("������������Ϣѡ��Ҫ�޸ĵĵط������޸���������3��")
            newinput=int(newinput)
            a=input("��������ĵ����ݣ�")
            a=str(a)
            sql="UPDATE teacher set "+list[newinput-1]+"="+a+" where name= '%s'" %(name)
            cursor.execute(sql)
            conn.commit()
            print("������Ϣ�ɹ�")
        except:
            conn.rollback()
    elif n=="3":
        #�鿴������Ϣ
        try:
            name=input("���Ҫ��ѯ�Ķ�����ʲô����ID����1����������2���������3�����ž���6����ҵѧУ������7��")
            list = ['ID', "name", "age", "sex", "education", "department", "school", "health", "title", "post"]
            name=int(name)
            tiaojian=str(input("���Ҫ��ѯ�Ķ�����ֵ��ʲô"))
            sql = "SELECT * FROM teacher WHERE "+ list[name-1] + " = '%s' " % (tiaojian)
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                ID_user = row[0]
                xingming = row[1]
                age = row[2]
                sex = row[3]
                education = row[4]
                bumen = row[5]
                school = row[6]
                health = row[7]
                title = row[8]
                post = row[9]
                # ��ӡ���
                print("�û���ţ�%s, ����:%s  ���䣺%s, �Ա�%s,�����̶ȣ� %s�� �������ţ� %s  ��ҵѧУ��%s �� ����״���� %s  ְ�ƣ�%s�� ְ��%s" % (
                    ID_user, xingming, age, sex, education, bumen, school, health, title, post))
                #print("\t")
        except:
            print("��������д���")
            conn.rollback()
    elif n == "4":  #ɾ��������Ϣ
        try:
            ID = input("����������ɾ���ĸ�����Ϣ��ID�� ")
            sql = "DELETE FROM teacher where ID = %s "
            cursor.execute(sql, (ID))
            conn.commit()
            print("ɾ���ɹ�")
        except:
            # Rollback in case there is any error
            print("��������ȷ��ID")
            conn.rollback()
    elif n=="5":
        try:
            sql = "SELECT * FROM teacher "
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                ID_user = row[0]
                xingming = row[1]
                age = row[2]
                sex = row[3]
                education = row[4]
                bumen = row[5]
                school=row[6]
                health=row[7]
                title=row[8]
                post=row[9]
                # ��ӡ���
                print("�û���ţ�%s, ����:%s  ���䣺%s, �Ա�%s,�����̶ȣ� %s�� �������ţ� %s  ��ҵѧУ��%s �� ����״���� %s  ְ�ƣ�%s�� ְ��%s" % (
                    ID_user, xingming, age, sex, education, bumen,school,health,title,post))
        except:
            print("��������д���")
            conn.rollback()
# selfInfomation("3")