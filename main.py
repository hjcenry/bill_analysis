import analysis.analysis_factory as analysis_factory
from constants import AnalysisType

if __name__ == '__main__':
    # 微信分析
    wechat_analysts = analysis_factory.create_analysts(AnalysisType.WE_CHAT)

    analysis_datas = wechat_analysts.do_analysis_action()

    for data in analysis_datas:
        print(data.to_string())
