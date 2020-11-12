#!/usr/bin/python

"""
ZetCode PySide tutorial 

In this example, we show how to emit a
signal. 

author: Jan Bodnar
website: zetcode.com
"""

import sys
from PySide2.QtWidgets import QHeaderView, QMainWindow, QTableView
from PySide2 import QtCore, QtGui, QtWidgets

class Communicate(QtCore.QObject):
    
    closeApp = QtCore.Signal()

class Example(QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.c = Communicate()
        self.c.closeApp.connect(self.close)       
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit()
        
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()