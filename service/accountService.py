# coding=UTF-8
# author: dbZhang
# update: 2021-12-14

# accountService.py
# class AccountService
# this file is control the business process

from repository.accountRepository import AccountRepository
from repository.accountEntity import AccountEntity
import string
import random
import re


class AccountService:
    # 限制属性
    __slots__ = ('caption', 'account', 'password', 'note')

    def __init__(self, caption=None, account=None, password=None, note=None):
        self.account = account
        self.caption = caption
        self.password = password
        self.note = note

    # add account
    def addAccount(self):
        account = AccountEntity(self.caption, self.account, self.password, self.note)
        repository = AccountRepository()
        return repository.addAccount(account.caption, account.account, account.password, account.note)

    # 查询所有账号的标题信息
    def queryCaptions(self):
        repository = AccountRepository()
        captions = repository.queryCaptions()
        return self.process_return_info(captions)

    # 根据某一个标题查询用户的信息
    def queryByCaption(self):
        repository = AccountRepository(caption=self.caption)
        account = repository.queryByCaption()
        return self.process_return_info(account)

    # 更新某一个账户的信息
    def updateAccount(self):
        repository = AccountRepository(self.caption, self.account, self.password, self.note)
        return repository.updateAccount()

    # 密码强度检测
    def passwordDetection(self):
        return self.detection(self.password)

    # 密码生成
    def passwordProduce(self):
        return self.createRandomStr()

    # 模糊搜索标题
    def searchLikesCaption(self):
        repository = AccountRepository(caption=self.caption)
        captions = repository.searchLikesCaption()
        return self.process_return_info(captions)

    # 删除账号
    def deleteAccount(self):
        repository = AccountRepository(caption=self.caption)
        return repository.deleteAccount()

    # 处理数据库查询返回的信息 从元组到列表
    @staticmethod
    def process_return_info(infos):
        res = []
        for i in infos:
            row = []
            for j in range(len(i)):
                row.append(i[j])
            res.append(row)
        return res

    # 随机生成一个8~15位的字符串
    @staticmethod
    def createRandomStr():
        charsets = string.ascii_letters+string.digits
        length = random.randint(8, 15)
        pwd = [random.choice(charsets) for i in range(length)]
        return ''.join(pwd)

    # 检测密码强度
    @staticmethod
    def detection(text):
        """
        判断字符串的强度登记
        :param text: 输入字符串
        :return: 返回字符串['弱',‘强’]
        """
        reg1 = r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$'
        reg2 = r'^[a-zA-Z]\w{5,17}$'
        res = re.match(pattern=reg1, string=text)
        if res is not None:
            return '强'
        else:
            res = re.match(pattern=reg2, string=text)
            if res is not None:
                return '中'
            else:
                return '弱'







