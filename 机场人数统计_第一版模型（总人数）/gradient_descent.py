from numpy import *
import main
import data_processing as dap
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
    theta = array([3, 1]).reshape(2, 1)
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




# 数据集大小 即20个数据点
# m = dap.num_date
m=10
rate = 10000
# x的坐标以及对应的矩阵
X1 = array(main.predict_num_weeks).reshape(m,1)/rate # 生成一个m行1列的向量，也就是x0，全是1
# X1 = array([33655,34058,27673,11752,10219,11466,13922,27433,35702,36206]).reshape(m,1)/10000
X0 = ones((m,1))  # 生成一个m行1列的向量，也就是x1，从1到m
X = hstack((X0, X1))  # 按照列堆叠形成数组，其实就是样本数据
# 对应的y坐标
Y = array([36840,34590,21738,7040,5998,8554,10160,21748,29923,31691]).reshape(m, 1)/rate
# 学习率
alpha = 0.01
optimal = gradient_descent(X, Y, alpha)
print('optimal:', optimal)
print('cost function:', cost_function(optimal, X, Y)[0][0])

Y_pre_optimal=optimal[0] + optimal[1]*X1
for i in range(len(Y_pre_optimal)):
    print(int(Y_pre_optimal[i][0]*rate))

