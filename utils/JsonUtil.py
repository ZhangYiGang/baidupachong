#!/usr/bin/env python
# coding:utf-8
'''=================================================
@Project -> File   ：test -> json_to_csv
@IDE    ：PyCharm
@Author ：zhang yigang
将有json array格式的转化为csv
@Date   ：19-7-15 上午9:12
@Desc   ：
=================================================='''
import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import  codecs

def json_to_csv(filepath):
    with open(filepath,"r") as fp:
        info = fp.read()
    json_info = json.loads(info)
    json_keys =[]
    info_array = []
    filename = filepath.split("/")[-1]
    file_suffix = filepath[filepath.index(".")+1:]
    filename = filename.replace(file_suffix, "csv")
    f = codecs.open(filename, 'wb', "gbk")
    # with open(filename, "wb") as fp:
    for index, item in enumerate(json_info):
            # info = []
            # json_dict = json.loads(item)
            json_dict = item
            # csv.register_dialect('my_csv', delimiter=' ', quoting=csv.QUOTE_NONE)
            if index == 0:
                keys = json_dict.keys()
                keys.sort()
                # [key[1:-1] for key in keys]
                json_keys.extend(keys)
                writer = csv.DictWriter(f, fieldnames=json_keys,dialect=csv.excel)
                writer.writeheader()
            else:
                 writer.writerow(json_dict)
            # for key in json_keys:
            #     info.append(json_dict[key])
            # info_array.append(info)
def testcsv(filename):
    json_to_csv(filename)
    # with open('names.csv', 'wb') as csvfile:
    #     fieldnames = ['first_name', 'last_name']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #
    #     writer.writeheader()
    #     writer.writerow({'first_name': 'Bak测试', 'last_name': 'Beans'})
    #     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})







