import processing as dap
import initail as ind
from matplotlib import pyplot as plt

#定义相对预计起飞的结束登机时间
ahead_time_start = 45
ahead_time_end = 120


# 读取数据
dic_list = dap.dealed_list
predict_num_weeks=[]
for i in range(len(dic_list)):
    max_num=0
    #当前在等待的航班
    curr_waiting_flight=[]
    for flight in dic_list[i]:
                if flight["机型"] in ind.passenger_flight:
                    curr_waiting_flight +=[
                        {"航班号":flight["航班号"],
                        "机型":flight["机型"],
                        "开始登机时间":flight["计划起飞时间"]-ahead_time_end,
                        "结束登机时间":flight["计划起飞时间"]-ahead_time_start}]

                    max_num += ind.flight_num[flight["机型"]]
    predict_num_weeks .append(max_num)
    # print("max_num")
    print(max_num)



