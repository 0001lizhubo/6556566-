# coding=gbk
import pymysql
def YanjiuInformation2(n,ID):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    ID_user = ID
    if n == "1":  # 查看个人科研信息
        try:
            #自然连接的关联查询
            sql = "SELECT * FROM keyan natural join teacher WHERE ID='%s'" % (ID_user)
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            #print(results)
            for row in results:
                ID_user = row[0]
                Proname = row[1]
                direction = row[2]
                station=row[3]
                papers = row[4]
                xingming=row[5]
                # 打印结果
                print("你的用户号编号：%s,姓名:%s  项目名称： %s,科研方向：%s,研究情况 %s，发表论文情况： %s" % (ID,xingming, Proname, direction,station, papers))
        except:
            conn.rollback()
            print("没有你的科研信息")
    elif n == "2":  # 添加自己的科研信息
        try:
            ID_user = ID
            Proname = input("请输入你的项目名称： ")
            direction = input("请输入你的科研方向： ")
            station=input("现在的研究状况:")
            papers = input("发表论文数量： ")
            #cursor = conn.cursor()
            # 执行sql语句
            sql = "INSERT INTO keyan(ID, Proname, direction,station, papers) VALUES(%s, %s, %s,%s,%s)"
            cursor.execute(sql,(ID_user,Proname, direction,station, papers))
            # 提交到数据库执行
            conn.commit()
        except:
            # Rollback in case there is any error
            conn.rollback()
    elif n == "3":
    # 回退到上一步
        print("回到上一步")
    elif n=="4":
        print("选择4论文篇数加1")
        sql = "UPDATE keyan set papers=papers+1 where ID='%s'"% (ID)
        cursor.execute(sql)
        conn.commit()
# YanjiuInformation2("1","100002")