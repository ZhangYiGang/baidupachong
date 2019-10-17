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