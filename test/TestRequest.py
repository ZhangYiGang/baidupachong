#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 17:22
# @Author  : zyg
# @Site    : 
# @File    : TestRequest.py
# @Software: PyCharm

import unittest
import sys
import os
from spider.Request import Request
from spider.FormatData import FormatData
from Result.ParseResult import ParseResult
from utils.FileUtil import FileUtils

# sys.setdefaultencoding('utf-8')
import time
# 如果执行的是func1，那么会返回一个func2的函数
def func1(func2):
    # 测试装饰器外层函数运行几次
    time1 = time.time()
    # print "qwer"
    # 外层函数从来没运行过
    def wrapper(*args,**kwargs):
        start_time = time.time()
        # print "开始时间"+str(time1)
        # print start_time
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
    print("asdf")
@outer(level=1)
def test_dector():
    pass
    # 为什么装饰器里的外层函数不执行呢
    # print "test1"
@func1
def test_dector2():
    print("test_dector2")

class TestRequest(unittest.TestCase):
    def setUp(self):
        pass

    def test_Response(self):
        request =  Request()
        print(request.get_baidu_text({'word': "ps培训", 'sa': 'tb'}))

    def test_dict(self):
        print(dict([1,2]))

    def test_count(self):
        request = Request()
        count = 0
        formatData = FormatData()
        searchResult = ParseResult()
        # while(True):
        count += 1
        response = request.get_baidu_text({'word': "192.168.0.1", 'sa': 'tb'})

        formatData.set_BS(response)
        result = formatData.get_first_non_ad()
        # formatData.get_useful_judge(result)
        searchResult.set_result(result)
        type = searchResult.judge_type()
        print("结果"+str(type))

    def test_clouse(self):
        test_dector
        # test_dector()
        print(test_dector.func_name)
        print(test_dector.__name__)
        print( test_dector.__closure__[0].cell_contents)
        print(test_dector.__closure__[1].cell_contents)

        # test_dector2()
        # time.sleep(0.2)
        # test_dector()
        # func1(func2)
        # another = func1(func2)
        # another()

    def test_download(self):
        # 小图片大小2388,4196
        #大图片18147,5746
        url = "https://ss0.bdstatic.com/9bA1vGfa2gU2pMbfm9GUKT-w/timg?wisealaddin&size=f200_200&quality=60&sec=1571968181&di=569202accdd1c09b949a0044661e10b0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fbaike%2Fpic%2Fitem%2Fd1160924ab18972b3554ca8ae6cd7b899e510a00.jpg"
        # url = "https://ss0.bdstatic.com/9bA1vGfa2gU2pMbfm9GUKT-w/timg?wisealaddin&size=f200_200&quality=60&sec=1571968008&di=3c1214067da26669d8110741bcacdf01&src=http%3A%2F%2Fimgsrc.baidu.com%2Fbaike%2Fpic%2Fitem%2F8644ebf81a4c510f9cb0d1976259252dd52aa5c2.jpg"
        # url = "https://ss0.bdstatic.com/9bA1vGfa2gU2pMbfm9GUKT-w/timg?wisealaddin&size=f960_540&quality=100&sec=1571967937&di=b27050369655e03ca36348d81313bfd1&src=http%3A%2F%2Ft12.baidu.com%2Fit%2Fu%3D3734041358%2C683429700%26fm%3D179%26app%3D35%26f%3DJPEG%3Fw%3D570%26h%3D320%26s%3D74A3BE1E0D424F49561688D1030030BB"
        # url = "https://ss1.bdstatic.com/7Ls0a8Sm1A5BphGlnYG/sys/portrait/item/2312cafdbeddbfe2d8a62a2d.jpg"
        # url = "https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=1447167364,3444772473&fm=179&app=35&f=JPEG?w=120&h=120&s=50343D73056157032ACC74EF03007020"
        FileUtils.download_from_url(url, "new")

    def test_path(self):
        print(FileUtils.get_project_dir())

    def test_enum(self):
        from Result.ResultType import ResultType
        print(ResultType.UNSURE.value ==2)

    def test_getip(self):
        from utils.TimeUtil import ExecuteTime

    def test_json(self):
        data = {"time": 123}
        print(str(data))
    def test_time(self):
        nowtime = 1571999440
        # 872
        import time
        a= time.time()
        print(round(a,3))
        print(round(1.23,3))
        print(round(1.234,3))

        # timearray = time.localtime(nowtime)
        # print time.strftime("%Y--%m--%d %H:%M:%S",timearray)

    def test_re(self):
        import re
        result  = re.match( re.compile(r"((\d{2,3}\.){3})\d{2,3}"),"10.108.115.57")
        print(result.groups())

    def test_single_task(self):
        request = Request()
        text = request.get_baidu_text({'word': "植物传播种子的方法"})
        if text:
            searchResult = ParseResult()
            formatData = FormatData()
            formatData.set_BS(text)
            result = formatData.get_first_non_ad()
            # formatData.get_useful_judge(result)
            searchResult.set_result(result)
            type = searchResult.judge_type()
            stastify_type_explain_string = searchResult.judge_satsify_type()
            print("类型是" + str(type) + "满足类型" + stastify_type_explain_string)

    def test_divide(self):
        # python的除法需要注意添加float
        print( 1 if float(4)/float(5) >0.1 else 0 )