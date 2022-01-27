from util import csv_reader
from analysis.analysts import Analysts
from analysis.model.analysis_data import AnalysisData
from constants import AnalysisType, OrderType, PaymentMode


class WechatAnalysts(Analysts):
    """
    微信账单分析
    """

    def __init__(self):
        pass

    def do_analysis_action(self):
        order_list = []
        # 读出所有文件
        for file_path in self.get_analysts_type().value["files"]:
            order_list.extend(csv_reader.read_file(file_path))

        analysis_datas = []
        for order in order_list:
            # 交易时间
            order_date_time = order[0].strip()
            # 交易类型
            payment_type = order[1].strip()
            # 交易对方
            payment_trader = order[2].strip()
            # 商品
            order_goods = "" if order[3].strip() == "/" else order[3]
            # 订单类型：收/支
            order_type = OrderType.value_of_tag(order[4].strip())
            # 金额(元)
            payment_money = float(order[5].strip().strip("¥"))
            # 支付方式
            payment_mode = PaymentMode.value_of_tag(order[6].strip())

            analysis_data = AnalysisData(order_date_time, payment_type, payment_trader, order_goods, order_type,
                                         payment_money, payment_mode)
            analysis_datas.append(analysis_data)

        return analysis_datas

    def get_analysts_type(self):
        return AnalysisType.WE_CHAT
