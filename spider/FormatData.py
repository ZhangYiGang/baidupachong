#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 17:35
# @Author  : zyg
# @Site    : 
# @File    : FormatData.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from utils.FileUtil import FileUtils
import json
class FormatData():
    """
    这个类主要用来返回第一个非广告类型的结果
    """
    item_class_filter_word = [u"c-result",u"result"]
    def __init__(self):
        self.bs = None
        self.no_ad = None
    def set_BS(self, text):
        self.bs = BeautifulSoup(text, 'html.parser')
        self.no_ad = None

    def get_first_non_ad(self):
        # 下面这一行代码就是第一个非广告的类型
        if not self.no_ad:
            result = self.bs.find("div", attrs={"class": "results"})
            result_iter = result.children
            for item in result_iter:
                if hasattr(item, "attrs") and "class" in item.attrs:
                    list1 = set(item.attrs["class"])
                    list2 = set(self.item_class_filter_word)
                    has_word = list2 <= list1
                    if has_word:
                        self.no_ad = item
                        return item
        else:
            return self.no_ad
        # for index, every_result in enumerate(result):
        #     if every_result.find_all(text = "广告"):
        #         print index
    def get_script(self):
        result = self.get_first_non_ad()
        link = result.find("link")
        if link:
            if link.attrs["href"].endswith("js"):
                 return True
        return False
    def get_useful_judge(self, result):
        switch_btn = result.find_all("ul", attrs = {"voice-action": "switch"})
        # print switch_btn

        # 获取到url 这个通常只给阿拉丁使用
    def get_url(self):
        # 第一个获取到的url
        # url_array = []
        result = self.get_first_non_ad()
        try:
            data_log = result.attrs["data-log"]
            html_json = data_log.encode("utf-8").replace("\'", "\"")
            url_data_log = json.loads(html_json)["mu"]
            # url_array.append(url_data_log)
            return url_data_log
        except Exception as e:
            # 在这里处理json的解析问题
            print("json解析错误" + e.message)
        # content = self.parse.find("div",attrs={"class":"c-result-content"})
        # if content:
        #     # 取出第一个内容
        #     content = next(content.children)
        #     if "rl-link-href" in content.attrs:
        #        #  还有rl-link-data-url
        #        url_data_href = content.attrs["rl-link-href"]
        #        print(url_data_href)
        # else:
        #     # tood 这里要加的是找到url
        #     pass
        # pass
    def get_article(self):
        result = self.get_first_non_ad()
        atricle = result.find("article")
        if atricle:
           return atricle
        else:
            return result
if __name__ == '__main__':
    text = FileUtils.get_text_from_file("/Users/bupt/untitled.html")
    formatData = FormatData()
    formatData.set_BS(text)
    result = formatData.get_first_non_ad()
    formatData.get_useful_judge(result)