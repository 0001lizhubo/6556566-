# coding=gbk
import pymysql
# �����ݿ�����
conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
cursor = conn.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
sql1="SELECT * FROM user WHERE ID='002'"
try:
    # ִ��SQL���
    cursor.execute(sql1)
    # �ύ�������ݿ�ִ��
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    # �������������ִ�лع�����
    conn.rollback()
#print('database version: %s' % data)
conn.close()
