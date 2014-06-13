# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Papermanage\UI\Login.ui'
#
# Created: Sun Jun 01 15:52:48 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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
        Dialog.resize(500, 300)
        Dialog.setMinimumSize(QtCore.QSize(500, 300))
        Dialog.setMaximumSize(QtCore.QSize(500, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./image/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 81))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("./image/Logo.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 112, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 150, 311, 20))
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 181, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 210, 311, 20))
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(70, 250, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 250, 71, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(234, 242, 150, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 30, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 148, 75, 23))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 208, 75, 23))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        QtCore.QObject.connect(self.pushButton_2,  QtCore.SIGNAL(_fromUtf8("clicked()")),  self.Signin)
        QtCore.QObject.connect(self.pushButton,  QtCore.SIGNAL(_fromUtf8("clicked()")),  self.Login)
        
    def Login(self):
        user = str(self.lineEdit.text())
        passwd = str(self.lineEdit_2.text())
        import ConnectSQL
        try:
            Login = ConnectSQL.ConnectSQL('192.168.175.128', 'yourgod',  '896499825',  'PaperManage')
            import Check
            if Check.isEmail(user):
               command = "select ID, Username, Userpasswd, Mail from User where Mail='" + user + "'"
            else:
                command = "select ID, Username, Userpasswd, Mail from User where Username='" + user + "'" 
            Login.query(command)
            result = Login.fetch_queryresult()
            # 如果没有查询到结果那么下面这一句result自然就会抛出异常了
            if (result[0][1] == user or result[0][3] == user) and (result[0][2] == passwd):
                self.ID = result[0][0]
                Dialog1.close()
                import Ui_Main
            else:
                raise
        except: 
            QtGui.QMessageBox.warning(Dialog1,  u"发生错误",  u"用户名或密码错误邮箱")
            
    def Signin(self):
        Dialog1.close()
        import sys
        # 根据模块是否是第一次加载来确定reload
        try:
            a = sys.modules
            a["UI.Ui_Signin"]
            import Ui_Signin
            reload(Ui_Signin)
        except:
            import Ui_Signin
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "论文资料管理系统", None))
        self.label_2.setText(_translate("Dialog", "用户名/邮箱", None))
        self.label_3.setText(_translate("Dialog", "密码", None))
        self.checkBox.setText(_translate("Dialog", "记住密码", None))
        self.checkBox_2.setText(_translate("Dialog", "自动登录", None))
        self.pushButton.setText(_translate("Dialog", "登录", None))
        self.label_6.setText(_translate("Dialog", "文档资料管理系统", None))
        self.pushButton_2.setText(_translate("Dialog", "注册帐号", None))
        self.pushButton_3.setText(_translate("Dialog", "密码找回", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
else:
    Dialog1 = QtGui.QDialog()
    ui1 = Ui_Dialog()
    ui1.setupUi(Dialog1)
    Dialog1.show()
    
