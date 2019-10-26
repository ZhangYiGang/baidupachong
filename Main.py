#coding=utf-8
from spider.GetTask import  GetTask
from spider.Request import  Request
from spider.FormatData import FormatData
from Result.ParseResult import ParseResult
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def execute():
    task_array = GetTask().get_task()
    request = Request()
    searchResult = ParseResult()
    type_array = []
    for single_task in task_array:
        text = request.get_baidu_text({'word':single_task})
        formatData = FormatData()
        formatData.set_BS(text)
        result = formatData.get_first_non_ad()
        # formatData.get_useful_judge(result)
        searchResult.set_result(result)
        type = searchResult.judge_type()
        type_array.append(type)
        print(single_task+"类型是"+str(type))
    print type_array
    print len(type_array)
if __name__=="__main__":
    execute()
    # print "a|b".split(".")