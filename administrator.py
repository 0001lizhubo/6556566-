# coding=gbk
# from register_or_login import *
from classInformation import *
from YanjiuInformation import *
from selfInfomation import  *
def administrator(ID):
    #print("�������ǹ���Ա�ˡ�")
    choose = input("��������Ҫ���еĲ���������0�˳���������1���������Ϣ���棬����2�����ѧ�����ѯ���棬����3���������Ϣ���棺")
    str(choose)
    while choose != "0":
        if choose == "1":
            print("��ϲ���������Ϣ���棡�����ѡ��\n 1��дĳ������Ϣ��2����ĳ������Ϣ��3�鿴ĳ������Ϣ��4ɾ��ĳ������Ϣ��5�鿴���еĽ�ְ����Ϣ,6�˵���һ��\n")
            n = input("�����룺")
            n = str(n)
            selfInfomation(n)
        elif choose == "2":
            print("��ϲ�����ѧ��Ϣ���棡�����ѡ��\n 1���ĳ���˽�ѧ��Ϣ��2�鿴ĳ���˽�ѧ��Ϣ��3ɾ����ѧ��Ϣ��4�˵���һ��,5�鿴���пγ̵���Ϣ\n")
            n = input("�����룺")
            n = str(n)
            classInformation(n)
        elif choose == "3":
            print("��ϲ���������Ϣ���棡�����ѡ��\n 1�鿴ĳ���˿�����Ϣ��2���ĳ���˿�����Ϣ��3ɾ��������Ϣ��4�˵���һ����5�鿴���п��е���Ϣ\n")
            n = input("�����룺")
            n = str(n)
            YanjiuInformation(n)
        else:
            print("�����������������0~3")
        choose = input("��������Ҫ���еĲ���������0�˳���������1���������Ϣ���棬����2�����ѧ�����ѯ���棬����3���������Ϣ���棺")
        str(choose)
    return 0