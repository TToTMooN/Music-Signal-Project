# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(960, 630)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.refSlider = QtGui.QSlider(self.centralWidget)
        self.refSlider.setGeometry(QtCore.QRect(50, 360, 401, 21))
        self.refSlider.setOrientation(QtCore.Qt.Horizontal)
        self.refSlider.setObjectName(_fromUtf8("refSlider"))
        self.refGraph = QtGui.QGraphicsView(self.centralWidget)
        self.refGraph.setGeometry(QtCore.QRect(50, 40, 401, 291))
        self.refGraph.setObjectName(_fromUtf8("refGraph"))
        self.userGraph = QtGui.QGraphicsView(self.centralWidget)
        self.userGraph.setGeometry(QtCore.QRect(480, 40, 401, 291))
        self.userGraph.setObjectName(_fromUtf8("userGraph"))
        self.userSlider = QtGui.QSlider(self.centralWidget)
        self.userSlider.setGeometry(QtCore.QRect(480, 360, 401, 20))
        self.userSlider.setOrientation(QtCore.Qt.Horizontal)
        self.userSlider.setObjectName(_fromUtf8("userSlider"))
        self.refPlayTime = QtGui.QLCDNumber(self.centralWidget)
        self.refPlayTime.setGeometry(QtCore.QRect(390, 390, 64, 23))
        self.refPlayTime.setObjectName(_fromUtf8("refPlayTime"))
        self.userPlayTime = QtGui.QLCDNumber(self.centralWidget)
        self.userPlayTime.setGeometry(QtCore.QRect(820, 390, 64, 23))
        self.userPlayTime.setObjectName(_fromUtf8("userPlayTime"))
        self.userpausebutton = QtGui.QPushButton(self.centralWidget)
        self.userpausebutton.setGeometry(QtCore.QRect(570, 390, 75, 23))
        self.userpausebutton.setObjectName(_fromUtf8("userpausebutton"))
        self.userplaybutton = QtGui.QPushButton(self.centralWidget)
        self.userplaybutton.setGeometry(QtCore.QRect(480, 390, 75, 23))
        self.userplaybutton.setObjectName(_fromUtf8("userplaybutton"))
        self.reffreqlabel = QtGui.QLabel(self.centralWidget)
        self.reffreqlabel.setGeometry(QtCore.QRect(50, 430, 81, 31))
        self.reffreqlabel.setObjectName(_fromUtf8("reffreqlabel"))
        self.reffreqtextbox = QtGui.QTextBrowser(self.centralWidget)
        self.reffreqtextbox.setGeometry(QtCore.QRect(110, 430, 141, 31))
        self.reffreqtextbox.setObjectName(_fromUtf8("reffreqtextbox"))
        self.refHzlabel = QtGui.QLabel(self.centralWidget)
        self.refHzlabel.setGeometry(QtCore.QRect(260, 430, 81, 31))
        self.refHzlabel.setObjectName(_fromUtf8("refHzlabel"))
        self.userfreqtextbox = QtGui.QTextBrowser(self.centralWidget)
        self.userfreqtextbox.setGeometry(QtCore.QRect(540, 430, 141, 31))
        self.userfreqtextbox.setObjectName(_fromUtf8("userfreqtextbox"))
        self.userHzlabel = QtGui.QLabel(self.centralWidget)
        self.userHzlabel.setGeometry(QtCore.QRect(690, 430, 81, 31))
        self.userHzlabel.setObjectName(_fromUtf8("userHzlabel"))
        self.userfreqlabel = QtGui.QLabel(self.centralWidget)
        self.userfreqlabel.setGeometry(QtCore.QRect(480, 430, 81, 31))
        self.userfreqlabel.setObjectName(_fromUtf8("userfreqlabel"))
        self.locktimecheckbox = QtGui.QCheckBox(self.centralWidget)
        self.locktimecheckbox.setGeometry(QtCore.QRect(660, 390, 111, 17))
        self.locktimecheckbox.setObjectName(_fromUtf8("locktimecheckbox"))
        self.recordbutton = QtGui.QPushButton(self.centralWidget)
        self.recordbutton.setGeometry(QtCore.QRect(820, 430, 75, 23))
        self.recordbutton.setObjectName(_fromUtf8("recordbutton"))
        self.refsignallabel = QtGui.QLabel(self.centralWidget)
        self.refsignallabel.setGeometry(QtCore.QRect(50, 20, 201, 16))
        self.refsignallabel.setObjectName(_fromUtf8("refsignallabel"))
        self.usersignallabel = QtGui.QLabel(self.centralWidget)
        self.usersignallabel.setGeometry(QtCore.QRect(480, 20, 201, 16))
        self.usersignallabel.setObjectName(_fromUtf8("usersignallabel"))
        self.reftablewidget = QtGui.QTableWidget(self.centralWidget)
        self.reftablewidget.setGeometry(QtCore.QRect(50, 470, 401, 101))
        self.reftablewidget.setObjectName(_fromUtf8("reftablewidget"))
        self.reftablewidget.setColumnCount(0)
        self.reftablewidget.setRowCount(0)
        self.usertablewidget = QtGui.QTableWidget(self.centralWidget)
        self.usertablewidget.setGeometry(QtCore.QRect(480, 470, 411, 101))
        self.usertablewidget.setObjectName(_fromUtf8("usertablewidget"))
        self.usertablewidget.setColumnCount(0)
        self.usertablewidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 960, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuImport = QtGui.QMenu(self.menuBar)
        self.menuImport.setObjectName(_fromUtf8("menuImport"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionImport_Ref_File = QtGui.QAction(MainWindow)
        self.actionImport_Ref_File.setObjectName(_fromUtf8("actionImport_Ref_File"))
        self.actionImport_User_File = QtGui.QAction(MainWindow)
        self.actionImport_User_File.setObjectName(_fromUtf8("actionImport_User_File"))
        self.menuImport.addSeparator()
        self.menuImport.addAction(self.actionImport_Ref_File)
        self.menuImport.addAction(self.actionImport_User_File)
        self.menuBar.addAction(self.menuImport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.refGraph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.userpausebutton.setText(_translate("MainWindow", "Pause", None))
        self.userplaybutton.setText(_translate("MainWindow", "Play", None))
        self.reffreqlabel.setText(_translate("MainWindow", "Frequency", None))
        self.refHzlabel.setText(_translate("MainWindow", "Hz", None))
        self.userHzlabel.setText(_translate("MainWindow", "Hz", None))
        self.userfreqlabel.setText(_translate("MainWindow", "Frequency", None))
        self.locktimecheckbox.setText(_translate("MainWindow", "Lock time with ref", None))
        self.recordbutton.setText(_translate("MainWindow", "Record", None))
        self.refsignallabel.setText(_translate("MainWindow", "Reference Signal", None))
        self.usersignallabel.setText(_translate("MainWindow", "User Signal", None))
        self.menuImport.setTitle(_translate("MainWindow", "Import", None))
        self.actionImport_Ref_File.setText(_translate("MainWindow", "Import Ref File", None))
        self.actionImport_User_File.setText(_translate("MainWindow", "Import User File", None))

