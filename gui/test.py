import unittest

import detailPage


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_setCaption(self):
        page = detailPage.Detail()
        page.setCaption('qq')

if __name__ == '__main__':
    unittest.main()
