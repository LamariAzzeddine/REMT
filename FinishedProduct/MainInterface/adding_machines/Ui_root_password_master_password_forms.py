# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\adding_machines\root_password_master_password_forms.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(413, 280)
        self.RootPassword_config = PasswordLineEdit(Form)
        self.RootPassword_config.setGeometry(QtCore.QRect(10, 140, 391, 33))
        self.RootPassword_config.setObjectName("RootPassword_config")
        self.StartTheConf_config = PrimaryPushButton(Form)
        self.StartTheConf_config.setGeometry(QtCore.QRect(250, 230, 153, 32))
        self.StartTheConf_config.setObjectName("StartTheConf_config")
        self.CancelTheConf_config = PushButton(Form)
        self.CancelTheConf_config.setGeometry(QtCore.QRect(130, 230, 102, 32))
        self.CancelTheConf_config.setObjectName("CancelTheConf_config")
        self.StrongBodyLabel = StrongBodyLabel(Form)
        self.StrongBodyLabel.setGeometry(QtCore.QRect(10, 10, 281, 19))
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setGeometry(QtCore.QRect(10, 30, 971, 21))
        self.BodyLabel.setObjectName("BodyLabel")
        self.BodyLabel_2 = BodyLabel(Form)
        self.BodyLabel_2.setGeometry(QtCore.QRect(10, 50, 691, 19))
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.BodyLabel_3 = BodyLabel(Form)
        self.BodyLabel_3.setGeometry(QtCore.QRect(10, 70, 191, 19))
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.RootUser_config = LineEdit(Form)
        self.RootUser_config.setGeometry(QtCore.QRect(10, 100, 391, 33))
        self.RootUser_config.setObjectName("RootUser_config")
        self.MasterPassword_config = PasswordLineEdit(Form)
        self.MasterPassword_config.setGeometry(QtCore.QRect(10, 180, 391, 33))
        self.MasterPassword_config.setObjectName("MasterPassword_config")
        self.ProgressBar_2 = ProgressBar(Form)
        self.ProgressBar_2.setGeometry(QtCore.QRect(10, 290, 391, 4))
        self.ProgressBar_2.setObjectName("ProgressBar_2")
        self.StrongBodyLabel_2 = StrongBodyLabel(Form)
        self.StrongBodyLabel_2.setGeometry(QtCore.QRect(10, 270, 111, 19))
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.RootPassword_config.setPlaceholderText(_translate("Form", "Password"))
        self.StartTheConf_config.setText(_translate("Form", "Start "))
        self.CancelTheConf_config.setText(_translate("Form", "Cancel"))
        self.StrongBodyLabel.setText(_translate("Form", "Enter the machine\'s root user and password"))
        self.BodyLabel.setText(_translate("Form", "Please be aware that the password you\'re entering in this form "))
        self.BodyLabel_2.setText(_translate("Form", "will be utilized solely for configuring the machine and will not be "))
        self.BodyLabel_3.setText(_translate("Form", "stored anywhere afterward."))
        self.RootUser_config.setPlaceholderText(_translate("Form", "Root user"))
        self.MasterPassword_config.setPlaceholderText(_translate("Form", "Master Password"))
        self.StrongBodyLabel_2.setText(_translate("Form", "Progress:"))
from qfluentwidgets import BodyLabel, LineEdit, PasswordLineEdit, PrimaryPushButton, ProgressBar, PushButton, StrongBodyLabel
