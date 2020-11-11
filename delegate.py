from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QDateTime
#from PySide2.QtWidgets import QHeaderView, QMainWindow, QTableView


class PushButtonDelegate(QtWidgets.QStyledItemDelegate):
    clicked = QtCore.Signal(QtCore.QModelIndex)

    def paint(self, painter, option, index):
        if (
            isinstance(self.parent(), QtWidgets.QAbstractItemView)
            and self.parent().model() is index.model()
        ):
            self.parent().openPersistentEditor(index)

    def createEditor(self, parent, option, index):
        button = QtWidgets.QPushButton(str(index.data()), parent)
        button.clicked.connect(lambda *args, ix=index: self.clicked.emit(ix))
        return button

    def setEditorData(self, editor, index):
        #editor.setText(str(index.data()))
        pass

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text())
        #pass