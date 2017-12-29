#-*- coding:utf-8 -*- 
import unittest
import HTMLTestRunnerCN
from common import Configuration as cc


listaa='C:\\Users\\selenium_python1\\test_case'
def creatsuite():
    
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa, pattern='test_*.py', top_level_dir=None)
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTest(test_case)
    return testunit
alltestname=creatsuite()

now=cc.getCurrentTime()
filename='C:\\Users\\selenium_python1\\report\\'+now+'result.html'
fp=file(filename,'wb')
runner=HTMLTestRunnerCN.HTMLTestRunner(
        stream = fp,
        title=u'自动化测试报告', 
        #description='详细测试用例结果',    #不传默认为空
        tester=u"cx"     #测试人员名字，不传默认为QA
        )
    #运行测试用例
runner.run(alltestname)