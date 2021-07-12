import sys
import requests
import json
import xlsxwriter
import time
import os
import datetime

# 程序打包: pyinstaller -F .\GetPayMessage.py
config = {'bear': 'Bearer 3437ac7a-5b06-4dea-8a35-c8d08b6adb09',
          'host': 'http://car.lgflsh.com'}
lotime = time.localtime()
module = 'None'
todaystr = f'{lotime.tm_year}-{lotime.tm_mon}-{lotime.tm_mday}'
url = 'http://platform.taoqicar.com/bills/api/paybills'  # 月供账单  monthcount
# url = 'http://platform.taoqicar.com/bills/api/getPayBillsWaterPage' # 交易流水 paybackdetail

# module 1
class monthcount:
    url = 'http://platform.taoqicar.com/bills/api/paybills'

    userName = ''  # 客户名称
    carNumber = ''  # 车牌号
    frameNumber = ''  # 车架号
    idCard = ''  # 证件号码
    id = ''  # 账单编号
    contractNumber = ''  # 合同编号
    contractMainBody = ''  # 合同主体
    signTime = ''  # 签署时间
    beginDate = ''  # 签署开始时间
    endDate = ''  # 签署结束时间
    bankNum = ''  # 银行卡号
    bankName = ''  # 还款银行
    periods = ''  # 还款期数
    channelName = ''  # 支付通道
    payTime = ''  # 支付时间
    ExcelTitle = [
        '客户名称',
        '车牌号',
        '车架号',
        '证件号码',
        '账单编号',
        '合同编号',
        '合同主体',
        '签署时间',
        '签署开始时间',
        '签署结束时间',
        '银行卡号',
        '还款银行',
        '还款期数',
        '支付通道',
        '支付时间'
    ]

    def __init__(self, pag):
        self.userName = pag['userName']
        self.carNumber = pag['carNumber']
        self.frameNumber = pag['frameNumber']
        self.idCard = pag['idCard']
        self.id = pag['id']
        self.contractNumber = pag['contractNumber']
        self.contractMainBody = pag['contractMainBody']
        self.signTime = str(pag['signTime']).replace(
            '+08:00', '').replace('T', ' ')
        self.beginDate = str(pag['beginDate']).replace(
            '+08:00', '').replace('T', ' ')
        self.endDate = str(pag['endDate']).replace(
            '+08:00', '').replace('T', ' ')
        self.bankNum = pag['bankNum']
        self.bankName = pag['bankName']
        self.periods = pag['periods']
        self.channelName = pag['channelName']
        self.payTime = str(pag['payTime']).replace(
            '+08:00', '').replace('T', ' ')

    def makeoutlst(self):
        ls = []
        ls.append(self.userName)
        ls.append(self.carNumber)
        ls.append(self.frameNumber)
        ls.append(self.idCard)
        ls.append(self.id)
        ls.append(self.contractNumber)
        ls.append(self.contractMainBody)
        ls.append(self.signTime)
        ls.append(self.beginDate)
        ls.append(self.endDate)
        ls.append(self.bankNum)
        ls.append(self.bankName)
        ls.append(self.periods)
        ls.append(self.channelName)
        ls.append(self.payTime)
        return ls

#module 2
class paybackdetail:
    url = 'http://platform.taoqicar.com/bills/api/getPayBillsWaterPage'

    userName = ''  # 客户名称
    carNumber = ''  # 车牌号
    frameNumber = ''  # 车架号
    idCard = ''  # 证件号码
    orderNum = ''  # 支付单号
    waterNumber = ''  # 交易流水号
    subjectName = ''  # 款项名称
    channelName = ""  # 支付通道
    waterFrom = ""  # 流水来源
    payTime = "",  # 支付时间
    payAccount = ""  # 付款账号姓名
    payNumber = ""  # 付款账号
    receiveAccount = ""  # 收款账号名称
    payBankName = ""  # 付款账号银行
    receiveBankName = ""  # 收款账号银行
    receiveNumber = ""  # 收款账号
    createTime = ""  # 创建时间
    contractNumber = ""  # 合同编号
    payDate = ""  # 还款日期
    doUser = ""  # 操作人
    bizMainBody = ""  # 业务主体
    actualAmountDueExcle = ''  # 交易金额(元)
    ExcelTitle = [
        '客户名称',
        '车牌号',
        '车架号',
        '证件号码',
        '支付单号',
        '交易流水号',
        '款项名称',
        '支付通道',
        '流水来源',
        '支付时间',
        '付款账号姓名',
        '付款账号',
        '收款账号名称',
        '付款账号银行',
        '收款账号银行',
        '收款账号',
        '创建时间',
        '合同编号',
        '还款日期',
        '操作人',
        '业务主体',
        '交易金额(元)'
    ]

    def __init__(self, pag):
        self.userName = pag['userName']
        self.carNumber = pag['carNumber']
        self.frameNumber = pag['frameNumber']
        self.idCard = pag['idCard']
        self.orderNum = pag['orderNum']
        self.waterNumber = pag['waterNumber']
        self.subjectName = pag['subjectName']
        self.channelName = str(pag['channelName'])
        self.waterFrom = pag['waterFrom']
        self.payTime = str(pag['payTime']).replace(
            '+08:00', '').replace('T', ' ')
        self.payAccount = pag['payAccount']
        self.payNumber = pag['payNumber']
        self.receiveAccount = pag['receiveAccount']
        self.payBankName = pag['payBankName']
        self.receiveBankName = pag['receiveBankName']
        self.receiveNumber = pag['receiveNumber']
        self.createTime = str(pag['createTime']).replace(
            '+08:00', '').replace('T', ' ')
        self.contractNumber = pag['contractNumber']
        self.payDate = str(pag['payDate']).replace(
            '+08:00', '').replace('T', ' ')
        self.doUser = pag['doUser']
        self.bizMainBody = pag['bizMainBody']
        self.actualAmountDueExcle = pag['actualAmountDueExcle']

    def makeoutlst(self):
        ls = []
        ls.append(self.userName)
        ls.append(self.carNumber)
        ls.append(self.frameNumber)
        ls.append(self.idCard)
        ls.append(self.orderNum)
        ls.append(self.waterNumber)
        ls.append(self.subjectName)
        ls.append(self.channelName)
        ls.append(self.waterFrom)
        ls.append(self.payTime)
        ls.append(self.payAccount)
        ls.append(self.payNumber)
        ls.append(self.receiveAccount)
        ls.append(self.payBankName)
        ls.append(self.receiveBankName)
        ls.append(self.receiveNumber)
        ls.append(self.createTime)
        ls.append(self.contractNumber)
        ls.append(self.payDate)
        ls.append(self.doUser)
        ls.append(self.bizMainBody)
        ls.append(self.actualAmountDueExcle)
        return ls


class payback:
    userName = 'Default'  # 客户名称
    carNumber = ''  # 车牌号
    frameNumber = ''  # 车架号
    idCard = ''  # 证件号码
    contractNumber = ''  # 合同编号
    paydetaillst = []  # 支付详情
    channells = []
    exportls = ''
    ExcelTitle = ['客户名称', '车牌号', '车架号', '证件号码', '合同编号', '支付通道']

    def __init__(self, contractNumber):
        self.contractNumber = contractNumber
        self.paydetaillst = []
        self.channells = []
        self.exportls = ''

    def make_channel_export(self):
        for pdtl in self.paydetaillst:
            # print('make_channel_export_channelName:',pdtl.channelName)#debug
            channelName = f'{pdtl.channelName}'
            if channelName not in self.channells:  # 判断是否记录
                self.channells.append(channelName)
                self.exportls = f'{self.exportls}{pdtl.channelName},{pdtl.payTime}|'

    def makeoutlst(self):
        ls = []
        ls.append(self.userName)
        ls.append(self.carNumber)
        ls.append(self.frameNumber)
        ls.append(self.idCard)
        ls.append(self.contractNumber)
        ls.append(self.exportls)
        return ls


def GetRequests(url, filename, page, para):
    header = {'Authorization': config['bear']}
    params = {'page': page,
              'size': 60,
              'contractNumber': para
              }  # 订单信息
    Print_To_Text(f'info{todaystr}.txt',
                  f'{time.asctime(time.localtime())}:para:{para}')
    response = requests.get(url, headers=header, params=params)  # 订单管理
    Print_To_Text(f'log{todaystr}.txt',
                  f'{time.asctime(time.localtime())}:正在处理url:{response.url}')
    # "log{}.txt".format(todaystr),"{}: 正在处理url:{}".format(time.asctime(lotime), response.url))
    if response.status_code != 200:
        Print_To_Text(f'error{todaystr}.log', response.text)
    Print_To_Text(filename, response.json())
    if 'error' in response.json():
        print('请确认Config.txt文件信息正确。(按回车键退出程序）')
        input()
        quit()
    return response


def Print_To_Text(filename, text):
    filpath = os.path.join(os.getcwd(), 'RunMessage')
    if not os.path.exists(filpath):
        os.mkdir(filpath)
    text_file = open(f'{os.path.join(filpath,filename)}',
                     "a+", encoding='utf8')
    text_file.writelines('{}\n'.format(text))
    text_file.close()


def prin_msg(request, paymsg):
    # paymsg = paybackdetail()#debug
    for pag in request.json():
        if pag['contractNumber'] != paymsg.contractNumber:
            continue
        # print('prin_msg_channelName:',str(pag['channelName']))#debug
        # 更改输出数据.
        if module == "2":
            # paybackdetail
            paymsg.paydetaillst.append(paybackdetail(pag))
        if module == "1":
            # monthcount
            paymsg.paydetaillst.append(monthcount(pag))

def ExportMessage(paymsglst):
    # 输出文件名.
    count = 1
    rowall = 0
    row = 0
    ls = []
    filename = f'Export{todaystr}'
    filpath = os.path.join(os.getcwd(), 'ExportFile')
    if not os.path.exists(filpath):
        os.mkdir(filpath)
    excelfile = os.path.join(filpath, f'{filename}_{count}.xlsx')
    while os.path.exists(excelfile):
        excelfile = os.path.join(filpath, f'{filename}_{count}.xlsx')
        count = count + 1
    # 输出 创建Excel
    workbook = xlsxwriter.Workbook(excelfile)
    wk = workbook.add_worksheet('支付渠道信息')
    wkall = workbook.add_worksheet('所有获取数据')
    # 数据详情
    for paymsg in paymsglst:
        # 输出基础数据.
        # paymsg = payback()#debug
        if row == 0:
            # 需要数据的表头
            ls.extend(paymsg.ExcelTitle)
            row = export_to_excel(wk, ls, row)
            ls.clear()
        ls.extend(paymsg.makeoutlst())
        row = export_to_excel(wk, ls, row)
        ls.clear()
        # 输出全量数据
        for det in paymsg.paydetaillst:
            # det = paybackdetail()#debug
            # paybackdetail
            if rowall == 0:
                # 全量数据的表头
                ls.extend(det.ExcelTitle)
                rowall = export_to_excel(wkall, ls, rowall)
                ls.clear()
            # monthcount
            # det = monthcount()  # debug.
            ls.extend(det.makeoutlst())
            rowall = export_to_excel(wkall, ls, rowall)
            ls.clear()
    workbook.close()
    print(f'数据导出结束，文件为：{excelfile}')


def export_to_excel(excel, linelst, row):
    for column in range(len(linelst)):
        excel.write(row, column, str(linelst[column]))
    return row+1


lst = [
    'TY20210600029',
    'GX20210600007'
]


def main():
    paymsglst = []
    count = 0
    totalcount = len(lst)
    for conN in lst:  # 遍历合同编号
        count = count + 1
        print(f'获取进度:{count}/{totalcount}',
              f'Start:{lotime.tm_hour}:{lotime.tm_min}:{lotime.tm_sec}',
              f'Now:{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}')
        # print(conN)#debug
        xtotalcount = -1
        page = 0
        paymsg = payback(conN)
        while(xtotalcount != 0):
            reque = GetRequests(url, f'gettitlemsg{todaystr}.json', page, conN)
            xtotalcount = len(reque.json())
            # print('xtotalcount:',xtotalcount)#debug
            if xtotalcount == 0:
                continue
            page = page + 1
            # print(f'page:{page},conN:{conN},count:{xtotalcount},relen:{len(reque.json())}url:{reque.url}')
            if len(reque.json()) != 0:  # 获取数据不为空
                # 判断是否是第一次
                if paymsg.userName == "Default":
                    for firstjs in reque.json():  # 遍历所有获取数据
                        if firstjs['contractNumber'] != conN:  # 剔除合同编号不同项
                            continue
                        paymsg.userName = firstjs['userName']
                        paymsg.carNumber = firstjs['carNumber']
                        paymsg.frameNumber = firstjs['frameNumber']
                        paymsg.idCard = firstjs['idCard']
                        paymsg.contractNumber = firstjs['contractNumber']
                        break
                # 处理数据
                prin_msg(reque, paymsg)
        paymsg.make_channel_export()
        # print('len:',len(paymsg.paydetaillst))#debug
        # 按合同编号将数据记录
        paymsglst.append(paymsg)

    ExportMessage(paymsglst)


if __name__ == "__main__":
    lst.clear()
    configpath = os.path.join(os.getcwd(), 'config.txt')
    # print(configpath)
    f = open(configpath, 'r', encoding='utf-8')
    line = f.readline()
    findmsg = False
    while line:
        line = f.readline()
        #
        if 'bear' in line:
            l = line.split(': "')[1].split('"')[0].replace('"', '')
            config['bear'] = l
        #
        if 'module' in line:
            l = line.split(': "')[1].split('"')[0].replace('"', '')
            module = l
            if module == '1':
                url = 'http://platform.taoqicar.com/bills/api/paybills'
            if module == '2':
                url = 'http://platform.taoqicar.com/bills/api/getPayBillsWaterPage'
        #
        if findmsg:
            if '"' in line:
                findmsg = False
            else:
                value = line.replace(' ', '').replace('\n', '')
                if value != "":
                    lst.append(str(value))

        if 'contractNumber' in line:
            findmsg = True
        #
    main()
    print('按回车结束程序.')
    input()
