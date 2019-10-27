#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 09:57
# @Author  : zyg
# @Site    : 
# @File    : SearchResult.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from ResultException import ResultException
from utils.FileUtil import  FileUtils
from spider.FormatData import FormatData
from Result.ResultType import ResultType
import json
import os,re
class ParseResult():
    """
    @:param type 表示处理结果类型 0:未知 1:自然结果 2:阿拉丁
    """
    def __init__(self):
        self.type = 0
        # Result/alading
        abs_path = os.path.abspath(__file__)
        project_path =abs_path[0:abs_path.index("Result")]
        alading_file = project_path+"Result"+os.sep+"alading.json"
        satisfy_file = project_path + "Result" + os.sep + "satisfy.json"
        self.judge_json = json.loads(FileUtils.get_text_from_file(alading_file))
        self.satisfy_json = json.loads(FileUtils.get_text_from_file(satisfy_file))

    def get_type(self):
        return self.type

    """
        @:param text 处理得到的结果
    """
    def set_result(self, result):
        self.parse = result
        # 顺便清除所有数据，主要是类型
        self.type = 0
        self.picture_type = 0


    #从json里面获取数据，如果一个都没有的话，则认为它不是阿拉丁
    def judge_type(self):
        has_judge_flag = False
        for html_label,css_dict in self.judge_json.items():
            for items in css_dict.items():
                #从alading.json里面取数据，json的每一个key只能对应一个value，但是一个key需要对应多个value时，那就分隔开
                for every_value in items[1].split("|"):
                    attrs_dict = {items[0]: every_value}
                    item_result = self.parse.find(html_label, attrs=attrs_dict)
                    if item_result is not None:
                        has_judge_flag = True
                        print(attrs_dict)
                        break

        if has_judge_flag is True:
            self.type = 2
        else:
            self.type = 1
        return self.type

    '''
   对于音乐||视频类型的判断，只有大多数命中时才认为它是 
   @:param type 类型，是音乐还是视频
    '''
    def judge_media_type(self, type):
        # 从satisfy——json的数据里面读取是否满足
        flag_count = 0
        has_satisfy_count = 0
        type_json = self.satisfy_json[type]
        for html_label,css_dict in type_json.items():
            # html_label是前面的span或者div，cssdict是类型
            for items in css_dict.items():
                for every_value in items[1].split("|"):
                    flag_count +=1
                    if items[0]=="text":
                        item_result = self.parse.find_all(re.compile(html_label))
                        item_result = self.search_text(item_result, every_value)
                        # item_result = self.parse.find_all(text= re.compile(every_value.encode("utf-8")))
                        # item_result = self.parse.find_all(html_label, text=re.compile(r".*"+ every_value+r".*"))
                        # item_result = self.parse.find_all(re.compile(r".*"+ every_value+r".*"))

                    else:
                        attrs_dict = {items[0]: every_value}
                        item_result = self.parse.find(html_label, attrs=attrs_dict)

                    if item_result:
                        has_satisfy_count+=1
                        continue
                        # break
        print has_satisfy_count,flag_count

    """
    判断类型里面是否有视频，图片，歌曲等
    只有在阿拉丁形式下才会判断有没有视频和歌曲等
    """
    def get_satsify_type(self):

        self.judge_picture_type()
        if self.type ==2:
            has_music_flag = self.judge_media_type("music")
            has_video_flag = self.judge_media_type("video")


    def judge_picture_type(self):
        img_results = self.parse.find_all(re.compile(r"img.*"))
        pic_related_json = self.satisfy_json["pic"]
        dir = pic_related_json["dir"]
        big_size = pic_related_json["bigSize"]
        small_size = pic_related_json["smallSize"]
        size_list = []
        for img_result in img_results:
            url = img_result.attrs["src"]
            img_path = FileUtils.download_from_url(url, dir)
            img_size = FileUtils.get_file_size(img_path)
            size_list.append( img_size>= big_size and ResultType.YES or  img_size<= small_size and ResultType.NO  or {ResultType.UNSURE:img_size}  )
        middle_type_count = 0
        for result_type in size_list:
                if result_type == ResultType.YES:
                    self.picture_type = 1
                    break
                elif result_type == ResultType.NO:
                    continue
                else:
                    middle_type_count+=1
        #         中等图片个数大于1也认为是图文模式
        if self.picture_type ==0 and middle_type_count>1:
            self.picture_type =1
        return self.picture_type

    '''
    搜寻需要的文本
    '''
    def search_text(self, results, every_value):
        for result in results:
            text =result.text
            result = re.compile(every_value).match(text)
            if result:
              return result.group(0)
        return None

    # 获取到url
    def get_url(self):
        # 第一个获取到的url
        url_array= []
        try:
            data_log = self.parse.attrs["data-log"]
            html_json = data_log.encode("utf-8").replace("\'","\"")
            url_data_log = json.loads(html_json)["mu"]
            url_array.append(url_data_log)
        except Exception as e:
            # 在这里处理json的解析问题
            pass
        content = self.parse.find("div",attrs={"class":"c-result-content"})
        if content:
            # 取出第一个内容
            content = next(content.children)
            if "rl-link-href" in content.attrs:
               url_data_href = content.attrs["rl-link-href"]
               print url_data_href
        else:
            # tood 这里要加的是找到url
            pass
        pass


if __name__ == '__main__':
    text = FileUtils.get_text_from_file("../picture.html")
    formatData = FormatData()
    formatData.set_BS(text)
    result = formatData.get_first_non_ad()
    # formatData.get_useful_judge(result)
    searchResult = ParseResult()
    searchResult.set_result(result)
    # print searchResult.judge_picture_type()
    print searchResult.get_url()

