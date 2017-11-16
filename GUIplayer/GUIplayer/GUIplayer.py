#!/usr/bin/env python
import sip
sip.setapi('QString', 2)

import sys
from PyQt4 import QtCore, QtGui

try:
    from PyQt4.phonon import Phonon
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "Music Player",
            "Your Qt installation does not have Phonon support.",
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.NoButton)
    sys.exit(1)

QtCore.QCoreApplication.setLibraryPaths(['C:\Anaconda2\Lib\site-packages\PyQt4\plugins'])
# This is the path
from playerUI import *
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QtGui.QMainWindow, self).__init__(parent)

        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.mediaObject.setTickInterval(1000)
        self.mediaObject.tick.connect(self.userTimeChange)
        self.mediaObject.totalTimeChanged.connect(self.userTotalTimeChange)
        #self.mediaObject.currentSourceChanged.connect(self.sourceChanged)
        Phonon.createPath(self.mediaObject, self.audioOutput)

        self.metaInformationResolver = Phonon.MediaObject(self)
        self.metaInformationResolver.stateChanged.connect(self.metaStateChanged)

        self.refAudioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.refMetaInformationResolver = Phonon.MediaObject(self)
        self.refMetaInformationResolver.stateChanged.connect(self.refMetaStateChanged)
        self.refMetaInformationResolver.totalTimeChanged.connect(self.refTotalTimeChange)
        Phonon.createPath(self.refMetaInformationResolver, self.refAudioOutput)
        

        self.setupUi(self)

        self.userSources = []
        self.refSources = []
        
        self.actionImport_User_File.triggered.connect(self.addUserFiles)
        self.actionImport_Ref_File.triggered.connect(self.addRefFiles)
        #init sliders
        self.userSlider.setValue(0)
        self.userSlider.setEnabled(False)
        self.userSlider.sliderPressed.connect(self.userSlidePress)
        self.userSlider.sliderReleased.connect(self.userSlideChange)

        self.refSlider.setValue(0)
        self.refSlider.setEnabled(False)
        self.refSlider.valueChange.connect(self.refSlideChange)
        #init buttons
        self.userplaybutton.clicked.connect(self.userPlayOrPause)
        self.userplaybutton.setEnabled(False)
        self.userpausebutton.clicked.connect(self.userPlayOrPause)
        self.userplaybutton.setEnabled(False)
        self.recordbutton.setEnabled(False)
        #init display time
        self.user_current_time = 0
        self.ref_current_time = 0
        #init LCD display start from 00:00
        self.userPlayTime.display("00:00")
        self.userPlayTime.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.refPlayTime.display("00:00")
        self.refPlayTime.setSegmentStyle(QtGui.QLCDNumber.Flat)
        #setup music table
        headers = ("Title", "Artist","Date")

        self.usertablewidget.setColumnCount(2)
        self.usertablewidget.setRowCount(0)
        self.usertablewidget.setHorizontalHeaderLabels(headers)
        self.usertablewidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.usertablewidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        
        self.reftablewidget.setColumnCount(2)
        self.reftablewidget.setRowCount(0)
        self.reftablewidget.setHorizontalHeaderLabels(headers)
        self.reftablewidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.reftablewidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)


        #init figure
        self.userscene = QtGui.QGraphicsScene()

        self.refscene = QtGui.QGraphicsScene()

    def guide(self):
        QtGui.QMessageBox.information(self, "About the spectrum frequency",
                "This is the guide for notes and frequency correspondence")

    def addUserFiles(self):
        file = QtGui.QFileDialog.getOpenFileName(self, "Select User Input File",
                QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation))
        self.mediaObject.setCurrentSource(Phonon.MediaSource(file))
        self.metaInformationResolver.setCurrentSource(Phonon.MediaSource(file))
        self.mediaObject.play()
        self.userplaybutton.setEnabled(True)
        self.userpausebutton.setEnabled(True)
        self.userSlider.setEnabled(True)
        #plot spectrum
        y, sr = librosa.load(file, duration = 10)
        D = librosa.stft(y, n_fft=2048*4, hop_length=2048/4)
        S = np.abs(D)
        A = librosa.amplitude_to_db(S, ref=np.max)
        librosa.display.specshow(A, y_axis='log', x_axis='time')
        plt.axis([0, 10, 128, 1024])
        #save file
        plt.savefig('userplot.png')
        self.userpixmap = QtGui.QPixmap("userplot.png")
        self.userpixmap = self.userpixmap.scaled(420,290)
        self.userscene.clear()
        self.userscene.addPixmap(self.userpixmap)
        self.userGraph.setScene(self.userscene)

    def addRefFiles(self):
        file = QtGui.QFileDialog.getOpenFileName(self, "Select Ref Input File",
                QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation))
        self.refMetaInformationResolver.setCurrentSource(Phonon.MediaSource(file))
        self.refSlider.setEnabled(True)
        self.refMetaInformationResolver.play()
        self.refMetaInformationResolver.stop()
        print self.refMetaInformationResolver.totalTime()
        self.refSlider.setRange(0, self.refMetaInformationResolver.totalTime())
        #plot spectrum
        y, sr = librosa.load(file, duration = 10)
        D = librosa.stft(y, n_fft=2048*4, hop_length=2048/4)
        S = np.abs(D)
        A = librosa.amplitude_to_db(S, ref=np.max)
        librosa.display.specshow(A, y_axis='log', x_axis='time')
        plt.axis([0, 10, 128, 1024])
        plt.savefig('refplot.png')
        #save file
        self.refpixmap = QtGui.QPixmap("refplot.png")
        self.refpixmap = self.refpixmap.scaled(420,290)
        self.refscene.clear()
        self.refscene.addPixmap(self.refpixmap)
        self.refGraph.setScene(self.refscene)


    def metaStateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            QtGui.QMessageBox.warning(self, "Error opening files",
                    self.metaInformationResolver.errorString())

            return
        metaData = self.metaInformationResolver.metaData()
        title = metaData.get('TITLE', [''])[0]
        if not title:
            title = self.metaInformationResolver.currentSource().fileName()
       
        titleItem = QtGui.QTableWidgetItem(title)
        titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)

        artist = metaData.get('ARTIST', [''])[0]
        artistItem = QtGui.QTableWidgetItem(artist)
        artistItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)


        currentRow = self.usertablewidget.rowCount()
        self.usertablewidget.insertRow(currentRow)
        self.usertablewidget.setItem(currentRow,0,titleItem)
        self.usertablewidget.setItem(currentRow,1,artistItem)

    def refMetaStateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            QtGui.QMessageBox.warning(self, "Error opening files",
                    self.refMetaInformationResolver.errorString())
            return
        metaData = self.refMetaInformationResolver.metaData()
        title = metaData.get('TITLE', [''])[0]
        if not title:
            title = self.metaInformationResolver.currentSource().fileName()
       
        titleItem = QtGui.QTableWidgetItem(title)
        titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)

        artist = metaData.get('ARTIST', [''])[0]
        artistItem = QtGui.QTableWidgetItem(artist)
        artistItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)


        currentRow = self.usertablewidget.rowCount()
        self.reftablewidget.insertRow(currentRow)
        self.reftablewidget.setItem(currentRow,0,titleItem)
        self.reftablewidget.setItem(currentRow,1,artistItem)

    def userPlayOrPause(self):
        if Phonon.PlayingState == self.mediaObject.state():
            self.mediaObject.pause()
        elif Phonon.PausedState == self.mediaObject.state():
            self.mediaObject.play()
    def userSlidePress(self):
        self.userSliderOldValue = self.userSlider.value()

    def userSlideChange(self):
        value = self.userSlider.value()
        self.mediaObject.seek(value)
        if self.locktimecheckbox.isChecked():
            change = value - self.userSliderOldValue
            self.refSlider.setValue(self.refSlider.value()+change)


    def refSlideChange(self):
        time = self.refSlider.value()
        self.ref_current_time = time
        displayTime = QtCore.QTime(0,(time / 60000) % 60, (time / 1000) % 60)
        self.refPlayTime.display(displayTime.toString('mm:ss'))
    
    def userTimeChange(self, time):  
        self.userSlider.setValue(time)
        self.user_current_time = time
        displayTime = QtCore.QTime(0,(time / 60000) % 60, (time / 1000) % 60)
        self.userPlayTime.display(displayTime.toString('mm:ss'))
        

    def userTotalTimeChange(self, time):
        self.userSlider.setRange(0,time)

    def refTotalTimeChange(self, time):
        self.refSlider.setRange(0,time)

    def quit(self):
        sys.exit()

if __name__ == '__main__':
    #print QtCore.QCoreApplication.libraryPaths()
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Music Spectrum Compare")
    app.setQuitOnLastWindowClosed(True)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
