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
        self.db =  MyDatabase('expenses.db')
        self._models = Models(self.db)
     
        self._view.initializeView(self._models)
        self.connectSignals()
        # self.initializeMainWindow()
        
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
        #Checks when the ADD USER button is clicked
        self._view.addUserButton.clicked.connect(self.addNewUser)
        self._view.addCategoryButton.clicked.connect(self.addNewCategory)


        self._view.valueInput.textChanged[str].connect(self.check_disable)
        self._view.usersDataInput.textChanged[str].connect(self.check_username_isempty)
        self._view.categoryDataInput.textChanged[str].connect(self.check_category_isempty)
        self._view.categoryTypoeDataInput.textChanged[str].connect(self.check_category_isempty)
        self._view.userInput.activated.connect(self.check_disable)
        self._view.categoryInput.activated.connect(self.check_disable)

   
    def updateTableView(self):
        self._view.updateTableView(self._models)
 
    def updateDateView(self):
        self._view.updateDateView(self._models)
        
      
        
    @Slot()
    def getSelectedRowData(self, index):
        
        row = index.row()
        expenseList = [self._view.expenseTable.model().index(row, col).data()
                for col in range(self._view.expenseTable.model().columnCount(0))]
        self._view.getSelectedRowData(expenseList)
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
        self.updateDateView()
        
    @Slot()
    def openUpdateWindow(self, index):
        row = index.row()
        expenseList = [self._view.expenseTable.model().index(row, col).data()
                    for col in range(self._view.expenseTable.model().columnCount(0))]
        if self._expenseForm is None:
            self._expenseForm = ExpenseForm()
        self._expenseForm.openUpdateWindow(expenseList, self._models)
        self._expenseForm.updateExpenseBtn.clicked.connect(self.updateExpense)
        self._expenseForm.c.close.connect(self.deleteForm)
   

    def updateExpense(self):
        idx= self._expenseForm.updIndex.text()
        date = self._expenseForm.updDate.date().toPython() 
        value = self._expenseForm.updValue.text()
        categoryIdx = self._expenseForm.updCategory.currentIndex()
        userIdx = self._expenseForm.updUser.currentIndex()
        self.db.updateExpense(idx, date, value, categoryIdx, userIdx)
        self.updateTableView()
        self.updateDateView()      
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
        self._expenseForm.c.close.connect(self.deleteForm)
        
    @Slot()
    def deleteExpense(self):
        idx= self._expenseForm.updIndex.text()
        # print(index.data(),"row:",index.row())  
        self.db.deleteExpense(idx)
        self.updateTableView()
        self.updateDateView()
        self._expenseForm.close() 
        self._expenseForm = None
       

    def addNewUser(self):  
        df = self.db.getAllUsers()
        user = self._view.usersDataInput.text()
    
        exists = user in df['username'].values.tolist()
        if exists:
            self._view.messageLabel.setText('username exists')
            print(f"username exists?: {exists}")
        else:
            self.db.insertUsers(user)
            self._view.usersDataTable.setModel(self._models.getUsersModel())
            self._view.messageLabel.setText('')

    def addNewCategory(self):  
        df = self.db.getAllCategories()
        category = self._view.categoryDataInput.text()
        cattype = self._view.categoryTypoeDataInput.text()
    
        exists = category in df['category_name'].values.tolist()
        if exists:
            self._view.messageLabel.setText('Category already exists')
        else:
            self.db.insertCategories(category, cattype)
            self._view.categoryDataTable.setModel(self._models.getCategoriesTableModel())
            self._view.categoryDataTable.setColumnHidden(0, True)
            self._view.messageLabel.setText('')

       
    def deleteForm(self):
        self._expenseForm = None
    
    @Slot()
    def check_disable(self):
        #pass
        if not self._view.valueInput.text() or not self._view.userInput.currentText() or not self._view.categoryInput.currentText():
            self._view.addExpenseBtn.setEnabled(False)
        else:
            self._view.addExpenseBtn.setEnabled(True)

    def check_username_isempty(self):
        if not self._view.usersDataInput.text():
            self._view.addUserButton.setEnabled(False)
        else:
            self._view.addUserButton.setEnabled(True)
    
    def check_category_isempty(self):
        if not self._view.categoryDataInput.text() or not self._view.categoryTypoeDataInput.text():
            self._view.addCategoryButton.setEnabled(False)
        else:
            self._view.addCategoryButton.setEnabled(True)


     