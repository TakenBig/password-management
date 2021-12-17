# coding=UTF-8

import mysql

if __name__ == '__main__':
    host = 'localhost'
    user = 'root'
    password = '123456'
    db = 'pwsbookdb'
    database = mysql.MySQL(host, user, password, db)
    # sql="INSERT INTO accountinfo (caption,account,password,note) values ('微信账号','wechat1508256957','zwb178679a','qq账号不是qq账号')"
    # print(sql)
    sql='select * from accountinfo '
    # sql="select * from accountinfo where account='wechat150825'"
    # sql="update accountinfo set caption='haha this is a test' where account='1508256957'"
    # sql="delete from accountinfo where account='1508256957'"
    # database.insert(sql)
    # qs=database.query(sql)
    # print(qs)
    print(database.query(sql))
