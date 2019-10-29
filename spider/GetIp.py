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
from Result.ResultException import ResultException
from utils.FileUtil import FileUtils
from utils.TimeUtil import ExecuteTime
import time
import json,re
ip_file_name = "baiduIp.txt"
class GetIp():
    # /这个是不包含时间的，因为这个请求需要绑定现在时间 经过解析时间戳是13位的 比正常时间多了3位
    ip_site_notime = "https://site.ip138.com/domain/read.do?domain=www.baidu.com&time="

    def __init__(self):
        self.ip_array = []
        self.ip_already = False

    def get_ip_fromsite(self):
        now_time = str(int(time.time()*1000))
        ip_site = self.ip_site_notime+now_time
        ip_file_absolute_path = FileUtils.get_project_dir() +ip_file_name

        # 因为与这个网站请求的数量过多，他限制了连接的数量，应该一直使用一个request或者设置下面这个header
        try:
            response = Request().get_request(ip_site, {'Connection': 'close'})
            # 这个js请求的是一个json数据，在回填到动态网页上去解析
            if response.status_code == 200:
                response_json = json.loads(response.text)
                pattern = re.compile(r"(\d{2,3}\.){3}\d{2,3}")
                ip_list = response_json["data"]
                for ip_json in ip_list:
                    ip_string = ip_json["ip"]
                    if re.match(pattern, ip_string):
                        self.ip_array.append(ip_string)
                with open(ip_file_absolute_path, "w") as ip_file:
                    ip_file.write(",\n".join(self.ip_array))
                self.ip_already = True
            else:
                # 请求失败了的话，从本地文件读取吧
                raise ResultException("ip请求失败")
        except Exception as e:
            if isinstance(e,ResultException):
                # 暂时来说两种异常都是一样的，不做过多处理
                pass
            with open(ip_file_absolute_path, "r") as ip_file:
                ip_all_string = ip_file.read()
                self.ip_array = ip_all_string.split(",\n")
                self.ip_already = True
    @ExecuteTime
    def get_ip_array(self, count):
        # 将每次执行完成的时间写进文件里面
        # 如果五次都执行失败了的话，则ip_array为空
        if self.ip_already :
            self.ip_already = False
            return True
        else:
            self.get_ip_fromsite()
            count+=1
            if count>5:
                self.ip_already = True
                self.ip_array =  []
            self.get_ip_array(count)
            return False



