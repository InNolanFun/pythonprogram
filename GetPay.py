import sys
import requests
import json
import xlsxwriter
import time
import os
import datetime

config = {'bear': 'Bearer 9179cb6c-ec18-42eb-a0f3-6f10c41ccf9d',
          'host': 'http://car.lgflsh.com'}
page = 0
lotime = time.localtime()
todaystr = '{}-{}-{}'.format(lotime.tm_year,lotime.tm_mon,lotime.tm_mday)
url = 'http://platform.taoqicar.com/bills/api/getPayBillsWaterPage?page=0&size=40&contractNumber={0}'
    #'http://platform.taoqicar.com/bills/api/paybills?page=0&size=40&contractNumber={0}'
     #'http://platform.taoqicar.com/bills/api/paybills?page=0&size=20&contractNumber=HBMGC1HK2018070001'
lst = ['TY20210600029',
'GX20210600007'
]


def main():
    i = 1
    for noo in lst:
        time.sleep(0.5)
        print('获取进度:{}/{}'.format(i, len(lst)))
        i = i+1
        # 支付通道  channelName
        # 合同编号  contractNumber
        # 用户名称  userName
        result = GetRequests(url.format(noo), 'gettitlemsg{}.json'.format(todaystr))
        mark_ls=[]
        for pag in result:
            if '您的账号已下线，请重新登录' in pag:
                print('您的账号已下线，请重新登录')
                break
            if 'channelName' in pag.keys():
                channelName = pag['channelName']
                contractNumber = pag['contractNumber']
            else:
                Print_To_Text("bug{}.txt".format(todaystr), "{}: 正在处理url:{}，noo:{}".format( 
                    time.asctime(time.localtime()), 'channelName不在json内,合同编号为:',noo))
                continue

            if contractNumber != noo:#可能因为模糊搜索找到错误合同编号
                continue
            userName = pag['userName']
            if channelName not in mark_ls:
                mark_ls.append(channelName)
        if  len(mark_ls)!=0:
            value = f'{noo}\t{channelName}\t{contractNumber}\t{mark_ls}\t{userName}'
            Print_To_Text(f'resultvalue{todaystr}.txt', value)
        


def GetRequests(url, filename):
    header = {'Authorization': config['bear']}
    params = {'page': page}  # 订单信息
    Print_To_Text("log{}.txt".format(todaystr), "{}: 正在处理url:{}".format( time.asctime(lotime), url))
    response = requests.get(url, headers=header, json=params)  # 订单管理
    if response.status_code != 200:
        Print_To_Text('error', response.text)
    result = json.loads(response.text)
    Print_To_Text(filename, response.text)
    return result


def Print_To_Text(filename, text):
    text_file = open(filename, "a+", encoding='utf8')
    text_file.writelines('{}\n'.format(text))
    text_file.close()


if __name__ == "__main__":
    main()
