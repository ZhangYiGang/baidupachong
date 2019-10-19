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
reload(sys)
sys.setdefaultencoding('utf-8')
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
        while(True):
            count+=1
            response = request.get_request({'word': "ps培训", 'sa': 'tb'})

            formatData.set_BS(response)
            result = formatData.get_first_non_ad()
            formatData.get_useful_judge(result)