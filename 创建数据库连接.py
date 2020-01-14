# coding=gbk
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter
import pymysql

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.wm_title("人事管理系统")
        self.geometry("700x600")
        self.resizable(width = False,height = False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # 创建一个菜单项，类似于导航栏
        menubar=Menu(self)
        # 创建菜单项
        menubar.add_cascade(label="登录",command=lambda: self.show_frame(StartPage))
        menubar.add_cascade(label="注册",command=lambda: self.show_frame(PageOne))
        menubar.add_cascade(label="个人信息填写",command=lambda: self.show_frame(PageTwo))
        menubar.add_cascade(label="个人信息查询",command=lambda: self.show_frame(PageThree))
        menubar.add_cascade(label="部门人员查询",command=lambda: self.show_frame(PageFore))
        menubar.add_cascade(label="专业配置",command=lambda: self.show_frame(PageFive))
        menubar.add_cascade(label="学历配置",command=lambda: self.show_frame(PageSix))
        menubar.add_cascade(label="生日查询",command=lambda: self.show_frame(PageSeven))
        self['menu']=menubar

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree,PageFore,PageFive,PageSix,PageSeven):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # 切换，提升当前 tk.Frame z轴顺序

#登录
class StartPage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)

        labeltxt = tk.Label(self,
                        text = "用户登录",
                        font = ("楷体",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 240,y = 50)

        labelt1 = tk.Label(self,
                        text = "账户:",
                        font = ("楷体",25)
                        )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 210,y = 200)

        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 300,y = 215)

        # 登录密码
        labelt2 = tk.Label(self,
                            text = "密码:",
                            font = ("楷体",25)
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 210,y = 320)

        var2 = StringVar()
        e2 = Entry(self,
                  textvariable = var2,
                   show = "*"
                  )
        e2.pack()
        e2.place(x = 300,y = 335)

        # 按钮设计
        btnkaishi = tk.Button(self,
                              text="直接登录",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 50,y = 470)

        btnkaishi = tk.Button(self,
                              text="立即注册",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command=lambda: root.show_frame(PageOne)
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 500,y = 470)

#注册账号信息
class PageOne(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)

        labeltxt = tk.Label(self,
                            text = "账号注册",
                            font = ("楷体",40),
                            )
        labeltxt.pack()
        labeltxt.place(x = 240,y = 50)

        # 登录账号
        labelt1 = tk.Label(self,
                            text = "账户:",
                            font = ("楷体",25)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 200,y = 140)

        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 305,y = 150)

        # 登录密码
        labelt2 = tk.Label(self,
                            text = "密码:",
                            font = ("楷体",25)
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 200,y = 240)

        var2 = StringVar()
        e2 = Entry(self,
                  textvariable = var2,
                   show = "*"
                  )
        e2.pack()
        e2.place(x = 305,y = 250)

        # 确认密码
        labelt3 = tk.Label(self,
                            text = "确认密码:",
                            font = ("楷体",25)
                            )
        labelt3.pack(padx=5, pady=10, side=tk.LEFT)
        labelt3.place(x = 150,y = 350)

        var3 = StringVar()
        e3 = Entry(self,
                  textvariable = var3,
                   show = "*"
                  )
        e3.pack()
        e3.place(x = 305,y = 365)

        def show1():
                basedata = {
                          'host':'localhost',
                          'port':3306,
                          'user':'root',
                          'passwd':'HSHP0907',
                          'db':'hrm',
                          'charset':'utf8'
                          }
                # 打开数据库连接
                conn = pymysql.connect(**basedata)

                try:
                    User=str(e1.get())
                    Passwd=int(e2.get())

                    # 使用 cursor() 方法创建一个游标对象 cursor
                    cursor = conn.cursor()
                    print()

                    sql = "INSERT INTO userpasswd(user,passwd ) \
                      VALUES ('%s', '%s' )" % \
                    (  User, Passwd )

                    cursor.execute(sql)

                    # commit 修改
                    conn.commit()

                    # 关闭游标
                    cursor.close()

                    # 关闭链接
                    conn.close()
                    print("添加成功")

                except:
                    print("添加记录失败")

                    # 发生错误时回滚
                    conn.rollback()

        # 按钮设计
        btnkaishi = tk.Button(self,
                              text="立即注册",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command = show1
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 50,y = 470)

        btnkaishi = tk.Button(self,
                              text="返回登录",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command=lambda: self.show_frame(StartPage)
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 500,y = 470)

# 注册个人信息页面
class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "用户注册",
                        font = ("楷体",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 230,y = 10)
        # 姓名
        labelt1 = tk.Label(self,
                            text = "姓名:",
                            font = ("楷体",17)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 70)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 80)

        # 年龄
        labelt2 = tk.Label(self,
                            text = "年龄:",
                            font = ("楷体",17)
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 350,y = 70)
        var2 = StringVar()
        e2 = Entry(self,
                  textvariable = var2,
                  )
        e2.pack()
        e2.place(x = 420,y = 80)

        # 性别
        labelt3 = tk.Label(self,
                            text = "性别:",
                            font = ("楷体",17)
                            )
        labelt3.pack(padx=5, pady=10, side=tk.LEFT)
        labelt3.place(x = 100,y = 150)
        var3 = StringVar()
        e3 = Entry(self,
                  textvariable = var3,
                  )
        e3.pack()
        e3.place(x = 170,y = 160)

        # 生日
        labelt4 = tk.Label(self,
                            text = "生日:",
                            font = ("楷体",17)
                            )
        labelt4.pack(padx=5, pady=10, side=tk.LEFT)
        labelt4.place(x = 350,y = 150)
        var4 = StringVar()
        e4 = Entry(self,
                  textvariable = var4,
                  )
        e4.pack()
        e4.place(x = 420,y = 160)

        # 学历
        labelt5 = tk.Label(self,
                            text = "学历:",
                            font = ("楷体",17)
                            )
        labelt5.pack(padx=5, pady=10, side=tk.LEFT)
        labelt5.place(x = 100,y = 230)
        var5 = StringVar()
        e5 = Entry(self,
                  textvariable = var5,
                  )
        e5.pack()
        e5.place(x = 170,y = 240)

        # 专业
        labelt6 = tk.Label(self,
                            text = "专业:",
                            font = ("楷体",17)
                            )
        labelt6.pack(padx=5, pady=10, side=tk.LEFT)
        labelt6.place(x = 350,y = 230)
        var6 = StringVar()
        e6 = Entry(self,
                  textvariable = var6,
                  )
        e6.pack()
        e6.place(x = 420,y = 240)

        # 学校
        labelt7 = tk.Label(self,
                            text = "毕业学校:",
                            font = ("楷体",17)
                            )
        labelt7.pack(padx=5, pady=10, side=tk.LEFT)
        labelt7.place(x = 180,y = 285)
        var7 = StringVar()
        e7= Entry(self,
                  textvariable = var7,
                  )
        e7.pack()
        e7.place(x = 300,y = 295)

        # 手机号码
        labelt8 = tk.Label(self,
                            text = "手机号码:",
                            font = ("楷体",17)
                            )
        labelt8.pack(padx=5, pady=10, side=tk.LEFT)
        labelt8.place(x = 180,y = 335)
        var8 = StringVar()
        e8= Entry(self,
                  textvariable = var8,
                  )
        e8.pack()
        e8.place(x = 300,y = 345)

        # QQ邮箱
        labelt9 = tk.Label(self,
                            text = "QQ邮箱:",
                            font = ("楷体",17)
                            )
        labelt9.pack(padx=5, pady=10, side=tk.LEFT)
        labelt9.place(x = 180,y = 385)
        var9 = StringVar()
        e9= Entry(self,
                  textvariable = var9,
                  )
        e9.pack()
        e9.place(x = 300,y = 395)

         # 工作部门
        labelt10 = tk.Label(self,
                            text = "工作部门:",
                            font = ("楷体",17)
                            )
        labelt10.pack(padx=5, pady=10, side=tk.LEFT)
        labelt10.place(x = 180,y = 435)
        var10 = StringVar()
        e10= Entry(self,
                  textvariable = var10,
                  )
        e10.pack()
        e10.place(x = 300,y = 445)

        def show():
            basedata = {
                        'host':'localhost',
                        'port' : 3306,
                        'user':'root',
                        'passwd':'as123',
                        'db':'teacher',
                        'charset':'utf8'
                        }
            # 打开数据库连接
            conn = pymysql.connect(**basedata)
            try:
                Name=str(e1.get())
                Age=int(e2.get())
                Sex=str(e3.get())
                Bir=str(e4.get())
                Edu=str(e5.get())
                Pro=str(e6.get())
                School=str(e7.get())
                Tel=int(e8.get())
                Emile=str(e9.get())
                Dep=str(e10.get())
                # 使用 cursor() 方法创建一个游标对象 cursor
                cursor = conn.cursor()
                print(Name , Age , Sex , Bir ,Edu,Pro ,School,Tel,Emile,Dep)

                sql = "INSERT INTO userreg(name, \
                      age, sex , bir ,edu , pro ,school ,tel , emile, dep) \
                      VALUES ('%s','%d','%s','%s', '%s' ,'%s' ,'%s','%d' , '%s' ,'%s')" % \
                    (Name,Age, Sex , Bir ,Edu,Pro ,School,Tel,Emile,Dep)

                cursor.execute(sql)

                # commit 修改
                conn.commit()

                # 关闭游标
                cursor.close()

                # 关闭链接
                conn.close()
                print("添加成功")

            except:
                print("添加记录失败")

                # 发生错误时回滚
                conn.rollback()

        # 按钮设计
        btnkaishi = tk.Button(self,
                              text="立即注册",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command = show
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 50,y = 470)

        btnkaishi = tk.Button(self,
                              text="返回查询",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command=lambda: root.show_frame(PageThree)
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 500,y = 470)

# 个人信息查询
class PageThree(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "个人信息",
                        font = ("楷体",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 230,y = 10)
        # 姓名
        labelt1 = tk.Label(self,
                            text = "姓名:",
                            font = ("楷体",17)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 70)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 80)

        # 年龄
        labelt2 = tk.Label(self,
                            text = "年龄:",
                            font = ("楷体",17)
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 350,y = 70)
        var2 = StringVar()
        e2 = Entry(self,
                  textvariable = var2,
                  )
        e2.pack()
        e2.place(x = 420,y = 80)

        # 性别
        labelt3 = tk.Label(self,
                            text = "性别:",
                            font = ("楷体",17)
                            )
        labelt3.pack(padx=5, pady=10, side=tk.LEFT)
        labelt3.place(x = 100,y = 150)
        var3 = StringVar()
        e3 = Entry(self,
                  textvariable = var3,
                  )
        e3.pack()
        e3.place(x = 170,y = 160)

        # 生日
        labelt4 = tk.Label(self,
                            text = "生日:",
                            font = ("楷体",17)
                            )
        labelt4.pack(padx=5, pady=10, side=tk.LEFT)
        labelt4.place(x = 350,y = 150)
        var4 = StringVar()
        e4 = Entry(self,
                  textvariable = var4,
                  )
        e4.pack()
        e4.place(x = 420,y = 160)

        # 学历
        labelt5 = tk.Label(self,
                            text = "学历:",
                            font = ("楷体",17)
                            )
        labelt5.pack(padx=5, pady=10, side=tk.LEFT)
        labelt5.place(x = 100,y = 230)
        var5 = StringVar()
        e5 = Entry(self,
                  textvariable = var5,
                  )
        e5.pack()
        e5.place(x = 170,y = 240)

        # 专业
        labelt6 = tk.Label(self,
                            text = "专业:",
                            font = ("楷体",17)
                            )
        labelt6.pack(padx=5, pady=10, side=tk.LEFT)
        labelt6.place(x = 350,y = 230)
        var6 = StringVar()
        e6 = Entry(self,
                  textvariable = var6,
                  )
        e6.pack()
        e6.place(x = 420,y = 240)

        # 固定电话
        labelt7 = tk.Label(self,
                            text = "毕业学校:",
                            font = ("楷体",17)
                            )
        labelt7.pack(padx=5, pady=10, side=tk.LEFT)
        labelt7.place(x = 180,y = 290)
        var7 = StringVar()
        e7= Entry(self,
                  textvariable = var7,
                  )
        e7.pack()
        e7.place(x = 300,y = 300)

        # 手机号码
        labelt8 = tk.Label(self,
                            text = "手机号码:",
                            font = ("楷体",17)
                            )
        labelt8.pack(padx=5, pady=10, side=tk.LEFT)
        labelt8.place(x = 180,y = 350)
        var8 = StringVar()
        e8= Entry(self,
                  textvariable = var8,
                  )
        e8.pack()
        e8.place(x = 300,y = 360)

        # QQ邮箱
        labelt9 = tk.Label(self,
                            text = "QQ邮箱:",
                            font = ("楷体",17)
                            )
        labelt9.pack(padx=5, pady=10, side=tk.LEFT)
        labelt9.place(x = 180,y = 410)
        var9 = StringVar()
        e9= Entry(self,
                  textvariable = var9,
                  )
        e9.pack()
        e9.place(x = 300,y = 420)

        # 按钮设计
        btnkaishi = tk.Button(self,
                              text="立即查询",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 50,y = 470)

        btnkaishi = tk.Button(self,
                              text="查询其他",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 500,y = 470)

#部门人员查询
class PageFore(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "部门人员查询",
                        font = ("楷体",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 180,y = 10)

        labelt1 = tk.Label(self,
                            text = "请输入所要查询的部门:",
                            font = ("楷体",20)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 100)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 140)

        b1=tk.Button(self,text='查询',width = 15,height = 3,activeforeground = "red")
        b1.pack(padx = 5, pady = 10)
        b1.place(x=500,y=110)

        labelt2 = tk.Label(self,
                            text = "查询部门的结果:",
                            font = ("楷体",20),
                            fg = "red"
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 10,y = 200)

        scrolly = Scrollbar(self)
        scrolly.pack(side=RIGHT, fill=Y)
        l=tk.Listbox(self,width = 70,height = 17,exportselection = False,yscrollcommand=scrolly.set)
        l.pack()
        l.place(x=10,y = 260)

#专业配置
class PageFive(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "专业配置",
                        font = ("楷体",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 200,y = 10)

        labelt1 = tk.Label(self,
                            text = "请输入所要查询的专业:",
                            font = ("楷体",20)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 100)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 140)

        b1=tk.Button(self,text='查询',width = 15,height = 3,activeforeground = "red")
        b1.pack(padx = 5, pady = 10)
        b1.place(x=500,y=110)

        labelt2 = tk.Label(self,
                            text = "查询专业的结果:",
                            font = ("楷体",20),
                            fg = "red"
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 10,y = 200)

        scrolly = Scrollbar(self)
        scrolly.pack(side=RIGHT, fill=Y)
        l=tk.Listbox(self,width = 70,height = 17,exportselection = False,yscrollcommand=scrolly.set)
        l.pack()
        l.place(x=10,y = 260)

#学历查询
class PageSix(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "学历查询",
                        font = ("楷体",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 200,y = 10)

        labelt1 = tk.Label(self,
                            text = "请输入所要查询的学历:",
                            font = ("楷体",20)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 100)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 140)

        b1=tk.Button(self,text='查询',width = 15,height = 3,activeforeground = "red")
        b1.pack(padx = 5, pady = 10)
        b1.place(x=500,y=110)

        labelt2 = tk.Label(self,
                            text = "查询学历的结果:",
                            font = ("楷体",20),
                            fg = "red"
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 10,y = 200)

        scrolly = Scrollbar(self)
        scrolly.pack(side=RIGHT, fill=Y)
        l=tk.Listbox(self,width = 70,height = 17,exportselection = False,yscrollcommand=scrolly.set)
        l.pack()
        l.place(x=10,y = 260)

#生日查询
class PageSeven(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "生日查询",
                        font = ("楷体",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 200,y = 10)

        labelt1 = tk.Label(self,
                            text = "请输入所要查询的人员:",
                            font = ("楷体",20)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 100)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 140)

        b1=tk.Button(self,text='查询',width = 15,height = 3,activeforeground = "red")
        b1.pack(padx = 5, pady = 10)
        b1.place(x=500,y=110)

        labelt2 = tk.Label(self,
                            text = "查询结果:",
                            font = ("楷体",20),
                            fg = "red"
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 10,y = 200)

        scrolly = Scrollbar(self)
        scrolly.pack(side=RIGHT, fill=Y)
        l=tk.Listbox(self,width = 70,height = 17,exportselection = False,yscrollcommand=scrolly.set)
        l.pack()
        l.place(x=10,y = 260)


if __name__ == '__main__':
    # 实例化Application
    app = Application()

    # 主消息循环:
    app.mainloop()
