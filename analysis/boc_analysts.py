from analysis.analysts import Analysts
from analysis.model.analysis_data import AnalysisData
from constants import AnalysisType, OrderType, PaymentMode


class BocAnalysts(Analysts):
    """
    中国银行账单分析
    """

    def __init__(self):
        super().__init__()
        self.cut_pre_row = 0
        self.cut_end_row = 0

    def convert_order_to_analysis_data(self, order):
        # 交易时间
        order_date_time = order[0].strip()
        # 交易类型
        payment_type = order[1].strip()
        # 交易对方
        payment_trader = order[2].strip()
        # 商品
        order_goods = ""

        if order[6].strip() is not None and order[6].strip() != "":
            # 订单类型：收/支
            order_type = OrderType.IN
            # 金额(元)
            payment_money = float(order[6].strip().replace(",", ""))
        else:
            # 订单类型：收/支
            order_type = OrderType.OUT
            # 金额(元)
            payment_money = float(order[7].strip().replace(",", ""))

        # 支付方式
        payment_mode = PaymentMode.BOC_BANK_5763

        return AnalysisData(order_date_time, self.get_analysts_type(), payment_type, payment_trader, order_goods,
                            order_type, payment_money, payment_mode)

    def get_analysts_type(self):
        return AnalysisType.BOC
