# coding=UTF-8
# author: dbZhang
# update: 2021-12-14

# accountEntity.py
# class AccountEntity
# this file is Account Entity

class AccountEntity:
    # 限制属性
    __slots__ = ('caption', 'account', 'password', 'note')

    def __init__(self, caption=None, account=None, password=None, note=None):
        self.account = account
        self.caption = caption
        self.password = password
        self.note = note

    def __str__(self):
        s = (self.caption, self.account, self.password, self.note)
        return str(s)

    def getallattrs(self):
        return [self.caption,self.account,self.password,self.note]

