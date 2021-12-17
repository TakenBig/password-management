# coding=UTF-8
# author: dbZhang
# update: 2021-12-14

# accountController.py
# Class AccountController
# expose the interface to gui

from service.accountService import AccountService


class AccountController:
    # 限制属性
    __slots__ = ('caption', 'account', 'password', 'note')

    def __init__(self, caption=None, account=None, password=None, note=None):
        self.account = account
        self.caption = caption
        self.password = password
        self.note = note

    # 增加新用户
    def addAccount(self):
        account_service = AccountService(self.caption, self.account, self.password, self.note)
        return account_service.addAccount()

    # 查询所有账户的标题信息
    def queryCaptions(self):
        account_service = AccountService()
        return account_service.queryCaptions()

    # 根据某一个标题查询用户的信息
    def queryByCaption(self):
        account_service = AccountService(caption=self.caption)
        return account_service.queryByCaption()

    # 更新某一个账户的信息
    def updateAccount(self):
        account_service = AccountService(self.caption, self.account, self.password, self.note)
        return account_service.updateAccount()

    # 密码强度检测
    def passwordDetection(self):
        account_service = AccountService(password=self.password)
        return account_service.passwordDetection()

    # 密码生成
    def passwordProduce(self):
        account_service = AccountService()
        return account_service.passwordProduce()

    # 模糊搜索标题
    def searchLikesCaption(self):
        account_service = AccountService(caption=self.caption)
        return account_service.searchLikesCaption()

    # 删除账号
    def deleteAccount(self):
        account_service = AccountService(caption=self.caption)
        return account_service.deleteAccount()