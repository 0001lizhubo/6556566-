# coding=gbk
import pymysql
def YanjiuInformation(n):
    conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
    cursor = conn.cursor()
    if n == "1":  # 查看个人科研信息
        try:
            ID = input("输入教师的科研号：")
            cursor = conn.cursor()
            sql = "SELECT * FROM keyan WHERE ID='%s'" % (ID)
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                ID = row[0]
                name = row[1]
                direction = row[2]
                station=row[3]
                papers = row[4]
                # 打印结果
                print("该教师的科研编号：%s,项目名称： %s,科研方向：%s,研究情况 %s，发表论文情况： %s" % (ID, name, direction,station, papers))
        except:
            print("Error: unable to fecth data")
    elif n == "2":  # 添加科研信息
        try:
            ID = input("请输入科研课题组老师的ID号：")
            Proname = input("请输入项目名称： ")
            direction = input("请输入科研方向： ")
            station=input("现在的研究状况:")
            papers = input("发表论文数量： ")
            # 执行sql语句
            sql = "INSERT INTO keyan(ID, Proname, direction,station, papers) VALUES(%s, %s, %s,%s,%s)"
            cursor.execute(sql,(ID,Proname, direction,station, papers))
            # 提交到数据库执行
            conn.commit()
        except:
            # Rollback in case there is any error
            conn.rollback()
    elif n == "3":  #删除信息
        try:
            ID = input("请输入你想删除的科研项目对应老师的ID： ")
            cursor = conn.cursor()
            sql = "DELETE FROM keyan where ID = %s "
            cursor.execute(sql, (ID))
            conn.commit()
            print("删除成功")
        except:
            # Rollback in case there is any error
            print("请输入正确的ID")
            conn.rollback()
    elif n == "4":
    # 回退到上一步
        print("回到上一步")
    elif n=="5":
        try:
            #sql = "SELECT * FROM keyan natural join teacher WHERE ID='%s'" % (ID_user)
            # 执行SQL语句
            #cursor.execute(sql)
            # 获取所有记录列表
            #results = cursor.fetchall()
            # print(results)
            sql = "SELECT * FROM keyan natural join teacher"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                ID_user = row[0]
                Proname = row[1]
                direction = row[2]
                station = row[3]
                papers = row[4]
                xingming = row[5]
                # 打印结果
                print("用户编号：%s,姓名:%s  项目名称： %s,科研方向：%s,研究情况 %s，发表论文篇数： %s" % (
                ID_user, xingming, Proname, direction, station, papers))
            # lentgh = len(results)
            # a = []
            # print("科研教师编号     科研课题名      科研方向     现阶段研究成果    发表的论文数量")
            # for i in range(0, lentgh):
            #     a.append(results[i])
            # for i in range(0, len(a)):
            #     print(a[i])
        except:
            conn.rollback()
# YanjiuInformation("5")