import data_processing as dap
import inital_data as ind
from matplotlib import pyplot as plt

#定义相对预计起飞的结束登机时间
ahead_time_start = 45
ahead_time_end = 120

# 定义绘图函数
def draw(pre):
    plt.figure(figsize=(20,8),dpi=80)
    plt.scatter(range(0,24),pre)
    plt.show()

# 读取数据
dic_list = dap.dic_list
predict_num_weeks=[]
for i in range(len(dic_list)):
    max_num=0
    #当前在等待的飞机
    curr_waiting_flight=[]
    for flight in dic_list[i]:
                # if flight["机型"] in ind.passenger_flight:
                    curr_waiting_flight +=[{"航班号":flight["航班号"],"机型":flight["机型"],
                                       "开始登机时间":flight["计划起飞时间"]-ahead_time_end,
                                        "结束登机时间":flight["计划起飞时间"]-ahead_time_start}]

                    max_num += ind.flight_num[flight["机型"]]

    total_num=0
    predict_num=[]
    # 注意转成数值型（未解决）
    for curr_time in range(0,24*60):#对于一天中的数据进行分析(以分钟为单位)
        total_num=0
        for some_flight in curr_waiting_flight:
            if curr_time < some_flight["开始登机时间"]:
                break
            else:
                # if curr_time == some_flight["结束登机时间"]-75: print("%s登机开始，此时为%d分钟"%(some_flight["航班号"],curr_time))
                total_num += ind.num_people(some_flight["机型"],curr_time,some_flight["开始登机时间"])
                # if curr_time == some_flight["结束登机时间"]:
                #     print("%s登机结束，此时为%d分钟"%(some_flight["航班号"],curr_time))
        # 将每一小时预计的人数存入一个列表中
        if curr_time % 60 == 0:
                predict_num.append(total_num/1000)
    predict_num_weeks .append(max_num)
    print(max_num)
    # draw(predict_num)



