# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(436, 666)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 391, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/210201-coinauto.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 150, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 351, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 311, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 210, 341, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 181, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 270, 341, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 181, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 310, 181, 16))
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(50, 370, 341, 21))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 410, 341, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(50, 450, 341, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 560, 341, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 590, 341, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(50, 620, 341, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 340, 151, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 340, 151, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Coin Auto"))
        self.label_2.setText(_translate("Dialog", "Bithumb API Connect Key"))
        self.label_3.setText(_translate("Dialog", "Bithumb API Secret Key"))
        self.label_4.setText(_translate("Dialog", "Choose Coin"))
        self.label_5.setText(_translate("Dialog", "Buy Price (￦)"))
        self.label_6.setText(_translate("Dialog", "Sell Price (￦)"))
        self.checkBox.setText(_translate("Dialog", "All responsibilities are yours"))
        self.pushButton.setText(_translate("Dialog", "Start Auto Trading"))
        self.label_7.setText(_translate("Dialog", "Please Buy Me a Cup of Coffee."))
        self.label_8.setText(_translate("Dialog", "ETH\t0x20B65F0C4027345163f0A4Ee9f9d6Dd39ec957A6"))
        self.label_9.setText(_translate("Dialog", "BTC\t3JUoGmQLfhFBNfKBWNa92wGQ7w13CxjoBy"))
        self.lineEdit_3.setText(_translate("Dialog", "0"))
        self.lineEdit_4.setText(_translate("Dialog", "0"))