import csv


def read_file(file_path):
    """
    读取文件
    :param file_path:
    :return: list
    """
    csv_file = open(file_path, "r", encoding='utf-8')
    reader = csv.reader(csv_file)
    item_list = []
    for item in reader:
        # 前18行都是标题
        if reader.line_num < 18:
            continue
        item_list.append(item)

    csv_file.close()
    return item_list
