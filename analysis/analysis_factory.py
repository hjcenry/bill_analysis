from analysis.boc_analysts import BocAnalysts
from analysis.cmbc_analysts import CmbcAnalysts
from analysis.wechat_analysts import WechatAnalysts
from analysis.alipay_analysts import AlipayAnalysts
from constants import AnalysisType


def create_analysts(analysis_type):
    """
    工厂方法
    :param analysis_type:
    :return:
    """
    if analysis_type is AnalysisType.WE_CHAT:
        return WechatAnalysts()
    if analysis_type is AnalysisType.ALIPAY:
        return AlipayAnalysts()
    if analysis_type is AnalysisType.CMBC:
        return CmbcAnalysts()
    if analysis_type is AnalysisType.BOC:
        return BocAnalysts()
    return None
