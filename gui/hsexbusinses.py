import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel,
                             QLineEdit, QCheckBox, QTextBrowser, QFileDialog, QMessageBox, QAction, QFormLayout)
import src.images

class mainWindowsGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        """
        定义基本GUI元素
        """
        self.setObjectName("MainWindow")
        self.resize(580, 430)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":img/gui_logo.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(290, 10, 281, 371))
        self.groupBox_9.setObjectName("groupBox_9")
        self.log_print_textbox = QtWidgets.QTextBrowser(self.groupBox_9)
        self.log_print_textbox.setGeometry(QtCore.QRect(10, 20, 261, 341))
        self.log_print_textbox.setObjectName("log_print_textbox")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 371))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 251, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.origin_pic_path_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.origin_pic_path_line.setObjectName("origin_pic_path_line")
        self.gridLayout.addWidget(self.origin_pic_path_line, 0, 0, 1, 1)
        self.origin_pic_path_button = QtWidgets.QPushButton(self.groupBox_2)
        self.origin_pic_path_button.setObjectName("origin_pic_path_button")
        self.gridLayout.addWidget(self.origin_pic_path_button, 0, 1, 1, 1)
        self.log_save_path_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.log_save_path_line.setObjectName("log_save_path_line")
        self.gridLayout.addWidget(self.log_save_path_line, 1, 0, 1, 1)
        self.log_save_path_button = QtWidgets.QPushButton(self.groupBox_2)
        self.log_save_path_button.setObjectName("log_save_path_button")
        self.gridLayout.addWidget(self.log_save_path_button, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 110, 251, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label)
        self.open_proxy_button = QtWidgets.QRadioButton(self.groupBox_3)
        self.open_proxy_button.setObjectName("open_proxy_button")
        self.horizontalLayout.addWidget(self.open_proxy_button)
        self.close_proxy_button = QtWidgets.QRadioButton(self.groupBox_3)
        self.close_proxy_button.setObjectName("close_proxy_button")
        self.horizontalLayout.addWidget(self.close_proxy_button)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 170, 251, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.widget = QtWidgets.QWidget(self.groupBox_4)
        self.widget.setGeometry(QtCore.QRect(10, 30, 231, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.start_path_line = QtWidgets.QLineEdit(self.widget)
        self.start_path_line.setObjectName("start_path_line")
        self.horizontalLayout_2.addWidget(self.start_path_line)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.end_path_line = QtWidgets.QLineEdit(self.widget)
        self.end_path_line.setObjectName("end_path_line")
        self.horizontalLayout_2.addWidget(self.end_path_line)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 250, 251, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_execute_button = QtWidgets.QPushButton(self.groupBox_5)
        self.start_execute_button.setObjectName("start_execute_button")
        self.horizontalLayout_3.addWidget(self.start_execute_button)
        self.end_execute_button = QtWidgets.QPushButton(self.groupBox_5)
        self.end_execute_button.setObjectName("end_execute_button")
        self.horizontalLayout_3.addWidget(self.end_execute_button)
        self.clear_log_button = QtWidgets.QPushButton(self.groupBox_5)
        self.clear_log_button.setObjectName("clear_log_button")
        self.horizontalLayout_3.addWidget(self.clear_log_button)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuproxy = QtWidgets.QMenu(self.menu)
        self.menuproxy.setObjectName("menuproxy")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionsocks5 = QtWidgets.QAction(self)
        self.actionsocks5.setObjectName("actionsocks5")
        self.actionhelp = QtWidgets.QAction(self)
        self.actionhelp.setObjectName("actionhelp")
        self.actionabout = QtWidgets.QAction(self)
        self.actionabout.setObjectName("actionabout")
        self.menuproxy.addAction(self.actionsocks5)
        self.menu.addAction(self.menuproxy.menuAction())
        self.menu_2.addAction(self.actionhelp)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionabout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.setWindowTitle("hsex图片对比工具")
        self.groupBox_9.setTitle("日志打印")
        self.groupBox.setTitle("参数输入")
        self.groupBox_2.setTitle("路径设置")
        self.origin_pic_path_button.setText("源文件")
        self.log_save_path_button.setText("日志路径")
        self.groupBox_3.setTitle("代理设置")
        self.label.setText("启用代理")
        self.open_proxy_button.setText("是")
        self.close_proxy_button.setText("否")
        self.close_proxy_button.setChecked(True)
        self.groupBox_4.setTitle("范围设置")
        self.label_2.setText("开始页")
        self.label_3.setText("结束页")
        self.groupBox_5.setTitle("执行操作")
        self.start_execute_button.setText("开始执行")
        self.end_execute_button.setText("结束执行")
        self.clear_log_button.setText("清理日志")
        self.menu.setTitle("设置")
        self.menuproxy.setTitle("本地代理")
        self.menu_2.setTitle("关于")
        self.actionsocks5.setText("socks5本地代理")
        self.actionhelp.setText("帮助")
        self.actionabout.setText("关于")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindowsGUI()
    # ex.execute_pyqt()
    sys.exit(app.exec_())
