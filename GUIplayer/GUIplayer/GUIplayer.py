#!/usr/bin/env python
import sip
sip.setapi('QString', 2)

import sys
import os
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
        self.graphHeight = 395
        super(QtGui.QMainWindow, self).__init__(parent)
        self.font = QtGui.QFont()
        self.font.setPointSize(14)
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
        
        self.userFreqList = None
        self.refFreqList = None
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
        self.userSlider.valueChanged.connect(self.userSlideValueChange)

        self.refSlider.setValue(0)
        self.refSlider.setEnabled(False)
        self.refSlider.valueChanged.connect(self.refSlideValueChange)
        #init buttons
        self.userplaybutton.clicked.connect(self.userPlayOrPause)
        self.userplaybutton.setEnabled(False)
        self.userplaybutton.setEnabled(False)
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
        self.usertablewidget.setFont(self.font)
        self.usertablewidget.setColumnCount(2)
        self.usertablewidget.setRowCount(0)
        self.usertablewidget.setHorizontalHeaderLabels(headers)
        self.usertablewidget.setColumnWidth(0,300)
        self.usertablewidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)
        self.usertablewidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.usertablewidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        
        self.reftablewidget.setFont(self.font)
        self.reftablewidget.setColumnCount(2)
        self.reftablewidget.setRowCount(0)
        self.reftablewidget.setHorizontalHeaderLabels(headers)
        self.reftablewidget.setColumnWidth(0,300)
        self.reftablewidget.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)
        self.reftablewidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.reftablewidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        self.userfreqtextbox.setFont(self.font)
        self.reffreqtextbox.setFont(self.font)

        #init figure
        self.userscene = QtGui.QGraphicsScene()
        self.refscene = QtGui.QGraphicsScene()

    def guide(self):
        QtGui.QMessageBox.information(self, "About the spectrum frequency",
                "This is the guide for notes and frequency correspondence")
    def my_range(self, start, end, step):
        while start != end:
            yield start
            start += step
    def plotSaveLibrosaFig(self, file, saveFileName):
        #plot spectrum
        y, sr = librosa.core.load(file, offset = 0.0, duration = 10.0)
        D = librosa.stft(y,n_fft=2048*4,hop_length=2048/4)
        #naive overtune filter: Filter0
        Filter0 = np.zeros(D.shape)
        for i in range(0,D.shape[1]):
            for j in range(40,80):
                Filter0[j,i]=1
        D = Filter0 * D
        Dmax=np.max(D,axis=0)
        Findex = np.zeros(D.shape[1])
        for i in range(0,D.shape[1]):
            for j in range(0,D.shape[0]):
                if D[j,i]==Dmax[i]:
                    Findex[i]=j
        #naive background noise filter: Filter
        Filter = np.zeros(D.shape)
        for i in range(0,D.shape[1]):
            for j in range(int (Findex[i]-2),int (Findex[i]+2)):
                Filter[j,i]=1
        D = Filter * D
        #detect the start/end point and align the two start points at zero
        startpoint = 0
        endpoint = D.shape[1]
        max = np.max(np.abs(D))
        for i in range(0,D.shape[1]):
            if np.max(D[:,i]) > 0.1*max:
                startpoint = i
                break
        for i in self.my_range(D.shape[1]-1,0,-1):
            if np.max(D[:,i]) > 0.1*max:
                endpoint = i
                break
        timegain = 10.0/431.0
        gain = 440.0/163.0
        #Findex is a list showing the frequecy with highest magnitude corresponging to a certain time flag
        librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max),y_axis='log', x_axis='time')
        Findex = Findex * gain
        xs = [130, 146, 165,175, 196, 220, 247, 261, 293, 329, 349, 391, 440, 493, 523, 587, 659, 698, 783, 880, 987]
        ylabels = ['C3','D3','E3','F3','G3','A3','B3','C4','D4','E4','F4','G4','A4','B4','C5','D5','E5','F5','G5','A5','B5']
        plt.yticks(xs,ylabels)
        plt.tight_layout()
        #plt.xlim((0,10))
        plt.ylim(120,512)
        plt.xlabel('')
        plt.ylabel('')
        plt.title('')
        plt.savefig(saveFileName)
        return Findex

    def addUserFiles(self):
        file = QtGui.QFileDialog.getOpenFileName(self, "Select User Input File",
                QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation))
        self.mediaObject.setCurrentSource(Phonon.MediaSource(file))
        self.metaInformationResolver.setCurrentSource(Phonon.MediaSource(file))
        self.mediaObject.play()
        self.userplaybutton.setEnabled(True)
        self.userSlider.setEnabled(True)
        # plot spectrum user
        saveFileName = 'userplot.png'
        self.userFreqList = self.plotSaveLibrosaFig(file, saveFileName)            
        # show the file on the scene
        self.userpixmap = QtGui.QPixmap(saveFileName)
        self.userpixmap = self.userpixmap.scaledToHeight(self.graphHeight)
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
        self.refSlider.setRange(0, self.refMetaInformationResolver.totalTime())
        #plot spectrum
        saveFileName = 'refplot.png'
        self.refFreqList = self.plotSaveLibrosaFig(file, saveFileName)
        #save file
        self.refpixmap = QtGui.QPixmap(saveFileName)
        self.refpixmap = self.refpixmap.scaledToHeight(self.graphHeight)
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
            title = os.path.basename(title)
       
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
            title = self.refMetaInformationResolver.currentSource().fileName()
            title = os.path.basename(title)
        titleItem = QtGui.QTableWidgetItem(title)
        titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)

        artist = metaData.get('ARTIST', [''])[0]
        artistItem = QtGui.QTableWidgetItem(artist)
        artistItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)


        currentRow = self.reftablewidget.rowCount()
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


    def refSlideValueChange(self):
        time = self.refSlider.value()
        self.ref_current_time = time
        displayTime = QtCore.QTime(0,(time / 60000) % 60, (time / 1000) % 60)
        self.refPlayTime.display(displayTime.toString('mm:ss'))
        timeGain = 431.0/10000.0
        pos = int(time * timeGain)
        freq = "%0.2f" % self.refFreqList[pos]
        self.reffreqtextbox.setText(str(freq))

    def userSlideValueChange(self):
        time = self.userSlider.value()
        displayTime = QtCore.QTime(0,(time / 60000) % 60, (time / 1000) % 60)
        self.userPlayTime.display(displayTime.toString('mm:ss'))
        timeGain = 431.0/10000.0
        pos = int(time * timeGain)
        freq = "%0.2f" % self.refFreqList[pos]
        self.userfreqtextbox.setText(str(freq))
    
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
