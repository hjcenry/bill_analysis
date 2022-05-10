import math

import analysis.analysis_factory as analysis_factory
from constants import AnalysisType, OrderType, config
from util import csv_writer, matlib_drawer, file_encoding_converter
import bill_common

if __name__ == '__main__':
    # 批量转换文件编码
    file_encoding_converter.check_convert(config.get_config("file_dir", "MAIN"))

    data_list = []
    for analysts_type in AnalysisType:
        analysts = analysis_factory.create_analysts(analysts_type)
        if analysts is None:
            continue
        data_list.extend(analysts.analysis())

    out_config = config.get_config_sec("OUT")

    # bill_common.print_debug(data_list)
    # 生成总账单
    bill_common.generate_total_bill(data_list)
    # 生成占比数据图
    bill_common.generate_pie_graph(data_list)
    # 生成红包数据图
    bill_common.generate_wechat_red_packet_graph()
