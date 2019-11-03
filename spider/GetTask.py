#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 17:35
# @Author  : zyg
# @Site    :
# @File    : FormatData.py
# @Software: PyCharm
from utils.ExcelUtil import myexcel
from utils.FileUtil import FileUtils
import os,json
key_words = ["1搜索检索词", "2结果类型", "3前1位站点", "4满足类型"]
class GetTask():
    def __init__(self):
        self.task_array = []

    def get_excels(self):
        self.excel_path = []
        for dirpath, dirnames, filenames in os.walk(FileUtils.get_project_dir()):
            for file in filenames:
                if file.endswith(".xlsx"):
                    print("现在处理文件"+file)
                    filepath = dirpath  + os.sep+file
                    self.excel_path.append(filepath)
        self.excel_dict = dict(zip(self.excel_path, [False for i in self.excel_path]))

    def get_task_singleexcel(self):
        excel = myexcel()
        for filepath in self.excel_dict.keys():
            if self.excel_dict[filepath] == False:
                excel.load_excel(filepath)
                json_array = excel.get_excel_array()
                # 获取第一列的key
                need_key = excel.get_excel_key(1)
                for every_json in json_array:
                    value_to_key = every_json[need_key]
                    self.task_array.append(value_to_key)
                last_not_blank = [ key.strip() == "" for key in self.task_array[::-1]].index(False)
                # 为了填补从第二行的数据，第二行到第n行
                return { filepath:self.task_array[0:len(self.task_array)-last_not_blank]}
            else:
                return  None
    def set_task_result(self, result):
        # result应该是个字典key是filepath，value是多层list
        # 在这里处理写入,从第二行写入
        filepath = result.keys()[0]
        json_array = []
        for single_result in result.values()[0]:
            json_array.append(dict(zip(key_words, single_result)))
        final_array_json = json.dumps(json_array)
        txt_file = filepath.replace("xlsx","txt")
        with open(txt_file, "w") as task_txt:
            task_txt.write(final_array_json)
        from utils.JsonUtil import json_to_csv
        json_to_csv(txt_file)
        pass

