# coding:utf-8

import matplotlib.pyplot as plt
from matplotlib import font_manager


def draw_pie_graph(datas: dict, data_title: str, save_file=None):
    """
    绘制饼图
    :param data_title:
    :param datas: 数据
    :param save_file: 保存文件
    oses = {
        'windows7': 60.86,
        'windows10': 18.46,
        'window8': 3.61,
        'windows xp': 10.3,
        'mac os': 6.78,
        '其他': 1.12
    }
    :return:
    """
    patches, texts, autotexts = plt.pie(datas.values(), autopct="%.2f%%", labels=datas.keys(), shadow=True)

    plt.rcParams['font.sans-serif'] = ['simhei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    for autotext in autotexts:
        # 设置分块的比例文字文字为白色
        autotext.set_color("w")
        # 设置分块的比例文字文字大小
        autotext.set_size(10)
    plt.title(data_title)
    if save_file is None:
        plt.show()
    else:
        plt.savefig(save_file)
    plt.clf()


def draw_bar_h(label_list: list, num_list: list, show_number: bool, data_title: str, x_label: str, y_label: str,
               save_file=None):
    fig, ax = plt.subplots(figsize=(20, 12))
    ax.barh(label_list, num_list)

    if show_number:
        for x, y in zip(label_list, num_list):
            ax.text(y + 0.05, x, y, fontsize=10, horizontalalignment='center')

    plt.title(data_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.rcParams['font.sans-serif'] = ['simhei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    if save_file:
        plt.savefig(save_file)
    else:
        plt.show()
    plt.clf()


def draw_bar(label_list: list, num_list: list, show_number: bool, data_title: str, x_label: str, y_label: str,
             save_file=None):
    """
    绘制柱状图
    :param label_list: 标签list
    :param num_list: 数字list
    :param show_number: 是否展示数字
    :param data_title: 标题
    :param x_label: x坐标文字
    :param y_label: y坐标文字
    :param save_file: 保存文件
    :return:
    """
    font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf", size=10)
    fig, ax = plt.subplots(figsize=(10, 6), textprops={"fontproperties": font})
    ax.bar(label_list, num_list)

    if show_number:
        for x, y in zip(label_list, num_list):
            ax.text(x, y + 0.05, y, fontsize=14, horizontalalignment='center')

    plt.title(data_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.rcParams['font.sans-serif'] = ['simhei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    if save_file:
        plt.savefig(save_file)
    else:
        plt.show()
    plt.clf()
