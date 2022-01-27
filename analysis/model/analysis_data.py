import json

from constants import OrderType, PaymentMode


class AnalysisData(object):

    def __init__(self, order_date_time: str, payment_type: str, payment_trader: str, order_goods: str,
                 order_type: OrderType, payment_money: float, payment_mode: PaymentMode):
        """
        初始订单数据
        :param order_date_time:交易时间
        :param payment_type:交易类型
        :param payment_trader:交易对方
        :param order_goods:商品
        :param order_type:订单类型：收/支
        :param payment_money:金额(元)
        :param payment_mode:支付方式
        """
        # 交易时间
        self.order_date_time = order_date_time
        # 交易类型
        self.payment_type = payment_type
        # 交易对方
        self.payment_trader = payment_trader
        # 商品
        self.order_goods = order_goods
        # 订单类型：收/支
        self.order_type = order_type
        # 金额(元)
        self.payment_money = payment_money
        # 支付方式
        self.payment_mode = payment_mode

    def to_string(self):
        return self.__dict__
