# coding=gbk
import pymysql
def classInformation(n):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n == "2":  # 查看教学信息
        ID=input("输入教师编号：")
        sql = "SELECT * FROM course WHERE ID='%s'" %(ID)
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

    elif n == "1":  # 添加个人教学信息
        ID = input("输入教师的编号：")
        cno=input("课程号：")
        cname=input("课程名：")
        name=input("教师姓名：")
        times=input("课时数：")
        credit=input("学分：")
        kechengxingzhi=input("课程概要:")
        sql = 'insert into course(ID,cno,cname,name,times,credit,kechengxingzhi) values(%s, %s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (ID,cno,cname,name,times,credit,kechengxingzhi))
        conn.commit()

    elif n == "3":  #删除信息
        try:
            cno = input("请输入你想删除的课程号： ")
            cursor = conn.cursor()
            sql = "DELETE FROM course where cno = %s "
            cursor.execute(sql, (cno))
            conn.commit()
            print("删除成功")
        except:
            # Rollback in case there is any error
            conn.rollback()
            print("请输入正确的课程号")
    elif n == "4":
    # 回退到上一步
        print("回到上一步")
    elif n=="5":
        sql = "SELECT * FROM course "
        cursor.execute(sql)
        results = cursor.fetchall()
        lentgh = len(results)
        a = []
        print("     教师编号     课程号      课程名     教师名    课时数  学分    课程简介 ")
        for i in range(0, lentgh):
            a.append(results[i])
        for i in range(0, len(a)):
            print(a[i])
            # print("\n")
#classInformation("5")