# coding=gbk
# from register_or_login import *
from classInformation2 import *
from YanjiuInfomation2 import *
from selfinformation_user import  *
def user_hanshu(ID):
    print("���������û��ˡ�\n")
    print("�û�ֻ��1.��Ӹ�����Ϣ��2.���ĸ�����Ϣ��3.��ѯ������Ϣ��4.�鿴���˽�ѧ��Ϣ��5.�鿴���˿�����Ϣ��6.��Ӹ����о���Ϣ\n")
    choose = input("��������Ҫ���еĲ���������0�˳���������1���������Ϣ���棬����2�����ѧ�����ѯ���棬����3���������Ϣ���棺")
    str(choose)
    while choose != "0":
        if choose == "1":
            print("��ϲ���������Ϣ���棡�����ѡ��\n1��д������Ϣ��2���¸��˵�������߲��ţ�3�鿴������Ϣ��4�˵���һ��\n")
            n = input("�����룺")
            n = str(n)
            selfInfomation2(n,ID)
        elif choose == "2":
            print("��ϲ�����ѧ��Ϣ���棡�����ѡ��\n1�鿴���˽�ѧ��Ϣ��2�鿴�Լ������ομ��ţ�3�˵���һ��\n")
            n = input("�����룺")
            n = str(n)
            classInformation2(n,ID)
        elif choose == "3":
            print("��ϲ�����ѧ��Ϣ���棡�����ѡ��\n1�鿴���˿�����Ϣ��2��Ӹ��˿�����Ϣ��3�˵���һ�� ��4�������ĵ�ƪ��\n")
            n = input("�����룺")
            n = str(n)
            YanjiuInformation2(n,ID)
        else:
            print("�����������������0~3")
        choose = input("��������Ҫ���еĲ���������0�˳���������1���������Ϣ���棬����2�����ѧ�����ѯ���棬����3���������Ϣ���棺")
        str(choose)
    return 0