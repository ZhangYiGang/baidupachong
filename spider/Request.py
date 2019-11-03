#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 17:10
# @Author  : zyg
# @Site    : 
# @File    : Request.py
# @Software: PyCharm
import requests
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Request():
    ip_array = []
    def __init__(self):
        self.set_headers(None)
        pass
    @classmethod
    def set_ip_array(cls, ip_array):
        Request.ip_array = ip_array

    def set_headers(self, headers):
        if headers is None:
            self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36"}
            # 手机header
            # self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
        else:
            self.headers = headers
    def get_baidu_text(self, keyword):
        if Request.ip_array:
            baidu_url = Request.ip_array[random.randint(0, len(Request.ip_array)-1)]
        else:
            baidu_url = "www.baidu.com"
        response = requests.get("http://"+baidu_url+"/s?", params=keyword, headers= self.headers)
        if response.status_code ==200 and "来自百度的搜索结果" in  response.text:

              return response.text
        else:
            print(baidu_url+"这里有问题"+"重拾关键字"+keyword)
            return self.get_baidu_text(keyword)

    def get_request(self, url,headers):
        headers = dict(headers.items()+self.headers.items())
        response = requests.get(url,headers = headers)
        return response