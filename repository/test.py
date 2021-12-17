import unittest
from accountRepository import AccountRepository


class MyTestCase(unittest.TestCase):

    def test_queryByCaption(self):
        ar = AccountRepository(caption='手机账号')
        ar.queryByCaption()

    def test_updateAccount(self):
        ar = AccountRepository(caption='qq', account='1508256957', password='abcdefgh', note='这是QQ')
        ar.updateAccount()

    def test_searchLikesCaption(self):
        ar = AccountRepository(caption='qq')
        print(ar.searchLikesCaption())

    def test_deleteAccount(self):
        ar = AccountRepository(caption='钱钱钱钱钱')
        print(ar.deleteAccount())


if __name__ == '__main__':
    unittest.main()
