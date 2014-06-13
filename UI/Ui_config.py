# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Papermanage\UI\config.ui'
#
# Created: Tue Jun 10 08:53:33 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import admin
from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(357, 502)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./image/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 331, 431))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 391))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setMaxLength(50)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout.addWidget(self.lineEdit_9, 6, 1, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setMaxLength(20)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setMaxLength(20)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout.addWidget(self.lineEdit_10, 7, 1, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setMaxLength(15)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setMaxLength(20)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setMaxLength(20)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout.addWidget(self.lineEdit_11, 8, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, -1, 50, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_14 = QtGui.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(29, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_17 = QtGui.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(30, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(110, 25, 54, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 170, 271, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 200, 75, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_19 = QtGui.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.spinBox = QtGui.QSpinBox(self.tab_4)
        self.spinBox.setGeometry(QtCore.QRect(170, 60, 51, 31))
        self.spinBox.setMinimum(30)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_20 = QtGui.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(230, 64, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(19, 15, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 40, 291, 41))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.listWidget = QtGui.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 256, 311))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 130, 41, 41))
        self.pushButton_4.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./image/del.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 80, 41, 41))
        self.pushButton_5.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./image/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_16 = QtGui.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(20, 45, 291, 31))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.listWidget_2 = QtGui.QListWidget(self.tab_3)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 80, 256, 311))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 80, 41, 41))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 130, 41, 41))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton_12 = QtGui.QPushButton(self.widget)
        self.pushButton_12.setGeometry(QtCore.QRect(280, 80, 41, 41))
        self.pushButton_12.setText(_fromUtf8(""))
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(self.widget)
        self.pushButton_13.setGeometry(QtCore.QRect(280, 130, 41, 41))
        self.pushButton_13.setText(_fromUtf8(""))
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.label_33 = QtGui.QLabel(self.widget)
        self.label_33.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.widget)
        self.label_34.setGeometry(QtCore.QRect(20, 45, 291, 31))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.listWidget_5 = QtGui.QListWidget(self.widget)
        self.listWidget_5.setGeometry(QtCore.QRect(20, 80, 256, 311))
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))
        self.tabWidget.addTab(self.widget, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(71, 460, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(171, 460, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(271, 460, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        
        QtCore.QObject.connect(self.pushButton_8,  QtCore.SIGNAL(_fromUtf8("clicked(bool)")),  self.chwd)  # 选择路径
        QtCore.QObject.connect(self.pushButton_3,  QtCore.SIGNAL(_fromUtf8("clicked(bool)")),  self.apply) # 应用按钮
        QtCore.QObject.connect(self.pushButton,   QtCore.SIGNAL(_fromUtf8("clicked(bool)")),  self.accept) # 确定按钮
        QtCore.QObject.connect(self.pushButton_2,  QtCore.SIGNAL(_fromUtf8("clicked(bool)")),  self.cancel) # 取消按钮
        
        QtCore.QObject.connect(self.pushButton_12,  QtCore.SIGNAL(_fromUtf8("clicked(bool)")),  self.addwork) # 同事加

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def addwork(self):
        pass
        
    
    def test(self):
        print 'Im tesging'
        
    def accept(self):
        """确定按钮，先apply再cancel"""
        self.apply()
        Dialog.close()
        
    def apply(self):
        """最下面的应用按钮，点击后会保存所有的信息，但是不会退出"""
        info1 = self.lineEdit_6.text().toUtf8()   # 职务
        info2 = self.lineEdit_7.text().toUtf8()   # 姓名
        info3 = self.lineEdit_9.text().toUtf8()   # 联系地址
        info4 = self.lineEdit_10.text().toUtf8()  # 电子邮件
        info5 = self.lineEdit_5.text().toUtf8()    # 电话
        info6 = self.lineEdit_11.text().toUtf8()   # 工作单位
        info7 = self.lineEdit_4.text().toUtf8()    # 仓库地址
        info8 = self.lineEdit.text().toUtf8()       # 用户名
        if self.radioButton_2.isChecked():           # 性别男
            info9 = 0
        else:
            info9 = 1
        info10 = self.comboBox.currentText().toUtf8()  # 学院
        
        # 又是一个一个挨着检查
        import Check
        import ConnectSQL
        Zhuce = ConnectSQL.ConnectSQL(admin.sql['host'], admin.sql['user'], admin.sql['passwd'], admin.sql['db'])
        # 检查邮箱地址是否正确
        if not Check.isEmail(info4):
            QtGui.QMessageBox.warning(Dialog,  u"发生错误",  u"请输入正确的邮箱地址")
            return
        
        # 检查邮箱的唯一性
        command = "select * from User where Mail='" + info4 + "'"
        count = Zhuce.query(command)
        result = Zhuce.fetch_queryresult()
        if count and result[0][3] != info4:
            QtGui.QMessageBox.warning(Dialog,  u"发生错误",  u"该邮箱已注册")
            return
        # 检查用户名的正确性
        if not Check.isStd(unicode(info8,  "utf-8")):
            QtGui.QMessageBox.warning(Dialog,  u"发生错误",  u"请输入正确的用户名(不得有特殊字符，长度为3-20)")
            return
        # 检查用户名的唯一性
        command = "select * from User where Username='" + info8 + "'"
        count = Zhuce.query(command)
        result = Zhuce.fetch_queryresult()
        if count[0] and result[0][1] != info8:
            QtGui.QMessageBox.warning(Dialog,  u"发生错误",  u"该用户名已注册")
            return
        if (not Check.isName(unicode(info2,  "utf-8"))) and (not info2.isEmpty()):
            QtGui.QMessageBox.warning(Dialog,  u"发生错误",  u"请输入正确的姓名（不得有特殊字符，长度为2-4）")
            return
        if (not Check.isTel(info5)) and (not info5.isEmpty()):
            QtGui.QMessageBox.warning(Dialog, u"发生错误",   u"请输入正确的电话号码（不得有特殊字符），长度为8或11")
            return 
        if (not Check.isZhiwu(unicode(info1,  "utf-8"))) and (not info1.isEmpty()):
            QtGui.QMessageBox.warning(Dialog,  u"发生错误",  u"请输入正确的职务信息（不得有特殊字符，长度为2-20）")
            return
        if (not Check.isZhiwu(unicode(info3,  "utf-8"))) and (not info3.isEmpty()):
            QtGui.QMessageBox.warning(Dialog, u"发生错误",   u"请输入正确的联系地址（不得有特殊字符，长度为6-20）")
            return
        if (not Check.isZhiwu(unicode(info6,  "utf-8"))) and (not info6.isEmpty()):
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"请输入正确的工作单位（不得有特殊字符，长度为6-20）")
            return
        
        # 唉，然后就是存入了。。。使用的是更新操作
        # 首先更新User表：
        command = "update User set Username = %s, Mail = %s where ID = %s"
        args = (info8,  info4,  Ui_Login.ui1.ID)
        Zhuce.execute(command,  args)
        # 然后更新OtherInfo表 
        command = "update OtherInfo set Name = %s, Gender = %s, Tele = %s, Duty = %s, Academy = %s, Addr = %s, Company = %s where ID = %s"
        args = (info2,  info9,  info5,  info1, info10,  info3,  info6,  Ui_Login.ui1.ID)
        Zhuce.execute(command,  args)
        # 再更新Repo表
        if len(info7) == 0:
            QtGui.QMessageBox.warning(Dialog,  u"发生错误",  u"仓库地址无效")
            return
        command = "select ID from Repo where ID = " + str(Ui_Login.ui1.ID)
        try:
            if Zhuce.query(command)[0]:   # 如果已经有了就更新，否则就添加
                print '这里'
                command = "update Repo set Hostpath = %s where ID = %s"
                args = (info7,  Ui_Login.ui1.ID)
                Zhuce.execute(command,  args)
            else:
                print '那里'
                command = "insert into Repo values(%s, %s, %s, %s, %s, %s)"
                args = (Ui_Login.ui1.ID,  info7,  '2014-06-12 00:00:00',  '2015-07-18 00:00:00',  '10',  '2014-07-17 00:00:00')
                Zhuce.execute(command,  args)
        except:
            QtGui.QMessageBox.warning(MainWindow,  u"发生错误",  u"仓库地址无效或与别人有重复")
            
        # 最后提交更改
        Zhuce.commit()
        
    def chwd(self):
        """选择仓库路径"""
        localpath = str(QtGui.QFileDialog.getExistingDirectory(Dialog, u"选择路径", '/',  QtGui.QFileDialog.ShowDirsOnly).toUtf8())
        self.lineEdit_4.setText(_translate("MainWindow",  localpath,   None))  # 仓库地址
        
    def cancel(self):
        """取消按钮，直接退出"""
        Dialog.close()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "设置", None))
        self.label_6.setText(_translate("Dialog", "电话", None))
        self.label_8.setText(_translate("Dialog", "学院", None))
        self.label_9.setText(_translate("Dialog", "联系地址", None))
        self.label_11.setText(_translate("Dialog", "工作单位", None))
        self.label_10.setText(_translate("Dialog", "电子邮件", None))
        self.comboBox.setItemText(0, _translate("Dialog", "计算机科学与技术学院", None))
        self.comboBox.setItemText(1, _translate("Dialog", "生物信息学院", None))
        self.comboBox.setItemText(2, _translate("Dialog", "通信与信息工程学院", None))
        self.comboBox.setItemText(3, _translate("Dialog", "软件工程学院", None))
        self.comboBox.setItemText(4, _translate("Dialog", "国际半导体新学院", None))
        self.comboBox.setItemText(5, _translate("Dialog", "自动化学院", None))
        self.comboBox.setItemText(6, _translate("Dialog", "体育学院", None))
        self.comboBox.setItemText(7, _translate("Dialog", "理学院", None))
        self.comboBox.setItemText(8, _translate("Dialog", "广电工程学院", None))
        self.comboBox.setItemText(9, _translate("Dialog", "经济管理学院", None))
        self.comboBox.setItemText(10, _translate("Dialog", "传媒艺术学院", None))
        self.comboBox.setItemText(11, _translate("Dialog", "外国语学院", None))
        self.comboBox.setItemText(12, _translate("Dialog", "国际学院", None))
        self.comboBox.setItemText(13, _translate("Dialog", "法学院", None))
        self.comboBox.setItemText(14, _translate("Dialog", "其他", None))
        self.label.setText(_translate("Dialog", "用户名", None))
        self.label_4.setText(_translate("Dialog", "姓名", None))
        self.label_7.setText(_translate("Dialog", "职务", None))
        self.label_5.setText(_translate("Dialog", "性别", None))
        self.radioButton_2.setText(_translate("Dialog", "男", None))
        self.radioButton.setText(_translate("Dialog", "女", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "个人", None))
        self.label_14.setText(_translate("Dialog", "仓库地址：", None))
        self.label_17.setText(_translate("Dialog", "用户ID：", None))
        self.label_18.setText(_translate("Dialog", "100", None))
        self.pushButton_8.setText(_translate("Dialog", "改变地址", None))
        self.label_19.setText(_translate("Dialog", "自动更新时间：", None))
        self.label_20.setText(_translate("Dialog", "分", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "仓库", None))
        self.label_12.setText(_translate("Dialog", "我的老师", None))
        self.label_15.setText(_translate("Dialog", "权限：你的老师能够访问你的仓库，知道你目前所研\n"
"究的内容。当然，前提是他的学生列表中也有你", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "老师", None))
        self.label_13.setText(_translate("Dialog", "我的学生", None))
        self.label_16.setText(_translate("Dialog", "权限：如果你的学生设置了你为他的老师，那么你就\n"
"能够访问他的仓库", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "学生", None))
        self.label_33.setText(_translate("Dialog", "我的同事", None))
        self.label_34.setText(_translate("Dialog", "权限：如果你的同事同时也设置你为他的同事，那么\n"
"你们就可以访问并修改对方的仓库", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "同事", None))
        self.pushButton.setText(_translate("Dialog", "确定", None))
        self.pushButton_2.setText(_translate("Dialog", "取消", None))
        self.pushButton_3.setText(_translate("Dialog", "应用", None))


        # 设置各个项的初始值，总共是9信息
        Mysql = Ui_Login.ui1.Login
        
        command = "select Username, Mail from User where ID = " + str(Ui_Login.ui1.ID)
        Mysql.query(command)
        userinfo = Mysql.fetch_queryresult()[0]  # 这个为本地的仓库目录
        
        command = "select Name, Gender, Tele, Duty, Academy, Addr, Company from OtherInfo where ID = " + str(Ui_Login.ui1.ID)
        Mysql.query(command)
        Info = Mysql.fetch_queryresult()[0]
        
        command = "select Hostpath from Repo where ID = " + str(Ui_Login.ui1.ID)
        Mysql.query(command)
        result = Mysql.fetch_queryresult()
        hostpath = ''
        if len(result) > 0 :
            hostpath = result[0][0]
        
        # 获得老师列表
        command = "select TID from Tea where ID = " + str(Ui_Login.ui1.ID)
        Mysql.query(command)
        tea = Mysql.fetch_queryresult(100)
        teacher = []
        for i in tea:
            command = "select Username from User where ID = " + str(i[0])
            Mysql.query(command)
            teacher.append(Mysql.fetch_queryresult()[0][0])
            
        # 获得学生列表
        command = "select SID from Stu where ID = " + str(Ui_Login.ui1.ID)
        Mysql.query(command)
        stu = Mysql.fetch_queryresult(100)
        student = []
        for i in stu:
            command = "select Username from User where ID = " + str(i[0])
            Mysql.query(command)
            student.append(Mysql.fetch_queryresult()[0][0])
            
        # 获得同事列表
        command = "select SID from Work where ID = " + str(Ui_Login.ui1.ID)
        Mysql.query(command)
        wo = Mysql.fetch_queryresult(100)
        work = []
        for i in wo:
            command = "select Username from User where ID = " + str(i[0])
            Mysql.query(command)
            work.append(Mysql.fetch_queryresult()[0][0])
        
        # 第一页：个人性信息
        self.lineEdit.setText(_translate("MainWindow", userinfo[0], None))  # 用户名
        self.lineEdit_6.setText(_translate("MainWindow",  Info[3],  None))  # 职务
        self.lineEdit_7.setText(_translate("MainWindow",  Info[0],  None))   # 姓名
        self.lineEdit_9.setText(_translate("MainWindow",  Info[5],  None))   # 联系地址
        self.lineEdit_10.setText(_translate("MainWindow",  userinfo[1],  None))  # 电子邮件
        self.lineEdit_5.setText(_translate("MainWindow",  Info[2],  None)) # 电话
        self.lineEdit_11.setText(_translate("MainWindow",  Info[6],  None))  # 工作单位
        if ord(Info[1]) == 1:                                                                 # 性别
            self.radioButton_2.setChecked(True)
            self.radioButton.setChecked(False)
        else:
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
        self.lineEdit_4.setText(_translate("MainWindow",  hostpath,   None))  # 仓库地址
        # 老师       
        for tea in teacher:
            item = QtGui.QListWidgetItem()
            item.setText(_translate("MainWindow", tea, None))
            self.listWidget.addItem(item)
        # 学生
        for s in student:
            item = QtGui.QListWidgetItem()
            item.setText(_translate("MainWindow",   s,  None))
            self.listWidget_2.addItem(item)
        for w in work:
            item = QtGui.QListWidgetItem()
            item.setText(_translate("MainWindow",  w,  None))
            self.listWidget_5.addItem(item)     

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
else:
    import Ui_Login
    Dialog = QtGui.QDialog()
    ui4 = Ui_Dialog()
    ui4.setupUi(Dialog)
    Dialog.exec_()

