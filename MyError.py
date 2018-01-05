# encoding = utf-8

class MyError(BaseException):
    def __init__(self,testCase):
        self.errInfo = testCase
    def __str__(self):
        return repr('{}测试不通过!!!'.format(self.errInfo))