# coding utf-8
import os
import chardet
from util.sys_logger import logger


# 获得所有文件的路径,传入根目录路径
def find_all_file(path: str, ext: str) -> str:
    for root, dirs, files in os.walk(path):
        for f in files:
            if ext is not None and f.endswith(ext):
                fullname = os.path.join(root, f)
                yield fullname
            pass
        pass
    pass


# 判断是不是utf-8编码方式
def judge_coding(path: str) -> dict:
    with open(path, 'rb') as f:
        content = f.read()[0:1024]
        c = chardet.detect(content)

    with open(path, 'r', encoding=c["encoding"]) as f:
        try:
            f.read()[0:1024]
            # 能正常读取，直接返回这个编码
            return c["encoding"]
        except Exception as e:
            # 实在不行，用我的遍历try大法
            return try_get_coding(path)


# 挨个尝试编码，下下策
def try_get_coding(file_path):
    file_list = ['gbk', 'gb2312', 'utf-8', 'utf-8-sig', 'utf-16', 'utf-16-sig']
    for coding in file_list:
        with open(file_path, 'r', encoding=coding) as f:
            try:
                f.read()[0:1024]
                return coding
            except Exception as e:
                continue
    return None


# 修改文件编码方式
def change_to_utf_file(file: str, ext: str):
    c = judge_coding(file)
    change(file, c if c is not None else "utf-8")
    if c is not None and c != 'utf-8':
        logger.info("{} 编码方式已从{}改为 utf-8".format(file, c))


# 修改文件编码方式
def change_to_utf_files(path: str, ext: str):
    for i in find_all_file(path, ext):
        change_to_utf_file(i)
        c = judge_coding(i)
        change(i, c if c is not None else "utf-8")
        if c is not None and c != 'utf-8':
            logger.info("{} 编码方式已从{}改为 utf-8".format(i, c))


def change(path: str, coding: str):
    if coding is None:
        return
    if coding == 'utf-8':
        return
    text = None
    with open(path, 'r', encoding=coding) as f:
        try:
            text = f.read()
        except Exception as e:
            try_get_coding(path)

    if text is not None:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)


# 查看所有文件编码方式
def check(path: str, ext: str):
    for i in find_all_file(path, ext):
        with open(i, 'rb')[0:1024] as f:
            logger.info(chardet.detect(f.read())['encoding'], ': ', i)


def check_convert(path):
    ext = ".csv"
    change_to_utf_files(path, ext)
