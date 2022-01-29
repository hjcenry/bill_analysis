import csv


def read_file(file_path, cut_pre_row, cut_end_row):
    """
    读取文件
    :param cut_pre_row:
    :param cut_end_row:
    :param file_path:
    :return: list
    """
    csv_file = open(file_path, "r", encoding='utf-8')
    reader = csv.reader(csv_file)

    cut_pre_row = cut_pre_row if cut_pre_row is not None else 0
    cut_end_row = cut_end_row if cut_end_row is not None else 0

    item_list = []

    for item in reader:
        # 去掉标题行
        if reader.line_num <= cut_pre_row:
            continue
        item_list.append(item)

    # 去掉尾行
    for i in range(len(item_list) - 1, len(item_list) - cut_end_row - 1, -1):
        item_list.remove(item_list[i])

    csv_file.close()
    return item_list
