# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 300)
        self.updateExpenseBtn = QPushButton(Form)
        self.updateExpenseBtn.setObjectName(u"updateExpenseBtn")
        self.updateExpenseBtn.setGeometry(QRect(170, 230, 160, 40))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.updateExpenseBtn.setFont(font)
        self.editExpenseBox = QGroupBox(Form)
        self.editExpenseBox.setObjectName(u"editExpenseBox")
        self.editExpenseBox.setGeometry(QRect(10, 10, 480, 200))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(14)
        self.editExpenseBox.setFont(font1)
        self.updDate = QDateEdit(self.editExpenseBox)
        self.updDate.setObjectName(u"updDate")
        self.updDate.setGeometry(QRect(190, 40, 170, 25))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(16)
        self.updDate.setFont(font2)
        self.updDate.setCalendarPopup(True)
        self.updUser = QComboBox(self.editExpenseBox)
        self.updUser.setObjectName(u"updUser")
        self.updUser.setGeometry(QRect(190, 160, 170, 30))
        self.updCategory = QComboBox(self.editExpenseBox)
        self.updCategory.setObjectName(u"updCategory")
        self.updCategory.setGeometry(QRect(190, 120, 170, 30))
        self.updValue = QLineEdit(self.editExpenseBox)
        self.updValue.setObjectName(u"updValue")
        self.updValue.setGeometry(QRect(190, 80, 170, 30))
        self.updValue.setFont(font2)
        self.updCategoryLbl = QLabel(self.editExpenseBox)
        self.updCategoryLbl.setObjectName(u"updCategoryLbl")
        self.updCategoryLbl.setGeometry(QRect(80, 120, 91, 21))
        self.updCategoryLbl.setFont(font1)
        self.updValueLbl = QLabel(self.editExpenseBox)
        self.updValueLbl.setObjectName(u"updValueLbl")
        self.updValueLbl.setGeometry(QRect(80, 80, 81, 21))
        self.updValueLbl.setFont(font1)
        self.updUserLbl = QLabel(self.editExpenseBox)
        self.updUserLbl.setObjectName(u"updUserLbl")
        self.updUserLbl.setGeometry(QRect(80, 160, 81, 21))
        self.updUserLbl.setFont(font1)
        self.updDateLbl = QLabel(self.editExpenseBox)
        self.updDateLbl.setObjectName(u"updDateLbl")
        self.updDateLbl.setGeometry(QRect(80, 40, 111, 21))
        self.updDateLbl.setFont(font1)
        self.updIndexLbl = QLabel(self.editExpenseBox)
        self.updIndexLbl.setObjectName(u"updIndexLbl")
        self.updIndexLbl.setGeometry(QRect(80, 0, 111, 21))
        self.updIndexLbl.setFont(font1)
        self.updIndex = QLineEdit(self.editExpenseBox)
        self.updIndex.setObjectName(u"updIndex")
        self.updIndex.setGeometry(QRect(190, 0, 41, 25))
        self.updIndex.setFont(font2)
        self.updIndex.setReadOnly(True)
        self.deleteExpenseBtn = QPushButton(Form)
        self.deleteExpenseBtn.setObjectName(u"deleteExpenseBtn")
        self.deleteExpenseBtn.setEnabled(True)
        self.deleteExpenseBtn.setGeometry(QRect(170, 230, 160, 40))
        self.deleteExpenseBtn.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0395\u03bd\u03b7\u03bc\u03ad\u03c1\u03c9\u03c3\u03b7 \u0395\u03b3\u03c1\u03b1\u03c6\u03ae\u03c2", None))
        self.updateExpenseBtn.setText(QCoreApplication.translate("Form", u"\u0395\u039d\u0397\u039c\u0395\u03a1\u03a9\u03a3\u0397", None))
        self.editExpenseBox.setTitle("")
        self.updValue.setText("")
        self.updCategoryLbl.setText(QCoreApplication.translate("Form", u"\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1:", None))
        self.updValueLbl.setText(QCoreApplication.translate("Form", u"\u03a4\u03b9\u03bc\u03ae:", None))
        self.updUserLbl.setText(QCoreApplication.translate("Form", u"\u03a7\u03c1\u03ae\u03c3\u03c4\u03b7\u03c2:", None))
        self.updDateLbl.setText(QCoreApplication.translate("Form", u"\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1:", None))
        self.updIndexLbl.setText(QCoreApplication.translate("Form", u"AA:", None))
        self.updIndex.setText("")
        self.deleteExpenseBtn.setText(QCoreApplication.translate("Form", u"\u0394\u0399\u0391\u0393\u03a1\u0391\u03a6\u0397", None))
    # retranslateUi

