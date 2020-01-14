# coding=gbk
import pymysql
def classInformation2(n,ID):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n == "1":  # 查看个人教学信息
        ID_user=ID
        sql = "SELECT * FROM course WHERE ID='%s'" %(ID_user)
        cursor.execute(sql)
        results = cursor.fetchall()
        lentgh=len(results)
        a=[]
        print("教师编号  课程号  课程名   教师名    课时数    学分    课程简介 ")
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
        print("一共%s门" %results)
    elif n == "3":
    # 回退到上一步
        print("回到上一步")
#classInformation2("2","333")