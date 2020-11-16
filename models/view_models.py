from PySide2.QtCore import Qt
from PySide2 import QtCore,QtGui
from datetime import datetime

from database.db import MyDatabase

class Models:
    def __init__(self, db):
        # self.db = MyDatabase('expenses.db')
        self.db = db
        

    def getExpenseModel(self, month, category, user):
        df = self.db.getAllExpenses()
        filteredData = df.loc[(df['date'].str.contains(pat = month)) & (df['username'].str.contains(pat = user)) & (df['category_name'].str.contains(pat = category))]
        self.total = filteredData['value'].sum().round(3)
        # print(filteredData)
        self.dfModel = ExpensesAbstractTableModel(data=filteredData)
        return self.dfModel

    def getMonthsModel(self):
        df = self.db.getAllMonths()
        self.dfModel = MonthsAbstractListModel(data= df['Months'])
        # print( df['Months'])
        return self.dfModel

    def getUsersModel(self):
        df = self.db.getAllUsers()
        self.dfModel = UsersAbstractListModel(data= df['username'])
        return self.dfModel
    
    def getCategoriesModel(self):
        df = self.db.getAllCategoriesName()
        self.dfModel = CategoriesAbstractListModel(data= df['category_name'])
        return self.dfModel

    def getCategoriesTableModel(self):
        df = self.db.getAllCategories()
        self.dfModel = CategoriesAbstractTableModel(data= df)
        return self.dfModel

class ExpensesAbstractTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(ExpensesAbstractTableModel, self).__init__()
        self._data = data
        

    def rowCount(self, index):
        return len(self._data.values)

    def columnCount(self, index):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                #value = str(self._data.values[index.row()][index.column()])
                value = str(self._data.iloc[index.row(),index.column()])
                if index.column() == 1: 
                    if len(value) == 0: 
                        return value 
                    else:
                        date_time_obj=datetime.strptime(value, '%Y-%m-%d').date()
                        return  '  %s  ' % date_time_obj.strftime("%d/%m/%Y")
                if isinstance(value, float):
                    # Render float to 2 dp
                    return "%.20f" % value
                value = value + "   "
                return value
        return None
    
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Id", "  Date  ", "  Value  ", "  Name  ", "  Category  ", "  Description  ",   " Edit ", " Delete ")[section]
        else:
            return "{}".format(section)


class MonthsAbstractListModel(QtCore.QAbstractListModel):
    def __init__(self, data):
        super(MonthsAbstractListModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            
            value = str(self._data.iloc[index.row()])
            if len(value) == 0:
                return None
            else:
                return  datetime.strptime(value, "%m-%Y").strftime("%B-%Y")    
                # date_object = datetime.strptime(value, "%m-%Y")
                # return date_object.strftime("%B-%Y")
                
            #return text
           
    def rowCount(self, index):
            return len(self._data.values)


class UsersAbstractListModel(QtCore.QAbstractListModel):
    def __init__(self, data):
        super(UsersAbstractListModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = str(self._data.iloc[index.row()])
            return value

    def rowCount(self, index):
        return len(self._data.values)


class CategoriesAbstractListModel(QtCore.QAbstractListModel):
    def __init__(self, data):
        super(CategoriesAbstractListModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = str(self._data.iloc[index.row()])
            return value

    def rowCount(self, index):
        return len(self._data.values)

class CategoriesAbstractTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(CategoriesAbstractTableModel, self).__init__()
        self._data = data
        

    def rowCount(self, index):
        return len(self._data.values)

    def columnCount(self, index):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                #value = str(self._data.values[index.row()][index.column()])
                value = str(self._data.iloc[index.row(),index.column()])
                strValue = value+"  "
                return strValue
        return None
    
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("id", "  Category  ", "  Description  ")[section]
        else:
            return "{}".format(section)