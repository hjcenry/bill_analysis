import csv


def write_file(file_path, head_list: list, content_list: list):
    """
    写入文件
    :param file_path:
    :param head_list:
    :param content_list:
    :return:
    """
    f = open(file_path, 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(head_list)
    csv_writer.writerows(content_list)
    f.close()
