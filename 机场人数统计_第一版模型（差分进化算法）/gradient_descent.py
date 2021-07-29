from numpy import *
import main
import processing as dap
# 定义代价函数
def cost_function(theta, X, Y):
    diff = dot(X, theta) - Y  # dot() 数组需要像矩阵那样相乘，就需要用到dot()
    return (1/(2*m)) * dot(diff.transpose(), diff)


# 定义代价函数对应的梯度函数
def gradient_function(theta, X, Y):
    diff = dot(X, theta) - Y
    return (1/m) * dot(X.transpose(), diff)

# 梯度下降迭代
def gradient_descent(X, Y, alpha):
    theta = array([1, 1]).reshape(2, 1)
    gradient = gradient_function(theta, X, Y)
    while not (all(abs(gradient) <= 1e-5)):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta, X, Y)
        print("theta is:",theta[0],theta[1])
        print("gradient is:",gradient[0],gradient[1])
    return theta

# 根据数据画出对应的图像
def plot(X, Y, theta):
    import matplotlib.pyplot as plt
    ax = plt.subplot(111)  # 这是我改的
    ax.scatter(X, Y, s=5, c="red", marker="o")
    plt.xlabel("时间/小时",fontproperties="SimSun")
    plt.ylabel("人数/千人",fontproperties="SimSun")
    # title = plt.title(dap.date + "航站楼人数随时间变化", fontproperties="SimSun" ,fontsize='large')
    x = arange(1,m+1)  # x的范围
    y = theta[0] + theta[1]*x
    ax.plot(x, y)
    plt.show()




# 数据集大小
date=dap.date_real_num
m = len(date)
rate = 10000
predict=main.predict_num_weeks
# x的坐标以及对应的矩阵
X1 = array(predict).reshape(m,1)/rate # 生成一个m行1列的向量，也就是x0，全是1
X0 = ones((m,1))  # 生成一个m行1列的向量，也就是x1，从1到m
X = hstack((X0, X1))  # 按照列堆叠形成数组，其实就是样本数据
# 对应的y坐标
Y = array(date).reshape(m, 1)/rate
# 学习率
alpha = 0.01
optimal = gradient_descent(X, Y, alpha)
print('optimal:', optimal)
print('cost function:', cost_function(optimal, X, Y)[0][0])

Y_pre_optimal=optimal[0] + optimal[1]*X1
Y_pre_num=[]
for i in range(len(Y_pre_optimal)):
    Y_pre_num.append(int(Y_pre_optimal[i][0]*rate))
    print(Y_pre_num[i])

