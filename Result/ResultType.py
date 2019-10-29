#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 16:37
# @Author  : zyg
# @Site    : 
# @File    : ResultType.py
# @Software: PyCharm
from enum import Enum
"""
用来表示结果的类型
"""
class ResultType(Enum):
#以下三个是用来判断单个类型里面的是否
    YES = 1
    NO = 0
    UNSURE =2
#以下是判断站点类型的

#以下是判断满足类型的
#从前到后分别是是否阿拉丁 图片 音乐和视频
    ONLY_WORD = [1, 0, 0, 0 ]
    ONLY_WORD1 = [2,0,0,0]
    VIDEO_AND_WORD = [2, 1, 0, 1]
    VIDEO_AND_WORD_2 = [2, 0, 0, 1]
    MUSIC = [2,1,1,0]
    MUSIC_2 = [2,0,1,0]
    MUSIC_3 = [2,0,1,1]
    PICTURE = [2, 1,0,0]