# coding=gbk
import pymysql
def selfInfomation(n):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n=="1":#填写（插入）个人信息
        ID=input("输入你的编号：")
        name=input("输入你的名字：")
        age=input("你的年龄（输入20~75之间的数字）：")
        sex=input("你的性别（输入1为男，输入2为女。默认为男）：")
        if sex=="1":
            sex="男"
        elif sex=="2":
            sex="女"
        else:
            sex="男"
        education = input("你的学历：")
        department=input("你所属的部门（01为文学部，02为理学部，03为农业部，04为信息学部，05为工学部，06为医学部）：")
        school=input("你的毕业学校：")
        health=input("你的健康状况：")
        title=input("你的职称：")#职称
        post=input("你的职务：")#职务
        #rewards=input("你的工资：")
        sql = 'insert into teacher(ID, name, age, sex, education, department, school, health,title,post) values(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)'
        # sql = "INSERT INTO teacher(ID ,name,age,sex, education, department, school, health,title,post,rewards) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s);"
        cursor.execute(sql,(ID, name, age, sex, education, department, school, health,title,post))
        conn.commit()
        print("插入信息成功")
    elif n=="2":#更新个人信息，先打印个人的信息，然后给他选择修改那个信息
        try:
            name = input("你的要更新信息的人的名字：")
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
            newinput=input("请根据输出的信息选择要修改的地方，如修改年龄输入3：")
            newinput=int(newinput)
            a=input("输入你想改的内容：")
            a=str(a)
            sql="UPDATE teacher set "+list[newinput-1]+"="+a+" where name= '%s'" %(name)
            cursor.execute(sql)
            conn.commit()
            print("更新信息成功")
        except:
            conn.rollback()
    elif n=="3":
        #查看个人信息
        try:
            name=input("你的要查询的东西是什么，如ID就输1，姓名就输2，年龄就输3，部门就输6，毕业学校就输入7：")
            list = ['ID', "name", "age", "sex", "education", "department", "school", "health", "title", "post"]
            name=int(name)
            tiaojian=str(input("你的要查询的东西的值是什么"))
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
                # 打印结果
                print("用户编号：%s, 姓名:%s  年龄：%s, 性别：%s,教育程度： %s， 所属部门： %s  毕业学校：%s ， 健康状况： %s  职称：%s， 职务：%s" % (
                    ID_user, xingming, age, sex, education, bumen, school, health, title, post))
                #print("\t")
        except:
            print("你的输入有错误")
            conn.rollback()
    elif n == "4":  #删除个人信息
        try:
            ID = input("请输入你想删除的个人信息的ID： ")
            sql = "DELETE FROM teacher where ID = %s "
            cursor.execute(sql, (ID))
            conn.commit()
            print("删除成功")
        except:
            # Rollback in case there is any error
            print("请输入正确的ID")
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
                # 打印结果
                print("用户编号：%s, 姓名:%s  年龄：%s, 性别：%s,教育程度： %s， 所属部门： %s  毕业学校：%s ， 健康状况： %s  职称：%s， 职务：%s" % (
                    ID_user, xingming, age, sex, education, bumen,school,health,title,post))
        except:
            print("你的输入有错误")
            conn.rollback()
# selfInfomation("3")