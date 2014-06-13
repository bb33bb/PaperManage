# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Papermanage\UI\Signin.ui'
#
# Created: Sun Jun 01 15:53:54 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import pic_rc
import admin
from PyQt4 import QtCore, QtGui
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(530, 510)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(530, 510))
        Dialog.setMaximumSize(QtCore.QSize(530, 510))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 450, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 50, 431, 391))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_5 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setMaxLength(15)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 5, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
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
        self.gridLayout.addWidget(self.comboBox, 7, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setMaxLength(50)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout.addWidget(self.lineEdit_9, 8, 2, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMaxLength(20)
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setMaxLength(20)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout.addWidget(self.lineEdit_7, 3, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setMaxLength(20)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout.addWidget(self.lineEdit_6, 6, 2, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setMaxLength(20)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout.addWidget(self.lineEdit_10, 9, 2, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setMaxLength(20)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout.addWidget(self.lineEdit_11, 10, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 1, 3, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 2, 3, 1, 1)
        self.label_21 = QtGui.QLabel(self.layoutWidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout.addWidget(self.label_21, 9, 3, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(5, 5))
        self.label_12.setMaximumSize(QtCore.QSize(5, 5))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("./image/asterisk.png")))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setMinimumSize(QtCore.QSize(5, 5))
        self.label_16.setMaximumSize(QtCore.QSize(5, 5))
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setPixmap(QtGui.QPixmap(_fromUtf8("./image/asterisk.png")))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 1, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setMinimumSize(QtCore.QSize(5, 5))
        self.label_17.setMaximumSize(QtCore.QSize(5, 5))
        self.label_17.setText(_fromUtf8(""))
        self.label_17.setPixmap(QtGui.QPixmap(_fromUtf8("./image/asterisk.png")))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 2, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.layoutWidget)
        self.label_18.setMinimumSize(QtCore.QSize(5, 5))
        self.label_18.setMaximumSize(QtCore.QSize(5, 5))
        self.label_18.setText(_fromUtf8(""))
        self.label_18.setPixmap(QtGui.QPixmap(_fromUtf8("./image/asterisk.png")))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 9, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.lineEdit_7)
        Dialog.setTabOrder(self.lineEdit_7, self.radioButton_2)
        Dialog.setTabOrder(self.radioButton_2, self.radioButton)
        Dialog.setTabOrder(self.radioButton, self.lineEdit_5)
        Dialog.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        Dialog.setTabOrder(self.lineEdit_6, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.lineEdit_9)
        Dialog.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        Dialog.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        Dialog.setTabOrder(self.lineEdit_11, self.pushButton)
        
        QtCore.QObject.connect(self.pushButton,  QtCore.SIGNAL(_fromUtf8("clicked()")),  self.Signin)
        QtCore.QObject.connect(Dialog, QtCore.SIGNAL(_fromUtf8("finished(int)")), self.finish)
        
    def finish(self):
        import Ui_Login
        reload(Ui_Login)

    def Signin(self):
        """就按照从上到下的顺序来"""
        info1 = self.lineEdit.text().toUtf8()               # 用户名
        info2 = str(self.lineEdit_2.text())                 # 密码
        info3 = str(self.lineEdit_3.text())                 # 确认密码
        info4 = self.lineEdit_7.text().toUtf8()            # 姓名
        info5 = self.radioButton_2.isChecked()           # 性别男
        info6 = self.lineEdit_5.text().toUtf8()            # 电话
        info7 = self.lineEdit_6.text().toUtf8()            # 职务
        info8 = self.comboBox.currentText().toUtf8()  # 学院
        info9 = self.lineEdit_9.text().toUtf8()            # 联系地址
        info10 = self.lineEdit_10.text().toUtf8()         # 电子邮件
        info11 = self.lineEdit_11.text().toUtf8()         # 工作单位

        # 还是一个一个挨着检查吧，检查的时候顺便把用户名info1和电子邮件info10的唯一性给检查了
        import Check
        import ConnectSQL
        Zhuce = ConnectSQL.ConnectSQL(admin.sql['host'], admin.sql['user'], admin.sql['passwd'], admin.sql['db'])
        # 检查邮箱地址是否正确
        if not Check.isEmail(info10):
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"请输入正确的邮箱地址")
            return
        
        # 检查邮箱的唯一性
        command = "select * from User where Mail='" + info10 + "'"
        if Zhuce.query(command)[0]:
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"该邮箱已注册")
            return
        # 检查用户名的正确性
        if not Check.isStd(unicode(info1,  "utf-8")):
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"请输入正确的用户名(不得有特殊字符，长度为3-20)")
            return
        # 检查用户名的唯一性
        command = "select * from User where Username='" + info1 + "'"
        if Zhuce.query(command)[0]:
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"该用户名已注册")
            return
        # 检查密码的正确性
        if not Check.isPass(info2):
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"请输入正确的密码（长度为6-20）")
            return
        if info2 != info3:
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"两次密码输入不匹配")
            return
        if (not Check.isName(unicode(info4,  "utf-8"))) and (not info4.isEmpty()):
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"请输入正确的姓名（不得有特殊字符，长度为2-4）")
            return
        if (not Check.isTel(info6)) and (not info6.isEmpty()):
            QtGui.QMessageBox.warning(Dialog2, u"发生错误",   u"请输入正确的电话号码（不得有特殊字符），长度为8或11")
            return 
        if (not Check.isZhiwu(unicode(info7,  "utf-8"))) and (not info7.isEmpty()):
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"请输入正确的职务信息（不得有特殊字符，长度为2-20）")
            return
        if (not Check.isZhiwu(unicode(info9,  "utf-8"))) and (not info9.isEmpty()):
            QtGui.QMessageBox.warning(Dialog2, u"发生错误",   u"请输入正确的联系地址（不得有特殊字符，长度为6-20）")
            return
        if (not Check.isZhiwu(unicode(info11,  "utf-8"))) and (not info11.isEmpty()):
            QtGui.QMessageBox.warning(Dialog2,  u"发生错误",  u"请输入正确的工作单位（不得有特殊字符，长度为6-20）")
            return
        
        # 所有信息正确无误后就可以直接执行注册命令了
        # 首先应该是活得最大的ID，需要注意的是返回值是一个tuple
        Zhuce.query("select max(ID) from User")
        ID = Zhuce.fetch_queryresult()[0][0] + 1
        
        try:
            # 首先插入User表
            command = "insert into User values(%s, %s, %s, %s)"
            args = (ID,  info1,  info2,  info10)
            Zhuce.execute(command,  args)
            # 然后插入OtherInfo表
            command = "insert into OtherInfo values(%s, %s, %s, %s, %s, %s, %s, %s)"
            args = (ID,  info4,  info5,  info6,  info7,  info8,  info9,  info11)
            Zhuce.execute(command,  args)
        except:
            print '晓求不得有啥子错误'
        
        else:
            # 然后是新建一个远程仓库，上面的ID就是它的ID
            try:
                MyRepo = MyFtp(100,  admin.ftp['ip'], admin.ftp['port'], admin.ftp['timeout'], admin.ftp['admin'],  admin.ftp['passwd'])
                MyRepo.cd('..')
                MyRepo.mkdir(str(ID))
                MyRepo.cd(str(ID))
                MyRepo.mkdir('.trash')
            except:
                print 'FTP连接失败'
            
            Zhuce.commit()
            Zhuce.close()
            QtGui.QMessageBox.information(Dialog2,  u"成功提示",  u"注册成功")
            Dialog2.close()
            import Ui_Login
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "帐号注册", None))
        self.pushButton.setText(_translate("Dialog", "提交", None))
        self.label_9.setText(_translate("Dialog", "联系地址", None))
        self.label_8.setText(_translate("Dialog", "学院", None))
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
        self.label_6.setText(_translate("Dialog", "电话", None))
        self.label_11.setText(_translate("Dialog", "工作单位", None))
        self.label_2.setText(_translate("Dialog", "密码", None))
        self.label_5.setText(_translate("Dialog", "性别", None))
        self.label_3.setText(_translate("Dialog", "确认密码", None))
        self.radioButton_2.setText(_translate("Dialog", "男", None))
        self.radioButton.setText(_translate("Dialog", "女", None))
        self.label_7.setText(_translate("Dialog", "职务", None))
        self.label_4.setText(_translate("Dialog", "姓名", None))
        self.label_10.setText(_translate("Dialog", "电子邮件", None))
        self.label_13.setText(_translate("Dialog", "用户名，用于登录", None))
        self.label_14.setText(_translate("Dialog", "请输入密码，区分大小写", None))
        self.label_15.setText(_translate("Dialog", "请再次输入密码", None))
        self.label_21.setText(_translate("Dialog", "方便密码找回", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
else:
    Dialog2 = QtGui.QDialog()
    ui2 = Ui_Dialog()
    ui2.setupUi(Dialog2)
    Dialog2.show()
