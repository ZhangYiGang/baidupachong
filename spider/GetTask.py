from utils.get_info_from_excel import myexcel


class GetTask():
    def __int__(self):
        self.task_array = []
    def get_task(self):
        excel = myexcel()
        excel.load_excel("part1.xlsx")
        json_array = excel.get_excel_array()
        need_key = excel.get_excel_key(1)
        for every_json in json_array:
            value_to_key = every_json[need_key]
            self.task_array.append(value_to_key)