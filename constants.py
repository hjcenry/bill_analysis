from enum import Enum
from analysis.config.config import Config

config = Config('analysis/config/config.ini')


# 订单类型
class OrderType(Enum):
    # 收入
    IN = {
        "name": "收入",
        "tags": ["收入"]
    }
    # 支出
    OUT = {
        "name": "支出",
        "tags": ["支出"]
    }
    # 其他
    DEFAULT = {
        "name": "其他",
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
        "name": "微信零钱",
        "tags": ["零钱"]
    }
    # 招商银行
    CMBC_BANK = {
        "name": "招商银行",
        "tags": ["招商银行(1436)", "招商银行储蓄卡(1436)", "招商银行(1832)", "招商银行储蓄卡(1832)"]
    }
    # 招商银行信用卡
    CMBC_BANK_CREDIT = {
        "name": "招商银行信用卡",
        "tags": ["招商银行(8599)", "招商银行信用卡(8599)"]
    }
    # 中国银行
    BOC_BANK = {
        "name": "中国银行",
        "tags": ["中国银行(5763)"]
    }
    # 支付宝花呗
    ALIPAY_HUA_BEI = {
        "name": "花呗",
        "tags": ["花呗", "花呗&现金抵价券"]
    }
    # 余额宝
    ALIPAY_YUE_BAO = {
        "name": "余额宝",
        "tags": ["余额宝"],
    }
    # 其他
    DEFAULT = {
        "name": "其他",
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
    WE_CHAT = {"name": "微信"}
    # 支付宝
    ALIPAY = {"name": "支付宝"}
    # 招商银行
    CMBC = {"name": "招商银行"}
    # 中国银行
    BOC = {"name": "中国银行"}


# 过滤操作
class FilterOperator(Enum):
    # 精确匹配
    EXACT = {
        "symbol": "="
    }
    # 精确匹配不相等
    NOT_EQUAL = {
        "symbol": "!="
    }
    # 开头
    START_WITH = {
        "symbol": "start"
    }
    # 结尾
    END_WITH = {
        "symbol": "end"
    }
    # 包含
    CONTAINS = {
        "symbol": "has"
    }

    @staticmethod
    def value_of_symbol(symbol):
        for member in FilterOperator:
            if symbol == member.value["symbol"]:
                return member
        return FilterOperator.EXACT

    def match(self, content: str, target: str):
        if self == FilterOperator.EXACT:
            return target == content
        if self == FilterOperator.NOT_EQUAL:
            return target != content
        if self == FilterOperator.START_WITH:
            return target.startswith(content)
        if self == FilterOperator.END_WITH:
            return target.endswith(content)
        if self == FilterOperator.CONTAINS:
            return target.__contains__(content)
