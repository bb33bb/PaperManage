# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Papermanage\UI\Main.ui'
#
# Created: Thu Jun 05 10:35:02 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
import admin
import pic_rc
import Ui_Login
from ftp import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 517)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setPlaceholderText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.comboBox_2 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_3 = QtGui.QComboBox(self.centralWidget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(50, 20))
        self.comboBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line_3 = QtGui.QFrame(self.centralWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.ActionMask)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        

        item = QtGui.QTableWidgetItem()
        
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.line_2 = QtGui.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_3.addWidget(self.line_2)
        MainWindow.setCentralWidget(self.centralWidget)
        
        # 添加工具栏
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        # 添加状态栏 
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        # 回收站
        self.trash = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/Icon_trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trash.setIcon(icon3)
        self.trash.setObjectName(_fromUtf8("trash"))
        # 删除
        self.delete_2 = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/Icon_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_2.setIcon(icon4)
        self.delete_2.setObjectName(_fromUtf8("delete_2"))
        # 查看
        self.look = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/Icon_look.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.look.setIcon(icon5)
        self.look.setObjectName(_fromUtf8("look"))
        # 设置
        self.config = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/Icon_config.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.config.setIcon(icon6)
        self.config.setObjectName(_fromUtf8("config"))
        # 打印
        self.actionPrint = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon7)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        # 同步
        self.action = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/synchronization.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action.setIcon(icon)
        self.action.setObjectName(_fromUtf8("action"))
        # 下载
        self.action_2 = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_2.setIcon(icon9)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        # 时间
        self.label = QtGui.QLabel()
        self.label.setGeometry(QtCore.QRect(280, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        
        # 把各个action添加到工具栏 
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_2)
        self.toolBar.addAction(self.look)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.config)
        self.toolBar.addAction(self.delete_2)
        self.toolBar.addAction(self.trash)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.label) # 这就是时间
        self.tableWidget.resizeColumnToContents(0)
        
        self.Dir = Dir  # Dir就是连接ftp时获得的
        maxRow = len(self.Dir[0]) + len(self.Dir[1])
        self.tableWidget.setRowCount(maxRow)

        self.printlist()

        # 同步按钮的旋转
        self.rotate = 0   #  这两行用来支持旋转，必须在timer之前定义
        self.timer_rotate = QtCore.QTimer()
        QtCore.QObject.connect(self.timer_rotate,  QtCore.SIGNAL("timeout()"),  self.Rotate)

        # 处理时间的显示
        self.time = ""
        self.date = ""
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer,  QtCore.SIGNAL("timeout()"),  self.OnTimer)
        self.timer.start(10)
        self.OnTimer()
        
        # 键盘按键函数，动态添加的类
        origin = self # 这样可以使得在该方法中能调用slef中的方法
        def keyPressEvent(self,  event):
            key = event.key()
            if key == QtCore.Qt.Key_Backspace:
                origin.back()
            if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
                if origin.tableWidget.currentRow() >= 0:
                    origin.tableWidget.emit(QtCore.SIGNAL("Enter"),  origin.tableWidget.currentRow())
                if MainWindow.focusWidget() == origin.lineEdit_2:
                    origin.search()

        QtGui.QMainWindow.keyPressEvent = keyPressEvent
        
        # 各种信号与事件
        # 双击和按下Enter进入某目录
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("cellDoubleClicked(int,int)")), self.enter)        
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL(_fromUtf8("Enter")), self.enter)
        # 单击right或left按钮
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),  self.back)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ahead)
        # 单击动作事件
        QtCore.QObject.connect(self.trash,  QtCore.SIGNAL(_fromUtf8("triggered(bool)")),  self.E_trash) # 回收站事件
        QtCore.QObject.connect(self.delete_2,  QtCore.SIGNAL(_fromUtf8("triggered(bool)")),  self.dele) # 删除事件
        QtCore.QObject.connect(self.action_2,  QtCore.SIGNAL(_fromUtf8("triggered(bool)")),  self.download) # 下载事件
        QtCore.QObject.connect(self.action,  QtCore.SIGNAL(_fromUtf8("triggered(bool)")),  self.synchronize) # 同步事件
        QtCore.QObject.connect(self.actionPrint,  QtCore.SIGNAL(_fromUtf8("triggered(bool)")),  self.slotPrint)  #打印事件
        QtCore.QObject.connect(self.pushButton_3,  QtCore.SIGNAL(_fromUtf8("clicked()")),  self.search) # 搜索按钮
        QtCore.QObject.connect(self.config,  QtCore.SIGNAL(_fromUtf8("triggered(bool)")),  self.myconfig)  # 设置按钮
        QtCore.QObject.connect(self.look,  QtCore.SIGNAL(_fromUtf8("triggered(bool)")),  self.watch)  # 查看别人的库

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def watch(self):
        MyRepo.cd('/')
        import Ui_Login
        Mysql = Ui_Login.ui1.Login
        self.Dir = MyRepo.ls()
        Dir = [Ui_Login.ui1.ID]
        command = "select SID from Stu where ID = 100"
        Mysql.query(command)
        stu =  Mysql.fetch_queryresult(100) # 这个为本地的仓库目录
        for id in stu:
            if Dir.count(id) == 0:
                Dir.append(id[0])
        command = "select SID from Work where ID = 100"
        Mysql.query(command)
        stu =  Mysql.fetch_queryresult(100) # 这个为本地的仓库目录
        for id in stu:
            if Dir.count(id) == 0:
                Dir.append(id[0])
        print Dir


        maxRow = len(Dir)
        self.tableWidget.setRowCount(maxRow)
        row = 0
        
        
        for doc in Dir:
            item = QtGui.QTableWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)            
            item.setIcon(icon)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(row,  0,  item)
            

            command = "select Username from User where ID = " + str(doc)
            Mysql.query(command)
            name =  Mysql.fetch_queryresult()[0][0] # 这个为本地的仓库目录   
            
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("MainWindow",  name,  None))
            self.tableWidget.setItem(row,  1,  item)
            row += 1

    def myconfig(self):
        """配置选项"""
        import Ui_config
        reload(Ui_config)

    def search(self):
        """
        搜索功能，搜索的是当前目录下的所有文件，而不是像百度云那样的搜索的是所有文件夹
        搜索过后直接显示相对本目录的路径以及文件名
        """
        text = str(self.lineEdit_2.text().toUtf8())
        # 直接遍历当前的item就行了
        self.Dir = MyRepo.ls()
        maxRow = len(self.Dir[0]) + len(self.Dir[1])
        row = 0
        
        for doc in self.Dir[1]:
            if doc.find(text) >= 0:
                item = QtGui.QTableWidgetItem()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(row,  0,  item)
                
                item = QtGui.QTableWidgetItem()
                item.setText(_translate("MainWindow",  doc,  None))
                self.tableWidget.setItem(row,  1,  item)
                row += 1
                
        for doc in self.Dir[0]:
            if doc.find(text) >= 0:
                item = QtGui.QTableWidgetItem()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/text.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)                
                item.setIcon(icon)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(row,  0,  item)
                
                item = QtGui.QTableWidgetItem()
                item.setText(_translate("MainWindow",  doc,  None))
                self.tableWidget.setItem(row,  1,  item)
                row += 1
        self.tableWidget.setRowCount(row)
        

    def slotPrint(self):
        """打印动作，目前只支持对文本的打印"""
        maxRow = len(self.Dir[0]) + len(self.Dir[1])
        for i in range(maxRow):
            item = self.tableWidget.item(i,  0)
            if item.checkState() == 2:
                # 如果是txt文件就直接打印
                item = self.tableWidget.item(i,  1)
                name = str(item.text().toUtf8())
                try:
                    self.Dir[0].index(name)  # 检测是不是文件，如果是文件则直接打印
                    # 获取打印文本
                    self.text = QtGui.QTextEdit()
                    file = QtCore.QFile(name)
                    if file.open(QtCore.QIODevice.ReadOnly| QtCore.QIODevice.Text):
                        textStream = QtCore.QTextStream(file)
                        while not textStream.atEnd():
                            self.text.append(textStream.readLine())
                    file.close()
                    # 打印过程
                    printer = QtGui.QPrinter()
                    printDialog = QtGui.QPrintDialog(printer,  MainWindow)
                    if printDialog.exec_():
                        doc = self.text.document()
                        doc.print_(printer)
                except:
                    print '目前只支持对txt文件的打印'        

    def synchronize(self):
        """最难的同步功能"""
        self.timer_rotate.start(200)
        # 首先改变当前目录到工作目录
        import Ui_Login
        Mysql = Ui_Login.ui1.Login
        command = "select Hostpath from Repo where ID = " + str(Ui_Login.ui1.ID)
        Mysql.query(command)
        Hostpath =  Mysql.fetch_queryresult()[0][0]  # 这个为本地的仓库目录
        print Hostpath
        MyRepo.upfile(Hostpath,  Ui_Login.ui1.ID)
        self.timer_rotate.stop()

    def download(self):
        """点击工具栏上的下载按钮下载文件"""
        # 获得保存路径
        maxRow = len(self.Dir[0]) + len(self.Dir[1])
        localpath = str(QtGui.QFileDialog.getExistingDirectory(MainWindow, "Open Image", '/',  QtGui.QFileDialog.ShowDirsOnly).toUtf8())
        # 遍历当前目录来下载，可能是文件可能是文件夹
        for i in range(maxRow):
            item = self.tableWidget.item(i,  0)
            if item.checkState() == 2:
                # 如果是文件就直接下载
                item = self.tableWidget.item(i,  1)
                name = str(item.text().toUtf8())
                try:
                    self.Dir[0].index(name)  # 如果能成功表示要下载的只是文件
                    MyRepo.downfile(name,  localpath)
                except:# 现在要下载的就是文件夹了  
                    MyRepo.downdir(name,  localpath)
        

    def dele(self):
        """删除事件，其中item.checkState()==2表示该被选中"""
        current = MyRepo.pwd()
        maxRow = len(self.Dir[0]) + len(self.Dir[1])
        # 直接遍历当前目录，如果有checkState=2的就当场删除
        for i in range(maxRow):
            item = self.tableWidget.item(i, 0)
            if item.checkState() == 2:
                # 如果删除的是文件就��接删除
                item = self.tableWidget.item(i,  1)
                name = str(item.text().toUtf8())  # 获取要删除的Item名
                try:
                    self.Dir[0].index(name)   # 如果能成功执行表示要删除的是文件
                    MyRepo.rm(name,  Ui_Login.ui1.ID)
                except:                        # 否则要删除的就是文件夹了
                    MyRepo.rmdir(name,  Ui_Login.ui1.ID)

        # 删除完了过后还要更新当前目录
        MyRepo.cd(current)
        self.printlist()
    
    def E_trash(self):
        """进入回收站事件"""
        MyRepo.cd('/' + str(Ui_Login.ui1.ID) + '/.trash')
        self.printlist()
        
    def test(self):
       print "I'm testing."

    def back(self):
        """返回一级目录，可以使用键盘消除键即backspace或者点击倒退按钮pushButton"""
        if MyRepo.pwd().count('/') == 1:
            return
        MyRepo.cd('..')
        self.printlist()
    
    def ahead(self):
        """点击right按钮进入指定目录"""
        if self.tableWidget.currentRow() >= 0:
            self.enter(self.tableWidget.currentRow())

    def enter(self,  row):
        """单击cell进入目录的事件，参数只需要那个行就行了"""
        item = self.tableWidget.item(row, 1)
        if MyRepo.pwd() == '/':
                import Ui_Login
                Mysql = Ui_Login.ui1.Login
                name = 'wanghao'
                command = "select ID from User where Username = "  + "'" + str(item.text().toUtf8()) + "'"#str(item.text().toUtf8())
                print command
                Mysql.query(command)
                ID =  Mysql.fetch_queryresult()[0][0] # 这个为本地的仓库目录   
        else:
            ID = str(item.text().toUtf8())
        MyRepo.cd('/' + str(ID))
        self.printlist()
    
    def printlist(self):
        """打印当前目录的内容到tablelist里面去"""
        self.Dir = MyRepo.ls()
        maxRow = len(self.Dir[0]) + len(self.Dir[1])
        self.tableWidget.setRowCount(maxRow)
        row = 0
        # 先打印目录
        for doc in self.Dir[1]:
            item = QtGui.QTableWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)            
            item.setIcon(icon)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(row,  0,  item)
            
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("MainWindow",  doc,  None))
            self.tableWidget.setItem(row,  1,  item)
            row += 1
        # 再打印文件
        for doc in self.Dir[0]:
            item = QtGui.QTableWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/text.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(row,  0,  item)
            
            item = QtGui.QTableWidgetItem()
            item.setText(_translate("MainWindow",  doc,  None))
            self.tableWidget.setItem(row,  1,  item)
            row += 1
        # 修改lineEdit显示的目录位置
        if MyRepo.pwd() == '/' + str(Ui_Login.ui1.ID):
            self.lineEdit.setText(_translate("MainWindow", "/我的仓库/", None))
        elif MyRepo.pwd() == '/':
            self.lineEdit.setText(_translate("MainWindow",  "/选择仓库/",  None))
        elif MyRepo.pwd().find('/' + str(Ui_Login.ui1.ID)) != -1:
            self.lineEdit.setText(_translate("MainWindow", "/我的仓库/" + MyRepo.pwd().split('/',  2)[2], None))
        else:
            self.lineEdit.setText(_translate("MainWindow",  "/别人的仓库",  None))
        
    def Rotate(self):
        """旋转那张图片"""    
        self.rotate += 1 
        if self.rotate == 3:
            self.rotate = 0
        if self.rotate % 3 ==0:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/synchronization.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.action.setIcon(icon)
        elif self.rotate % 3 == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/synchronization1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.action.setIcon(icon)            
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/synchronization.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.action.setIcon(icon)
        
    # 每秒钟改变显示时间的那个字符串
    def OnTimer(self):
        localtime = time.localtime() 
        tm_min = localtime.tm_min
        if int(tm_min) < 10:
            tm_min = "0" + str(tm_min)
        self.time = str(localtime.tm_hour) + ":" + str(tm_min)
        self.date = str(localtime.tm_year) + "/" + str(localtime.tm_mon) + "/" + str(localtime.tm_mday)
        self.label.setText(_translate("Dialog", "   " + self.time + "\n "+ self.date, None))   # 这是时间
        
        self.toolBar.setIconSize(QtCore.QSize(MainWindow.width() / 9,  40))  # 
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "文档资料管理系统", None))
        self.lineEdit.setText(_translate("MainWindow", "/我的仓库/", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "自己", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "他人", None))
        self.pushButton_3.setText(_translate("MainWindow", "搜索", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "视图", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "图标", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "详细信息", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "排序", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "按文件名", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "按大小", None))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "按修改时间", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "全选", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件名", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "大小", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "修改时间", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.trash.setText(_translate("MainWindow", "回收站", None))
        self.trash.setToolTip(_translate("MainWindow", "回收站", None))
        self.delete_2.setText(_translate("MainWindow", "删除", None))
        self.delete_2.setToolTip(_translate("MainWindow", "删除", None))
        self.look.setText(_translate("MainWindow", "查看", None))
        self.look.setToolTip(_translate("MainWindow", "查看老师、学生或同事的资料", None))
        self.config.setText(_translate("MainWindow", "设置", None))
        self.config.setToolTip(_translate("MainWindow", "设置", None))
        self.actionPrint.setText(_translate("MainWindow", "print", None))
        self.actionPrint.setToolTip(_translate("MainWindow", "打印", None))
        self.action.setText(_translate("MainWindow", "同步", None))
        self.action.setToolTip(_translate("MainWindow", "同步所有", None))
        self.action_2.setText(_translate("MainWindow", "下载", None))
        self.action_2.setToolTip(_translate("MainWindow", "下载", None))
        
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "点击这里搜索当前目录文件", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
else:
    # 先连接FTP
    try:
        MyRepo = MyFtp(Ui_Login.ui1.ID,  admin.ftp['ip'], admin.ftp['port'], admin.ftp['timeout'], admin.ftp['admin'],  admin.ftp['passwd'])
        Dir = MyRepo.ls()
    except:
        print 'FTP连接失败'
    
    MainWindow = QtGui.QMainWindow()
    ui3 = Ui_MainWindow()
    ui3.setupUi(MainWindow)
    MainWindow.show()
