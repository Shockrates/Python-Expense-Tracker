# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1205, 835)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(20, 16))
        self.input_tab = QWidget()
        self.input_tab.setObjectName(u"input_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.input_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.expenseTableGroup = QGroupBox(self.input_tab)
        self.expenseTableGroup.setObjectName(u"expenseTableGroup")
        self.verticalLayout = QVBoxLayout(self.expenseTableGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filtersGroup = QGroupBox(self.expenseTableGroup)
        self.filtersGroup.setObjectName(u"filtersGroup")
        self.filtersGroup.setMinimumSize(QSize(800, 0))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        self.filtersGroup.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.filtersGroup)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dateLbl = QLabel(self.filtersGroup)
        self.dateLbl.setObjectName(u"dateLbl")
        self.dateLbl.setMinimumSize(QSize(60, 0))
        self.dateLbl.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        font1.setKerning(True)
        self.dateLbl.setFont(font1)

        self.horizontalLayout_3.addWidget(self.dateLbl, 0, Qt.AlignRight)

        self.dateFilter = QComboBox(self.filtersGroup)
        self.dateFilter.setObjectName(u"dateFilter")
        self.dateFilter.setMinimumSize(QSize(150, 25))

        self.horizontalLayout_3.addWidget(self.dateFilter)

        self.userLbl = QLabel(self.filtersGroup)
        self.userLbl.setObjectName(u"userLbl")
        self.userLbl.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(12)
        self.userLbl.setFont(font2)

        self.horizontalLayout_3.addWidget(self.userLbl, 0, Qt.AlignRight)

        self.userFilter = QComboBox(self.filtersGroup)
        self.userFilter.setObjectName(u"userFilter")
        self.userFilter.setMinimumSize(QSize(150, 25))

        self.horizontalLayout_3.addWidget(self.userFilter)

        self.categoryLbl = QLabel(self.filtersGroup)
        self.categoryLbl.setObjectName(u"categoryLbl")
        self.categoryLbl.setMaximumSize(QSize(100, 16777215))
        self.categoryLbl.setFont(font2)

        self.horizontalLayout_3.addWidget(self.categoryLbl, 0, Qt.AlignRight)

        self.categoryFilter = QComboBox(self.filtersGroup)
        self.categoryFilter.setObjectName(u"categoryFilter")
        self.categoryFilter.setMinimumSize(QSize(150, 25))

        self.horizontalLayout_3.addWidget(self.categoryFilter)


        self.verticalLayout.addWidget(self.filtersGroup)

        self.expenseTable = QTableView(self.expenseTableGroup)
        self.expenseTable.setObjectName(u"expenseTable")
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(16)
        self.expenseTable.setFont(font3)

        self.verticalLayout.addWidget(self.expenseTable)


        self.horizontalLayout_4.addWidget(self.expenseTableGroup)

        self.verticalGroupBox = QGroupBox(self.input_tab)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.inputGroup = QGroupBox(self.verticalGroupBox)
        self.inputGroup.setObjectName(u"inputGroup")
        self.inputGroup.setMinimumSize(QSize(0, 200))
        self.inputGroup.setMaximumSize(QSize(16777215, 250))
        self.inputGroup.setFont(font)
        self.gridLayout = QGridLayout(self.inputGroup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.categoryInputlbl = QLabel(self.inputGroup)
        self.categoryInputlbl.setObjectName(u"categoryInputlbl")

        self.gridLayout.addWidget(self.categoryInputlbl, 3, 0, 1, 1, Qt.AlignRight)

        self.dateInput = QDateEdit(self.inputGroup)
        self.dateInput.setObjectName(u"dateInput")
        self.dateInput.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateInput, 0, 1, 1, 1)

        self.addExpenseBtn = QPushButton(self.inputGroup)
        self.addExpenseBtn.setObjectName(u"addExpenseBtn")
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.addExpenseBtn.setFont(font4)

        self.gridLayout.addWidget(self.addExpenseBtn, 4, 0, 1, 2)

        self.valueInputLbl = QLabel(self.inputGroup)
        self.valueInputLbl.setObjectName(u"valueInputLbl")
        self.valueInputLbl.setMinimumSize(QSize(40, 0))
        self.valueInputLbl.setFont(font)

        self.gridLayout.addWidget(self.valueInputLbl, 1, 0, 1, 1, Qt.AlignRight)

        self.valueInput = QLineEdit(self.inputGroup)
        self.valueInput.setObjectName(u"valueInput")
        self.valueInput.setMinimumSize(QSize(130, 0))
        self.valueInput.setFont(font3)

        self.gridLayout.addWidget(self.valueInput, 1, 1, 1, 1, Qt.AlignVCenter)

        self.userInputLbl = QLabel(self.inputGroup)
        self.userInputLbl.setObjectName(u"userInputLbl")

        self.gridLayout.addWidget(self.userInputLbl, 2, 0, 1, 1, Qt.AlignRight)

        self.categoryInput = QComboBox(self.inputGroup)
        self.categoryInput.setObjectName(u"categoryInput")

        self.gridLayout.addWidget(self.categoryInput, 3, 1, 1, 1, Qt.AlignVCenter)

        self.userInput = QComboBox(self.inputGroup)
        self.userInput.setObjectName(u"userInput")

        self.gridLayout.addWidget(self.userInput, 2, 1, 1, 1)

        self.dateInputLbl = QLabel(self.inputGroup)
        self.dateInputLbl.setObjectName(u"dateInputLbl")

        self.gridLayout.addWidget(self.dateInputLbl, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.inputGroup)

        self.displaySelection = QTextEdit(self.verticalGroupBox)
        self.displaySelection.setObjectName(u"displaySelection")
        self.displaySelection.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout_2.addWidget(self.displaySelection)


        self.horizontalLayout_4.addWidget(self.verticalGroupBox)

        self.tabWidget.addTab(self.input_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridGroupBox = QGroupBox(self.tab_2)
        self.gridGroupBox.setObjectName(u"gridGroupBox")
        self.gridGroupBox.setGeometry(QRect(10, 10, 821, 571))
        self.gridGroupBox.setFont(font3)
        self.gridLayout_2 = QGridLayout(self.gridGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, -1, -1, -1)
        self.usersDataLabel = QLabel(self.gridGroupBox)
        self.usersDataLabel.setObjectName(u"usersDataLabel")

        self.gridLayout_2.addWidget(self.usersDataLabel, 1, 0, 1, 1)

        self.categoryDataTable = QTableView(self.gridGroupBox)
        self.categoryDataTable.setObjectName(u"categoryDataTable")
        self.categoryDataTable.setMaximumSize(QSize(460, 16777215))

        self.gridLayout_2.addWidget(self.categoryDataTable, 2, 1, 1, 1)

        self.usersDataTable = QListView(self.gridGroupBox)
        self.usersDataTable.setObjectName(u"usersDataTable")
        self.usersDataTable.setMinimumSize(QSize(230, 0))
        self.usersDataTable.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self.usersDataTable, 2, 0, 1, 1, Qt.AlignLeft)

        self.categoryDataLabel = QLabel(self.gridGroupBox)
        self.categoryDataLabel.setObjectName(u"categoryDataLabel")

        self.gridLayout_2.addWidget(self.categoryDataLabel, 1, 1, 1, 1)

        self.usersDataInput = QLineEdit(self.gridGroupBox)
        self.usersDataInput.setObjectName(u"usersDataInput")
        self.usersDataInput.setMinimumSize(QSize(230, 0))
        self.usersDataInput.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self.usersDataInput, 3, 0, 1, 1)

        self.dataInputGroup = QGroupBox(self.gridGroupBox)
        self.dataInputGroup.setObjectName(u"dataInputGroup")
        self.dataInputGroup.setMaximumSize(QSize(462, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.dataInputGroup)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.categoryDataInput = QLineEdit(self.dataInputGroup)
        self.categoryDataInput.setObjectName(u"categoryDataInput")
        self.categoryDataInput.setMinimumSize(QSize(220, 0))
        self.categoryDataInput.setMaximumSize(QSize(230, 16777215))

        self.horizontalLayout_2.addWidget(self.categoryDataInput)

        self.categoryTypoeDataInput = QLineEdit(self.dataInputGroup)
        self.categoryTypoeDataInput.setObjectName(u"categoryTypoeDataInput")
        self.categoryTypoeDataInput.setMinimumSize(QSize(220, 0))
        self.categoryTypoeDataInput.setMaximumSize(QSize(230, 16777215))

        self.horizontalLayout_2.addWidget(self.categoryTypoeDataInput, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.dataInputGroup, 3, 1, 1, 1)

        self.addUserButton = QPushButton(self.gridGroupBox)
        self.addUserButton.setObjectName(u"addUserButton")

        self.gridLayout_2.addWidget(self.addUserButton, 4, 0, 1, 1)

        self.addCategoryButton = QPushButton(self.gridGroupBox)
        self.addCategoryButton.setObjectName(u"addCategoryButton")

        self.gridLayout_2.addWidget(self.addCategoryButton, 4, 1, 1, 1)

        self.messageLabel = QLabel(self.gridGroupBox)
        self.messageLabel.setObjectName(u"messageLabel")

        self.gridLayout_2.addWidget(self.messageLabel, 5, 0, 1, 2, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1205, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dateLbl.setText(QCoreApplication.translate("MainWindow", u"\u0397\u039c\u0395\u03a1\u039f\u039c\u0397\u039d\u0399\u0391:", None))
        self.userLbl.setText(QCoreApplication.translate("MainWindow", u"\u03a7\u03a1\u0397\u03a3\u03a4\u0397\u03a3:", None))
        self.categoryLbl.setText(QCoreApplication.translate("MainWindow", u"\u039a\u0391\u03a4\u0397\u0393\u039f\u03a1\u0399\u0391:", None))
        self.categoryInputlbl.setText(QCoreApplication.translate("MainWindow", u"\u039a\u0391\u03a4\u0397\u0393\u039f\u03a1\u0399\u0391:", None))
        self.addExpenseBtn.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03a1\u039f\u03a3\u0398\u0397\u039a\u0397", None))
        self.valueInputLbl.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u039f\u03a3\u039f:", None))
        self.userInputLbl.setText(QCoreApplication.translate("MainWindow", u"\u03a7\u03a1\u0397\u03a3\u03a4\u0397\u03a3:", None))
        self.dateInputLbl.setText(QCoreApplication.translate("MainWindow", u"\u0397\u039c\u0395\u03a1\u039f\u039c\u0397\u039d\u0399\u0391:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.input_tab), QCoreApplication.translate("MainWindow", u"\u0395\u0399\u03a3\u0391\u0393\u03a9\u0393\u0397", None))
        self.usersDataLabel.setText(QCoreApplication.translate("MainWindow", u"\u03a7\u03c1\u03ae\u03c3\u03c4\u03b5\u03c2", None))
        self.categoryDataLabel.setText(QCoreApplication.translate("MainWindow", u"\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2", None))
        self.addUserButton.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03a7\u03c1\u03ae\u03c3\u03c4\u03b7", None))
        self.addCategoryButton.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1\u03c2", None))
        self.messageLabel.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

