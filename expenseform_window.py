from PySide2 import QtCore
from resources.expenseform import Ui_Form
from PySide2.QtWidgets import QMainWindow
from datetime import datetime, date

#DECLARE CLASS IN ORDER TOSEND A SIGNAL
class Communicate(QtCore.QObject):
    
    close = QtCore.Signal()


class ExpenseForm(QMainWindow, Ui_Form):

    def __init__(self):
        super(ExpenseForm, self).__init__()
        self.setupUi(self)
        self.c = Communicate()
    
    def openDeleteWindow(self, expenseList, models):
        #INITIALIZES THE expenseForm WINDOW DATA
        self.updUser.setModel(models.getUsersModel())
        self.updCategory.setModel(models.getCategoriesModel())
        self.updIndex.setText(expenseList[0])            
        self.updDate.setDate(datetime.strptime(expenseList[1], '  %d/%m/%Y  '))
        self.updDate.setReadOnly(True)
        self.updValue.setText(expenseList[2])
        self.updValue.setReadOnly(True)
        self.updCategory.setCurrentText(expenseList[3])
        self.updCategory.setEnabled(False)
        self.updUser.setCurrentText(expenseList[4])
        self.updUser.setEnabled(False)
        self.updateExpenseBtn.hide()
        self.deleteExpenseBtn.show()
        self.show() 

  
    def openUpdateWindow(self, expenseList, models):
        
        self.updUser.setModel(models.getUsersModel())
        self.updCategory.setModel(models.getCategoriesModel())
        self.updIndex.setText(expenseList[0])            
        self.updDate.setDate(datetime.strptime(expenseList[1], '  %d/%m/%Y  '))
        self.updValue.setText(expenseList[2])
        self.updCategory.setCurrentText(expenseList[3])
        self.updUser.setCurrentText(expenseList[4])
        self.updateExpenseBtn.show()
        self.deleteExpenseBtn.hide()
        self.show()
    
    #EMMIT SIGNAL WHEN WINDOW CLOSES
    def closeEvent(self, event):
        self.c.close.emit()
        