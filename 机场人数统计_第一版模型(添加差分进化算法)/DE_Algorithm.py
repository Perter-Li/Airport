from numpy import *
from matplotlib import pyplot as plt
import processing as dap
import main
X_data=main.predict_num_weeks
Y_data=dap.date_real_num
X_in=array(X_data).reshape(1,len(X_data))
Y_in=array(Y_data).reshape(1,len(Y_data))

def initial(N,m):
    X=[]
    for i in range(N):
        X.append([])
        for j in range(m):
            X[i].append(random.uniform(-1,1))
    return X
    pass

def effective_randint_best(best):
    r=[best,0,0]
    while True:
        r[1]=random.randint(1,N)
        r[2]= random.randint(1,N)
        if r[0] != r[1] and r[1] != r[2]:
            return (r[0],r[1],r[2])

def effective_randint():
    while True:
        r=random.randint(1,N,3)
        if r[0] != r[1] and r[1] != r[2]:
            return (r[0],r[1],r[2])

def cost_function(theta):
    #采用Rosenbrkck函数
    sum_cost=0
    for i in range(len(X_data)):
        # sum_cost=(theta[0] + theta[1]*X_in[0][i] + theta[2]*(X_in[0][i]**2)-Y_in[0][i])**2
        sum_cost=(theta[0]*X_in[0][i] + theta[1]*(X_in[0][i]**2)-Y_in[0][i])**2
        # sum_cost +=(theta[0] + theta[1]*X_in[0][i]-Y_in[0][i])**2
    return sum_cost
    pass

def best_unit(X):
    min_index=0
    min_cost=cost_function(X[0])
    for i in range(N):
        if cost_function(X[i]) < min_cost:
            min_index=i
            min_cost=cost_function(X[i])
    return min_index
#定义种群规模
N = 100
#定义维数
n = 2
#定义交叉率
Cr = 0.9
#定义步长
step_length = 0.01




#代数限制，也即终止条件
generations= 30

#初始化种群
X=initial(N,n)
for offspring in range(generations):
    #计算当前种群中最优的个体
    best = best_unit(X)
    v=[]
    u=[]
    for i in range(N):
        r1,r2,r3=effective_randint_best(best)
        # r1,r2,r3=effective_randint()
        # tmep列表 用于计算X[r1] + step_length * (X[r2]-X[r3])
        temp =[X[r1][j] +step_length * (X[r2][j]-X[r3][j]) for j in range(n) ]
        v.append(temp)
        u.append(v[i])
        Jr=random.randint(1,n)
        for j in range(n):
            RC_j=random.random()
            if RC_j < Cr or Jr==j:
                u[i][j]=v[i][j]
            else:
                u[i][j]=X[i][j]
    for i in range(N):
        if(cost_function(X[i]) > cost_function(u[j])):
            for j in range(n):
                X[i]=u[i]

optimal_cost=[]
for i in range(N):
    optimal_cost.append(cost_function(X[i]))
    # print(optimal_cost[i],X[i])

best = best_unit(X)
print(best,X[best])
print(min(optimal_cost))
optimal_data=[]
for i in range(len(X_data)):
    # temp=int((X[best][0]+X[best][1]*X_in[0][i] + X[best][2]*(X_in[0][i])**2))
    temp=int((X[best][0]*X_in[0][i] + X[best][1]*(X_in[0][i])**2))
    # temp=int((X[best][0]+X[best][1]*X_in[0][i] ))
    optimal_data.append(temp)
    print(temp)
