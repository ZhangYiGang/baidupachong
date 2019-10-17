#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:10
# @Author  : zyg
# @Site    : 
# @File    : ResultException.py
# @Software: PyCharm
class ResultException(Exception):
    def __init__(self, descrption = None):
        if descrption is not None:
            self.descrption = descrption
