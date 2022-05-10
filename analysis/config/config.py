import configparser


class Config(object):
    # 配置信息
    config_dict: None

    def __init__(self, file_path):
        self.file_path = file_path
        self.cf = configparser.RawConfigParser()
        self.reload(file_path)

    def reload(self, file_path):
        """
        重载配置文件
        :param file_path:
        :return:
        """
        self.cf.read(file_path, encoding='utf-8')
        secs = self.cf.sections()
        config_dict = {}
        for sec in secs:
            items = self.cf.items(sec)
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
            for s in self.config_dict:
                if key in self.config_dict[s]:
                    return self.config_dict[s][key]
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
