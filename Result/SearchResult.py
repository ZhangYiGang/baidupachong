#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 09:57
# @Author  : zyg
# @Site    : 
# @File    : SearchResult.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from ResultException import ResultException
from utils.FileUtils import  FileUtils
from spider.FormatData import FormatData
import json
class SearchResult():
    """
    @:param type 表示处理结果类型 0:未知 1:自然结果 2:阿拉丁
    """
    def __init__(self):
        self.type = 0
        with open("alading.json","r") as alading_file:
            self.judege_json = json.load(alading_file)

    def get_type(self):
        return self.type

    """
        @:param text 处理得到的结果
    """
    def set_result(self, result):
        self.parse = result
            # BeautifulSoup(text, "html.parser")

    #从json里面获取数据，如果一个都没有的话，则认为它不是阿拉丁
    def judge_type(self):
        for html_label,css_dict in self.judege_json.items():
            for items in css_dict.items():
                attrs_dict ={items[0]:items[1]}
                item_result = self.parse.find(html_label,attrs = attrs_dict)
                if item_result is not  None:
                    self.type = 1
                    print "该结果是阿拉丁"

if __name__ == '__main__':
    text = FileUtils.get_text_from_file("/Users/bupt/untitled.html")
    formatData = FormatData()
    formatData.set_BS(text)
    result = formatData.get_first_non_ad()
    # formatData.get_useful_judge(result)
    searchResult = SearchResult()
    searchResult.set_result(result)
    searchResult.judge_type()