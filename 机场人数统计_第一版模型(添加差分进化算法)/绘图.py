import numpy as np
import matplotlib.pyplot as plt
import processing as dap
import gradient_descent as gd
import DE_Algorithm as DE

x = range(1,gd.m+1)
y1=gd.date
y2=gd.predict
y3= gd.Y_pre_num

line1, =plt.plot(x, y1, marker='o', mec='r', mfc='w')
line2, =plt.plot(x, y2, marker='*', ms=10)
line3, =plt.plot(x,y3, marker='s',ms=10)
plt.legend([line1, line2,line3], ["实际总人数变化曲线", "考虑货机预测人数变化曲线","GD调参之后的预计人数变化曲线"],loc='best',frameon=False,prop="SimSun")
plt.xlabel('时间/周次',fontproperties="SimSun"); plt.ylabel('人数/个',fontproperties="SimSun");
plt.title(dap.weekday+"人数变化曲线图", fontproperties="SimSun" ,fontsize='large')
plt.show()

y1=DE.Y_data
y2=DE.X_data
y3= DE.optimal_data
x = range(1,len(y1)+1)

line1, =plt.plot(x, y1, marker='o', mec='r', mfc='w')
line2, =plt.plot(x, y2, marker='*', ms=10)
line3, =plt.plot(x,y3, marker='s',ms=10)
plt.legend([line1, line2,line3], ["实际总人数变化曲线", "考虑货机预测人数变化曲线","DE调参之后的预计人数变化曲线"],loc='best',frameon=False,prop="SimSun")
plt.xlabel('时间/周次',fontproperties="SimSun"); plt.ylabel('人数/个',fontproperties="SimSun");
plt.title(dap.weekday+"人数变化曲线图", fontproperties="SimSun" ,fontsize='large')
plt.show()
