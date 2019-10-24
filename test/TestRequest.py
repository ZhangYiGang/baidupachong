#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 17:22
# @Author  : zyg
# @Site    : 
# @File    : TestRequest.py
# @Software: PyCharm

import unittest
import sys
from spider.Request import Request
from spider.FormatData import FormatData
from Result.SearchResult import SearchResult
reload(sys)
sys.setdefaultencoding('utf-8')
import time
# 如果执行的是func1，那么会返回一个func2的函数
def func1(func2):
    # 测试装饰器外层函数运行几次
    time1 = time.time()
    print "qwer"
    # 外层函数从来没运行过
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print "开始时间"+str(time1)
        print start_time
        return func2(*args,**kwargs)
    return wrapper
def outer(level):
    def middle(func):
        # 中层这一步将函数名装填进去
        def wrapper(*args,**kwargs):
            if level==1:
                func()
        # 到最后装饰器返回的是这个函数，里面的args，kwargs都是运行时复制过去的
        # 等于说运行时直接运行这个函数
        return wrapper

    return middle
# 等到都成功之后就将wrapper这个函数名复制给原函数
def func2():
    print "asdf"
@outer(level=1)
def test_dector():
    # 为什么装饰器里的外层函数不执行呢
    print "test1"
@func1
def test_dector2():
    print "test_dector2"

class TestRequest(unittest.TestCase):
    def setUp(self):
        pass

    def test_Response(self):
        request =  Request()
        print request.get_request({'word':"ps培训", 'sa':'tb'})

    def test_dict(self):
        print dict([1,2])

    def test_count(self):
        request = Request()
        count = 0
        formatData = FormatData()
        searchResult = SearchResult()
        # while(True):
        count += 1
        response = request.get_request({'word': "192.168.0.1", 'sa': 'tb'})

        formatData.set_BS(response)
        result = formatData.get_first_non_ad()
        # formatData.get_useful_judge(result)
        searchResult.set_result(result)
        type = searchResult.judge_type()
        print "结果"+str(type)

    def test_clouse(self):
        test_dector
        # test_dector()
        print test_dector.func_name
        print test_dector.__name__
        print test_dector.__closure__[0].cell_contents
        print test_dector.__closure__[1].cell_contents

        # test_dector2()
        # time.sleep(0.2)
        # test_dector()
        # func1(func2)
        # another = func1(func2)
        # another()