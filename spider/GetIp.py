#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 17:12
# @Author  : zyg
# @Site    : 
# @File    : GetIp.py
# @Software: PyCharm
"""
因为获取到百度的ip可以是多个，所以为了减少被封的可能性，应该尝试换几个ip
"""
from Request import Request
from bs4 import BeautifulSoup

class GetIp():
    # ip_site = "https://site.ip138.com/www.baidu.com/"
    ip_site = "https://site.ip138.com/domain/read.do?domain=www.baidu.com&time=1571999440872"
    def get_ip_fromsite(self):
        response = Request().get_request(self.ip_site)
        bs = BeautifulSoup(response.text, 'html.parser')
        div_contains_ip = bs.find("div",attrs={"id":"curadress"})
        for single_ip in div_contains_ip.children:
            print single_ip
        pass
