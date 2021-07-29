import scipy.stats
#from scipy.stats import norm
# 定义机型的最大载客量
flight_num={
"319":	122,
"320":  152,
"321":	179,
"32B":	166,
"32D":	166,
"32V":	166,
"332":	278,
"333":	284,
"359":	314,
"738":	164,
"73G":	170,
"73H":	170,
"73W":	170,
"748":	270,
"773":	270,
"77L":	300,
"77W":	368,
"788":	180,
"789":	276,
"343":  295,
"739":  180,
"763":	225,
"346":	350,
"33F":  180,
"ARJ":  90,
"388":  555
}

passenger_flight=[
"32V"   ,
"73H"	,
"320"	,
"32B"	,
"73W"	,
"739"	,
"73G"	,
"32D"   ,
"321"	,
"738"	,
"346"	,
"ARJ"]

att_rate=0.9


def total_num_people(type):
    return flight_num[type]

#上座率可能是一个分布，之后再修改
def attendence():
    return att_rate


# 定义正态分布函数，用于返回当前时刻的该航班的人数
def normal_fun(type,time,start_time):
    mu = 258
    sigma = 195
    # P = scipy.stats.norm.cdf(time,mu,sigma)-scipy.stats.norm.cdf(start_time,mu,sigma)
    P = scipy.stats.norm.cdf(time,mu,sigma)
    # print(P)
    return flight_num[type]*P
    # if time % 60 == 0:
    #     return flight_num[type]
    # else:
    #     return 0


def num_people(type,time,start_time):
    return normal_fun(type,time,start_time) * attendence()
