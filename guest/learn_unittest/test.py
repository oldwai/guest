# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import os
import time
import unittest

import HTMLTestRunner

from guest.learn_unittest.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(10,2)

    def tearDown(self):
        pass

    def test_add(self):
        add_result = self.cal.add()
        self.assertEqual(add_result,12)

    def test_sub(self):
        add_result = self.cal.sub()
        self.assertEqual(add_result,8)

    def test_mult(self):
        add_result = self.cal.mul()
        self.assertEqual(add_result,20)

    def test_div(self):
        add_result = self.cal.div()
        self.assertEqual(add_result,5)



if __name__ == "__main__":
    #unittest.main()
    #构建测试用例集
    suite = unittest.TestSuite()
    tests = ["test_add","test_sub","test_mult","test_div"]
    suite.addTest(CalculatorTest("test_add"))
    suite.addTest(CalculatorTest("test_sub"))
    suite.addTest(CalculatorTest("test_mult"))
    suite.addTest(CalculatorTest("test_div"))

    # #执行测试
    # 1、获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 报告存放路径
    report_path = os.getcwd()
    print(report_path)
    # 2、html报告文件路径
    report_abspath = os.path.join(report_path, "result_"+now+".html")

    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'接口自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    #runner = unittest.TextTestRunner()
    runner.run(suite)