# coding=gbk
import pymysql
import tkinter as tk
import tkinter.messagebox
import pickle
from sha import *
# �����ݿ�����
conn = pymysql.connect('localhost', 'root', 'as123', 'teacher')
cursor = conn.cursor()
# ����
window = tk.Tk()
window.title('��ӭ�������¹������ݿ�ϵͳ')
window.geometry('480x300')
# ��������ͼƬ
canvas = tk.Canvas(window, height=300, width=500)
imagefile = tk.PhotoImage(file='1015.png')
image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
canvas.pack(side='top')
# ��ǩ �û�������
tk.Label(window, text='�û���:').place(x=100, y=150)
tk.Label(window, text='����:').place(x=100, y=190)
# �û��������
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
# ���������
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


# ��¼����
def usr_log_in():
    # ������ȡ�û�������
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # �ӱ����ֵ��ȡ�û���Ϣ�����û�����½��������ݿ�
    sql="SELECT ID,password FROM user WHERE ID='%s'" %(usr_name)
    cursor.execute(sql)
    results = cursor.fetchall()
    # �ж��û����������Ƿ�ƥ��
    # print(results)
    # print(usr_name)
    # if True:
    a=results[0]
    if usr_name ==a[0] and usr_pwd==a[1]:
        tk.messagebox.showinfo(title='welcome',
                               message='��ӭ����' + usr_name)
    else:
        tk.messagebox.showerror(message='�������')
# �û������벻��Ϊ��
    if usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='�û���������Ϊ��')
# �������ݿ��е����Ƿ�ע��Ŀ�
    else:
        is_signup = tk.messagebox.askyesno('��ӭ', '����û��ע�ᣬ�Ƿ�����ע��')
        if is_signup:
            usr_sign_up()

# ע�ắ��

def usr_sign_up():
    # ȷ��ע��ʱ����Ӧ����
    def signtowcg():
        # ��ȡ������ڵ�����
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # ���ؼ��������û���Ϣ,���û���������û���ϢΪ��
        sql = "SELECT ID,password FROM user WHERE ID='%s'" % (nn)
        cursor.execute(sql)
        results = cursor.fetchall()
        # ����û������ڡ�����Ϊ�ա�����ǰ��һ��
        print(results)
        if not results:#resultΪ�գ��û������ڣ���������ע��
            ID = nn
            password = np
            if np == '' or nn == '':
                tk.messagebox.showerror('����', '�û���������Ϊ��')
                window_sign_up.destroy()
            elif np != npf:
                tk.messagebox.showerror('����', '����ǰ��һ��')
                window_sign_up.destroy()
            sql = "INSERT INTO user VALUES('%s',%s,'%s')" % (ID, password, 1)
            cursor.execute(sql)
            tk.messagebox.showinfo('��ӭ', 'ע��ɹ�')
            # ע��ɹ��ر�ע���
            window_sign_up.destroy()
        elif nn in results[0]:
            tk.messagebox.showerror('����', '�û����Ѵ���')
        # ע����Ϣû���������û�������д�����ݿ�

    # �½�ע�����
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('ע��')
    # �û�����������ǩ�������
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='�û�����').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # �����������ǩ�������
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='���������룺').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # �ظ������������ǩ�������
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='���ٴ��������룺').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # ȷ��ע�ᰴť��λ��
    bt_confirm_sign_up = tk.Button(window_sign_up, text='ȷ��ע��',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)


# �˳��ĺ���
def usr_sign_quit():
    window.destroy()


# ��¼ ע�ᰴť
bt_login = tk.Button(window, text='��¼', command=usr_log_in)
bt_login.place(x=140, y=230)
bt_logup = tk.Button(window, text='ע��', command=usr_sign_up)
bt_logup.place(x=210, y=230)
bt_logquit = tk.Button(window, text='�˳�', command=usr_sign_quit)
bt_logquit.place(x=280, y=230)
# ��ѭ��
window.mainloop()
