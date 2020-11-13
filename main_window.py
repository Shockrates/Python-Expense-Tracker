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
    
    #SETS STARTING VALUES TO INPUT AND SEARCH FIELDS BASED ON PASSING MODEL
    def initializeView(self, model):

        self.userFilter.setModel(model.getUsersModel())
        self.categoryFilter.setModel(model.getCategoriesModel())
        self.dateFilter.setModel(model.getMonthsModel())
        curIndex=self.dateFilter.findText(date.today().strftime("%B-%Y"))
        self.dateFilter.setCurrentIndex(curIndex)
        self.usersDataTable.setModel(model.getUsersModel())

        self.categoryInput.setModel(model.getCategoriesModel())
        self.userInput.setModel(model.getUsersModel())
        self.updateTableView(model)
        self.show()
    

    def updateTableView(self, model):
        #Gets the selected Month 
        if len(self.dateFilter.currentText()) == 0:
            date=""
        else:
            date = datetime.strptime(self.dateFilter.currentText(), "%B-%Y").strftime("%Y-%m")
        #Gets Selected Category
        category = self.categoryFilter.currentText()
        #Gets Selected User
        user = self.userFilter.currentText()
        #Create a model based on the selections
        expenseModel = model.getExpenseModel(date, category, user)
        #Sets the View
        self.expenseTable.setModel(expenseModel)  
        #Hides the Index Column
        self.expenseTable.setColumnHidden(0, True)

    def updateDateView(self, model):
        selectedDate =  self.dateFilter.currentIndex()
        self.dateFilter.setModel(model.getMonthsModel()) 
        self.dateFilter.setCurrentIndex(selectedDate) 

    def getSelectedRowData(self, expenseList):
        
        displayString = ''

        self.dateInput.setDate(datetime.strptime(expenseList[1], '  %d/%m/%Y  '))
        self.valueInput.setText(expenseList[2])
        self.categoryInput.setCurrentText(expenseList[3])
        self.userInput.setCurrentText(expenseList[4])  

        displayString +="<span style=' font-weight:600;'>Date: "+str(expenseList[1])+"</span><br>"
        displayString +="Value: "+str(expenseList[2])+"<br>"  
        displayString +="Category: "+str(expenseList[3])+"<br>"
        displayString +="User: "+str(expenseList[4])+"<br>"

        self.displaySelection.setText(displayString)
      
    


        
   