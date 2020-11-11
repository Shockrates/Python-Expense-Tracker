from PySide2.QtCore import QObject, QRegExp, QSortFilterProxyModel, Qt, SIGNAL, Slot
from PySide2.QtGui import QFont
from datetime import datetime, date
# from models.expensesAbstractTableModel import ExpensesAbstractTableModel
# from models.categoriesAbstractTableModel import CategoriesAbstractListModel
# from models.usersAbstractListModel import UsersAbstractListModel
# from models.monthsAbstractListModel import MonthsAbstractListModel
from models.view_models import Models
from database.db import MyDatabase

class MainController(QObject):
    def __init__(self, view):
        super().__init__()
        self._view = view
        self._models = Models()
        
       
        
        self._view.userFilter.setModel(self._models.getUsersModel())
        self._view.categoryFilter.setModel(self._models.getCategoriesModel())
        self._view.dateFilter.setModel(self._models.getMonthsModel())
        curIndex=self._view.dateFilter.findText(date.today().strftime("%B-%Y"))
        self._view.dateFilter.setCurrentIndex(curIndex)

        self._view.categoryInput.setModel(self._models.getCategoriesModel())
        self._view.userInput.setModel(self._models.getUsersModel())

        
        self.updateTableView()
        self.connectSignals()

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

        #checks when the "UPDATE EXPENSE (ΕΝΗΜΕΡΩΣΗ)" button is pressed
        #self._view.expenseForm.updateExpenseBtn.clicked.connect(self.updateExpense)
        #checks when the "DELETE EXPENSE (ΔΙΑΓΑΡΦΗ)" button is pressed
        self._view.expenseForm.clicked.connect(self.deleteExpense)


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
        #self._view.testLineEdit.setText(str(self._expensesModel.getTotal()))
    
    @Slot()
    def getSelectedRowData(self, index):
        font = QFont
        displayString = ''
        selected_indexes = self._view.expenseTable.selectionModel().selectedRows()  
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

            db =  MyDatabase('expenses.db')
            db.insertExpenses(value, date, categoryIdx, userIdx)
            self.updateTableView()
            self._view.dateFilter.setModel(self._models.getMonthsModel())      

    @Slot()
    def openUpdateWindow(self, index):
      
        selected_indexes = self._view.expenseTable.selectionModel().selectedRows()  
        
        row = index.row()
        expenseList = [self._view.expenseTable.model().index(row, col).data()
                    for col in range(self._view.expenseTable.model().columnCount(0))]
        self._view.expenseForm.updIndex.setText(expenseList[0])            
        self._view.expenseForm.updDate.setDate(datetime.strptime(expenseList[1], '  %d/%m/%Y  '))
        self._view.expenseForm.updValue.setText(expenseList[2])
        self._view.expenseForm.updCategory.setCurrentText(expenseList[3])
        self._view.expenseForm.updUser.setCurrentText(expenseList[4])
        self._view.expenseForm.updateExpenseBtn.show()
        self._view.expenseForm.deleteExpenseBtn.hide()
        self._view.expenseForm.show()

    @Slot()
    def openDeleteWindow(self, index):
        categoryModel = self._models.getCategoriesModel()
        userModel = self._models.getUsersModel()
        self._view.openDeleteWindow(index, categoryModel, userModel)

        # selected_indexes = self._view.expenseTable.selectionModel().selectedRows()  
        # row = index.row()
        # expenseList = [self._view.expenseTable.model().index(row, col).data()
        #             for col in range(self._view.expenseTable.model().columnCount(0))]
        # self._view.expenseForm.updIndex.setText(expenseList[0])            
        # self._view.expenseForm.updDate.setDate(datetime.strptime(expenseList[1], '  %d/%m/%Y  '))
        # self._view.expenseForm.updDate.setReadOnly(True)
        # self._view.expenseForm.updValue.setText(expenseList[2])
        # self._view.expenseForm.updValue.setReadOnly(True)
        # self._view.expenseForm.updCategory.setCurrentText(expenseList[3])
        # self._view.expenseForm.updCategory.setEnabled(False)
        # self._view.expenseForm.updUser.setCurrentText(expenseList[4])
        # self._view.expenseForm.updUser.setEnabled(False)
        # self._view.expenseForm.updateExpenseBtn.hide()
        # self._view.expenseForm.deleteExpenseBtn.show()
        # self._view.expenseForm.show()
    @Slot()
    def deleteExpense(self):
        idx= self._view.expenseForm.updIndex.text()
        # print(index.data(),"row:",index.row())  
        self.db.deleteExpense(idx)
        self.updateTableView()
        self._view.dateFilter.setModel(self._models.getMonthsModel())  
        self._view.expenseForm.close()


    @Slot()
    def check_disable(self):
        #pass
        if not self._view.valueInput.text() or not self._view.userInput.currentText() or not self._view.categoryInput.currentText():
            self._view.addExpenseBtn.setEnabled(False)
        else:
            self._view.addExpenseBtn.setEnabled(True)