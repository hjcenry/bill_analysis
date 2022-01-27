from analysis.analysts import Analysts
from constants import AnalysisType


class AlipayAnalysts(Analysts):
    """
    支付宝账单分析
    """

    def __init__(self):
        pass

    def do_analysis_action(self):
        pass

    def get_analysts_type(self):
        return AnalysisType.ALIPAY
