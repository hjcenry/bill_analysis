from datetime import datetime

from analysis.analysts import Analysts
from analysis.model.analysis_data import AnalysisData
from constants import AnalysisType, OrderType, PaymentMode


class CmbcAnalysts(Analysts):
    """
    招商银行账单分析
    """

    def __init__(self):
        super().__init__()
        self.cut_pre_row = 8
        self.cut_end_row = 3

    def convert_order_to_analysis_data(self, order):
        if order[6].strip() == "转账   何金成":
            # 自己给自己的交易不做记录
            return None

        # 交易时间
        order_date_time = order[0].strip() + order[1].strip()
        datetime_object = datetime.strptime(order_date_time, '%Y%m%d%H:%M:%S')
        order_date_time = datetime_object.strftime("%Y/%m/%d")
        # 交易类型
        payment_type = order[5].strip()
        # 交易对方
        payment_trader = ""
        # 商品
        order_goods = order[6].strip()

        if order[2].strip() is not None and order[2].strip() != "":
            # 订单类型：收/支
            order_type = OrderType.IN
            # 金额(元)
            payment_money = float(order[2].strip())
        else:
            # 订单类型：收/支
            order_type = OrderType.OUT
            # 金额(元)
            payment_money = float(order[3].strip())

        # 支付方式
        payment_mode = PaymentMode.CMBC_BANK_1436

        return AnalysisData(order_date_time, self.get_analysts_type(), payment_type, payment_trader, order_goods,
                            order_type, payment_money, payment_mode)

    def get_analysts_type(self):
        return AnalysisType.CMBC
