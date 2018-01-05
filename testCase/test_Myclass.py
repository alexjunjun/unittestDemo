# encoding = UTF-8
import os
import unittest

import sys

from MyError import MyError
from lib.log_config import get_logger
from target.myClass import Myclass
_mylogger = get_logger(os.path.basename(__file__))

class test_Myclass(unittest.TestCase):
    """test myClass.py"""
    @classmethod
    def setUpClass(cls):
        print('setUp...')
    @classmethod
    def tearDownClass(cls):
        print('tearDown ...')

    def test_1_div_1(self):
        """ test_1_div_1"""
        print('test 1/1 ...')
        self.assertEqual(1, Myclass().div(1, 1),  'test failed')

    def test_3_div_6(self):
        """test_3_div_5"""
        print('test 3/5 ...')
        try:
            self.assertTrue(Myclass().div(3, 6) == 0.4)
        except:
            print('test_3_div_5:测试失败')

    def test_3_div_4(self):
        """test_3_div_4"""
        '''test_3_div_4'''
        print('test 3/4 ...')
        # self.assertEqual(Myclass().div(3, 4), 3/5)
        try :
            self.assertEqual(Myclass().div(3, 4), 3/5)
        except AssertionError:
            raise MyError(sys._getframe().f_code.co_name)
        except MyError as msg:
            print('测试失败 %s' %msg)
            _mylogger.error(u'测试失败 %s' %msg)


    @unittest.skipIf(True, 'skip')
    def test_3_div_4_2(self):
        """test_3_div_4_2"""
        '''test_3_div_4_2'''
        print('test 3/4 ...')
        # self.assertEqual(Myclass().div(3, 4), 3/5)
        try :
            self.assertEqual(Myclass().div(3, 4), 3/4)
        except AssertionError:
            raise MyError(sys._getframe().f_code.co_name)
        except MyError as msg:
            print('测试失败 %s' %msg)


if __name__ == '__main__':
    unittest.main()

