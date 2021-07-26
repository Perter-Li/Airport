import json
base_path = "C:/Users/李稳强/Desktop/列车顶部异物检测项目/机场人群预测/数据/航班信息有关/"

fp = open(base_path+"5月10日-7月24日T1航站楼信息.json",'r',encoding='utf-8')
ret_dic=fp.read()
dic=json.loads(ret_dic)
inf_list=dic['data']
num_date=int(input("请输入日期数目"))
str = input("请输入数据日期（2021-5-10至2021-7-24）——格式（年-月-日）")
date=str.split()
dic_list=[]
for i in range(0,len(date)):
    path =base_path + date[i]+'具体信息'
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
        if dic["航班日期"].split()[0].split('/')[0] == date[i].split('-')[0]\
                and dic["航班日期"].split()[0].split('/')[1] == date[i].split('-')[1]\
                and dic["航班日期"].split()[0].split('/')[2] == date[i].split('-')[2]:

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
            # print(dic["航班号"])
        else:
            continue
    fpw.close()

    fptr = open(path,'r',encoding='utf-8')
    fptr.readline()
    dic_list.append([])
    while True:
        lines= fptr.readline()
        if not lines:
            break
        temp=dict()
        for str in lines.split():
            temp["航班号"]=lines.split()[0]
            temp["机型"]=lines.split()[1]
            temp["计划起飞时间"]=int(lines.split()[5].split(':')[0])*60 +int(lines.split()[5].split(':')[1])
        dic_list[i].append(temp)
    print(dic_list[i])

