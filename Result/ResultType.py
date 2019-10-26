#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 16:37
# @Author  : zyg
# @Site    : 
# @File    : ResultType.py
# @Software: PyCharm
from enum import Enum
"""
用来表示结果的类型
"""
class ResultType(Enum):
#以下三个是用来判断单个类型里面的是否
    YES = 1
    NO = 0
    UNSURE =2
#以下是判断站点类型的