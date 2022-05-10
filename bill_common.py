import math
import os

import analysis.analysis_factory as analysis_factory
from constants import AnalysisType, OrderType, config
from util import csv_writer, matlib_drawer
from util.sys_logger import logger


def generate_total_bill(data_list, out_dir=None, out_file=None, out_total=True):
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
    if out_total:
        content_list.append(["总账:" + str(total_in - total_out), "总收入:" + str(total_in), "总支出:" + str(total_out)])

    for content in content_list:
        logger.info(content)

    if out_dir is None and out_file is None:
        out = config.get_config("file_dir", "MAIN") + config.get_config("bill_file", "OUT")
    else:
        out = out_dir + '/' + out_file
    csv_writer.write_file(out, head_list, content_list)
    return out, round(total_in, 2), round(total_out, 2)


def generate_wechat_red_packet_graph(save_file=None, bill_files=None, absolute_path=False):
    """
    统计微信红包
    :param bill_files:
    :param absolute_path:
    :param save_file 保存的文件
    :return:
    """
    # 加载红包数据
    red_packet_analysts = analysis_factory.create_analysts(AnalysisType.WE_CHAT)
    if red_packet_analysts is None:
        return
    red_packet_data_list = red_packet_analysts.analysis(do_filter=True, bill_files=bill_files,
                                                        absolute_path=absolute_path)

    user_red_packet = {}
    for data in red_packet_data_list:
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

        receive_file_name = save_file
        if save_file is not None:
            receive_file_name = os.path.dirname(os.path.abspath(save_file)) + '/' + user + '-收红包-' + os.path.basename(
                save_file)

        matlib_drawer.draw_bar_h(receive_label_list, receive_num_list, False, user + "收红包", "金额（元）", "对方",
                                 save_file=receive_file_name)

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

        send_file_name = save_file
        if save_file is not None:
            send_file_name = os.path.dirname(
                os.path.abspath(save_file)) + '/' + user + '-' + '-发红包-' + os.path.basename(
                save_file)

        matlib_drawer.draw_bar_h(send_label_list, send_num_list, False, user + "发红包", "金额（元）", "对方",
                                 save_file=send_file_name)


def generate_pie_graph(data_list, save_file=None):
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
    matlib_drawer.draw_pie_graph(final_in_datas, "收入占比", save_file=save_file)

    # 支出数据
    final_out_datas = get_datas_to_draw_pie_graph(out_datas, other_ratio, total_out)
    matlib_drawer.draw_pie_graph(final_out_datas, "支出占比", save_file=save_file)


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


def print_debug(data_list):
    for data in data_list:
        print(data.to_string())
