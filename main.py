import math

import analysis.analysis_factory as analysis_factory
from constants import AnalysisType, OrderType, config
from util import csv_writer, matlib_drawer, file_encoding_converter


def generate_total_bill():
    head_list = ["日期", "统计来源", "统计渠道", "交易类型", "交易对方", "商品", "订单类型", "金额", "支付方式"]
    content_list = []
    # 总支出
    total_out = 0
    # 总收入
    total_in = 0

    for data in data_list:
        payment_money = data.payment_money
        if data.order_type == OrderType.IN:
            total_in += payment_money
        else:
            total_out += payment_money
            payment_money = data.payment_money * -1

        content = [data.order_date_time, data.user, data.data_from.value["name"], data.payment_type,
                   data.payment_trader, data.order_goods, data.order_type.value["name"], payment_money,
                   data.payment_mode.value["name"]]
        content_list.append(content)
    content_list.append(["总账:" + str(total_in - total_out), "总收入:" + str(total_in), "总支出:" + str(total_out)])
    for content in content_list:
        print(content)

    out_file = config.get_config("file_dir", "MAIN") + out_config["bill_file"]
    print("开始写文件:" + out_file)
    csv_writer.write_file(out_file, head_list, content_list)
    print("写文件:" + out_file + "完成")


def generate_wechat_red_packet_graph():
    """
    统计微信红包
    :return:
    """
    user_red_packet = {}
    for data in data_list:
        # 过滤出红包数据
        if "微信红包" not in data.payment_type or "退款" in data.payment_type:
            continue

        user = data.user

        # 第一个是收，第二个是发
        if user not in user_red_packet:
            user_red_packet[user] = [{}, {}]
        red_packet = user_red_packet[user]

        receive_packet = red_packet[0]
        send_packet = red_packet[1]
        trader = data.payment_trader
        payment_money = math.fabs(data.payment_money)

        if data.order_type == OrderType.IN:
            # 收红包
            receive_packet[trader] = float(receive_packet[trader]) + payment_money \
                if trader in receive_packet \
                else payment_money
        else:
            # 发红包
            trader = trader[2: len(trader)]
            send_packet[trader] = float(send_packet[trader]) + payment_money \
                if trader in send_packet \
                else payment_money

    for user in user_red_packet:
        red_packet = user_red_packet[user]
        # 收红包
        receive_packet = red_packet[0]
        receive_label_list = []
        receive_num_list = []
        for data in sorted(receive_packet.items(), key=lambda kv: (kv[1], kv[0])):
            trader = data[0]
            if trader in user:
                # 排除自己人
                continue

            payment_money = float('%.2f' % data[1])

            receive_label_list.append(trader + " - " + str(payment_money))
            receive_num_list.append(payment_money)
        matlib_drawer.draw_bar_h(receive_label_list, receive_num_list, False, user + "收红包", "金额（元）", "对方")

        # 发红包
        send_packet = red_packet[1]
        send_label_list = []
        send_num_list = []
        for data in sorted(send_packet.items(), key=lambda kv: (kv[1], kv[0])):
            trader = data[0]
            if trader in user:
                # 排除自己人
                continue

            payment_money = float('%.2f' % data[1])

            send_label_list.append(trader + " - " + str(payment_money))
            send_num_list.append(payment_money)
        matlib_drawer.draw_bar_h(send_label_list, send_num_list, False, user + "发红包", "金额（元）", "对方")


def generate_pie_graph():
    # 多少比例以下归为其他
    other_ratio = 2
    # 总支出
    total_out = 0
    # 总收入
    total_in = 0

    # 收入数据
    in_datas = {}
    # 支出数据
    out_datas = {}

    for data in data_list:
        payment_money = data.payment_money
        if data.order_type == OrderType.IN:
            total_in += payment_money
        else:
            total_out += payment_money
            payment_money = data.payment_money * -1

        if data.order_type == OrderType.IN:
            payment_datas = in_datas
        else:
            payment_datas = out_datas

        # 累计数据
        payment_type = data.payment_type

        if payment_type in payment_datas:
            payment_datas[payment_type] = float(payment_datas[payment_type]) + payment_money
        else:
            payment_datas[payment_type] = payment_money

    # 收入数据
    final_in_datas = get_datas_to_draw_pie_graph(in_datas, other_ratio, total_in)
    matlib_drawer.draw_pie_graph(final_in_datas, "收入占比")

    # 支出数据
    final_out_datas = get_datas_to_draw_pie_graph(out_datas, other_ratio, total_out)
    matlib_drawer.draw_pie_graph(final_out_datas, "支出占比")


def get_datas_to_draw_pie_graph(datas, other_ratio, total):
    final_datas = {}
    final_remain_ratio = 100
    final_remain_money = 0
    for data in sorted(datas.items(), key=lambda kv: (kv[1], kv[0])):
        payment_type = data[0]
        payment_money = float('%.2f' % math.fabs(data[1]))

        ratio = 0 if total == 0 else payment_money / total * 100
        if ratio <= other_ratio:
            final_remain_money = final_remain_money + payment_money
            continue
        ratio = float('%.2f' % ratio)

        final_datas[payment_type + " - " + str(payment_money)] = ratio
        final_remain_ratio = final_remain_ratio - ratio

    if final_remain_ratio > 0:
        final_remain_ratio = float('%.2f' % final_remain_ratio)
        final_remain_money = float('%.2f' % final_remain_money)
        final_datas["其他 - " + str(final_remain_money)] = final_remain_ratio

    return final_datas


def print_debug():
    for data in data_list:
        print(data.to_string())


if __name__ == '__main__':

    # 批量转换文件编码
    file_encoding_converter.check_convert(config.get_config("file_dir", "MAIN"))

    data_list = []
    for analysts_type in AnalysisType:
        analysts = analysis_factory.create_analysts(analysts_type)
        if analysts is None:
            continue
        data_list.extend(analysts.analysis())

    out_config = config.get_config_sec("OUT")

    # print_debug()
    # 生成总账单
    generate_total_bill()
    # 生成占比数据图
    generate_pie_graph()
    # 生成红包数据图
    generate_wechat_red_packet_graph()
