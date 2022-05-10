import os
from abc import abstractmethod

from constants import config, FilterOperator
from util import csv_reader, file_encoding_converter
from util.sys_logger import logger


class Analysts:

    def __init__(self):
        self.config = config.get_config_sec(self.get_analysts_type().name)

    def load_file(self, bill_files=None, bill_file_dir=None, absolute_path=False):
        """
        加载文件
        :param bill_files:
        :param bill_file_dir:
        :param absolute_path:
        :return:
        """
        user_order_map = {}
        # 读出所有文件
        files = bill_files
        if files is None:
            files = self.config["files"].split(";")

        file_dir = bill_file_dir
        if file_dir is not None:
            file_dir = config.get_config("file_dir", "MAIN")

        for file_path in files:
            if len(file_path) == 0:
                continue
            if not absolute_path:
                file_path = file_dir + file_path

            if not os.path.exists(file_path):
                logger.error("[" + file_path + "]不存在，请检查路径!!!")
                continue

            file_name = os.path.basename(file_path)

            # 用户，默认空
            user_name = " "
            if "-" in file_name:
                # 文件名中取名字
                user_name = file_name.split("-")[0]
                if "/" in user_name:
                    user_name = user_name.rsplit("/", 1)[1]

            if user_name in user_order_map:
                order_list = user_order_map[user_name]
            else:
                user_order_map[user_name] = []
                order_list = user_order_map[user_name]

            # 批量转换文件编码
            file_encoding_converter.change_to_utf_file(file_path, '.csv')

            order_list.extend(csv_reader.read_file(file_path, self.cut_pre_row, self.cut_end_row))

        return user_order_map

    def analysis(self, do_filter=True, bill_files=None, bill_file_dir=None, absolute_path=False):
        """
        分析
        :param do_filter:
        :param bill_files: 文件
        :param bill_file_dir: 文件目录
        :param absolute_path: 是否是绝对路径
        :return:
        """
        user_order_map = self.load_file(bill_files=bill_files, bill_file_dir=bill_file_dir, absolute_path=absolute_path)

        analysis_datas = []

        for user in user_order_map:
            order_list = user_order_map[user]

            for order in order_list:
                if do_filter and not self.filter(order):
                    # 过滤处理
                    continue

                analysis_data = self.convert_order_to_analysis_data(order)
                if analysis_data is None:
                    continue

                analysis_data.set_user(user)
                analysis_datas.append(analysis_data)

        return analysis_datas

    def filter(self, order):
        """
        过滤关键字
        :param order:
        :return:
        """
        ignore_filters = self.config["ignore_filters"]
        if ignore_filters is None or ignore_filters == "":
            return True

        for ignore_filter in ignore_filters.split(";"):
            if ignore_filter is None or ignore_filter == "":
                continue

            # 遍历每一个判断条件，某一个满足，就return True
            filt_result = False
            for self_filter in ignore_filter.split("&&"):
                if self_filter is None or self_filter == "":
                    continue

                # 判断所有条件都满足，这个子条件才算满足
                filters = self_filter.split("|")
                if len(filters) != 3:
                    continue
                col = filters[0]
                symbol = filters[1]
                content = filters[2]

                operator = FilterOperator.value_of_symbol(symbol)
                if not operator.match(content, order[int(col)].strip()):
                    filt_result = True
                    break

            if not filt_result:
                return False

        return True

    @abstractmethod
    def convert_order_to_analysis_data(self):
        """
        分析行为
        :return:AnalysisData
        """
        pass

    @abstractmethod
    def get_analysts_type(self):
        """
        获取分析类型
        :return:
        """
        pass
