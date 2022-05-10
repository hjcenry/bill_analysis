# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledZpRouk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1107, 909)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.actionexit.setShortcutContext(Qt.WidgetShortcut)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(5, 10, 1081, 831))
        self.tool = QWidget()
        self.tool.setObjectName(u"tool")
        self.verticalLayoutWidget_3 = QWidget(self.tool)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 20, 1031, 1381))
        self.tool_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.tool_layout.setSpacing(6)
        self.tool_layout.setContentsMargins(9, 9, 9, 9)
        self.tool_layout.setObjectName(u"tool_layout")
        self.tool_layout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFocusPolicy(Qt.WheelFocus)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 1011, 251))
        self.config_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.config_layout.setSpacing(6)
        self.config_layout.setContentsMargins(9, 9, 9, 9)
        self.config_layout.setObjectName(u"config_layout")
        self.config_layout.setContentsMargins(0, 20, 0, 0)
        self.config_path_layout = QFormLayout()
        self.config_path_layout.setSpacing(6)
        self.config_path_layout.setObjectName(u"config_path_layout")
        self.wechat_label = QLabel(self.verticalLayoutWidget)
        self.wechat_label.setObjectName(u"wechat_label")

        self.config_path_layout.setWidget(0, QFormLayout.LabelRole, self.wechat_label)

        self.wechat_layout = QHBoxLayout()
        self.wechat_layout.setSpacing(6)
        self.wechat_layout.setObjectName(u"wechat_layout")
        self.wechat_file = QLineEdit(self.verticalLayoutWidget)
        self.wechat_file.setObjectName(u"wechat_file")
        self.wechat_file.setEnabled(False)

        self.wechat_layout.addWidget(self.wechat_file)

        self.wechat_file_choose = QPushButton(self.verticalLayoutWidget)
        self.wechat_file_choose.setObjectName(u"wechat_file_choose")

        self.wechat_layout.addWidget(self.wechat_file_choose)

        self.config_path_layout.setLayout(0, QFormLayout.FieldRole, self.wechat_layout)

        self.alipay_label = QLabel(self.verticalLayoutWidget)
        self.alipay_label.setObjectName(u"alipay_label")

        self.config_path_layout.setWidget(1, QFormLayout.LabelRole, self.alipay_label)

        self.alipay_layout = QHBoxLayout()
        self.alipay_layout.setSpacing(6)
        self.alipay_layout.setObjectName(u"alipay_layout")
        self.alipay_file = QLineEdit(self.verticalLayoutWidget)
        self.alipay_file.setObjectName(u"alipay_file")
        self.alipay_file.setEnabled(False)

        self.alipay_layout.addWidget(self.alipay_file)

        self.alipay_file_choose = QPushButton(self.verticalLayoutWidget)
        self.alipay_file_choose.setObjectName(u"alipay_file_choose")

        self.alipay_layout.addWidget(self.alipay_file_choose)

        self.config_path_layout.setLayout(1, QFormLayout.FieldRole, self.alipay_layout)

        self.cmbc_label = QLabel(self.verticalLayoutWidget)
        self.cmbc_label.setObjectName(u"cmbc_label")

        self.config_path_layout.setWidget(2, QFormLayout.LabelRole, self.cmbc_label)

        self.cmbc_layout = QHBoxLayout()
        self.cmbc_layout.setSpacing(6)
        self.cmbc_layout.setObjectName(u"cmbc_layout")
        self.cmbc_file = QLineEdit(self.verticalLayoutWidget)
        self.cmbc_file.setObjectName(u"cmbc_file")
        self.cmbc_file.setEnabled(False)

        self.cmbc_layout.addWidget(self.cmbc_file)

        self.cmbc_file_choose = QPushButton(self.verticalLayoutWidget)
        self.cmbc_file_choose.setObjectName(u"cmbc_file_choose")

        self.cmbc_layout.addWidget(self.cmbc_file_choose)

        self.config_path_layout.setLayout(2, QFormLayout.FieldRole, self.cmbc_layout)

        self.boc_label = QLabel(self.verticalLayoutWidget)
        self.boc_label.setObjectName(u"boc_label")

        self.config_path_layout.setWidget(3, QFormLayout.LabelRole, self.boc_label)

        self.boc_layout = QHBoxLayout()
        self.boc_layout.setSpacing(6)
        self.boc_layout.setObjectName(u"boc_layout")
        self.boc_file = QLineEdit(self.verticalLayoutWidget)
        self.boc_file.setObjectName(u"boc_file")
        self.boc_file.setEnabled(False)

        self.boc_layout.addWidget(self.boc_file)

        self.boc_file_choose = QPushButton(self.verticalLayoutWidget)
        self.boc_file_choose.setObjectName(u"boc_file_choose")

        self.boc_layout.addWidget(self.boc_file_choose)

        self.config_path_layout.setLayout(3, QFormLayout.FieldRole, self.boc_layout)

        self.out_dir_label = QLabel(self.verticalLayoutWidget)
        self.out_dir_label.setObjectName(u"out_dir_label")

        self.config_path_layout.setWidget(4, QFormLayout.LabelRole, self.out_dir_label)

        self.out_dir_layout = QHBoxLayout()
        self.out_dir_layout.setSpacing(6)
        self.out_dir_layout.setObjectName(u"out_dir_layout")
        self.out_dir = QLineEdit(self.verticalLayoutWidget)
        self.out_dir.setObjectName(u"out_dir")
        self.out_dir.setEnabled(False)

        self.out_dir_layout.addWidget(self.out_dir)

        self.out_dir_choose = QPushButton(self.verticalLayoutWidget)
        self.out_dir_choose.setObjectName(u"out_dir_choose")

        self.out_dir_layout.addWidget(self.out_dir_choose)

        self.config_path_layout.setLayout(4, QFormLayout.FieldRole, self.out_dir_layout)

        self.config_layout.addLayout(self.config_path_layout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start = QPushButton(self.verticalLayoutWidget)
        self.start.setObjectName(u"start")

        self.horizontalLayout_2.addWidget(self.start)

        self.open_out_dir = QPushButton(self.verticalLayoutWidget)
        self.open_out_dir.setObjectName(u"open_out_dir")

        self.horizontalLayout_2.addWidget(self.open_out_dir)

        self.open_config_ini = QPushButton(self.verticalLayoutWidget)
        self.open_config_ini.setObjectName(u"open_config_ini")

        self.horizontalLayout_2.addWidget(self.open_config_ini)

        self.config_layout.addLayout(self.horizontalLayout_2)

        self.tool_layout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.clear_log = QPushButton(self.groupBox_2)
        self.clear_log.setObjectName(u"clear_log")
        self.clear_log.setGeometry(QRect(10, 440, 1011, 23))
        self.console_log = QTextEdit(self.groupBox_2)
        self.console_log.setObjectName(u"console_log")
        self.console_log.setGeometry(QRect(10, 20, 1011, 401))

        self.tool_layout.addWidget(self.groupBox_2)

        self.tool_layout.setStretch(0, 1)
        self.tool_layout.setStretch(1, 4)
        self.tabWidget.addTab(self.tool, "")
        self.info = QWidget()
        self.info.setObjectName(u"info")
        self.verticalLayoutWidget_2 = QWidget(self.info)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 1061, 791))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.info_text = QTextEdit(self.verticalLayoutWidget_2)
        self.info_text.setObjectName(u"info_text")

        self.verticalLayout.addWidget(self.info_text)

        self.tabWidget.addTab(self.info, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1107, 22))
        self.exit_menu = QMenu(self.menubar)
        self.exit_menu.setObjectName(u"exit_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.exit_menu.menuAction())
        self.exit_menu.addAction(self.actionexit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u8d26\u5355\u6c47\u603b\u5de5\u5177", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"\u8d26\u5355\u6c47\u603b\u5206\u6790\u5de5\u5177", None))
        self.wechat_label.setText(QCoreApplication.translate("MainWindow", u"\u5fae\u4fe1\u8d26\u5355", None))
        self.wechat_file_choose.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.alipay_label.setText(QCoreApplication.translate("MainWindow", u"\u652f\u4ed8\u5b9d\u8d26\u5355", None))
        self.alipay_file_choose.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.cmbc_label.setText(QCoreApplication.translate("MainWindow", u"\u62db\u5546\u94f6\u884c\u8d26\u5355", None))
        self.cmbc_file_choose.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.boc_label.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u56fd\u94f6\u884c\u8d26\u5355", None))
        self.boc_file_choose.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.out_dir_label.setText(
            QCoreApplication.translate("MainWindow", u"\u6c47\u603b\u8d26\u5355\u76ee\u5f55", None))
        self.out_dir_choose.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5206\u6790", None))
        self.open_out_dir.setText(
            QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8d26\u5355\u76ee\u5f55", None))
        self.open_config_ini.setText(
            QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u914d\u7f6e\u6587\u4ef6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u53f0", None))
        self.clear_log.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tool),
                                  QCoreApplication.translate("MainWindow", u"\u5206\u6790\u5de5\u5177", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info),
                                  QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.exit_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi
