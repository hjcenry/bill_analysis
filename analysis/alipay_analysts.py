from analysis.analysts import Analysts
from analysis.model.analysis_data import AnalysisData
from constants import AnalysisType, OrderType, PaymentMode


class AlipayAnalysts(Analysts):
    """
    支付宝账单分析
    """

    def __init__(self):
        super().__init__()
        self.cut_pre_row = 2
        self.cut_end_row = 21

    def convert_order_to_analysis_data(self, order):
        # 交易时间
        order_date_time = order[10].split(" ")[0]
        # 交易类型
        payment_type = order[7].strip()
        # 交易对方
        payment_trader = order[1].strip()
        # 商品
        order_goods = "" if order[3].strip() == "/" else order[3].strip()
        # 订单类型：收/支
        order_type = OrderType.value_of_tag(order[0].strip())
        if order_type == OrderType.DEFAULT:
            # 支付的其他收入计算
            return None
        # 金额(元)
        payment_money = float(order[5].strip())
        # 支付方式
        payment_mode = PaymentMode.value_of_tag(order[4].strip())

        return AnalysisData(order_date_time, self.get_analysts_type(), payment_type, payment_trader, order_goods,
                            order_type, payment_money, payment_mode)

    def get_analysts_type(self):
        return AnalysisType.ALIPAY
