#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 20:47
# @Author  : zyg
# @Site    : 
# @File    : FileUtil.py
# @Software: PyCharm
import urllib
import os
class FileUtils():
    @classmethod
    def get_text_from_file(cls, filename):
        with open(filename, mode='r') as file:
            return file.read()
    @classmethod
    def download_from_url(self, url, dir):
        # dir是本系统的相对路径
        if url and dir:
            dir = FileUtils.get_project_dir() + dir
            if not os.path.exists(dir):
                os.mkdir(dir)
            res = urllib.urlopen(url).read()
            path = dir +os.sep+ url[-8:-1] + ".jpg"
            with open(path, "w") as write_file:
                write_file.write(res)
        return path
    @classmethod
    def  get_file_size(self, path ):
        if os.path.exists(path):
                file_size = os.path.getsize(path)
                return  file_size
        #     返回文件大小为0代表默认它是小文件
        return 0

    @classmethod
    def get_project_dir(cls):
        path = os.path.abspath(__file__)
        project_dir = os.sep.join(path.split(os.sep)[0:-2])
        return project_dir+os.sep