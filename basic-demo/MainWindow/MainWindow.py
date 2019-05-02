# coding:utf-8
# һ���򵥵İ����ı��༭�򡢲˵������˵���������ļ򵥴���demo
# status: AC
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # �ı��༭��
        textEdit = QTextEdit()
        # ���õ�ǰ������������ؼ�Ϊ�ı��༭��
        self.setCentralWidget(textEdit)

        # ����һ�����Խ����˳�������action
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        # ���ò�����ݼ�
        exitAct.setShortcut('Ctrl+Q')
        # �����˳������������ʱ��״̬����ʾ�ı�
        exitAct.setStatusTip('Exit Application')
        # ���ź�
        exitAct.triggered.connect(self.close)

        # չʾ״̬��
        self.statusBar()

        # �˵���
        menubar = self.menuBar()
        # �ļ��˵�
        fileMenu = menubar.addMenu('&File')
        # ���˳�������ӵ��ļ��˵�
        fileMenu.addAction(exitAct)

        # ������
        toolbar = self.addToolBar('Exit')
        # ���˳�������ӵ�������
        toolbar.addAction(exitAct)

        # ���ô���λ�á���С�����⣬����ʾ����
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main Window')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
