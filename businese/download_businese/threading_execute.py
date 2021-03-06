import time

from PyQt5.QtCore import QThread, pyqtSignal, QWaitCondition, QMutex
from businese.download_businese.BusinessProcessing import executeElement


class signalThreading(QThread):
    sin_out = pyqtSignal(str)
    sin_work_status = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        # 设置工作状态和初始值
        self.working = True
        self.is_First_time = True
        self.get = executeElement()
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def __del__(self):
        # 线程状态改为和线程终止
        self.working = False
        # self.wait()

    def pause(self):
        """
        线程暂停
        :return:
        """
        self.working = False

    def start_execute_init(self):
        """
        线程开始
        :return:
        """
        self.working = True
        self.cond.wakeAll()

    def get_businese_param(self, start_page_num, end_page_num, log_path_flor, proxy_ip_port=None):
        """
        获取一些业务需要的参数
        :param start_page_num: 开始页
        :param end_page_num: 结束页
        :param log_path_flor: 日志保持路径
        :param proxy_ip_port: 代理ip，如果有的话
        :return:
        """
        self.start_page_num = start_page_num
        self.end_page_num = end_page_num
        self.log_path = log_path_flor
        self.ip_port = proxy_ip_port

    def run(self):
        """
        主方法，对比图片使用
        :return:
        """
        while self.working:
            self.mutex.lock()

            if self.working is False:
                # self.cond.wait(self.mutex)
                self.sin_out.emit("线程已停止运行")
                self.sin_work_status.emit(False)
                self.mutex.unlock()
                return None

            star_number = self.start_page_num
            end_number = self.end_page_num

            for i in range(int(star_number), int(end_number)):

                if self.working is False:
                    # self.cond.wait(self.mutex)
                    self.sin_out.emit("程序已结束运行 %s " % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    self.sin_work_status.emit(False)
                    self.mutex.unlock()
                    return None
                self.sin_work_status.emit(True)
                url = 'https://hsex.men/list-' + str(i) + '.htm'
                self.get.goto_picture(url=url, pic_path_save=self.log_path, ip_port=self.ip_port)
                recode_page = "第 %d 页的数据检查完了 %s" % (i, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                self.sin_out.emit(recode_page)

            self.mutex.unlock()
            self.pause()
        self.sin_out.emit("线程已停止运行(或已完成循环对比)")


class getNetWorkStatus(QThread):
    sin_work_status = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.get = executeElement()
        self.ip_port = None

    def get_network_status(self, ip_port=None):
        self.ip_port = ip_port

    def run(self):
        result = self.get.get_network_status(url="https://hsex.men", ip_port=self.ip_port)
        self.sin_work_status.emit(result)