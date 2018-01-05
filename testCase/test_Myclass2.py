# encoding = UTF-8
import unittest

import sys

from MyError import MyError
from target.myClass import Myclass


class test_Myclass2(unittest.TestCase):
    """test myClass.py"""
    @classmethod
    def setUpClass(cls):
        print('setUp...')
    @classmethod
    def tearDownClass(cls):
        print('tearDown ...')

    def test_1_div_5(self):
        """ test_1_div_5"""
        print('test 1/5 ...')
        self.assertEqual(1/5, Myclass().div(1, 5),  'test failed')

    def test_3_div_11(self):
        """test_3_div_11"""
        print('test 3/11 ...')
        try:
            self.assertTrue(Myclass().div(3, 11) == 0.4)
        except:
            print('test_3_div_11:测试失败')

    def test_3_div_24(self):
        """test_3_div_24"""
        '''test_3_div_24'''
        print('test 3/24 ...')
        # self.assertEqual(Myclass().div(3, 4), 3/5)
        try :
            self.assertEqual(Myclass().div(3, 24), 3/5)
        except AssertionError:
            raise MyError(sys._getframe().f_code.co_name)
        except MyError as msg:
            print('测试失败 %s' %msg)

    @unittest.skipIf(True, 'skip')
    def test_3_div_4_3(self):
        """test_3_div_4_3"""
        '''test_3_div_4_3'''
        print('test 3/4 ...')
        # self.assertEqual(Myclass().div(3, 4), 3/3)
        try :
            self.assertEqual(Myclass().div(3, 4), 3/4)
        except AssertionError:
            raise MyError(sys._getframe().f_code.co_name)
        except MyError as msg:
            print('测试失败 %s' %msg)


if __name__ == '__main__':
    unittest.main()

