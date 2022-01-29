import configparser
import json


class Config(object):
    # 配置信息
    config_dict: None

    def __init__(self, file_path):
        cf = configparser.RawConfigParser()
        cf.read(file_path, encoding='utf-8')
        secs = cf.sections()
        config_dict = {}
        for sec in secs:
            items = cf.items(sec)
            item_dict = {}
            for item in items:
                item_dict[item[0]] = item[1]
            config_dict[sec] = item_dict

        self.config_dict = config_dict

    def get_config(self, key, sec):
        """
        获取配置
        :param key:
        :param sec:
        :return:
        """
        if sec is not None and sec in self.config_dict:
            return self.config_dict[sec][key]
        else:
            for (k, v) in self.config_dict:
                if key in v:
                    return v[key]
            return None

    def get_config_sec(self, sec):
        """
        获取配置
        :param sec:
        :return:
        """
        if sec is not None and sec in self.config_dict:
            return self.config_dict[sec]
        else:
            return {}

    def get_config_dict(self):
        """
        获取配置dict
        :return:
        """
        return self.config_dict
