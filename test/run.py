import sys
from PyQt5 import QtCore, QtWidgets, QtCore

# 导入设计的页面
from homepage import Ui_MainWindow as Homepage_Ui
from input import Ui_MainWindow as Input_Ui
from menu import Ui_MainWindow as Menu_Ui
from result import Ui_MainWindow as Result_Ui
from roadmap import Ui_MainWindow as Roadmap_Ui
from voice import Ui_MainWindow as VoiceInput_Ui

# 主窗口
class MenuWindow(QtWidgets.QMainWindow, Menu_Ui):

    # switch_window1 = QtCore.pyqtSignal()            # 跳转信号
    # switch_window2 = QtCore.pyqtSignal()            # 跳转信号
    # switch_window3 = QtCore.pyqtSignal()            # 跳转信号

    switch_window_voice = QtCore.pyqtSignal()       # 跳转信号
    switch_window_homepage = QtCore.pyqtSignal()    # 跳转信号
    switch_window_menu = QtCore.pyqtSignal()        # 跳转信号
    switch_window_roadmap = QtCore.pyqtSignal()     # 跳转信号

    def __init__(self):
        super(MenuWindow, self).__init__()
        self.setupUi(self)
        self.menuButton.clicked.connect(self.goMenu)
        self.homepageButton.clicked.connect(self.goHomepage)
        self.voiceSearchButton.clicked.connect(self.goVoice)
        self.road1Button.clicked.connect(self.goRoadmap)
        self.road2Button.clicked.connect(self.goRoadmap)
        self.road3Button.clicked.connect(self.goRoadmap)

    def goMenu(self):
        self.switch_window_menu.emit()

    def goHomepage(self):
        self.switch_window_homepage.emit()

    def goVoice(self):
        self.switch_window_voice.emit()

    def goRoadmap(self):
        self.switch_window_roadmap.emit()

# 首页窗口
class HomepageWindow(QtWidgets.QMainWindow, Homepage_Ui):
    def __init__(self):
        super(HomepageWindow, self).__init__()
        self.setupUi(self)
        # self.menuButton.clicked.connect(self.goMenu)
        # self.homepageButton.clicked.connect(self.goHomepage)


# 语音窗口
class VoiceWindow(QtWidgets.QMainWindow, VoiceInput_Ui):
    def __init__(self):
        super(VoiceWindow, self).__init__()
        self.setupUi(self)
        # self.menuButton.clicked.connect(self.goMenu)
        # self.homepageButton.clicked.connect(self.goHomepage)

# 路线窗口
class RoadmapWindow(QtWidgets.QMainWindow, Roadmap_Ui):
    def __init__(self):
        super(RoadmapWindow, self).__init__()
        self.setupUi(self)
        # self.menuButton.clicked.connect(self.goMenu)
        # self.homepageButton.clicked.connect(self.goHomepage)

# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass
    # 跳转到 Menu 窗口
    def show_menu(self):
        self.menu = MenuWindow()
        self.menu.switch_window_homepage.connect(self.show_homepage)
        self.menu.switch_window_voice.connect(self.show_voice)
        self.menu.switch_window_roadmap.connect(self.show_roadmap)
        self.menu.show()
    # 跳转到 homepage 窗口, 关闭原页面
    def show_homepage(self):
        self.homepage = HomepageWindow()
        self.menu.close()
        self.homepage.show()
    # 跳转到 voice 窗口, 关闭原页面
    def show_voice(self):
        self.voice = VoiceWindow()
        self.menu.close()
        self.voice.show()
    # 跳转到 roadmap 窗口, 关闭原页面
    def show_roadmap(self):
        self.roadmap = RoadmapWindow()
        self.menu.close()
        self.roadmap.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()   # 控制器实例
    controller.show_menu()      # 默认展示的是 menu 页面
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()