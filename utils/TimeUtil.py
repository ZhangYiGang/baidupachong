# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 14:49
# @Author  : zyg
# @FileName: TimeUtil.py
# @Software: PyCharm
# 这个类主要是为了计算消耗时间
import time,os,json
from utils.FileUtil import FileUtils
from config.Config  import Config
def ExecuteTime(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if result:
            end_time = time.time()
            format_time_now = TimeUtil.get_string_format(end_time)
            data = {"time": format_time_now}
            FileUtils.write_data_to_file(Config.ip_complete_time_file, json.dumps(data))
            return result

    return wrapper
class TimeUtil():

    # 获取两个时间的间隔
    @classmethod
    def get_time_space(cls,before_time):
        now_time = time.time()
        space_time = int(now_time - before_time)
        return space_time

    @classmethod
    def get_string_format(cls, timeuint):
        local_time = time.localtime(timeuint)
        format_time_now = time.strftime("%Y%m%d:%H%M%S", local_time)
        return format_time_now

    @classmethod
    def get_time_format(cls, time_format_string):
        # local_time = time.localtime(time_format_string)
        format_time_now = time.strptime(time_format_string,"%Y%m%d:%H%M%S" )
        parse_time = int(time.mktime(format_time_now))
        return parse_time

