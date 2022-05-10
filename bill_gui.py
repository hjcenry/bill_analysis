import datetime
import json
import logging
import logging.handlers
import os
import sys
import threading

from PySide2 import QtWidgets, QtGui
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QFileDialog, QLineEdit, QMessageBox

import bill_common
from analysis import analysis_factory
from constants import AnalysisType
from constants import config
from gui.bill_ui_window import Ui_MainWindow
from util.sys_logger import logger


class BillGui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.running_lock = threading.Lock()
        # config.ini
        self.config_ini_file = os.getcwd() + '/' + config.file_path
        # cookie
        self.cookie_file_name = "./cookie"
        # 汇总账单
        self.out_bill_file_name = "汇总账单.csv"
        # 占比数据饼图
        self.ratio_pic = "占比图.jpg"
        # 红包数据饼图
        self.red_packet_pic = "红包数据图.jpg"

        self.cookie = {}
        self.logger = logger
        self.setWindowIcon(QIcon('icon.png'))
        self.load_qss()
        self.setupUi(self)
        self.init_ui()
        # 绑定点击事件
        self.bind_click_events()

    def init_ui(self):
        self.tabWidget.setCurrentIndex(0)
        if os.path.exists(self.cookie_file_name):
            with open(self.cookie_file_name, 'r') as f:
                self.cookie = json.load(f)

        # 微信
        self.init_text(line_edit=self.wechat_file, cookie_key='choose_wechat_file', dialog_text="上次选择微信账单:")
        # 支付宝
        self.init_text(line_edit=self.alipay_file, cookie_key='choose_alipay_file', dialog_text="上次选择支付宝账单:")
        # 招商银行
        self.init_text(line_edit=self.cmbc_file, cookie_key='choose_cmbc_file', dialog_text="上次选择招商银行账单:")
        # 中国银行
        self.init_text(line_edit=self.boc_file, cookie_key='choose_boc_file', dialog_text="上次选择中国银行账单:")
        # 输出目录
        self.out_dir.setText(self.get_last_choose_dir())
        self.update_state_text("输出目录:", color="blue")
        self.update_state_text(self.out_dir.text())
        # 说明文本
        info_html = config.get_config("info_html", "INFO")
        with open(info_html, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.info_text.setHtml('\r\n'.join(lines))

    def init_text(self, dialog_text=None, line_edit=None, cookie_key=None, config_key=None):
        if config_key is not None:
            files_text = config.get_config("files", config_key)
        if cookie_key is not None and line_edit is not None:
            if cookie_key in self.cookie:
                files_text = self.cookie[cookie_key]
            line_edit.setText(files_text)

            self.update_state_text(state_text=dialog_text, color="blue")
            for file in files_text.split(";"):
                self.update_state_text(file)

    # 窗口关闭按钮事件
    def closeEvent(self, event):
        with open(self.cookie_file_name, 'w') as f:
            json.dump(self.cookie, f)

    def show_question_dialog(self, show_title='', show_content='', default_choose=False):
        """
        展示选择对话框
        :param show_title:
        :param show_content:
        :param default_choose:
        :return:
        """
        reply = QMessageBox.question(self, show_title, show_content,
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes if default_choose else QMessageBox.No)
        return reply == QMessageBox.Yes

    def load_qss(self):
        file = 'gui/window.qss'
        with open(file, 'rt', encoding='utf8') as f:
            style_sheet = f.read()
        # self.setStyleSheet(style_sheet)
        f.close()

    def bind_click_events(self):
        self.start.clicked.connect(self.start_analysis_async)
        self.clear_log.clicked.connect(self.do_clear_log)
        self.wechat_file_choose.clicked.connect(self.choose_wechat_file)
        self.alipay_file_choose.clicked.connect(self.choose_alipay_file)
        self.cmbc_file_choose.clicked.connect(self.choose_cmbc_file)
        self.boc_file_choose.clicked.connect(self.choose_boc_file)
        self.out_dir_choose.clicked.connect(self.choose_out_dir)
        self.open_out_dir.clicked.connect(self.do_open_out_dir)
        self.open_config_ini.clicked.connect(self.do_open_config_ini)
        self.actionexit.triggered.connect(self.close)

    def do_open_out_dir(self):
        if self.out_dir.text() is None or len(self.out_dir.text()) == 0:
            self.update_state_text("请选择输出目录!", color="red")
            return
        os.startfile(self.out_dir.text())

    def do_open_config_ini(self):
        os.startfile(self.config_ini_file)

    def choose_out_dir(self):
        out_files_dir = QFileDialog.getExistingDirectory(self, "选择输出目录", self.get_last_choose_dir())
        if out_files_dir is None or len(out_files_dir) == 0:
            return
        self.out_dir.setText(out_files_dir)
        self.save_cookie("choose_out_dir", out_files_dir)
        self.save_last_choose_dir(out_files_dir)

    def choose_file(self, dialog_text="选择账单", line_edit=None, cookie_key=None):
        """
        选择文件
        :return:
        """
        if line_edit is None:
            return
        file_names = QFileDialog.getOpenFileNames(self, dialog_text, self.get_last_choose_dir(), "Csv Files(*.csv)")
        if file_names is None or len(file_names) == 0:
            return

        files = ';'.join(file_names[0])
        if len(files) > 0:
            line_edit.setText(files)
            self.update_state_text(dialog_text, color="blue")

            choose_dir = None
            for file in files.split(";"):
                if choose_dir is None:
                    choose_dir = os.path.dirname(os.path.abspath(file))

                self.update_state_text(file)

            if cookie_key is not None:
                self.save_cookie(cookie_key, files)
            if choose_dir is not None:
                self.save_last_choose_dir(choose_dir)

    def get_last_choose_dir(self):
        last_dir = self.get_cookie("last_choose_dir")
        if last_dir is None:
            return os.getcwd()
        return last_dir

    def save_last_choose_dir(self, choose_dir: str):
        self.save_cookie("last_choose_dir", choose_dir)

    def save_cookie(self, key=None, value=None):
        if key is None or len(key) == 0:
            return
        if value is None or len(value) == 0:
            return
        self.cookie[key] = value

    def get_cookie(self, key=None):
        if key is None or key not in self.cookie:
            return
        return self.cookie[key]

    def choose_wechat_file(self):
        """
        选择微信文件
        :return:
        """
        self.choose_file(dialog_text="选择微信账单", line_edit=self.wechat_file, cookie_key="choose_wechat_file")

    def choose_alipay_file(self):
        """
        选择支付宝文件
        :return:
        """
        self.choose_file(dialog_text="选择支付宝账单", line_edit=self.alipay_file, cookie_key="choose_alipay_file")

    def choose_cmbc_file(self):
        """
        选择招商银行文件
        :return:
        """
        self.choose_file(dialog_text="选择招商银行账单", line_edit=self.cmbc_file, cookie_key="choose_cmbc_file")

    def choose_boc_file(self):
        """
        选择中国银行文件
        :return:
        """
        self.choose_file(dialog_text="选择中国银行账单", line_edit=self.boc_file, cookie_key="choose_boc_file")

    def set_logger(self):
        self.logger.setLevel(logging.INFO)

    def update_state_text(self, state_text, color=None, error=None):
        if error is not None:
            self.logger.error(state_text, error)
        else:
            self.logger.info(state_text)

        self.console_log.moveCursor(QtGui.QTextCursor.End)

        if color is not None:
            state_text = "<font color=%s>%s</font>" % (color, state_text)
        else:
            state_text = "<font>%s</font>" % state_text

        self.console_log.insertHtml(
            '<font><b>%s</b></font> > %s' % (datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S"), state_text))
        self.console_log.insertPlainText("\r\n")

    def analysis(self, data_list: list, analysts_type: AnalysisType, line_edit: QLineEdit):
        self.update_state_text("开始分析%s账单" % analysts_type.value["name"])
        analysts = analysis_factory.create_analysts(analysts_type)
        if analysts is None:
            return
        if line_edit.text() is None or len(line_edit.text()) == 0:
            self.update_state_text("%s没有选择账单文件" % analysts_type.value["name"], color="red")
            return
        try:
            result = analysts.analysis(bill_files=line_edit.text().split(";"), absolute_path=True)
            data_list.extend(result)
        except Exception as e:
            self.update_state_text('%s账单分析异常!' % analysts_type.value["name"], color="red", error=e)

    def start_analysis_async(self):
        if self.running_lock.locked():
            self.update_state_text("正在运行中", color="red")
        else:
            self.start.setEnabled(False)
            self.running_lock.acquire(blocking=True)
            threading.Thread(target=self.start_analysis, name="analysis_thread").start()

    def start_analysis(self):
        try:
            if self.out_dir.text() is None or len(self.out_dir.text()) == 0:
                self.update_state_text("请选择输出目录!", color="red")
                return

            data_list = []
            self.update_state_text("开始分析账单", color="blue")
            self.analysis(data_list, AnalysisType.WE_CHAT, self.wechat_file)
            self.analysis(data_list, AnalysisType.ALIPAY, self.alipay_file)
            self.analysis(data_list, AnalysisType.CMBC, self.cmbc_file)
            self.analysis(data_list, AnalysisType.BOC, self.boc_file)

            bill_common.print_debug(data_list)
            # # 生成总账单
            self.update_state_text("开始生成汇总账单", color="blue")
            bill, total_in, total_out = bill_common.generate_total_bill(data_list, out_dir=self.out_dir.text(),
                                                                        out_file=self.out_bill_file_name,
                                                                        out_total=False)
            self.update_state_text("生成汇总账单[%s]" % bill, color="green")
            # 生成占比数据图
            self.update_state_text("开始生成收入支持占比数据图", color="blue")
            ratio_pic_file = self.out_dir.text() + "/" + self.ratio_pic
            bill_common.generate_pie_graph(data_list, save_file=ratio_pic_file)
            # 生成红包数据图
            if len(self.wechat_file.text()) > 0:
                red_packet_file = self.out_dir.text() + "/" + self.red_packet_pic
                self.update_state_text("开始生成红包数据图", color="blue")
                bill_common.generate_wechat_red_packet_graph(save_file=red_packet_file,
                                                             bill_files=self.wechat_file.text().split(";"),
                                                             absolute_path=True)

            self.update_state_text("账单总收入<font color=green>[%s]</font>" % total_in)
            self.update_state_text("账单总支出<font color=red>[%s]</font>" % total_out)
            total_amount = round((total_in - total_out), 2)
            if total_amount >= 0:
                total_amount_text = '<font color=green>[%s]</font>' % total_amount
            else:
                total_amount_text = '<font color=red>[%s]</font>' % total_amount

            self.update_state_text("账单总账%s" % total_amount_text)

            self.update_state_text("汇总账单分析完成", color="green")
        except Exception as e:
            self.update_state_text("账单分析异常", color="red", error=e)
        finally:
            self.running_lock.release()
            self.start.setEnabled(True)

    def do_clear_log(self):
        """
        清空log
        :return:
        """
        if self.show_question_dialog(show_title="警告", show_content="确认清空日志吗", default_choose=False):
            self.console_log.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    bill_gui = BillGui()
    bill_gui.show()
    sys.exit(app.exec_())
