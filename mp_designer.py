# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mp.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql


class Ui_MainWindow(object):
    def initDatabase(self):
        self.conn = sql.connect('mydatabase.sqlite3')
        item_table = """CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT, item VARCHAR(255) ,prices DOUBLE)"""
        try:
            self.conn.execute(item_table)
            self.conn.commit()
        except Exception as e:
            print(e)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 356)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enter_item = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.enter_item.setGeometry(QtCore.QRect(0, 20, 181, 21))
        self.enter_item.setObjectName("enter_item")
        self.enter_price = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.enter_price.setGeometry(QtCore.QRect(180, 20, 181, 21))
        self.enter_price.setObjectName("enter_price")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(374, 20, 101, 23))
        self.btn_add.setStyleSheet("background-color:#55aaff")
        self.btn_add.setObjectName("btn_add")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(0, 40, 311, 211))
        self.list.setObjectName("list")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(310, 60, 171, 23))
        self.btn_search.setStyleSheet("background-color:#55aaff")
        self.btn_search.setObjectName("btn_search")
        self.btn_view = QtWidgets.QPushButton(self.centralwidget)
        self.btn_view.setGeometry(QtCore.QRect(310, 200, 171, 23))
        self.btn_view.setStyleSheet("background-color:#55aaff")
        self.btn_view.setObjectName("btn_view")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(310, 230, 171, 23))
        self.btn_clear.setStyleSheet("background-color:#55aaff")
        self.btn_clear.setObjectName("btn_clear")
        self.enter_item_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.enter_item_2.setGeometry(QtCore.QRect(310, 100, 181, 21))
        self.enter_item_2.setObjectName("enter_item_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 260, 169, 23))
        self.label.setObjectName("label")
        self.sum = QtWidgets.QLabel(self.centralwidget)
        self.sum.setGeometry(QtCore.QRect(200, 260, 151, 21))
        self.sum.setObjectName("sum")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(390, 260, 81, 31))
        self.date.setObjectName("date")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 47, 13))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.initDatabase()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_add.clicked.connect(self.addItem)
        self.btn_search.clicked.connect(self.searchItem)
        self.btn_view.clicked.connect(self.viewItem)
        self.btn_clear.clicked.connect(self.clearItem)
        self.displayData()
        self.addValues()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add.setText(_translate("MainWindow", "ADD"))
        self.btn_search.setText(_translate("MainWindow", "SEARCH"))
        self.btn_view.setText(_translate("MainWindow", "VIEW"))
        self.btn_clear.setText(_translate("MainWindow", "CLEAR"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#00007f;\">TOTAL EXPENSES</span></p></body></html>"))
        self.sum.setText(_translate("MainWindow", "TextLabel"))
        self.date.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00007f;\">ENTER</span></p></body></html>"))

    def addItem(self):
        item = self.enter_item.toPlainText()
        price = self.enter_price.toPlainText()
        if item and price:
            self.addData(itemName=item, priceV=price)
        else:
            self.enter_item.setPlaceholderText("Enter Item to be added")
            self.enter_price.setPlaceholderText("Enter Price of the Item")
        self.addValues()
        self.clearItem()

    def searchItem(self):
        itemSearch = self.enter_item_2.toPlainText()
        if itemSearch:
            search = f"""SELECT * FROM data WHERE item LIKE '%{itemSearch}%' """
            try:
                result = self.conn.execute(search)
                iSearch = result.fetchall()
                self.displaySingleData(iSearch)
            except Exception as e:
                print(e)

    def viewItem(self):
        pass

    def clearItem(self):
        self.enter_item.clear()
        self.enter_price.clear()

    def addValues(self):
        sumV = """SELECT SUM(prices) FROM data"""
        result = self.conn.execute(sumV)
        itemSum = result.fetchall()
        self.sum.setText(str(itemSum[0][0]))

    def displayData(self):
        display = """SELECT * FROM data"""
        result = self.conn.execute(display)
        itemList = result.fetchall()
        self.list.clear()
        for item in itemList:
            name = item[1]
            price = item[2]
            self.list.addItem(f'{name}    {price}')

    def displaySingleData(self, data):
        self.list.clear()
        for d in data:
            self.list.addItem(f'{d[0]}\t{d[1]}\t{d[2]}')


def addData(self, itemName, priceV):
    add = """INSERT INTO data VALUES(null,'{}','{}')""".format(itemName, priceV)
    try:
        self.conn.execute(add)
        self.conn.commit()
    except Exception as e:
        print(e)
    self.displayData()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
