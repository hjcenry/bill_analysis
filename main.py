import analysis.analysis_factory as analysis_factory
from constants import AnalysisType, OrderType
from util import csv_writer

if __name__ == '__main__':

    data_list = []
    for analysts_type in AnalysisType:
        analysts = analysis_factory.create_analysts(analysts_type)
        if analysts is None:
            continue
        data_list.extend(analysts.analysis())

    head_list = ["日期", "统计来源", "交易类型", "交易对方", "商品", "订单类型", "金额", "支付方式"]

    content_list = []

    total_out = 0
    total_in = 0
    for data in data_list:
        payment_money = data.payment_money
        if data.order_type == OrderType.IN:
            total_in += payment_money
        else:
            total_out += payment_money
            payment_money = data.payment_money * -1

        content = [data.order_date_time,
                   data.data_from.value["name"], data.payment_type, data.payment_trader,
                   data.order_goods, data.order_type.value["name"],
                   payment_money, data.payment_mode.value["name"]]
        content_list.append(content)

    content_list.append(["总账:" + str(total_in - total_out), "总收入:" + str(total_in), "总支出:" + str(total_out)])
    for content in content_list:
        print(content)

    out_file = "bills/bill.csv"
    print("开始写文件:" + out_file)
    csv_writer.write_file(out_file, head_list, content_list)
    print("写文件:" + out_file + "完成")
