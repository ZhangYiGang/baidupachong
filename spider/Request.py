#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 17:10
# @Author  : zyg
# @Site    : 
# @File    : Request.py
# @Software: PyCharm
import requests
class Request():
    def __init__(self):
        self.set_headers(None)
        pass

    def set_headers(self, headers):
        if headers is None:
            self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"}
            # 手机header
            # self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        else:
            self.headers = headers
    def get_baidu_text(self, keyword):
        response = requests.get("http://www.baidu.com/s?", params=keyword, headers= self.headers)
        return response.text

    def get_request(self, url,headers):
        headers = dict(headers.items()+self.headers.items())
        response = requests.get(url,headers = headers)
        return response