# coding=gbk
import pymysql
def selfInfomation2(n,ID):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n=="1":#��д�����룩������Ϣ
        ID_user=ID
        sql = "SELECT * FROM teacher WHERE ID='%s'" % (ID)
        cursor.execute(sql)
        results = cursor.fetchone()
        if results is not None:#���ݿ����Լ��������ĸ�����Ϣ�ˣ���ô
            print("�����Ϣ�Ѿ����ڣ���ѡ��2�����޸�")
        else:
            name=input("����������֣�")
            age=input("������䣨����20~75֮������֣���")
            sex=input("����Ա�����1Ϊ�У�����2ΪŮ��Ĭ��Ϊ�У���")
            if sex == "1":
                sex = "��"
            elif sex == "2":
                sex = "Ů"
            else:
                sex = "��"
            education = input("���ѧ����")
            department=input("�������Ĳ��ţ�01Ϊ��ѧ����02Ϊ��ѧ����03Ϊũҵ����04Ϊ��Ϣѧ����05Ϊ��ѧ����06Ϊҽѧ������")
            school=input("��ı�ҵѧУ��")
            health=input("��Ľ���״����")
            title=input("���ְ�ƣ�")#ְ��
            post=input("���ְ��")#ְ��
            #rewards=input("��Ĺ��ʣ�")
            sql = 'insert into teacher(ID, name, age, sex, education, department, school, health,title,post) values(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)'
            # sql = "INSERT INTO teacher(ID_user ,name,age,sex, education, department, school, health,title,post,rewards) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s);"
            cursor.execute(sql,(ID, name, age, sex, education, department, school, health,title,post))
            conn.commit()
    elif n=="2":#���¸�����Ϣ���ȴ�ӡ���˵���Ϣ��Ȼ�����ѡ���޸��Ǹ���Ϣ
        try:
            print("��ĸ�����ϢΪ��\n")
            sql = "SELECT * FROM teacher WHERE ID='%s'" % (ID)
            cursor.execute(sql)
            results = cursor.fetchall()
            a = results[0]
            c = []
            for b in a:
                c.append(b)
            print(c)
            list=['ID', "name", "age","sex", "education", "department", "school", "health","title","post"]
            newinput=input("������������Ϣѡ��Ҫ�޸ĵĵط����޸���������3���޸Ĳ�������6��")
            newinput=int(newinput)
            if newinput>10:
                print("�����޸ķ�Χ")
                pass
            elif newinput<=10:
                a=str(input("��������ĳɶ��٣�"))

                sql="UPDATE teacher set "+list[newinput-1]+"="+a+" where ID= '%s'" %(ID)
                cursor.execute(sql)
                conn.commit()
        except:
            print("��Ӧ�úúõİ�Ҫ�����룡")
            conn.rollback()
    elif n=="3":
        #�鿴������Ϣ
        try:
            print("��ĸ�����ϢΪ��\n")
            sql = "SELECT * FROM teacher WHERE ID='%s'" % (ID)
            cursor.execute(sql)
            results = cursor.fetchall()
            a = results[0]
            c=[]
            for b in a:
                c.append(b)
            print(c)

        except:
            conn.rollback()
#selfInfomation2("1","1000004")