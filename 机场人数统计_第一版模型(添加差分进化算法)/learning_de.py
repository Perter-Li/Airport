# from numpy import  *
#
# err = 1e-5
# n = 1
# len = 0.01
# m = 20
#
# def pre_function(X,theta):
#     return X.dot(theta)
#     pass
#
#
# def cost_function(X,theta,Y):
#     tmp = dot(X,theta)-Y
#     return (1/(2*m))*dot(tmp.transpose(),tmp)
#     pass
#
#
# def descent_function(X,Y):
#     theta=zeros(n+1).reshape(n+1,1)
#     theta_des=(1/m)*dot(X.transpose(),dot(X, theta) - Y)
#     while any(abs(theta_des) > err):
#         theta=theta- len *theta_des
#         theta_des=(1/m)*dot(X.transpose(),dot(X, theta) - Y)
#         print(theta_des)
#     return theta
#     pass
#
#
# # 定义变量个数
# # X = ones((m,n+1)).reshape(m,n+1)
# # theta = zeros(n+1).reshape(n+1,1)
# Y=arange(1,m+1).reshape(m,1)
# # # x的坐标以及对应的矩阵
# X0 = ones((m, 1))  # 生成一个m行1列的向量，也就是x0，全是1
# X1 = arange(1, m+1).reshape(m, 1)  # 生成一个m行1列的向量，也就是x1，从1到m
# X = hstack((X0, X1))  # 按照列堆叠形成数组，其实就是样本数据
# # # 对应的y坐标
# # Y = array([
# #     3, 4, 5, 5, 2, 4, 7, 8, 11, 8, 12,
# #     11, 13, 13, 16, 17, 18, 17, 19, 21
# # ]).reshape(m, 1)
# optimal=descent_function(X,Y)
# print("optimal[0] is %.2f"%(optimal[0]))
# print("optimal[1] is %.2f"%(optimal[1]))
# print('cost function:', cost_function( X,optimal, Y))
#
# # # 根据数据画出对应的图像
# # def plot(X, Y, theta):
# #     import matplotlib.pyplot as plt
# #     ax = plt.subplot(111)  # 这是我改的
# #     ax.scatter(X, Y, s=5, c="red", marker="o")
# #     ax.plot(X,Y)
# #     plt.show()
# #
# # X=arange(1,m+1)
# # plot(X,Y,optimal)
#
#
# def plot(X, Y, theta):
#     import matplotlib.pyplot as plt
#     ax = plt.subplot(111)  # 这是我改的
#     ax.scatter(X, Y, s=30, c="red", marker="s")
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     x = arange(0, m+1, 0.2)  # x的范围
#     y = theta[0] + theta[1]*x
#     ax.plot(x, y)
#     plt.show()
#
# X=arange(1,m+1).reshape(m,1)
# plot(X, Y, optimal)
#


x = [(3.3655,1),(3.4058,1),(2.7673,1),(1.1752,1),(1.0219,1),(1.1466,1),(1.3922,1),(2.7433,1),(3.5702,1),(3.6206,1)]
y = [3.6840,3.4590,2.1738,0.7040,0.5998,0.8554,1.0160,2.1748,2.9923,3.1691]
my_break=0.00001
alpha=0.01
diff=0
error1,error0=0,0
theta0,theta1,theta2=0,0,0
sum0,sum1,sum2=0,0,0
count=0
while True:
    for i in range(len(x)):
        #批量更新参数
        diff=y[i]-(theta0*x[i][0]+theta1*x[i][1])
        sum0=sum0+alpha*diff*x[i][0]
        sum1=sum1+alpha*diff*x[i][1]
        count+=1
    theta0,theta1=sum0,sum1
    error1=0
    for i in range(len(x)):
        error1+=(y[i]-(theta0*x[i][0]+theta1*x[i][1]))**2/2
        count+=1
    if abs(error1-error0)<my_break:
        break
    else:
        error0=error1
print("Done: theta0:{0}, theta1:{1}, theta2:{2}.".format(theta0,theta1,theta2))

