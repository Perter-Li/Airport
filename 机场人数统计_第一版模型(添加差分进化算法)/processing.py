import json
base_path = "C:/Users/李稳强/Desktop/列车顶部异物检测项目/机场人群预测/数据/航班信息有关/"


fp = open(base_path+"5月10日-7月24日T1航站楼信息.json",'r',encoding='utf-8')
ret_dic=fp.read()
dic=json.loads(ret_dic)
inf_list=dic['data']
fp.close()

#读出realdate.json文件，将返回结果存入rd_dic
rd_fp=open(base_path + "realdate.json",'r',encoding='utf-8')
ret_rd_dic=rd_fp.read()
rd_dic=json.loads(ret_rd_dic)
rd_fp.close()


weekday=input("请输入具体预计的周几（周一至周日）")
#将周几对应的具体日期存入date列表中
date=[]
date_real_num=[]
for day in rd_dic:
    if day["周几"]==weekday:
       date.append(day["日期"])
       date_real_num.append(day["实际总人数"])

#预处理过的数据存入dealed_list中
dealed_list=[]
for i in range(0,len(date)):
    divide_data=date[i].split('/')
    path =base_path +"航班具体信息/"+ divide_data[0]+'-'+divide_data[1]+'-'+divide_data[2]+'具体信息'
    fpw = open(path,'w',encoding='utf-8')
    fpw.write("航班号")
    fpw.write('\t')
    fpw.write("机型")
    fpw.write('\t')
    fpw.write("航班日期")
    fpw.write('\t\t\t')
    fpw.write("计划起飞时间")
    fpw.write('\t\t\t')
    fpw.write("预计起飞时间")
    fpw.write('\t\t\t')
    fpw.write("实际起飞时间")
    fpw.write('\n')
    for dic in inf_list:
        if dic["航班日期"].split()[0].split('/')[0] == divide_data[0]\
                and dic["航班日期"].split()[0].split('/')[1] == divide_data[1]\
                and dic["航班日期"].split()[0].split('/')[2] == divide_data[2]:

            fpw.write(dic["航班号"])
            fpw.write('\t')
            fpw.write(dic["机型"])
            fpw.write('\t')
            fpw.write(dic["航班日期"])
            len_data=len(dic["航班日期"])
            fpw.write('\t\t')
            if dic["计划起飞时间"]=="":
                fpw.write('-'*len_data)
            else:
                fpw.write(dic["计划起飞时间"])
            fpw.write('\t\t\t')
            if dic["预计起飞时间"]=="":
                fpw.write('-'*len_data)
            else:
                fpw.write(dic["预计起飞时间"])
            fpw.write('\t\t\t')
            if dic["实际起飞时间"]=="":
                fpw.write('-'*len_data)
            else:
                fpw.write(dic["实际起飞时间"])
            fpw.write('\n')
        else:
            continue
    fpw.close()

    fptr = open(path,'r',encoding='utf-8')
    fptr.readline()
    dealed_list.append([])
    while True:
        lines= fptr.readline()
        if not lines:
            break
        temp=dict()
        for str in lines.split():
            temp["航班号"]=lines.split()[0]
            temp["机型"]=lines.split()[1]
            temp["计划起飞时间"]=int(lines.split()[5].split(':')[0])*60 +int(lines.split()[5].split(':')[1])
        dealed_list[i].append(temp)
    print(dealed_list[i])

