from resources.mainwindow import Ui_MainWindow
from expenseform_window import ExpenseForm
#from views.editexpense_window import EditExpense
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QDateTime
from PySide2.QtWidgets import QHeaderView, QMainWindow, QTableView
from delegate import PushButtonDelegate
from datetime import datetime, date
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
    
        
        #SET QTableView Headers
        self.horizontal_header = self.expenseTable.horizontalHeader() 
        self.horizontal_header.setSectionResizeMode(
                               QHeaderView.ResizeToContents
                               )
        #self.horizontal_header.setStretchLastSection(True)
        self.horizontal_header.setDefaultAlignment(Qt.AlignLeft)   
        self.expenseTable.verticalHeader().hide()
        
        #SET WIDGET BEHAVIOR
        self.dateInput.setDateTime(QDateTime.currentDateTime()) 
        self.expenseTable.setSelectionBehavior(QTableView.SelectRows)
        self.addExpenseBtn.setEnabled(False)
        validator = QtGui.QDoubleValidator()
        self.valueInput.setValidator(validator)
 

        #SET DELEGATES
        self.editDelegate = PushButtonDelegate(self.expenseTable)
        self.deleteDelegate = PushButtonDelegate(self.expenseTable)
        self.expenseTable.setItemDelegateForColumn(5, self.editDelegate)
        self.expenseTable.setItemDelegateForColumn(6, self.deleteDelegate)
    
   

    


        
   