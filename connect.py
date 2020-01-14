# coding=gbk
import pymysql
# 打开数据库连接
conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
cursor = conn.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
sql1="SELECT * FROM user WHERE ID='002'"
try:
    # 执行SQL语句
    cursor.execute(sql1)
    # 提交事务到数据库执行
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    # 如果发生错误则执行回滚操作
    conn.rollback()
#print('database version: %s' % data)
conn.close()
