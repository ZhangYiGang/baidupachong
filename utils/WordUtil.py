#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 21:23
# @Author  : zyg
# @Site    : 
# @File    : WordUtil.py
# @Software: PyCharm
class WordUtil():
    @classmethod
    def del_transform_in_json(cls, text):
        print text
        if r"\\" in text:
            return text.replace(r'\\',"\\")
        else:
            return text
if __name__== "__main__":
    import re


    result = re.compile(u".*歌曲$").match(    '强军战歌 - 歌曲')
    print result.group(0)
    # print WordUtil().del_transform_in_json(r"\\s")
