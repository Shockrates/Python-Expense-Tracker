from resources.expenseform import Ui_Form
from PySide2.QtWidgets import QMainWindow

class ExpenseForm(QMainWindow, Ui_Form):
    def __init__(self):
        super(ExpenseForm, self).__init__()
        self.setupUi(self)