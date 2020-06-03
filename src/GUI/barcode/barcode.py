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
        MainWindow.resize(1268, 711)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.96)
        MainWindow.setStyleSheet("background:white;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.scanBtn.setGeometry(QtCore.QRect(870, 340, 141, 29))
        self.scanBtn.setStyleSheet("background:#41B883;\n"
"color:white;\n"
"font-family:黑体;\n"
"")
        self.scanBtn.setObjectName("scanBtn")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(1120, 670, 97, 29))
        self.exitBtn.setStyleSheet("background:#F76260;\n"
"color:white;\n"
"font-family:黑体;")
        self.exitBtn.setObjectName("exitBtn")
        self.exportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportBtn.setGeometry(QtCore.QRect(270, 20, 97, 29))
        self.exportBtn.setStyleSheet("background:#41B883;\n"
"color:white;\n"
"font-family:黑体;\n"
"")
        self.exportBtn.setObjectName("exportBtn")
        self.importBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(70, 20, 97, 29))
        self.importBtn.setStyleSheet("background:#41B883;\n"
"color:white;\n"
"font-family:黑体;\n"
"")
        self.importBtn.setObjectName("importBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 320, 70, 20))
        self.label.setStyleSheet("font-family:黑体;\n"
"font-size:20px;")
        self.label.setObjectName("label")
        self.fileList = QtWidgets.QTableWidget(self.centralwidget)
        self.fileList.setGeometry(QtCore.QRect(20, 60, 1231, 251))
        self.fileList.setStyleSheet("opcity:0.9;")
        self.fileList.setObjectName("fileList")
        self.fileList.setColumnCount(5)
        self.fileList.setRowCount(0)
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 360, 50, 20))
        self.label_2.setStyleSheet("font-family:黑体;\n"
"font-size:20px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 670, 90, 20))
        self.label_3.setStyleSheet("font-family:黑体;\n"
"font-size:20px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 670, 90, 20))
        self.label_4.setStyleSheet("font-family:黑体;\n"
"font-size:20px;")
        self.label_4.setObjectName("label_4")
        self.resultList = QtWidgets.QTableWidget(self.centralwidget)
        self.resultList.setGeometry(QtCore.QRect(15, 391, 1231, 261))
        self.resultList.setObjectName("resultList")
        self.resultList.setColumnCount(4)
        self.resultList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultList.setHorizontalHeaderItem(3, item)
        self.totalFile = QtWidgets.QLabel(self.centralwidget)
        self.totalFile.setGeometry(QtCore.QRect(100, 320, 41, 20))
        self.totalFile.setStyleSheet("font-family:黑体;\n"
"font-size:20px;")
        self.totalFile.setObjectName("totalFile")
        self.successScan = QtWidgets.QLabel(self.centralwidget)
        self.successScan.setGeometry(QtCore.QRect(210, 670, 41, 20))
        self.successScan.setStyleSheet("font-family:黑体;\n"
"font-size:20px;\n"
"color:green;")
        self.successScan.setObjectName("successScan")
        self.failScan = QtWidgets.QLabel(self.centralwidget)
        self.failScan.setGeometry(QtCore.QRect(380, 670, 41, 20))
        self.failScan.setStyleSheet("font-family:黑体;\n"
"font-size:20px;\n"
"color:red;")
        self.failScan.setObjectName("failScan")
        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(150, 340, 651, 30))
        self.prompt.setStyleSheet("font-family:黑体;\n"
"font-size:30px;\n"
"color:#41B883;")
        self.prompt.setText("")
        self.prompt.setObjectName("prompt")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 30, 360, 20))
        self.label_5.setStyleSheet("font-family:黑体;\n"
"font-size:20px;")
        self.label_5.setObjectName("label_5")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(1100, 340, 141, 29))
        self.saveBtn.setStyleSheet("background:#41B883;\n"
"color:white;\n"
"font-family:黑体;\n"
"")
        self.saveBtn.setObjectName("saveBtn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 20, 30, 30))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(830, 340, 30, 30))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1060, 340, 30, 30))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1080, 670, 30, 30))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "条形码扫描王"))
        self.scanBtn.setText(_translate("MainWindow", "扫描"))
        self.exitBtn.setText(_translate("MainWindow", "退出程序"))
        self.exportBtn.setText(_translate("MainWindow", "导出数据"))
        self.importBtn.setText(_translate("MainWindow", "导入条形码"))
        self.label.setText(_translate("MainWindow", "文件数:"))
        item = self.fileList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.fileList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "大小"))
        item = self.fileList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "位置"))
        item = self.fileList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "创建日期"))
        item = self.fileList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "最近修改日期"))
        self.label_2.setText(_translate("MainWindow", "结果:"))
        self.label_3.setText(_translate("MainWindow", "成功扫描:"))
        self.label_4.setText(_translate("MainWindow", "失败扫描:"))
        item = self.resultList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.resultList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "状态"))
        item = self.resultList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "格式"))
        item = self.resultList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "值"))
        self.totalFile.setText(_translate("MainWindow", "0"))
        self.successScan.setText(_translate("MainWindow", "0"))
        self.failScan.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "(导出前确保data.xls目前处于关闭状态)"))
        self.saveBtn.setText(_translate("MainWindow", "另存为"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/import.png\" width=\"30\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/export.png\" width=\"30\"/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/scan.png\" width=\"30\"/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/save.png\" width=\"30\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/exit.png\" width=\"30\"/></p></body></html>"))

