from PyQt5 import QtCore, QtGui
import barcode
import sys
import time
import xlwt
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem

# 文件集合, 确保元素不重复
fileSet = set()


# method
def importEvent(mw, ui):
    files = QFileDialog.getOpenFileNames(mw, '打开文件', './', ("Images (*.png *.jpg *.bmp *.gif *.raw *.tif *.xpm)"))
    if not files[0]:
        return
    for i in files[0]:
        fileSet.add(i)
    ui.totalFileNum.setText(str(len(fileSet)))  # 文件总数
    ui.fileList.clearContents()
    ui.fileList.setRowCount(0)
    for file in fileSet:
        row = ui.fileList.rowCount()
        ui.fileList.insertRow(row)
        # 文件名
        fileNameItem = QTableWidgetItem(os.path.basename(file))
        fileNameItem.setTextAlignment(QtCore.Qt.AlignCenter)
        # 文件大小
        fileSizeItem = QTableWidgetItem(str("%.2f" % (os.path.getsize(file) / 1024)) + "KB")
        fileSizeItem.setTextAlignment(QtCore.Qt.AlignCenter)
        # 文件绝对路径
        filePathItem = QTableWidgetItem(file)
        filePathItem.setTextAlignment(QtCore.Qt.AlignCenter)
        # 文件创建时间
        createTimeItem = QTableWidgetItem(timeToStrTime(os.path.getctime(file)))
        createTimeItem.setTextAlignment(QtCore.Qt.AlignCenter)
        # 文件修改时间
        modifyTimeItem = QTableWidgetItem(timeToStrTime(os.path.getmtime(file)))
        modifyTimeItem.setTextAlignment(QtCore.Qt.AlignCenter)
        ui.fileList.setItem(row, 0, fileNameItem)
        ui.fileList.setItem(row, 1, fileSizeItem)
        ui.fileList.setItem(row, 2, filePathItem)
        ui.fileList.setItem(row, 3, createTimeItem)
        ui.fileList.setItem(row, 4, modifyTimeItem)


def timeToStrTime(timestamp):
    """将时间戳转化为格式时间字符串"""
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M', timeStruct)


def startScan(mw, ui):
    if len(fileSet) == 0:
        QMessageBox.information(mw, '提示', '你没有选择任何条形码图片文件!', QMessageBox.Ok, QMessageBox.Ok)
        return
    successCount = 0  # 成功检测数
    failCount = 0  # 失败检测数
    cmd = ".\\ZBar\\bin\\zbarimg.exe "
    ui.resultList.clearContents()
    ui.resultList.setRowCount(0)
    for file in fileSet:
        array = execCmd(cmd + file)  # 执行命令.\zbarimg.exe imgPath
        row = ui.resultList.rowCount()
        ui.resultList.insertRow(row)
        fileNameItem = QTableWidgetItem(os.path.basename(file))
        fileNameItem.setTextAlignment(QtCore.Qt.AlignCenter)
        if len(array) == 0:
            # 设置失败红色字体
            statusItem = QTableWidgetItem("扫描失败")
            statusItem.setTextAlignment(QtCore.Qt.AlignCenter)
            brush = QtGui.QBrush(QtGui.QColor(234, 31, 42))
            brush.setStyle(QtCore.Qt.NoBrush)
            statusItem.setForeground(brush)

            typeItem = QTableWidgetItem("请调整图片清晰度")
            typeItem.setTextAlignment(QtCore.Qt.AlignCenter)
            brush = QtGui.QBrush(QtGui.QColor(234, 31, 42))
            brush.setStyle(QtCore.Qt.NoBrush)
            typeItem.setForeground(brush)

            valueItem = QTableWidgetItem("请调整图片清晰度")
            valueItem.setTextAlignment(QtCore.Qt.AlignCenter)
            brush = QtGui.QBrush(QtGui.QColor(234, 31, 42))
            brush.setStyle(QtCore.Qt.NoBrush)
            valueItem.setForeground(brush)
            failCount += 1
        else:
            # 设置成功绿色字体
            statusItem = QTableWidgetItem("扫描成功")
            statusItem.setTextAlignment(QtCore.Qt.AlignCenter)
            brush = QtGui.QBrush(QtGui.QColor(35, 177, 32))
            brush.setStyle(QtCore.Qt.NoBrush)
            statusItem.setForeground(brush)

            result = array[0].split(":")  # 分离字符串得到条形码格式和内容
            codebarType = result[0]  # 条形码格式
            codebarValue = result[1].strip()  # 条形码内容, 去掉两端的空格、制表符trim()函数
            typeItem = QTableWidgetItem(codebarType)
            typeItem.setTextAlignment(QtCore.Qt.AlignCenter)

            valueItem = QTableWidgetItem(codebarValue)
            valueItem.setTextAlignment(QtCore.Qt.AlignCenter)
            successCount += 1
        ui.resultList.setItem(row, 0, fileNameItem)
        ui.resultList.setItem(row, 1, statusItem)
        ui.resultList.setItem(row, 2, typeItem)
        ui.resultList.setItem(row, 3, valueItem)
        ui.successScanNum.setText(str(successCount))  # 设置成功扫描的文件数
        ui.failScanNum.setText(str(failCount))


def exportEvent(mw, ui):
    """保存到excel"""
    if len(fileSet) == 0:
        QMessageBox.information(mw, '提示', '你没有选择任何条形码图片文件!', QMessageBox.Ok, QMessageBox.Ok)
        return
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('sheet1')
    # 样式
    t = xlwt.Font()
    t.colour_index = 10  # 红色字体
    redColorFont = xlwt.XFStyle()
    redColorFont.font = t

    t = xlwt.Font()
    t.colour_index = 57  # 绿色字体
    greenColorFont = xlwt.XFStyle()
    greenColorFont.font = t

    # 参数对应 行, 列, 值
    worksheet.write(0, 0, label='文件名')
    worksheet.col(0).width = 256 * 20
    worksheet.write(0, 1, label='扫描状态')
    worksheet.write(0, 2, label='格式')
    worksheet.write(0, 3, label='值')
    worksheet.col(3).width = 256 * 20
    worksheet.write(0, 4, label='文件路径')
    worksheet.col(4).width = 256 * 80

    cmd = ".\\ZBar\\bin\\zbarimg.exe "
    row = 1
    for file in fileSet:
        worksheet.write(row, 0, label=os.path.basename(file))
        array = execCmd(cmd + file)
        if len(array) == 0:
            worksheet.write(row, 1, u'扫描失败', redColorFont)
        else:
            worksheet.write(row, 1, u'扫描成功', greenColorFont)
            result = array[0].split(":")
            worksheet.write(row, 2, label=result[0])
            worksheet.write(row, 3, label=result[1].strip())
        worksheet.write(row, 4, label=file)
        row += 1
    # 保存
    workbook.save('.\\data.xls')


def exitEvent(mw):
    """退出事件"""
    mw.close()


def execCmd(cmd):
    """执行控制台命令"""
    result = os.popen(cmd)
    text = result.readlines()
    result.close()
    return text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = barcode.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    # 主体代码

    # 字段显示宽度
    ui.fileList.setColumnWidth(0, 150)
    ui.fileList.setColumnWidth(1, 150)
    ui.fileList.setColumnWidth(2, 500)
    ui.fileList.setColumnWidth(3, 200)
    ui.fileList.setColumnWidth(4, 200)
    ui.resultList.setColumnWidth(0, 150)
    ui.resultList.setColumnWidth(1, 150)
    ui.resultList.setColumnWidth(2, 400)
    ui.resultList.setColumnWidth(3, 400)

    # 按钮
    ui.exportBtn.clicked.connect(lambda: exportEvent(mw, ui))  # 导出按钮
    ui.scanBtn.clicked.connect(lambda: startScan(mw, ui))  # 扫描按钮
    ui.importBtn.clicked.connect(lambda: importEvent(mw, ui))  # 导入按钮
    ui.exitBtn.clicked.connect(lambda: exitEvent(mw))  # 退出按钮
    sys.exit(app.exec_())
