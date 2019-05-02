# coding:utf-8
# 一个简单的包含文本编辑框、菜单栏、菜单项、工具栏的简单窗口demo
# status: AC
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 文本编辑框
        textEdit = QTextEdit()
        # 设置当前窗口中心区域控件为文本编辑框
        self.setCentralWidget(textEdit)

        # 创建一个可以进行退出操作的action
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        # 设置操作快捷键
        exitAct.setShortcut('Ctrl+Q')
        # 设置退出操作鼠标悬浮时的状态栏显示文本
        exitAct.setStatusTip('Exit Application')
        # 绑定信号
        exitAct.triggered.connect(self.close)

        # 展示状态栏
        self.statusBar()

        # 菜单栏
        menubar = self.menuBar()
        # 文件菜单
        fileMenu = menubar.addMenu('&File')
        # 将退出操作添加到文件菜单
        fileMenu.addAction(exitAct)

        # 工具栏
        toolbar = self.addToolBar('Exit')
        # 将退出操作添加到工具栏
        toolbar.addAction(exitAct)

        # 设置窗口位置、大小、标题，并显示出来
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main Window')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
