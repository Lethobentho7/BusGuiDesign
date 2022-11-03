import sys
import input
# 导入相关模块

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    # 控件由xx自动生成的类接管
    # 创建一个类实例
    ui = input.Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    # 进入主循环
    sys.exit(app.exec_())