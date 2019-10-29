#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 11:23
# @Author  : zyg
# @Site    : 
# @File    : Config.py
# @Software: PyCharm
# 配置文件的设置
import os,json
from utils.FileUtil import FileUtils
class Config():
    config_dir = FileUtils.get_project_dir()+ "config" + os.sep

    ip_complete_time = 0
    ip_complete_time_file = ""
    space_time = 0

    # ip_time.json单独存在的原因是因为ip_time是一个不断变化而且需要保存的文件
    def load_Constant(self):
        config_json = json.loads(FileUtils.get_text_from_file(Config.config_dir  + "config.json"))
        Config.ip_complete_time_file = config_json["ip_time"]
        Config.ip_complete_time_file = Config.config_dir + Config.ip_complete_time_file
        Config.ip_complete_time = json.loads(FileUtils.get_text_from_file(Config.ip_complete_time_file))["time"]
        Config.space_time = config_json["space_time"]
