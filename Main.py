from spider.GetTask import  GetTask
from spider.Request import  Request
from spider.FormatData import FormatData
def execute():
    task_array = GetTask().get_task()
    request = Request()
    for single_task in task_array:
        text = request.get_request(single_task)
        formatData = FormatData()
        formatData.set_BS(text)
        result = formatData.get_first_non_ad()
        # formatData.get_useful_judge(result)
        searchResult = SearchResult()
        searchResult.set_result(result)
        searchResult.judge_type()