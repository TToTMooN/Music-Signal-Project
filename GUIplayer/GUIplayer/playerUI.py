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
        MainWindow.resize(1366, 768)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.refSlider = QtGui.QSlider(self.centralWidget)
        self.refSlider.setGeometry(QtCore.QRect(70, 460, 571, 21))
        self.refSlider.setOrientation(QtCore.Qt.Horizontal)
        self.refSlider.setObjectName(_fromUtf8("refSlider"))
        self.refGraph = QtGui.QGraphicsView(self.centralWidget)
        self.refGraph.setGeometry(QtCore.QRect(70, 40, 571, 401))
        self.refGraph.setObjectName(_fromUtf8("refGraph"))
        self.userGraph = QtGui.QGraphicsView(self.centralWidget)
        self.userGraph.setGeometry(QtCore.QRect(720, 40, 571, 401))
        self.userGraph.setObjectName(_fromUtf8("userGraph"))
        self.userSlider = QtGui.QSlider(self.centralWidget)
        self.userSlider.setGeometry(QtCore.QRect(720, 460, 571, 20))
        self.userSlider.setOrientation(QtCore.Qt.Horizontal)
        self.userSlider.setObjectName(_fromUtf8("userSlider"))
        self.refPlayTime = QtGui.QLCDNumber(self.centralWidget)
        self.refPlayTime.setGeometry(QtCore.QRect(553, 480, 81, 41))
        self.refPlayTime.setObjectName(_fromUtf8("refPlayTime"))
        self.userPlayTime = QtGui.QLCDNumber(self.centralWidget)
        self.userPlayTime.setGeometry(QtCore.QRect(1213, 480, 81, 41))
        self.userPlayTime.setObjectName(_fromUtf8("userPlayTime"))
        self.userplaybutton = QtGui.QPushButton(self.centralWidget)
        self.userplaybutton.setGeometry(QtCore.QRect(740, 490, 111, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userplaybutton.setFont(font)
        self.userplaybutton.setObjectName(_fromUtf8("userplaybutton"))
        self.reffreqlabel = QtGui.QLabel(self.centralWidget)
        self.reffreqlabel.setGeometry(QtCore.QRect(70, 530, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reffreqlabel.setFont(font)
        self.reffreqlabel.setObjectName(_fromUtf8("reffreqlabel"))
        self.reffreqtextbox = QtGui.QTextBrowser(self.centralWidget)
        self.reffreqtextbox.setGeometry(QtCore.QRect(180, 530, 141, 33))
        self.reffreqtextbox.setObjectName(_fromUtf8("reffreqtextbox"))
        self.refHzlabel = QtGui.QLabel(self.centralWidget)
        self.refHzlabel.setGeometry(QtCore.QRect(330, 530, 81, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.refHzlabel.setFont(font)
        self.refHzlabel.setObjectName(_fromUtf8("refHzlabel"))
        self.userfreqtextbox = QtGui.QTextBrowser(self.centralWidget)
        self.userfreqtextbox.setGeometry(QtCore.QRect(830, 530, 141, 33))
        self.userfreqtextbox.setObjectName(_fromUtf8("userfreqtextbox"))
        self.userHzlabel = QtGui.QLabel(self.centralWidget)
        self.userHzlabel.setGeometry(QtCore.QRect(980, 530, 81, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userHzlabel.setFont(font)
        self.userHzlabel.setObjectName(_fromUtf8("userHzlabel"))
        self.userfreqlabel = QtGui.QLabel(self.centralWidget)
        self.userfreqlabel.setGeometry(QtCore.QRect(720, 530, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userfreqlabel.setFont(font)
        self.userfreqlabel.setObjectName(_fromUtf8("userfreqlabel"))
        self.locktimecheckbox = QtGui.QCheckBox(self.centralWidget)
        self.locktimecheckbox.setGeometry(QtCore.QRect(900, 490, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.locktimecheckbox.setFont(font)
        self.locktimecheckbox.setObjectName(_fromUtf8("locktimecheckbox"))
        self.refsignallabel = QtGui.QLabel(self.centralWidget)
        self.refsignallabel.setGeometry(QtCore.QRect(70, 10, 201, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.refsignallabel.setFont(font)
        self.refsignallabel.setObjectName(_fromUtf8("refsignallabel"))
        self.usersignallabel = QtGui.QLabel(self.centralWidget)
        self.usersignallabel.setGeometry(QtCore.QRect(720, 10, 211, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usersignallabel.setFont(font)
        self.usersignallabel.setObjectName(_fromUtf8("usersignallabel"))
        self.reftablewidget = QtGui.QTableWidget(self.centralWidget)
        self.reftablewidget.setGeometry(QtCore.QRect(60, 580, 571, 111))
        self.reftablewidget.setObjectName(_fromUtf8("reftablewidget"))
        self.reftablewidget.setColumnCount(0)
        self.reftablewidget.setRowCount(0)
        self.usertablewidget = QtGui.QTableWidget(self.centralWidget)
        self.usertablewidget.setGeometry(QtCore.QRect(720, 580, 571, 111))
        self.usertablewidget.setObjectName(_fromUtf8("usertablewidget"))
        self.usertablewidget.setColumnCount(0)
        self.usertablewidget.setRowCount(0)
        self.userRecordButton = QtGui.QPushButton(self.centralWidget)
        self.userRecordButton.setGeometry(QtCore.QRect(1180, 530, 111, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userRecordButton.setFont(font)
        self.userRecordButton.setObjectName(_fromUtf8("userRecordButton"))
        self.compareButton = QtGui.QPushButton(self.centralWidget)
        self.compareButton.setGeometry(QtCore.QRect(70, 490, 111, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.compareButton.setFont(font)
        self.compareButton.setObjectName(_fromUtf8("compareButton"))
        self.reffreqlabel_2 = QtGui.QLabel(self.centralWidget)
        self.reffreqlabel_2.setGeometry(QtCore.QRect(200, 490, 101, 33))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reffreqlabel_2.setFont(font)
        self.reffreqlabel_2.setObjectName(_fromUtf8("reffreqlabel_2"))
        self.similarityText = QtGui.QTextBrowser(self.centralWidget)
        self.similarityText.setGeometry(QtCore.QRect(290, 490, 81, 33))
        self.similarityText.setObjectName(_fromUtf8("similarityText"))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.similarityText.setFont(font)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
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
        self.actionGuide_Book = QtGui.QAction(MainWindow)
        self.actionGuide_Book.setObjectName(_fromUtf8("actionGuide_Book"))
        self.menuImport.addSeparator()
        self.menuImport.addAction(self.actionImport_Ref_File)
        self.menuImport.addAction(self.actionImport_User_File)
        self.menuImport.addAction(self.actionGuide_Book)
        self.menuBar.addAction(self.menuImport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.refGraph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.userplaybutton.setText(_translate("MainWindow", "Play/Pause", None))
        self.reffreqlabel.setText(_translate("MainWindow", "Frequency", None))
        self.refHzlabel.setText(_translate("MainWindow", "Hz", None))
        self.userHzlabel.setText(_translate("MainWindow", "Hz", None))
        self.userfreqlabel.setText(_translate("MainWindow", "Frequency", None))
        self.locktimecheckbox.setText(_translate("MainWindow", "Lock time with ref signal", None))
        self.refsignallabel.setText(_translate("MainWindow", "Reference Signal", None))
        self.usersignallabel.setText(_translate("MainWindow", "User Signal", None))
        self.userRecordButton.setText(_translate("MainWindow", "Record", None))
        self.compareButton.setText(_translate("MainWindow", "Compare", None))
        self.reffreqlabel_2.setText(_translate("MainWindow", "Similarity:", None))
        self.menuImport.setTitle(_translate("MainWindow", "Menu", None))
        self.actionImport_Ref_File.setText(_translate("MainWindow", "Import Ref File", None))
        self.actionImport_User_File.setText(_translate("MainWindow", "Import User File", None))
        self.actionGuide_Book.setText(_translate("MainWindow", "Guide Book", None))

