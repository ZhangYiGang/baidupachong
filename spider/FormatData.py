#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 17:35
# @Author  : zyg
# @Site    : 
# @File    : FormatData.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from utils.FileUtils import FileUtils
class FormatData():
    """
    这个类主要用来返回第一个非广告类型的结果
    """
    item_class_filter_word = "c-result result"
    def __init__(self):
        self.bs = None
    def set_BS(self, text):
        self.bs = BeautifulSoup(text, 'html.parser')

    def get_first_non_ad(self):
        # 下面这一行代码就是第一个非广告的类型
        result = self.bs.find("div", class_= self.item_class_filter_word)
        return  result
        # for index, every_result in enumerate(result):
        #     if every_result.find_all(text = "广告"):
        #         print index
    def get_useful_judge(self, result):
        switch_btn = result.find_all("ul", attrs = {"voice-action": "switch"})
        print switch_btn
if __name__ == '__main__':
    text = FileUtils.get_text_from_file("/Users/bupt/untitled.html")
    formatData = FormatData()
    formatData.set_BS(text)
    result = formatData.get_first_non_ad()
    formatData.get_useful_judge(result)