# coding=UTF-8
# author: dbZhang
# update: 2021-12-14

# accountRepository.py
# class AccountRepository
# this file is used to write or read the database


from db.mysql import MySQL


class AccountRepository:
    __HOST = 'localhost'
    __USER = 'root'
    __PASSWORD = '123456'
    __DB = 'pwsbookdb'

    def __init__(self, caption=None, account=None, password=None, note=None):
        self.caption = caption
        self.account = account
        self.password = password
        self.note = note

    # 添加账户
    def addAccount(self, caption, account, password, note):
        # print(type(caption))
        sql = '''INSERT INTO accountinfo (caption,account,password,note) values ("%s","%s","%s","%s");''' % (
            caption, account, password, note)
        print(sql)
        database = MySQL(self.__HOST, self.__USER, self.__PASSWORD, self.__DB)
        try:
            database.insert(sql=sql)
            return True
        except Exception as exception:
            print(exception.args)
            return False

    # 查询所有账户的标题信息
    def queryCaptions(self):
        sql = 'select caption from accountinfo '
        database = MySQL(self.__HOST, self.__USER, self.__PASSWORD, self.__DB)
        try:
            queryres = database.query(sql)
            return queryres
        except Exception as exception:
            print(exception.args)
            return False

    # 根据某一个标题查询用户的信息
    def queryByCaption(self):
        sql = "select * from accountinfo where caption='%s'" % self.caption
        database = MySQL(self.__HOST, self.__USER, self.__PASSWORD, self.__DB)
        try:
            res = database.query(sql)
            return res
        except Exception as e:
            print(e.args)
            return False

    # 更新某一个账户的信息
    def updateAccount(self):
        sql = '''update accountinfo set caption="%s",account="%s",password="%s",note="%s" where account="%s"''' % (
            self.caption, self.account, self.password, self.note, self.account)
        database = MySQL(self.__HOST, self.__USER, self.__PASSWORD, self.__DB)
        try:
            database.updata(sql)
            return True
        except Exception as exception:
            print(exception.args)
            return False

    # 模糊搜索标题
    def searchLikesCaption(self):
        sql = ''' select caption from accountinfo where caption like \'%''' + self.caption + '''%\''''
        database = MySQL(self.__HOST, self.__USER, self.__PASSWORD, self.__DB)
        try:
            res = database.query(sql)
            return res
        except Exception as e:
            print(e.args)
            return False

    # 删除某一个账户
    def deleteAccount(self):
        sql = '''delete from accountinfo where caption="%s"''' % self.caption
        database = MySQL(self.__HOST, self.__USER, self.__PASSWORD, self.__DB)
        try:
            database.delete(sql)
            return True
        except Exception as e:
            print(e.args)
            return False
