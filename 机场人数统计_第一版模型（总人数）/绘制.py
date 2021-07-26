import numpy as np
import matplotlib.pyplot as plt


x = range(1,11)
y1=[36840,
34590,
21738,
7040,
5998,
8554,
10160,
21748,
29923,
31691
]
y2=[
33655,
34058,
27673,
11752,
10219,
11466,
13922,
27433,
35702,
36206
]
y3=[
49896,
49401,
35917,
14536,
13815,
15004,
16845,
30509,
42471,
46722,

]
y4=[
    30868,
31296,
24510,
7588,
5959,
7284,
9895,
24255,
33044,
33579,
]
line1, =plt.plot(x, y1, marker='o', mec='r', mfc='w')
line2, =plt.plot(x, y2, marker='*', ms=10)
line3, =plt.plot(x,y3, marker='s',ms=10)
line4,=plt.plot(x,y4,marker='+')
plt.legend([line1, line2,line3,line4], ["实际总人数变化曲线", "考虑货机预测人数变化曲线","不考虑货机预测人数变化曲线","调参之后的预计人数变化曲线"],loc='best',frameon=False,prop="SimSun")
plt.xlabel('时间/周次',fontproperties="SimSun"); plt.ylabel('人数/个',fontproperties="SimSun");
plt.title("周一人数变化曲线图", fontproperties="SimSun" ,fontsize='large')
plt.show()
