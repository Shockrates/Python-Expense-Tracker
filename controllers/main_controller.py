from PySide2.QtCore import QObject, QRegExp, QSortFilterProxyModel, Qt, SIGNAL, Slot
from PySide2.QtGui import QFont
from datetime import datetime, date
from main_window import MainWindow
from expenseform_window import ExpenseForm
from models.view_models import Models
from database.db import MyDatabase

class MainController(QObject):
    def __init__(self):
        super().__init__()
        self._view = MainWindow()
        self._expenseForm = None
        self._models = Models()
        self.db =  MyDatabase('expenses.db')
            
        self._view.userFilter.setModel(self._models.getUsersModel())
        self._view.categoryFilter.setModel(self._models.getCategoriesModel())
        self._view.dateFilter.setModel(self._models.getMonthsModel())
        curIndex=self._view.dateFilter.findText(date.today().strftime("%B-%Y"))
        self._view.dateFilter.setCurrentIndex(curIndex)

        self._view.categoryInput.setModel(self._models.getCategoriesModel())
        self._view.userInput.setModel(self._models.getUsersModel())
    
        self.updateTableView()
        self.connectSignals()
        self.initializeMainWindow()

    @Slot()
    def connectSignals(self):
        #Checks when the Month-Year Combobox Changes 
        self._view.dateFilter.currentTextChanged.connect(self.updateTableView)
        self._view.userFilter.currentTextChanged.connect(self.updateTableView)
        self._view.categoryFilter.currentTextChanged.connect(self.updateTableView)
        #Checks when a row in he table is clicked
        self._view.expenseTable.clicked.connect(self.getSelectedRowData)
        #Checks when the ADD EXPENSE button is clicked
        self._view.addExpenseBtn.clicked.connect(self.addNewExpense)
        #Checks when the EDIT and DELETE buttons are pressed
        self._view.editDelegate.clicked.connect(self.openUpdateWindow)
        self._view.deleteDelegate.clicked.connect(self.openDeleteWindow)

        self._view.valueInput.textChanged[str].connect(self.check_disable)
        self._view.userInput.activated.connect(self.check_disable)
        self._view.categoryInput.activated.connect(self.check_disable)

    @Slot()
    def updateTableView(self):

        #Gets the selected Month 
        if len(self._view.dateFilter.currentText()) == 0:
            text=""
        else:
            text = datetime.strptime(self._view.dateFilter.currentText(), "%B-%Y").strftime("%Y-%m")
        #Gets Selected Category
        category = self._view.categoryFilter.currentText()
        #Gets Selected User
        user = self._view.userFilter.currentText()
        #Create a model based on the selections
        self.expenseModel = self._models.getExpenseModel(text, category, user)
        #Sets the View
        self._view.expenseTable.setModel(self.expenseModel)  
        #Hides the Index Column
        self._view.expenseTable.setColumnHidden(0, True)
        
      
        
    @Slot()
    def getSelectedRowData(self, index):
        
        displayString = ''
        row = index.row()
        expenseList = [self._view.expenseTable.model().index(row, col).data()
                for col in range(self._view.expenseTable.model().columnCount(0))]
        self._view.dateInput.setDate(datetime.strptime(expenseList[1], '  %d/%m/%Y  '))
        self._view.valueInput.setText(expenseList[2])
        self._view.categoryInput.setCurrentText(expenseList[3])
        self._view.userInput.setCurrentText(expenseList[4])  

        displayString +="<span style=' font-weight:600;'>Date: "+str(expenseList[1])+"</span><br>"

        displayString +="Value: "+str(expenseList[2])+"<br>"  
        displayString +="Category: "+str(expenseList[3])+"<br>"
        displayString +="User: "+str(expenseList[4])+"<br>"
        self._view.displaySelection.setText(displayString)
        self.check_disable()
    
    @Slot()
    def addNewExpense(self):  
    
        date = self._view.dateInput.date().toPython() 
        value = self._view.valueInput.text()
        categoryIdx = self._view.categoryInput.currentIndex()
        userIdx = self._view.userInput.currentIndex()
        print("categoryIdx: ", categoryIdx, "userIdx: ", userIdx)
        self.db.insertExpenses(value, date, categoryIdx, userIdx)
        self.updateTableView()
        selectedDate =  self._view.dateFilter.currentIndex()
        self._view.dateFilter.setModel(self._models.getMonthsModel()) 
        self._view.dateFilter.setCurrentIndex(selectedDate)
        
    @Slot()
    def openUpdateWindow(self, index):
        row = index.row()
        expenseList = [self._view.expenseTable.model().index(row, col).data()
                    for col in range(self._view.expenseTable.model().columnCount(0))]
        if self._expenseForm is None:
            self._expenseForm = ExpenseForm()
     
        self._expenseForm.openUpdateWindow(expenseList, self._models)
        self._expenseForm.updateExpenseBtn.clicked.connect(self.updateExpense)
   

    def updateExpense(self):
        idx= self._expenseForm.updIndex.text()
        date = self._expenseForm.updDate.date().toPython() 
        value = self._expenseForm.updValue.text()
        categoryIdx = self._expenseForm.updCategory.currentIndex()
        userIdx = self._expenseForm.updUser.currentIndex()
        self.db.updateExpense(idx, date, value, categoryIdx, userIdx)
        self.updateTableView()
        selectedDate =  self._view.dateFilter.currentIndex()
        self._view.dateFilter.setModel(self._models.getMonthsModel()) 
        self._view.dateFilter.setCurrentIndex(selectedDate)      
        self._expenseForm.close()
        self._expenseForm = None


    @Slot()
    def openDeleteWindow(self, index):
        row = index.row()
        expenseList = [self._view.expenseTable.model().index(row, col).data()
                    for col in range(self._view.expenseTable.model().columnCount(0))]
        if self._expenseForm is None:
            self._expenseForm = ExpenseForm()
   
        self._expenseForm.openDeleteWindow(expenseList, self._models)
        self._expenseForm.deleteExpenseBtn.clicked.connect(self.deleteExpense)
        

    def deleteForm(self):
        self._expenseForm = None

    @Slot()
    def deleteExpense(self):
        idx= self._expenseForm.updIndex.text()
        # print(index.data(),"row:",index.row())  
        self.db.deleteExpense(idx)
        self.updateTableView()
        selectedDate =  self._view.dateFilter.currentIndex()
        self._view.dateFilter.setModel(self._models.getMonthsModel()) 
        self._view.dateFilter.setCurrentIndex(selectedDate)
        self._expenseForm.close() 
        self._expenseForm = None
       
        

    @Slot()
    def check_disable(self):
        #pass
        if not self._view.valueInput.text() or not self._view.userInput.currentText() or not self._view.categoryInput.currentText():
            self._view.addExpenseBtn.setEnabled(False)
        else:
            self._view.addExpenseBtn.setEnabled(True)
    
    def showMainWindow(self):
        self._view.show()

    def initializeMainWindow(self):
        self._view.show()