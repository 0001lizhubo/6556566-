# 图书管理系统UI界面
import wx
import datetime
class wxGUI(wx.App):
    # 登陆界面
    
    def Login(self):
        self.frame_Login = wx.Frame(None, title="Login", size=(500, 300))
        self.panel_Login = wx.Panel(self.frame_Login, -1)
        self.label1      = wx.StaticText(self.panel_Login, -1, \
            '欢迎来到图书管理系统', pos=(100,60),style=wx.ALIGN_CENTER)
        font=wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        self.label1.SetFont(font)
        # Combobox1--选择身份
        self.label2=wx.StaticText(self.panel_Login,-1,'Identify',pos=(0,100),style=wx.ALIGN_LEFT)
        self.identify={'管理员':["管理员"],'学生':['112','113']}
        self.combobox1=wx.ComboBox(self.panel_Login,value="Click here",\
            choices=list(self.identify.keys()),pos=(100,100),size=(100,30))
        self.Bind(wx.EVT_COMBOBOX,self.Oncombo1,self.combobox1)

        #用户名
        self.label3=wx.StaticText(self.panel_Login,-1,'Student Number',\
            pos=(0,120),style=wx.ALIGN_LEFT)
        self.combobox2=wx.ComboBox(self.panel_Login,value="Click here",\
            choices=[],pos=(100,120),size=(100,30))
        self.Bind(wx.EVT_COMBOBOX,self.Oncombo2,self.combobox2)

        #密码
        self.label4=wx.StaticText(self.panel_Login,-1,'Password',\
            pos=(0,140),style=wx.ALIGN_LEFT)
        self.textpasswd = wx.TextCtrl(self.panel_Login, -1, \
            pos=(100, 145), size=(100, 20), style=wx.TE_PASSWORD)        

        self.button_paswd = wx.Button(self.panel_Login, -1, 'OK', pos=(160, 200))
        self.Bind(wx.EVT_BUTTON, self.OnButton_paswd, self.button_paswd)
        self.button_paswd.SetDefault()
        self.frame_Login.Show()

    def Oncombo1(self,event):
        shenfen=self.combobox1.GetValue() #返回切换按钮的状态（开/关
        self.combobox2.Set(self.identify[shenfen])

    def Oncombo2(self,event):
        wx.MessageBox(self.combobox2.GetValue())   

    #校验用户名与密码
    def OnButton_paswd(self, event):
        userName = self.combobox2.GetValue()
        userPassword = self.textpasswd.GetValue()
        if userName == "管理员" and userPassword == "123456":
            wx.MessageBox("密码正确")
            self.Management_Menu()
        elif (userName == "112" and userPassword=="123") \
            or (userName=="113"and userPassword=="345"):
            wx.MessageBox("密码正确")
            self.Student_Menu()            
        else:
            wx.MessageBox("密码或用户名错误")


#管理员界面

    def Management_Menu(self):
        self.frame_Login.Destroy()
        self.frame_Manage = wx.Frame(None, -1, title="书籍管理", size=(500, 300))
        self.panel_Manage  = wx.Panel(self.frame_Manage, -1)
        self.label5        = wx.StaticText(
        self.panel_Manage, -1, '欢迎来到图书管理系统', pos=(100, 60), style=wx.ALIGN_CENTER)
        self.font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        self.label5.SetFont(self.font)

        #创建管理员菜单
        self.menuBar=wx.MenuBar() #创建菜单栏
        self.menu=wx.Menu() #创建菜单
        self.menuLook=self.menu.Append(101,'Look Books') #创建菜单项
        self.menudetail=self.menu.Append(102,'Books detail')
        self.menuAppend=self.menu.Append(103,'Add Books')
        self.menuBar.Append(self.menu,"&Edit")#将菜单添加至菜单栏

        self.menu=wx.Menu()
        self.menuSwitch=self.menu.Append(201,'Switch Login')
        self.menuout=self.menu.Append(202,"Security Out")
        self.menuBar.Append(self.menu,'&system')

        self.frame_Manage.SetMenuBar(self.menuBar)
        #为菜单绑定事件处理函数
        self.Bind(wx.EVT_MENU,self.OnLook,self.menuLook)
        self.Bind(wx.EVT_MENU,self.OnDetail,self.menudetail)
        self.Bind(wx.EVT_MENU,self.OnAdd,self.menuAppend)
        self.Bind(wx.EVT_MENU,self.OnSwitch,self.menuSwitch)
        self.Bind(wx.EVT_MENU,self.OnOut,self.menuout)
        self.frame_Manage.Show()

    #管理员查看图书
    def OnLook(self,event):
        file="Python程序设计  董富国  清华大学出版社 5  1F \n \
        数据结构  严蔚敏  清华大学出版社  5  1F \n 西游记  吴承恩  人民出版社   4  2F \n  \
        爱丽丝梦游仙境  Lewis Carroll  人民出版社  5  3F"
        wx.MessageBox(file)

    #管理员查看图书详情,新窗口
    def OnDetail(self,event):
        
        self.frame_Detail = wx.Frame(None, -1, title="书籍详细信息", size=(300, 300))
        self.panel_Detail  = wx.Panel(self.frame_Detail, -1)        
        self.lable6=wx.StaticText(self.panel_Detail,-1,'bookName',pos=(0,100),style=wx.ALIGN_LEFT)
        self.Book_name={"西游记":["数量：4","已借出：1"],\
            "数据结构":["数量：5","已借出：1"],"python程序设计":["数量：5","已借出：0"],\
            "爱丽丝梦游仙境":["数量：5","已借出：0"]}
        self.combobox_bookname=wx.ComboBox(self.panel_Detail,value="点击选择书籍",\
            choices=list(self.Book_name.keys()),pos=(100,100),size=(100,30))
        self.Bind(wx.EVT_COMBOBOX,self.Oncombo_bookname,self.combobox_bookname)
        self.frame_Detail.Show()

    def Oncombo_bookname(self,event):
        
        shuming=self.combobox_bookname.GetValue()
        detail=str(self.Book_name[shuming])
        wx.MessageBox(detail)

    #管理员添加图书
    def OnAdd(self,event):
        self.frame_Add=wx.Frame(None,-1,title='添加图书',size=(300,300))
        self.panel_Add=wx.Panel(self.frame_Add,-1)
        self.lable7=wx.StaticText(self.panel_Add,-1,'图书名称',pos=(20,60),style=wx.ALIGN_LEFT)
        self.textName=wx.TextCtrl(self.panel_Add,-1,pos=(100,60),size=(100,20),style=wx.TE_LEFT)
        self.label8=wx.StaticText(self.panel_Add,-1,'作者',pos=(20,80),style=wx.ALIGN_LEFT)
        self.textAuthor=wx.TextCtrl(self.panel_Add,-1,pos=(100,80),size=(100,20),style=wx.TE_LEFT)
        self.label9=wx.StaticText(self.panel_Add,-1,'出版社',pos=(20,100),style=wx.ALIGN_LEFT)
        self.textPublish=wx.TextCtrl(self.panel_Add,-1,pos=(100,100),size=(100,20),style=wx.TE_LEFT)
        self.label10=wx.StaticText(self.panel_Add,-1,'数量',pos=(20,120),style=wx.ALIGN_LEFT)
        self.textNumber=wx.TextCtrl(self.panel_Add,-1,pos=(100,120),size=(100,20),style=wx.TE_LEFT)
        self.label11=wx.StaticText(self.panel_Add,-1,'楼层',pos=(20,140),style=wx.ALIGN_LEFT)
        self.textFloor=wx.TextCtrl(self.panel_Add,-1,pos=(100,140),size=(100,20),style=wx.TE_LEFT)
        self.button_add=wx.Button(self.panel_Add,-1,'OK',pos=(180,200))
        self.Bind(wx.EVT_BUTTON,self.OnButton_Add,self.button_add)
        self.frame_Add.Show()

    def OnButton_Add(self,event):
        bookname=self.textName.GetValue()
        bookauthor=self.textAuthor.GetValue()
        bookpublish=self.textPublish.GetValue()
        booknumber=self.textNumber.GetValue()
        bookfloor=self.textFloor.GetValue()
        message="添加成功！\n" + "书名："+bookname+"\n"+"作者："+bookauthor+"\n"+"出版社："\
            +bookpublish+"\n"+"数量；"+booknumber+"\n"+"楼层："+bookfloor+"F"
        wx.MessageBox(message)

    #切换登陆
    def OnSwitch(self,event):
        self.frame_Manage.Destroy()
        self.Login()

    def OnOut(self,event):
        wx.MessageBox("谢谢您的使用！")
        self.frame_Manage.Destroy()


#x学生界面

    def Student_Menu(self):
        self.frame_Login.Destroy()
        self.frame_Stu=wx.Frame(None,-1,title="学生系统", size=(500, 300))
        self.panel_Stu=wx.Panel(self.frame_Stu, -1)
        #字体设置
        self.label12        = wx.StaticText(
        self.panel_Stu, -1, '欢迎来到图书管理系统', pos=(100, 60), style=wx.ALIGN_CENTER)
        self.font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        self.label12.SetFont(self.font) 

        #创建学生菜单
        self.menuBar1=wx.MenuBar() #创建菜单栏
        self.menu=wx.Menu() #创建菜单
        self.menuLook=self.menu.Append(101,'Look Books') #创建菜单项
        self.menudetail=self.menu.Append(102,'Books detail')
        self.menuLend=self.menu.Append(103,'Lend Books')
        self.menuBack=self.menu.Append(104,'Back Books')
        self.menuBar1.Append(self.menu,"&operate")#将菜单添加至菜单栏

        self.menu=wx.Menu()
        self.menuSwitch=self.menu.Append(201,'Switch Login')
        self.menuout=self.menu.Append(202,"Security Out")
        self.menuBar1.Append(self.menu,'&system')

        self.frame_Stu.SetMenuBar(self.menuBar1) 

        #为菜单绑定事件处理函数
        self.Bind(wx.EVT_MENU,self.OnLook,self.menuLook)
        self.Bind(wx.EVT_MENU,self.OnDetail,self.menudetail)
        self.Bind(wx.EVT_MENU,self.OnLend,self.menuLend)
        self.Bind(wx.EVT_MENU,self.OnBack,self.menuBack)
        self.Bind(wx.EVT_MENU,self.OnSwitch_stu,self.menuSwitch)
        self.Bind(wx.EVT_MENU,self.OnOut_stu,self.menuout)
        self.frame_Stu.Show()

    #借书部分
    def OnLend(self,event):
        self.frame_Lend=wx.Frame(None,-1,title="Lend Books", size=(500, 300))
        self.panel_Lend=wx.Panel(self.frame_Lend,-1)
        self.a={"西游记":["1","2","3"],"Python程序设计":["1","2","3","4","5"], \
            "爱丽丝梦游仙境":["1","2","3","4","5"],"数据结构":["1","2","3","4"]}
        self.label13=wx.StaticText(self.panel_Lend,-1,'BookName',pos=(20,80),style=wx.ALIGN_LEFT)
        self.combobox3=wx.ComboBox(self.panel_Lend,value="请选择书籍",\
            choices=list(self.a.keys()),pos=(100,80),size=(100,30))
        self.label14=wx.StaticText(self.panel_Lend,-1,'Number',pos=(20,100),style=wx.ALIGN_LEFT)
        self.combobox4=wx.ComboBox(self.panel_Lend,value="请选择数量",\
            choices=[],pos=(100,100),size=(100,30))
        self.button_Lend=wx.Button(self.panel_Lend,-1,'OK',pos=(180,150))
        self.Bind(wx.EVT_COMBOBOX,self.Oncombo3,self.combobox3)
        self.frame_Lend.Show()


    def Oncombo3(self,event):
        self.mingzi=self.combobox3.GetValue() #返回切换按钮的状态（开/关
        self.combobox4.Set(self.a[self.mingzi])
        self.Bind(wx.EVT_BUTTON,self.Onbutton_Lend,self.button_Lend)

    def Onbutton_Lend(self,event):
        self.ltime = datetime.datetime.now()  # 借出时间
        self.ltimes = self.ltime.strftime('%Y-%m-%d %H:%M:%S')
        message2="借出成功！ \n"+"书名："+self.mingzi+"\n"+"借出时间："+self.ltimes
        wx.MessageBox(message2)
        self.frame_Lend.Destroy()

    #还书部分
    def OnBack(self,event):
        self.b={"西游记":["1","2","3"],"Python程序设计":["1","2","3","4","5"],\
            "爱丽丝梦游仙境":["1","2","3","4","5"],"数据结构":["1","2","3","4"]}
        self.frame_Back=wx.Frame(None,-1,title="Back Books", size=(500, 300))
        self.panel_Back=wx.Panel(self.frame_Back,-1)
        self.label15=wx.StaticText(self.panel_Back,-1,'BookName',pos=(20,80),style=wx.ALIGN_LEFT)
        self.combobox5=wx.ComboBox(self.panel_Back,value="请选择书籍",\
            choices=list(self.b.keys()),pos=(100,80),size=(100,30))
        self.label16=wx.StaticText(self.panel_Back,-1,'Number',pos=(20,120),style=wx.ALIGN_LEFT)
        self.textBack_Number=wx.TextCtrl(self.panel_Back,-1,pos=(100,120),size=(100,20),style=wx.TE_LEFT)  
        self.button_Back=wx.Button(self.panel_Back,-1,'OK',pos=(180,200))
        self.Bind(wx.EVT_BUTTON,self.OnButton_Back,self.button_Back)
        self.frame_Back.Show()   

    def OnButton_Back(self,event):
        sm=self.combobox5.GetValue()
        num=self.textBack_Number.GetValue()
        self.ltime2 = datetime.datetime.now()  # 借出时间
        self.ltimes2 = self.ltime2.strftime('%Y-%m-%d %H:%M:%S')
        message3="归还成功！ \n"+"书名："+sm+"\n"+"归还时间："+self.ltimes2
        wx.MessageBox(message3)
        self.frame_Back.Destroy()

        #切换登陆
    def OnSwitch_stu(self,event):
        self.frame_Stu.Destroy()
        self.Login()

    def OnOut_stu(self,event):
        wx.MessageBox("谢谢您的使用！")
        self.frame_Stu.Destroy()

app = wxGUI()
app.Login()
app.MainLoop()


     

