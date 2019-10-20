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
import os
class SearchResult():
    """
    @:param type 表示处理结果类型 0:未知 1:自然结果 2:阿拉丁
    """
    def __init__(self):
        self.type = 0
        # Result/alading
        abs_path = os.path.abspath(__file__)
        project_path =abs_path[0:abs_path.index("baidupachong")]+"baidupachong\\"
        with open(project_path+"Result\\alading.json","r") as alading_file:
            self.judge_json = json.load(alading_file)

    def get_type(self):
        return self.type

    """
        @:param text 处理得到的结果
    """
    def set_result(self, result):
        self.parse = result
        self.type = 0
            # BeautifulSoup(text, "html.parser")

    #从json里面获取数据，如果一个都没有的话，则认为它不是阿拉丁
    def judge_type(self):
        has_judge_flag = False
        for html_label,css_dict in self.judge_json.items():
            for items in css_dict.items():
                #从alading.json里面取数据，json的每一个key只能对应一个value，但是一个key需要对应多个value时，那就分隔开
                for every_value in items[1].split("|"):
                    attrs_dict = {items[0]: every_value}
                    item_result = self.parse.find(html_label, attrs=attrs_dict)
                    if item_result is not None:
                        has_judge_flag = True
                        print(attrs_dict)
                        break

        if has_judge_flag is True:
            self.type = 2
        else:
            self.type = 1
        return self.type
if __name__ == '__main__':
    text = FileUtils.get_text_from_file("/Users/bupt/untitled.html")
    formatData = FormatData()
    formatData.set_BS(text)
    result = formatData.get_first_non_ad()
    # formatData.get_useful_judge(result)
    searchResult = SearchResult()
    searchResult.set_result(result)
    searchResult.judge_type()