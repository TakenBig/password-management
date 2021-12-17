import unittest
from accountController import AccountController


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_queryByCaption(self):
        controller = AccountController(caption='qq')
        qs = controller.queryByCaption()
        print(qs)

if __name__ == '__main__':
    unittest.main()
