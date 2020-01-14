# coding=gbk
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter
import pymysql

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.wm_title("���¹���ϵͳ")
        self.geometry("700x600")
        self.resizable(width = False,height = False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # ����һ���˵�������ڵ�����
        menubar=Menu(self)
        # �����˵���
        menubar.add_cascade(label="��¼",command=lambda: self.show_frame(StartPage))
        menubar.add_cascade(label="ע��",command=lambda: self.show_frame(PageOne))
        menubar.add_cascade(label="������Ϣ��д",command=lambda: self.show_frame(PageTwo))
        menubar.add_cascade(label="������Ϣ��ѯ",command=lambda: self.show_frame(PageThree))
        menubar.add_cascade(label="������Ա��ѯ",command=lambda: self.show_frame(PageFore))
        menubar.add_cascade(label="רҵ����",command=lambda: self.show_frame(PageFive))
        menubar.add_cascade(label="ѧ������",command=lambda: self.show_frame(PageSix))
        menubar.add_cascade(label="���ղ�ѯ",command=lambda: self.show_frame(PageSeven))
        self['menu']=menubar

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree,PageFore,PageFive,PageSix,PageSeven):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # �ĸ�ҳ���λ�ö��� grid(row=0, column=0), λ���ص���ֻ��������Ŀɼ�����
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # �л���������ǰ tk.Frame z��˳��

#��¼
class StartPage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)

        labeltxt = tk.Label(self,
                        text = "�û���¼",
                        font = ("����",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 240,y = 50)

        labelt1 = tk.Label(self,
                        text = "�˻�:",
                        font = ("����",25)
                        )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 210,y = 200)

        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 300,y = 215)

        # ��¼����
        labelt2 = tk.Label(self,
                            text = "����:",
                            font = ("����",25)
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

        # ��ť���
        btnkaishi = tk.Button(self,
                              text="ֱ�ӵ�¼",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 50,y = 470)

        btnkaishi = tk.Button(self,
                              text="����ע��",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command=lambda: root.show_frame(PageOne)
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 500,y = 470)

#ע���˺���Ϣ
class PageOne(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)

        labeltxt = tk.Label(self,
                            text = "�˺�ע��",
                            font = ("����",40),
                            )
        labeltxt.pack()
        labeltxt.place(x = 240,y = 50)

        # ��¼�˺�
        labelt1 = tk.Label(self,
                            text = "�˻�:",
                            font = ("����",25)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 200,y = 140)

        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 305,y = 150)

        # ��¼����
        labelt2 = tk.Label(self,
                            text = "����:",
                            font = ("����",25)
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

        # ȷ������
        labelt3 = tk.Label(self,
                            text = "ȷ������:",
                            font = ("����",25)
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
                # �����ݿ�����
                conn = pymysql.connect(**basedata)

                try:
                    User=str(e1.get())
                    Passwd=int(e2.get())

                    # ʹ�� cursor() ��������һ���α���� cursor
                    cursor = conn.cursor()
                    print()

                    sql = "INSERT INTO userpasswd(user,passwd ) \
                      VALUES ('%s', '%s' )" % \
                    (  User, Passwd )

                    cursor.execute(sql)

                    # commit �޸�
                    conn.commit()

                    # �ر��α�
                    cursor.close()

                    # �ر�����
                    conn.close()
                    print("��ӳɹ�")

                except:
                    print("��Ӽ�¼ʧ��")

                    # ��������ʱ�ع�
                    conn.rollback()

        # ��ť���
        btnkaishi = tk.Button(self,
                              text="����ע��",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command = show1
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 50,y = 470)

        btnkaishi = tk.Button(self,
                              text="���ص�¼",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command=lambda: self.show_frame(StartPage)
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 500,y = 470)

# ע�������Ϣҳ��
class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "�û�ע��",
                        font = ("����",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 230,y = 10)
        # ����
        labelt1 = tk.Label(self,
                            text = "����:",
                            font = ("����",17)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 70)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 80)

        # ����
        labelt2 = tk.Label(self,
                            text = "����:",
                            font = ("����",17)
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 350,y = 70)
        var2 = StringVar()
        e2 = Entry(self,
                  textvariable = var2,
                  )
        e2.pack()
        e2.place(x = 420,y = 80)

        # �Ա�
        labelt3 = tk.Label(self,
                            text = "�Ա�:",
                            font = ("����",17)
                            )
        labelt3.pack(padx=5, pady=10, side=tk.LEFT)
        labelt3.place(x = 100,y = 150)
        var3 = StringVar()
        e3 = Entry(self,
                  textvariable = var3,
                  )
        e3.pack()
        e3.place(x = 170,y = 160)

        # ����
        labelt4 = tk.Label(self,
                            text = "����:",
                            font = ("����",17)
                            )
        labelt4.pack(padx=5, pady=10, side=tk.LEFT)
        labelt4.place(x = 350,y = 150)
        var4 = StringVar()
        e4 = Entry(self,
                  textvariable = var4,
                  )
        e4.pack()
        e4.place(x = 420,y = 160)

        # ѧ��
        labelt5 = tk.Label(self,
                            text = "ѧ��:",
                            font = ("����",17)
                            )
        labelt5.pack(padx=5, pady=10, side=tk.LEFT)
        labelt5.place(x = 100,y = 230)
        var5 = StringVar()
        e5 = Entry(self,
                  textvariable = var5,
                  )
        e5.pack()
        e5.place(x = 170,y = 240)

        # רҵ
        labelt6 = tk.Label(self,
                            text = "רҵ:",
                            font = ("����",17)
                            )
        labelt6.pack(padx=5, pady=10, side=tk.LEFT)
        labelt6.place(x = 350,y = 230)
        var6 = StringVar()
        e6 = Entry(self,
                  textvariable = var6,
                  )
        e6.pack()
        e6.place(x = 420,y = 240)

        # ѧУ
        labelt7 = tk.Label(self,
                            text = "��ҵѧУ:",
                            font = ("����",17)
                            )
        labelt7.pack(padx=5, pady=10, side=tk.LEFT)
        labelt7.place(x = 180,y = 285)
        var7 = StringVar()
        e7= Entry(self,
                  textvariable = var7,
                  )
        e7.pack()
        e7.place(x = 300,y = 295)

        # �ֻ�����
        labelt8 = tk.Label(self,
                            text = "�ֻ�����:",
                            font = ("����",17)
                            )
        labelt8.pack(padx=5, pady=10, side=tk.LEFT)
        labelt8.place(x = 180,y = 335)
        var8 = StringVar()
        e8= Entry(self,
                  textvariable = var8,
                  )
        e8.pack()
        e8.place(x = 300,y = 345)

        # QQ����
        labelt9 = tk.Label(self,
                            text = "QQ����:",
                            font = ("����",17)
                            )
        labelt9.pack(padx=5, pady=10, side=tk.LEFT)
        labelt9.place(x = 180,y = 385)
        var9 = StringVar()
        e9= Entry(self,
                  textvariable = var9,
                  )
        e9.pack()
        e9.place(x = 300,y = 395)

         # ��������
        labelt10 = tk.Label(self,
                            text = "��������:",
                            font = ("����",17)
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
            # �����ݿ�����
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
                # ʹ�� cursor() ��������һ���α���� cursor
                cursor = conn.cursor()
                print(Name , Age , Sex , Bir ,Edu,Pro ,School,Tel,Emile,Dep)

                sql = "INSERT INTO userreg(name, \
                      age, sex , bir ,edu , pro ,school ,tel , emile, dep) \
                      VALUES ('%s','%d','%s','%s', '%s' ,'%s' ,'%s','%d' , '%s' ,'%s')" % \
                    (Name,Age, Sex , Bir ,Edu,Pro ,School,Tel,Emile,Dep)

                cursor.execute(sql)

                # commit �޸�
                conn.commit()

                # �ر��α�
                cursor.close()

                # �ر�����
                conn.close()
                print("��ӳɹ�")

            except:
                print("��Ӽ�¼ʧ��")

                # ��������ʱ�ع�
                conn.rollback()

        # ��ť���
        btnkaishi = tk.Button(self,
                              text="����ע��",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command = show
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 50,y = 470)

        btnkaishi = tk.Button(self,
                              text="���ز�ѯ",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              command=lambda: root.show_frame(PageThree)
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 500,y = 470)

# ������Ϣ��ѯ
class PageThree(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "������Ϣ",
                        font = ("����",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 230,y = 10)
        # ����
        labelt1 = tk.Label(self,
                            text = "����:",
                            font = ("����",17)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 70)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 80)

        # ����
        labelt2 = tk.Label(self,
                            text = "����:",
                            font = ("����",17)
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 350,y = 70)
        var2 = StringVar()
        e2 = Entry(self,
                  textvariable = var2,
                  )
        e2.pack()
        e2.place(x = 420,y = 80)

        # �Ա�
        labelt3 = tk.Label(self,
                            text = "�Ա�:",
                            font = ("����",17)
                            )
        labelt3.pack(padx=5, pady=10, side=tk.LEFT)
        labelt3.place(x = 100,y = 150)
        var3 = StringVar()
        e3 = Entry(self,
                  textvariable = var3,
                  )
        e3.pack()
        e3.place(x = 170,y = 160)

        # ����
        labelt4 = tk.Label(self,
                            text = "����:",
                            font = ("����",17)
                            )
        labelt4.pack(padx=5, pady=10, side=tk.LEFT)
        labelt4.place(x = 350,y = 150)
        var4 = StringVar()
        e4 = Entry(self,
                  textvariable = var4,
                  )
        e4.pack()
        e4.place(x = 420,y = 160)

        # ѧ��
        labelt5 = tk.Label(self,
                            text = "ѧ��:",
                            font = ("����",17)
                            )
        labelt5.pack(padx=5, pady=10, side=tk.LEFT)
        labelt5.place(x = 100,y = 230)
        var5 = StringVar()
        e5 = Entry(self,
                  textvariable = var5,
                  )
        e5.pack()
        e5.place(x = 170,y = 240)

        # רҵ
        labelt6 = tk.Label(self,
                            text = "רҵ:",
                            font = ("����",17)
                            )
        labelt6.pack(padx=5, pady=10, side=tk.LEFT)
        labelt6.place(x = 350,y = 230)
        var6 = StringVar()
        e6 = Entry(self,
                  textvariable = var6,
                  )
        e6.pack()
        e6.place(x = 420,y = 240)

        # �̶��绰
        labelt7 = tk.Label(self,
                            text = "��ҵѧУ:",
                            font = ("����",17)
                            )
        labelt7.pack(padx=5, pady=10, side=tk.LEFT)
        labelt7.place(x = 180,y = 290)
        var7 = StringVar()
        e7= Entry(self,
                  textvariable = var7,
                  )
        e7.pack()
        e7.place(x = 300,y = 300)

        # �ֻ�����
        labelt8 = tk.Label(self,
                            text = "�ֻ�����:",
                            font = ("����",17)
                            )
        labelt8.pack(padx=5, pady=10, side=tk.LEFT)
        labelt8.place(x = 180,y = 350)
        var8 = StringVar()
        e8= Entry(self,
                  textvariable = var8,
                  )
        e8.pack()
        e8.place(x = 300,y = 360)

        # QQ����
        labelt9 = tk.Label(self,
                            text = "QQ����:",
                            font = ("����",17)
                            )
        labelt9.pack(padx=5, pady=10, side=tk.LEFT)
        labelt9.place(x = 180,y = 410)
        var9 = StringVar()
        e9= Entry(self,
                  textvariable = var9,
                  )
        e9.pack()
        e9.place(x = 300,y = 420)

        # ��ť���
        btnkaishi = tk.Button(self,
                              text="������ѯ",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 50,y = 470)

        btnkaishi = tk.Button(self,
                              text="��ѯ����",
                              width = 20,
                              height = 4,
                              activeforeground = "red",
                              )
        btnkaishi.pack(padx = 5, pady = 10, side = tk.LEFT)
        btnkaishi.place(x = 500,y = 470)

#������Ա��ѯ
class PageFore(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "������Ա��ѯ",
                        font = ("����",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 180,y = 10)

        labelt1 = tk.Label(self,
                            text = "��������Ҫ��ѯ�Ĳ���:",
                            font = ("����",20)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 100)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 140)

        b1=tk.Button(self,text='��ѯ',width = 15,height = 3,activeforeground = "red")
        b1.pack(padx = 5, pady = 10)
        b1.place(x=500,y=110)

        labelt2 = tk.Label(self,
                            text = "��ѯ���ŵĽ��:",
                            font = ("����",20),
                            fg = "red"
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 10,y = 200)

        scrolly = Scrollbar(self)
        scrolly.pack(side=RIGHT, fill=Y)
        l=tk.Listbox(self,width = 70,height = 17,exportselection = False,yscrollcommand=scrolly.set)
        l.pack()
        l.place(x=10,y = 260)

#רҵ����
class PageFive(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "רҵ����",
                        font = ("����",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 200,y = 10)

        labelt1 = tk.Label(self,
                            text = "��������Ҫ��ѯ��רҵ:",
                            font = ("����",20)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 100)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 140)

        b1=tk.Button(self,text='��ѯ',width = 15,height = 3,activeforeground = "red")
        b1.pack(padx = 5, pady = 10)
        b1.place(x=500,y=110)

        labelt2 = tk.Label(self,
                            text = "��ѯרҵ�Ľ��:",
                            font = ("����",20),
                            fg = "red"
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 10,y = 200)

        scrolly = Scrollbar(self)
        scrolly.pack(side=RIGHT, fill=Y)
        l=tk.Listbox(self,width = 70,height = 17,exportselection = False,yscrollcommand=scrolly.set)
        l.pack()
        l.place(x=10,y = 260)

#ѧ����ѯ
class PageSix(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "ѧ����ѯ",
                        font = ("����",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 200,y = 10)

        labelt1 = tk.Label(self,
                            text = "��������Ҫ��ѯ��ѧ��:",
                            font = ("����",20)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 100)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 140)

        b1=tk.Button(self,text='��ѯ',width = 15,height = 3,activeforeground = "red")
        b1.pack(padx = 5, pady = 10)
        b1.place(x=500,y=110)

        labelt2 = tk.Label(self,
                            text = "��ѯѧ���Ľ��:",
                            font = ("����",20),
                            fg = "red"
                            )
        labelt2.pack(padx=5, pady=10, side=tk.LEFT)
        labelt2.place(x = 10,y = 200)

        scrolly = Scrollbar(self)
        scrolly.pack(side=RIGHT, fill=Y)
        l=tk.Listbox(self,width = 70,height = 17,exportselection = False,yscrollcommand=scrolly.set)
        l.pack()
        l.place(x=10,y = 260)

#���ղ�ѯ
class PageSeven(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        labeltxt = tk.Label(self,
                        text = "���ղ�ѯ",
                        font = ("����",40),
                        )
        labeltxt.pack()
        labeltxt.place(x = 200,y = 10)

        labelt1 = tk.Label(self,
                            text = "��������Ҫ��ѯ����Ա:",
                            font = ("����",20)
                            )
        labelt1.pack(padx=5, pady=10, side=tk.LEFT)
        labelt1.place(x = 100,y = 100)
        var1 = StringVar()
        e1 = Entry(self,
                  textvariable = var1,
                  )
        e1.pack()
        e1.place(x = 170,y = 140)

        b1=tk.Button(self,text='��ѯ',width = 15,height = 3,activeforeground = "red")
        b1.pack(padx = 5, pady = 10)
        b1.place(x=500,y=110)

        labelt2 = tk.Label(self,
                            text = "��ѯ���:",
                            font = ("����",20),
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
    # ʵ����Application
    app = Application()

    # ����Ϣѭ��:
    app.mainloop()
