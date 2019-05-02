# coding:utf-8
# status: AC
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog,QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open a new file')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300,300,350, 300)
        self.setWindowTitle('File Dialog')
        self.show()
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:/github/pyqt5-learn/basic-demo', filter = '*.py')
        if fname[0]:
            with open(fname[0], 'r') as fin:
                data = fin.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
