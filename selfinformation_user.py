# coding=gbk
import pymysql
def selfInfomation2(n,ID):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n=="1":#填写（插入）个人信息
        ID_user=ID
        sql = "SELECT * FROM teacher WHERE ID='%s'" % (ID)
        cursor.execute(sql)
        results = cursor.fetchone()
        if results is not None:#数据库中以及存在他的个人信息了，那么
            print("你的信息已经存在，请选择2进行修改")
        else:
            name=input("输入你的名字：")
            age=input("你的年龄（输入20~75之间的数字）：")
            sex=input("你的性别（输入1为男，输入2为女。默认为男）：")
            if sex == "1":
                sex = "男"
            elif sex == "2":
                sex = "女"
            else:
                sex = "男"
            education = input("你的学历：")
            department=input("你所属的部门（01为文学部，02为理学部，03为农业部，04为信息学部，05为工学部，06为医学部）：")
            school=input("你的毕业学校：")
            health=input("你的健康状况：")
            title=input("你的职称：")#职称
            post=input("你的职务：")#职务
            #rewards=input("你的工资：")
            sql = 'insert into teacher(ID, name, age, sex, education, department, school, health,title,post) values(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)'
            # sql = "INSERT INTO teacher(ID_user ,name,age,sex, education, department, school, health,title,post,rewards) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s);"
            cursor.execute(sql,(ID, name, age, sex, education, department, school, health,title,post))
            conn.commit()
    elif n=="2":#更新个人信息，先打印个人的信息，然后给他选择修改那个信息
        try:
            print("你的个人信息为：\n")
            sql = "SELECT * FROM teacher WHERE ID='%s'" % (ID)
            cursor.execute(sql)
            results = cursor.fetchall()
            a = results[0]
            c = []
            for b in a:
                c.append(b)
            print(c)
            list=['ID', "name", "age","sex", "education", "department", "school", "health","title","post"]
            newinput=input("请根据输出的信息选择要修改的地方，修改年龄输入3，修改部门输入6：")
            newinput=int(newinput)
            if newinput>10:
                print("超出修改范围")
                pass
            elif newinput<=10:
                a=str(input("输入你想改成多少："))

                sql="UPDATE teacher set "+list[newinput-1]+"="+a+" where ID= '%s'" %(ID)
                cursor.execute(sql)
                conn.commit()
        except:
            print("你应该好好的按要求输入！")
            conn.rollback()
    elif n=="3":
        #查看个人信息
        try:
            print("你的个人信息为：\n")
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