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

        self.metaInformationResolver = Phonon.MediaObject(self)
        self.metaInformationResolver.stateChanged.connect(self.metaStateChanged)
        Phonon.createPath(self.mediaObject, self.audioOutput)

        self.setupUi(self)

        self.userSources = []
        
        self.actionImport_User_File.triggered.connect(self.addUserFiles)
        #init sliders
        self.refSlider.setValue(0)
        self.userSlider.setValue(0)
        self.refSlider.setEnabled(False)
        self.userSlider.setEnabled(False)
        self.userSlider.sliderReleased.connect(self.userSlideChange)

        #init buttons
        self.userplaybutton.clicked.connect(self.userPlayOrPause)
        self.userplaybutton.setEnabled(False)
        self.userpausebutton.clicked.connect(self.userPlayOrPause)
        self.userplaybutton.setEnabled(False)
        self.recordbutton.setEnabled(True)
        #init display time
        self.user_current_time = 0
        #init LCD display start from 00:00
        self.userPlayTime.display("00:00")
        self.refPlayTime.display("00:00")
        #setup music table
        headers = ("Title", "Artist","Date")
        self.usertablewidget.setColumnCount(2)
        self.usertablewidget.setRowCount(0)
        self.usertablewidget.setHorizontalHeaderLabels(headers)
        self.usertablewidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.usertablewidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        
        #init figure
        self.userscene = QtGui.QGraphicsScene()
        #self.userpixmap = QtGui.QPixmap("userback.png")
        #self.userpixmap = self.userpixmap.scaled(390,280)
        #self.userscene.addPixmap(self.userpixmap)
        #self.userGraph.setScene(self.userscene)

        self.refscene = QtGui.QGraphicsScene()
        self.refpixmap = QtGui.QPixmap("refback.jpg")
        self.refpixmap = self.refpixmap.scaled(390,280)
        self.refscene.addPixmap(self.refpixmap)
        self.refGraph.setScene(self.refscene)
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
        plt.ylabel('Frequency(Hz)')
        plt.xlabel('Time(s)')
        plt.axis([0, 10, 128, 1024])
        plt.title('Input spectrogram')
        plt.colorbar(format='%+2.0f dB')
        plt.savefig('userplot.png')
        self.userpixmap = QtGui.QPixmap("userplot.png")
        self.userpixmap = self.userpixmap.scaled(420,290)
        self.userscene.addPixmap(self.userpixmap)
        self.userGraph.setScene(self.userscene)

    def metaStateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            QtGui.QMessageBox.warning(self, "Error opening files",
                    self.metaInformationResolver.errorString())

            while self.sources and self.sources.pop() != self.metaInformationResolver.currentSource():
                pass

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


    def userPlayOrPause(self):
        if Phonon.PlayingState == self.mediaObject.state():
            self.mediaObject.pause()
        elif Phonon.PausedState == self.mediaObject.state():
            self.mediaObject.play()

    def userSlideChange(self):
        value = self.userSlider.value()
        self.mediaObject.seek(value)

    def userTimeChange(self, time):  
        self.userSlider.setValue(time)
        self.user_current_time = time
        displayTime = QtCore.QTime(0,(time / 60000) % 60, (time / 1000) % 60)
        self.userPlayTime.display(displayTime.toString('mm:ss'))

    def userTotalTimeChange(self, time):
        self.userSlider.setRange(0,time)

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
