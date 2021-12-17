# coding=UTF-8
# authorL: dbZhang
# updata: 2021-12-13

# mysql.py
# Class MySQL
# this file can operate the mysql database

import pymysql


class MySQL:
    # 限制属性
    __slots__ = ('host', 'user', 'passwd', 'db')

    def __init__(self, host=None, user=None, passwd=None, db=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    # 连接数据库
    def getConnection(self):
        if self.host == None:
            raise Exception('lacking parameter: HOST')
        if self.user == None:
            raise Exception('lacking parameter: USER')
        if self.passwd == None:
            raise Exception('lacking parameter: PASSWD')
        if self.db == None:
            raise Exception('lacking parameter: DB')
        try:
            dbconn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.db)
            return dbconn
        except Exception as e:
            # raise Exception('failed to connect database')
            print(e)

    # 插入
    def insert(self, sql):
        self.__execute(sql=sql)

    # 删除
    def delete(self, sql):
        self.__execute(sql=sql)

    # 更新
    def updata(self, sql):
        self.__execute(sql=sql)

    # 查询
    def query(self, sql):
        queryResult = self.__executeQuery(sql=sql)
        return queryResult

    # 执行sql语句:插入、删除、更新
    def __execute(self, sql):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
            connection.commit()  # commit by self


    # 执行sql语句:查询
    def __executeQuery(self, sql):
        connection = self.getConnection()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                queryResult = cursor.fetchall()
            connection.commit()  # commit by self
        return queryResult


if __name__ == '__main__':
    raise Exception('please use me as a package')
