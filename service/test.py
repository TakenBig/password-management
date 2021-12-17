import unittest
from accountService import AccountService


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_proess_return_info(self):
        testinput = (('qq', '1508256957', '123456789', ''), ('1508236', '1508sssd', '123456789', '151554545'))
        print(AccountService.process_return_info(testinput))

    def test_addAccount(self):
        accser = AccountService(caption='qq',account='1508256957', password='zwb178679a', note='这是QQ')
        accser.addAccount()

    def test_queryByCaption(self):
        accser = AccountService(caption='qq')
        print(accser.queryByCaption())

    def test_detection(self):
        accser = AccountService()
        print(accser.detection('aAAx12334'))

    def test_createRandomStr(self):
        accser = AccountService()
        print(accser.createRandomStr())


if __name__ == '__main__':
    unittest.main()
