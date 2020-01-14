"""
Created on 2019-03-16
@author:Jupiter
"""
import PySimpleGUI as sg
from scipy.interpolate import lagrange

# 修改插值多项式格式
def change(ret):
    length,nret = ret.order,'y='
    if length > 1:
        nret += str(round(ret.c[0],4))+'x^'+str(length)
        for i in range(length-2):
            if ret.c[i+1]>0:
                nret += '+' + str(round(ret.c[i+1],4))+'x^'+str(length-i-1)
            else :
                nret += str(round(ret.c[i+1],4))+'x^'+str(length-i-1)
    if length >= 1:
        if ret.c[-2] >= 0:
            nret += '+'+str(round(ret.c[-2],4))+'x'
        else :
            nret += str(round(ret.c[-2],4))+'x'
    if ret.c[-1] >= 0:
        nret += '+'+str(round(ret.c[-1],4))
    else :
        nret += str(round(ret.c[-1],4))

    return nret

# 获取插值节点数量
form1 = sg.FlexForm('输入插值节点数量(n≥2)')  
layout = [
          #[sg.InputCombo(['男','女','隐私'],auto_size_text=True)],
          [sg.Text('number', size=(5,1)), sg.InputText('')],
          [sg.Submit(), sg.Cancel()]
         ]
button, values = form1.Layout(layout).Read()
print(button, values[0])
form1.Close()

# 获取插值节点坐标
form2= sg.FlexForm('输入节点坐标')  
layout = []
for i in range(int(values[0])):
    layout.append([sg.Text('(x,y)', size=(3,2)),sg.Input(),sg.Input()])
layout.append( [sg.Text('Author:Jupiter')])
layout.append( [sg.Submit(), sg.Cancel()])

button, values = form2.Layout(layout).Read()
form2.Close()

x,y = [],[]
for i in range(len(values)//2):
    x.append(float(values[i*2]))
    y.append(float(values[i*2+1]))

print(button,x,y)
#ret = lagrange(x,y)
ret = change(lagrange(x,y))

# 输出多项式插值结果
form3= sg.FlexForm('多项式插值结果')
layout = [[sg.Text('插值多项式',size=(10,1))]]

for i in range(len(x)):
    layout.append([sg.Text('(x,y)'),sg.Text(x[i]),sg.Text(y[i])])
layout.append([sg.Text('------------------------------------')])
layout.append([sg.Text(ret)])
layout.append([sg.OK(),sg.Cancel(),sg.Text('Author:Jupiter')])

button, values = form3.Layout(layout).Read()
