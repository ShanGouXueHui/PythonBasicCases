# -*- coding: utf-8 -*-

import sys
import os
from PyQt6 import QtWidgets,QtGui

class NotePad(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.startUI()
    
    def startUI(self):
        #定义一个菜单，顶级名称显示文本
        memubar = self.menuBar()
        fileMenu = memubar.addMenu('&文件')
        
        #定义动作
        openFile = QtGui.QAction('打开',self)
        #设置快捷键
        openFile.setShortcut('Ctrl+O')
        #鼠标悬停后，显示的提示文本
        openFile.setStatusTip('打开新文件.')
        #点击菜单时，绑定一个信号（动作），这里指定一个自定义函数（包含具体动作）
        openFile.triggered.connect(self.displayDialogWindow)
        #将动作绑定在菜单上
        fileMenu.addAction(openFile)
        
        #退出App功能，与打开文件雷同
        exitApp = QtGui.QAction('&退出', self)
        exitApp.setShortcut('Ctrl+Q')
        exitApp.setStatusTip('退出应用')
        #使用QT原生动作
        exitApp.triggered.connect(QtWidgets.QApplication.instance().quit)
        fileMenu.addAction(exitApp)
        
        #定义一个工具栏
        self.toolbar = self.addToolBar('文件')
        #将打开文件绑定在工具栏上，动作与菜单动作一致
        self.toolbar.addAction(openFile)
        #将退出App绑定在工具栏上，动作与菜单动作一致
        self.addToolBar('退出')
        self.toolbar.addAction(exitApp)
        
        #添加文本编辑框，文本编辑部件居中显示
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        
        #使用 QMainWindow 创建状态栏
        self.statusBar().showMessage('Ready')   
        
        self.setGeometry(300,300,600,399)
        self.setWindowTitle('Note Pad Sample')
        self.show()
    
    def displayDialogWindow(self):
        homeDir = str(os.getcwd())
        #getOpenFileName 的第一个参数字符串是标题，第二个字符串指定对话框工作目录。
        #我们使用 os 模块来获取当前路径。默认情况下，文件过滤器设置为所有文件 (*)
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件',homeDir)
        
        if fileName[0]:
            with open(fileName[0], 'r', encoding='utf-8') as f:
                data = f.read()
                self.textEdit.setText(data)
                


#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    #定义应用程序
    app = QtWidgets.QApplication(sys.argv)
    #生成主界面
    np = NotePad()
    #调用应用程序的 exec() 方法时，应用程序进入主循环
    sys.exit(app.exec())