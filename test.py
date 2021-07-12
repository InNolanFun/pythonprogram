class paybackdetail:
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

    def __init__(        self,
        orderNum,
        waterNumber,
        subjectName,
        channelName,
        waterFrom,
        payTime,
        payAccount,
        payNumber,
        receiveAccount,
        payBankName,
        receiveBankName,
        receiveNumber,
        createTime,
        contractNumber,
        payDate,
        doUser,
        bizMainBody,
            actualAmountDueExcle
    ):
        self.orderNum = orderNum
        self.waterNumber = waterNumber
        self.subjectName = subjectName
        self.channelName = str(channelName)
        self.waterFrom = waterFrom
        self.payTime = str(payTime).replace('+08:00', '').replace('T', ' ')
        self.payAccount = payAccount
        self.payNumber = payNumber
        self.receiveAccount = receiveAccount
        self.payBankName = payBankName
        self.receiveBankName = receiveBankName
        self.receiveNumber = receiveNumber
        self.createTime = str(createTime).replace(
            '+08:00', '').replace('T', ' ')
        self.contractNumber = contractNumber
        self.payDate = str(payDate).replace('+08:00', '').replace('T', ' ')
        self.doUser = doUser
        self.bizMainBody = bizMainBody
        self.actualAmountDueExcle = actualAmountDueExcle


class payback:
    userName = ''#客户名称
    idCard=''#证件号码
    contractNumber=''#合同编号


    #userName = 'Default'  # 客户名称
    #carNumber = ''  # 车牌号
    #frameNumber = ''  # 车架号
    #idCard = ''  # 证件号码
    #contractNumber = ''  # 合同编号
    paydetaillst = []  # 支付详情
    channells = []
    exportls = ''

    def __init__(self, contractNumber):
        self.contractNumber = contractNumber
        self.paydetaillst = []
        self.channells = []
        self.exportls = ''

    def make_channel_export(self):
        for pdtl in self.paydetaillst:
            # print('make_channel_export_channelName:',pdtl.channelName)#debug
            if pdtl.channelName not in self.channells:  # 判断是否记录
                self.channells.append(f'{pdtl.channelName}')
                self.exportls = f'{self.exportls}{pdtl.channelName},{pdtl.payTime}|'

