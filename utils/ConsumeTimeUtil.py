# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 14:49
# @Author  : zyg
# @FileName: ConsumeTimeUtil.py
# @Software: PyCharm
# 这个类主要是为了计算消耗时间
import time
def ExecuteTime(func):
    def wrapper(self, *args,**kwargs):
        func(self,*args,**kwargs)
        end_time = time.time()
        return end_time
    return wrapper

# 获取两个时间的间隔
def get_time_space(before_time):
    now_time = time.time()
    space_time =int (now_time - before_time)
    return space_time
