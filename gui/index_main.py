# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jiang/Downloads/index_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_index_main(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("index_main")
        self.resize(320, 240)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 221))
        self.groupBox.setObjectName("groupBox")
        self.online_model_button = QtWidgets.QPushButton(self.groupBox)
        self.online_model_button.setGeometry(QtCore.QRect(40, 40, 91, 61))
        self.online_model_button.setObjectName("online_model_button")
        self.offline_model_button = QtWidgets.QPushButton(self.groupBox)
        self.offline_model_button.setGeometry(QtCore.QRect(170, 40, 91, 61))
        self.offline_model_button.setObjectName("offline_model_button")
        self.pic_download_model_button = QtWidgets.QPushButton(self.groupBox)
        self.pic_download_model_button.setGeometry(QtCore.QRect(40, 130, 91, 61))
        self.pic_download_model_button.setObjectName("pic_download_model_button")

        self.setWindowTitle("首页")
        self.groupBox.setTitle("请选择模式")
        self.online_model_button.setText("线上模式")
        self.offline_model_button.setText("线下模式")
        self.pic_download_model_button.setText("资源下载")

