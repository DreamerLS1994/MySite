from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse

import requests
import re

# Create your views here.

def ticketleft_init_view(request):
    return render(request,'tools/ticketleft_init.html')

def getStation(sta):
    STATION_DICT_URL = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9088'
    str = requests.get(STATION_DICT_URL).text

    #匹配中文的正则表达式
    area = re.findall("([\u4E00-\u9FA5]+)\|([A-Z]+)",str)
    area = dict(area)

    if sta in area:
        return area[sta]

def getUrl(from_sta, to_sta, date, ticket_type):
    from_sta_code = getStation(from_sta)
    to_sta_code = getStation(to_sta)
    
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=' + date + '&leftTicketDTO.from_station=' + from_sta_code + '&leftTicketDTO.to_station=' + to_sta_code + '&purpose_codes=' + ticket_type
    return url


@require_POST
def ticketleft_query_view(request):
    if request.is_ajax():
        from_sta = request.POST.get('from_sta')     
        to_sta = request.POST.get('to_sta')         
        train_date = request.POST.get('train_date')         
        ticket_type = request.POST.get('ticket_type') 

        url = getUrl(from_sta, to_sta, train_date, ticket_type)
        html = requests.get(url)
        if html.status_code == 200:
            list_All = []

            res = html.json()["data"]["result"]
            # print(res)
            sta_dict = html.json()["data"]["map"] #获得到一个字典  用于站点的汉字和字符标记转换
            for data in res:
                list_Child = []
                list = data.split("|") #分割，获取所有信息填入的list
                #print(list)
                if list[1]=='列车停运': #根据json 挨个分析
                    continue
                line_no = list[3]
                from_sta = list[6]
                to_sta = list[7]
                start_time = list[8]
                stop_time = list[9]
                cost_time = list[10]
				
		#字符串 赋值 ： or  两个都有值，取第一个，第一个没有值，取第二个
                TDZ=list[32] or "--"    #特等座
                YDZ=list[31] or "--"    #一等座
                EDZ=list[30] or "--"    #二等座
                RW=list[23] or "--"     #软卧
                YW=list[28] or "--"     #硬卧
                RZ=list[27] or "--"     #软座
                YZ=list[29] or "--"     #硬座
                WZ=list[26] or "--"  #无座  

                list_Child.append(line_no)
                list_Child.append(sta_dict[from_sta])
                list_Child.append(sta_dict[to_sta])
                list_Child.append(start_time)
                list_Child.append(stop_time)
                list_Child.append(cost_time)
                list_Child.append(TDZ)
                list_Child.append(YDZ)
                list_Child.append(EDZ)
                list_Child.append(RW)
                list_Child.append(YW)
                list_Child.append(RZ)
                list_Child.append(YZ)
                list_Child.append(WZ)
                
                list_All.append(list_Child)
            return JsonResponse({'msg':'成功！','res':list_All})
        return JsonResponse({'msg':'失败！','url':url})
