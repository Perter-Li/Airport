from matplotlib import pyplot as plt

Y_origal=[0,0,0,0,0,1043,1060,246,384,169,432,434,222,202,267,318,346,298,362,350,53,230,32,0]
X_origal=range(0,24)
plt.plot(X_origal,Y_origal)
# plt.xticks()
plt.xlabel("时间/小时",fontproperties="SimSun")
plt.ylabel("人数/人",fontproperties="SimSun")
plt.show()

Y_modified=[0,0,0,246,384,169,432,434,222,202,267,318,346,298,362,350,53,230,32,0]

bins =(max(Y_modified)-min(Y_modified))//100
plt.hist(Y_modified,bins=bins)
plt.title("剔除数据后，频数范围", fontproperties="SimSun" ,fontsize='large')
plt.xlabel("人数/人",fontproperties="SimSun")
plt.ylabel("频数/个",fontproperties="SimSun")
plt.show()
