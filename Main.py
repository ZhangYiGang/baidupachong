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
import requests
reload(sys)
requests.adapters.DEFAULT_RETRIES = 5
sys.setdefaultencoding('utf-8')
ip_txt_complete = 0
ip_array = []
def execute():
    task_array = GetTask().get_task()
    request = Request()
    searchResult = ParseResult()
    type_array = []
    for single_task in task_array:
        text = request.get_baidu_text({'word':single_task})
        if text:
            formatData = FormatData()
            formatData.set_BS(text)
            # result = formatData.get_first_non_ad()
            result = formatData.get_article()
            searchResult.set_result(result)
            type = searchResult.judge_type()
            stastify_type_explain_string = searchResult.judge_satsify_type()
            type_array.append(type)
            print(single_task + "类型是" + str(type)+"满足类型"+stastify_type_explain_string)
        else:
            pass
    #     这里去处理获取失败的结果

    print(type_array)
    print(len(type_array))

def get_ip():

    end_time_string =  Config.ip_complete_time
    space_time = TimeUtil.get_time_space(TimeUtil.get_time_format(end_time_string))
    if space_time> Config.space_time:
        # 超过指定时间才重新获取ip
        GetIp().get_ip_array(0)
    ip_array = FileUtils.get_text_from_file(FileUtils.get_project_dir()+"baiduIp.txt").split(",\n")
    Request.set_ip_array(ip_array)


if __name__=="__main__":
    Config().load_Constant()
    get_ip()
    execute()

    # print "a|b".split(".")