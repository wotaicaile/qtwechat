# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatpanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 691)
        Form.setStyleSheet("")
        self.Chatframe = QtWidgets.QFrame(Form)
        self.Chatframe.setGeometry(QtCore.QRect(40, 70, 531, 431))
        self.Chatframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Chatframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Chatframe.setObjectName("Chatframe")
        self.messageEdit = QtWidgets.QTextEdit(self.Chatframe)
        self.messageEdit.setGeometry(QtCore.QRect(20, 290, 491, 101))
        self.messageEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.messageEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.messageEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.messageEdit.setObjectName("messageEdit")
        self.sendPbn = QtWidgets.QPushButton(self.Chatframe)
        self.sendPbn.setGeometry(QtCore.QRect(440, 400, 61, 31))
        self.sendPbn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendPbn.setStyleSheet("background-color: rgb(215, 255, 255);\n"
"color:black;\n"
"box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
"\n"
"")
        self.sendPbn.setObjectName("sendPbn")
        self.label = QtWidgets.QLabel(self.Chatframe)
        self.label.setGeometry(QtCore.QRect(1, -6, 531, 281))
        self.label.setStyleSheet("\n"
"background-color: rgb(248, 248, 248);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.messageEdit_2 = QtWidgets.QTextEdit(self.Chatframe)
        self.messageEdit_2.setGeometry(QtCore.QRect(20, 30, 491, 231))
        self.messageEdit_2.setStyleSheet("\n"
"font-size:22px;\n"
"font-family: 微软雅黑;\n"
"\n"
"background-color: rgb(248, 248, 248);")
        self.messageEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.messageEdit_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.messageEdit_2.setObjectName("messageEdit_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Chatframe)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 511, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout1.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout1.setObjectName("MaingridLayout1")
        self.Backgroundlabel = QtWidgets.QLabel(self.Chatframe)
        self.Backgroundlabel.setGeometry(QtCore.QRect(-280, -50, 977, 583))
        self.Backgroundlabel.setStyleSheet("border-image: url(:/resource/background.png);")
        self.Backgroundlabel.setText("")
        self.Backgroundlabel.setObjectName("Backgroundlabel")
        self.Backgroundlabel.raise_()
        self.sendPbn.raise_()
        self.label.raise_()
        self.messageEdit_2.raise_()
        self.gridLayoutWidget.raise_()
        self.messageEdit.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.messageEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sendPbn.setText(_translate("Form", "发送"))
        self.messageEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:22px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
import main_rc
