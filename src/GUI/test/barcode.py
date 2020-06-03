# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'barcode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import resource
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 615)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(20, 10, 97, 29))
        self.importBtn.setObjectName("importBtn")
        self.exportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportBtn.setGeometry(QtCore.QRect(150, 10, 97, 29))
        self.exportBtn.setObjectName("exportBtn")
        self.fileList = QtWidgets.QTableWidget(self.centralwidget)
        self.fileList.setGeometry(QtCore.QRect(20, 50, 1051, 192))
        self.fileList.setObjectName("fileList")
        self.fileList.setColumnCount(5)
        self.fileList.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fileList.setItem(2, 4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 250, 72, 16))
        self.label.setObjectName("label")
        self.totalFileNum = QtWidgets.QLabel(self.centralwidget)
        self.totalFileNum.setGeometry(QtCore.QRect(160, 250, 72, 16))
        self.totalFileNum.setObjectName("totalFileNum")
        self.resultList = QtWidgets.QTableWidget(self.centralwidget)
        self.resultList.setGeometry(QtCore.QRect(20, 310, 1051, 192))
        self.resultList.setObjectName("resultList")
        self.resultList.setColumnCount(4)
        self.resultList.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setItem(1, 3, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 72, 16))
        self.label_3.setObjectName("label_3")
        self.scanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.scanBtn.setGeometry(QtCore.QRect(970, 260, 97, 29))
        self.scanBtn.setObjectName("scanBtn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 520, 72, 16))
        self.label_4.setObjectName("label_4")
        self.successScanNum = QtWidgets.QLabel(self.centralwidget)
        self.successScanNum.setGeometry(QtCore.QRect(120, 520, 72, 16))
        self.successScanNum.setObjectName("successScanNum")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 520, 72, 16))
        self.label_6.setObjectName("label_6")
        self.failScanNum = QtWidgets.QLabel(self.centralwidget)
        self.failScanNum.setGeometry(QtCore.QRect(280, 520, 72, 16))
        self.failScanNum.setObjectName("failScanNum")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(970, 520, 97, 29))
        self.exitBtn.setObjectName("exitBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.importBtn.setText(_translate("MainWindow", "导入"))
        self.exportBtn.setText(_translate("MainWindow", "导出"))
        item = self.fileList.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "第一行"))
        item = self.fileList.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "第二行"))
        item = self.fileList.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "第三行"))
        item = self.fileList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.fileList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "大小"))
        item = self.fileList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "位置"))
        item = self.fileList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "创建日期"))
        item = self.fileList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "修改日期"))
        __sortingEnabled = self.fileList.isSortingEnabled()
        self.fileList.setSortingEnabled(False)
        item = self.fileList.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.fileList.item(0, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.fileList.item(0, 2)
        item.setText(_translate("MainWindow", "1"))
        item = self.fileList.item(0, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.fileList.item(0, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.fileList.item(1, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.fileList.item(1, 1)
        item.setText(_translate("MainWindow", "2"))
        item = self.fileList.item(1, 2)
        item.setText(_translate("MainWindow", "2"))
        item = self.fileList.item(1, 3)
        item.setText(_translate("MainWindow", "2"))
        item = self.fileList.item(1, 4)
        item.setText(_translate("MainWindow", "2"))
        item = self.fileList.item(2, 0)
        item.setText(_translate("MainWindow", "3"))
        item = self.fileList.item(2, 1)
        item.setText(_translate("MainWindow", "3"))
        item = self.fileList.item(2, 2)
        item.setText(_translate("MainWindow", "3"))
        item = self.fileList.item(2, 3)
        item.setText(_translate("MainWindow", "3"))
        item = self.fileList.item(2, 4)
        item.setText(_translate("MainWindow", "3"))
        self.fileList.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "文件数:"))
        self.totalFileNum.setText(_translate("MainWindow", "0"))
        item = self.resultList.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "第一行"))
        item = self.resultList.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "第二行"))
        item = self.resultList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.resultList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "状态"))
        item = self.resultList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "格式"))
        item = self.resultList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "值"))
        __sortingEnabled = self.resultList.isSortingEnabled()
        self.resultList.setSortingEnabled(False)
        item = self.resultList.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.resultList.item(0, 1)
        item.setText(_translate("MainWindow", "1"))
        item = self.resultList.item(0, 2)
        item.setText(_translate("MainWindow", "1"))
        item = self.resultList.item(0, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.resultList.item(1, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.resultList.item(1, 1)
        item.setText(_translate("MainWindow", "2"))
        item = self.resultList.item(1, 2)
        item.setText(_translate("MainWindow", "2"))
        item = self.resultList.item(1, 3)
        item.setText(_translate("MainWindow", "2"))
        self.resultList.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "结果:"))
        self.scanBtn.setText(_translate("MainWindow", "扫描"))
        self.label_4.setText(_translate("MainWindow", "扫描成功:"))
        self.successScanNum.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "扫描失败:"))
        self.failScanNum.setText(_translate("MainWindow", "0"))
        self.exitBtn.setText(_translate("MainWindow", "退出"))
