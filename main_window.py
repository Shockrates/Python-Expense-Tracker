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
        
        #SET NEW WINDOWS HERE
        self.expenseForm = None

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
        # self.displaySelection.setDisabled(True)

        #SET DELEGATES
        self.editDelegate = PushButtonDelegate(self.expenseTable)
        self.deleteDelegate = PushButtonDelegate(self.expenseTable)
        self.expenseTable.setItemDelegateForColumn(5, self.editDelegate)
        self.expenseTable.setItemDelegateForColumn(6, self.deleteDelegate)
    
    def openDeleteWindow(self, index, categories, users):

        self.expenseForm = ExpenseForm()

        #INITIALIZES THE expenseForm WINDOW DATA
        self.expenseForm.updUser.setModel(users)
        self.expenseForm.updCategory.setModel(categories)
        self.expenseForm.deleteExpenseBtn.clicked.connect(self.clicked)

        selected_indexes = self.expenseTable.selectionModel().selectedRows()  
        #row = selected_indexes[0].row()
        row = index.row()
        expenseList = [self.expenseTable.model().index(row, col).data()
                    for col in range(self.expenseTable.model().columnCount(0))]
        self.expenseForm.updIndex.setText(expenseList[0])            
        self.expenseForm.updDate.setDate(datetime.strptime(expenseList[1], '  %d/%m/%Y  '))
        self.expenseForm.updDate.setReadOnly(True)
        self.expenseForm.updValue.setText(expenseList[2])
        self.expenseForm.updValue.setReadOnly(True)
        self.expenseForm.updCategory.setCurrentText(expenseList[3])
        self.expenseForm.updCategory.setEnabled(False)
        self.expenseForm.updUser.setCurrentText(expenseList[4])
        self.expenseForm.updUser.setEnabled(False)
        self.expenseForm.updateExpenseBtn.hide()
        self.expenseForm.deleteExpenseBtn.show()
        self.expenseForm.show()


        
   