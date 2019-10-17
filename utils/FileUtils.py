#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 20:47
# @Author  : zyg
# @Site    : 
# @File    : FileUtils.py
# @Software: PyCharm
class FileUtils():
    @classmethod
    def get_text_from_file(cls, filename):
        with open(filename, mode='r') as file:
            return file.read()