from abc import abstractmethod

from util import csv_reader
from constants import config, AnalysisType, FilterOperator


class Analysts:

    def __init__(self):
        self.config = config.get_config_sec(self.get_analysts_type().name)

    def load_file(self):
        """
        加载文件
        :return:
        """
        order_list = []
        # 读出所有文件
        files = self.config["files"]

        for file_path in files.split(";"):
            if file_path is None or file_path == "":
                continue
            order_list.extend(csv_reader.read_file(file_path, self.cut_pre_row, self.cut_end_row))
        return order_list

    def analysis(self):
        """
        分析
        :return:
        """
        order_list = self.load_file()

        analysis_datas = []
        for order in order_list:
            if not self.filter(order):
                continue

            analysis_data = self.convert_order_to_analysis_data(order)
            if analysis_data is None:
                continue
            analysis_datas.append(analysis_data)

        return analysis_datas

    def filter(self, order):
        ignore_filters = self.config["ignore_filters"]
        if ignore_filters is None or ignore_filters == "":
            return True
        for ignore_filter in ignore_filters.split(";"):
            if ignore_filter is None or ignore_filter == "":
                continue
            filters = ignore_filter.split("|")
            if len(filters) != 3:
                return True
            col = filters[0]
            symbol = filters[1]
            content = filters[2]

            operator = FilterOperator.value_of_symbol(symbol)
            if operator.match(content, order[int(col)].strip()):
                return False
        return True

    @abstractmethod
    def convert_order_to_analysis_data(self):
        """
        分析行为
        :return:AnalysisData list
        """
        pass

    @abstractmethod
    def get_analysts_type(self):
        """
        获取分析类型
        :return:
        """
        pass
