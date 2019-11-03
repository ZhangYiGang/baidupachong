#coding=utf-8
from spider.GetTask import  GetTask
from spider.Request import  Request
from spider.FormatData import FormatData
from Result.ParseResult import ParseResult
from utils.TimeUtil import TimeUtil
from utils.FileUtil import FileUtils
from spider.GetIp import GetIp
from config.Config import Config
import sys,os,time

import traceback
import requests
reload(sys)
requests.adapters.DEFAULT_RETRIES = 5
sys.setdefaultencoding('utf-8')
ip_txt_complete = 0
ip_array = []
parse_error = "解析失败"
def execute_task_array(task_array):
    request = Request()
    searchResult = ParseResult()
    type_array = []
    result_array = []
    for single_task in task_array:
        text = request.get_baidu_text({'word': single_task})
        if text:
            formatData = FormatData()
            formatData.set_BS(text)
            # result = formatData.get_first_non_ad()
            result = formatData.get_article()
            url = formatData.get_url()
            flag_has_script = formatData.get_script()
            searchResult.set_result(result,flag_has_script)
            type = searchResult.judge_type()
            stastify_type_explain_string = searchResult.judge_satsify_type()
            url_name = searchResult.judge_url_name(url,stastify_type_explain_string)
            type_array.append(type)
            str_type = "阿拉丁" if type==2 else "自然结果"
            result_single_list = [single_task, str_type, url_name, stastify_type_explain_string]
            result_array.append(result_single_list)
            print(single_task + "类型是" + str_type + "满足类型" + stastify_type_explain_string)
        else:
            result_single_list = [single_task, parse_error, parse_error, parse_error]
            result_array.append(result_single_list)
    return  result_array
def execute_task_array_other(task_array):
    request = Request()
    searchResult = ParseResult()
    type_array = []
    result_array = []
    for single_task in task_array:
        text = request.get_baidu_text({'word': single_task})
        if text:
            formatData = FormatData()
            formatData.set_BS(text)
            # result = formatData.get_first_non_ad()
            result = formatData.get_script()
            print(single_task + "类型是" + str(result) )
def execute():
    task_manager = GetTask()
    task_manager.get_excels()
    task_dict = task_manager.get_task_singleexcel()
    if task_dict:
        task_array = task_dict.values()[0]
        # result_array = execute_task_array_other(task_array)
        result_array = execute_task_array(task_array)

    task_dict[task_dict.keys()[0]] = result_array
    task_manager.set_task_result(task_dict)
        #     这里去处理获取失败的结果



def get_ip():

    end_time_string =  Config.ip_complete_time
    space_time = TimeUtil.get_time_space(TimeUtil.get_time_format(end_time_string))
    ip_manager = GetIp()
    if space_time> Config.space_time:
        # 超过指定时间才重新获取ip
        ip_manager.get_ip_array(0)
        ip_manager.del_unfluent_ip()
    ip_array = FileUtils.get_text_from_file(FileUtils.get_project_dir()+"baiduIp.txt").split(",\n")
    Request.set_ip_array(ip_array)


if __name__=="__main__":
    try:
       Config().load_Constant()
       get_ip()
       execute()
    except Exception as e:
        traceback.print_exc(file=open('error.txt', 'a+'))


    # print "a|b".split(".")