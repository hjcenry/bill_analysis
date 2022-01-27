from enum import Enum


# 订单类型
class OrderType(Enum):
    # 收入
    IN = {
        "tags": ["收入"]
    }
    # 支出
    OUT = {
        "tags": ["支出"]
    }
    # 其他
    DEFAULT = {
        "tags": ["其他"]
    }

    @staticmethod
    def value_of_tag(tag):
        for member in OrderType:
            if tag in member.value["tags"]:
                return member
        return OrderType.DEFAULT


# 支付方式
class PaymentMode(Enum):
    # 微信零钱
    WECHAT_CRASH = {
        "tags": ["零钱"]
    }
    # 招商银行1436
    CMBC_BANK_1436 = {
        "tags": ["招商银行(1436)"]
    }
    # 招商银行8599
    CMBC_BANK_8599 = {
        "tags": ["招商银行(8599)", "招商银行信用卡(8599)"]
    }
    # 支付宝花呗
    ALIPAY_HUA_BEI = {
        "tags": ["花呗", "花呗&现金抵价券"]
    }
    # 余额宝
    ALIPAY_YUE_BAO = {
        "tags": ["余额宝"],
    }
    # 其他
    DEFAULT = {
        "tags": ["其他"]
    }

    @staticmethod
    def value_of_tag(tag):
        for member in PaymentMode:
            if tag in member.value["tags"]:
                return member
        return PaymentMode.DEFAULT


# 分析类型
class AnalysisType(Enum):
    # 微信
    WE_CHAT = {
        "files": ["F:/project/bill_analysis/bills/wechat.csv"]
    }
    # 支付宝
    ALIPAY = {
        "files": ["F:/project/bill_analysis/bills/alipay.csv"]
    }
