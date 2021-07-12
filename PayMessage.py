import sys
import requests
import json
import xlsxwriter
import time
import os
import datetime

config = {'bear': 'Bearer 9179cb6c-ec18-42eb-a0f3-6f10c41ccf9d',
          'host': 'http://car.lgflsh.com'}
lotime = time.localtime()
todaystr = '{}-{}-{}'.format(lotime.tm_year, lotime.tm_mon, lotime.tm_mday)
url = 'http://platform.taoqicar.com/bills/api/getPayBillsWaterPage?page=0&size=40&contractNumber={0}'


def main():
    i = 1
    for noo in lst:
        time.sleep(0.5)
        print('获取进度:{}/{}'.format(i, len(lst)))
        i = i+1
        # 支付通道  channelName
        # 合同编号  contractNumber
        # 用户名称  userName
        result = GetRequests(url.format(
            noo), 'gettitlemsg{}.json'.format(todaystr))
        mark_ls = []
        for pag in result:
            if '您的账号已下线，请重新登录' in pag:
                print('您的账号已下线，请重新登录')
                break
            if 'channelName' in pag.keys():
                channelName = pag['channelName']
                contractNumber = pag['contractNumber']
            else:
                Print_To_Text("bug{}.txt".format(todaystr), "{}: 正在处理url:{}，noo:{}".format(
                    time.asctime(time.localtime()), 'channelName不在json内,合同编号为:', noo))
                continue

            if contractNumber != noo:  # 可能因为模糊搜索找到错误合同编号
                continue
            userName = pag['userName']
            if channelName not in mark_ls:
                mark_ls.append(channelName)
        if len(mark_ls) != 0:
            value = f'{noo}\t{channelName}\t{contractNumber}\t{mark_ls}\t{userName}'
            Print_To_Text(f'resultvalue{todaystr}.txt', value)


def GetRequests(url, filename, page, para):
    header = {'Authorization': config['bear']}
    params = {'page': page,
              'size': 60,
              'contractNumber': para
              }  # 订单信息
    Print_To_Text("log{}.txt".format(todaystr),
                  "{}: 正在处理url:{}".format(time.asctime(lotime), url))
    response = requests.get(url, headers=header, params=params)  # 订单管理
    if response.status_code != 200:
        Print_To_Text('error.log', response.text)
    Print_To_Text(filename, response.json())
    return response


def Print_To_Text(filename, text):
    text_file = open(filename, "a+", encoding='utf8')
    text_file.writelines('{}\n'.format(text))
    text_file.close()



def prin_msg(request,noo,channelNamelst):
    #request = GetRequests('http://platform.taoqicar.com/bills/api/getPayBillsWaterPage', 'test.json', page, i)
    #channelNamelst=[]#module test
    for pag in request.json():
        if '您的账号已下线，请重新登录' in pag:
                print('您的账号已下线，请重新登录')
                break
        if 'channelName' in pag.keys():
            channelName = pag['channelName']
            contractNumber = pag['contractNumber']
        else:
            Print_To_Text("bug{}.txt".format(todaystr), f"{time.asctime(time.localtime())}: channelName不在json内,合同编号为:{noo}")
            continue
        if contractNumber != noo:  # 可能因为模糊搜索找到错误合同编号
            continue
        if channelName not in channelNamelst:
                channelNamelst.append(channelName)    
        
lst = []

if __name__ == "__main__":
    # for i in lst:  # 遍历合同编号
    i = 'GD2018010077'
    xtotalcount = -1
    page = 0
    channelNamelst=[]
    while(xtotalcount != 0):
        reque = GetRequests('http://platform.taoqicar.com/bills/api/getPayBillsWaterPage', 'test.json', page, i)
        print(f'page:{page},i:{i},count:{xtotalcount},relen:{len(reque.json())}url:{reque.url}')
        prin_msg(reque,i,channelNamelst)
        xtotalcount = len(reque.json())
        page = page + 1
    print(len(channelNamelst))
    for j in channelNamelst:
        print(f'type:{type(j)},j:{j}')
    # main()

lst = ['TY20210600029',
       'GX20210600007',
       'ZJ20210500001',
       'SU20210500012',
       'HB20210500001',
       'NJ20210400054',
       'TY20210400087',
       'NJ20210400046',
       'TY20210400057',
       'NJ20210400044',
       'JH20210400020',
       'SJZ20210400015',
       'AH20210400001',
       'SC20210400003',
       'DG20210300039',
       'SJZ20210300057',
       'SJZ20210300053',
       'DG20210300020',
       'ZZ20210300016',
       'YN20210300007',
       'AA20210300003',
       'SJZ20210300002',
       'SX20210200003',
       'HL20210200002',
       'SD20210100025',
       'YN20210100074',
       'GZ20210100029',
       'GZ20210100022',
       'YC2021010001',
       'SX20210100029',
       'JX20210100009',
       'AA20210100009',
       'ZZ20210100006',
       'NJ20210100005',
       'SX20210100003',
       'NJ20210100000',
       'HZ20210100002',
       'QQHE20210100001',
       'GD20210100004',
       'YN20201200031',
       'SC20201200007',
       'GX20201200013',
       'SX20201200008',
       'HZ20201200001',
       'JH2020120011',
       'CQ20201200001',
       'JH20201200000',
       'GD2020110040',
       'QQHE20201100001',
       'SX2020110029',
       'SX2020110020',
       'SX2020110012',
       'YC2020110006',
       'HZ2020110006',
       'SC2020100031',
       '2020102516413310000710305567-1',
       'HZ2020100005',
       'LZ2020100001',
       'WZ2020100005',
       'QQHE2020090013',
       'QQHE2020090012',
       'SJZ2020090053',
       'SJZ2020090054',
       'DG2020090047',
       'WZ2020090027',
       'GX2020090022',
       'TY2020090022',
       'SU2020090001',
       'YN2020080039',
       'HL2020080011',
       'YN2020080025',
       'SX2020080012',
       'GD2020080002',
       'SD2020080001',
       'SJZ2020080001',
       'SU2020070087',
       'ZZ2020070032',
       'YN2020070034',
       'HB2020070009',
       'HB2020060036',
       'HL2020060016',
       'YN2020060014',
       'GZ2020060004',
       'GD2020060013',
       'QQHE2020050013',
       'GZ2020050004',
       'SC2020040023',
       'SX2020040021',
       'CC2020030002',
       'ZJ2020030008',
       'HZ2019110014',
       'GX2019110009',
       'GD2019100017',
       'CQ2019100006',
       'SD2019100004',
       'GD2019090074',
       'CQ2019090007',
       'JX2019090003',
       'SU2019080035',
       'WZ2019080002',
       'CC2019070004',
       'BZWXFC2019060001',
       'YC2019060012',
       'LGFC2019070001',
       'ZJ2019060006',
       'GD2019060008',
       'HZ2019060001',
       'SH2019050001',
       'SH2019040008',
       'GD2019040011',
       'SU2019030027',
       'SH2019030005',
       'JANC1HK2019010010',
       'SC2018120004',
       'GD2018120004',
       'SX2018110003',
       'SU2018110004',
       'HB2018100034',
       'SX2018100024',
       'HB2018100007',
       'NJ2018090017',
       'SX2018090023',
       'GZ2018090013',
       'JX2018090008',
       'HN2018080003',
       'HB2018080001',
       'NJ2018070032',
       'SD2018070015',
       'DG2018050012',
       'NC2018050001',
       'CQ2018020097',
       'AA2018010105',
       'GD2018010077',
       'NC2018010012',
       'AA2017120144',
       'GX2017110025',
       'SC2017110043',
       'CQ2017110002',
       'GX2017100001',
       'NJ2017090008',
       'GD2017090007',
       'AA2017090006',
       'WZ2017080019',
       'SU2017080024',
       ]
