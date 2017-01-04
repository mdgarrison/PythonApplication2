import sys
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
import numpy as np
import vlc


class VLCWidget(QWidget):
    vlcSignal = QtCore.pyqtSignal(int)

    def __init__(self, inputModel):
        super(VLCWidget, self).__init__()
        self.model = inputModel
        self.createUi()
        self.createVlcComponents()
        self.isPaused = True;

    def createUi(self):
        self.ui = uic.loadUi("QtDesigner/VLCWidget.ui", self)
        self.ui.vlcCheckBox.stateChanged.connect(self.handleVlcCheckBox)

        self.ui.volumeSlider.valueChanged.connect(self.setVolume)
        self.ui.positionSlider.sliderMoved.connect(self.setPosition)
        self.ui.playButton.clicked.connect(self.setPlay)
        self.ui.stopButton.clicked.connect(self.setStop)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.updateUI)

        self.ui.show()

    def createVlcComponents(self):
        self.instance = vlc.Instance('--no-video-on-top', '--fullscreen')
        self.mediaplayer = self.instance.media_player_new()
        self.mediaFile = self.instance.media_new("C:\\Users\\mdgar\\Desktop\\video.mp4")

        self.mediaplayer.set_media(self.mediaFile)
        self.mediaplayer.set_hwnd(self.ui.videoFrame.winId())
        self.mediaplayer.audio_set_volume(0)

    def setVolume(self, Volume):
        self.mediaplayer.audio_set_volume(Volume)

    def setPosition(self, position):
        self.mediaplayer.set_position(position / 1000.0)

    def setStop(self):
        self.mediaplayer.stop()

    def setPlay(self):
        self.mediaplayer.play()
        self.timer.start()

    def PlayPause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.playbutton.setText("Play")
            self.isPaused = True
        else:
            if self.mediaplayer.play() == -1:
                self.OpenFile()
                return
            self.mediaplayer.play()
            self.playbutton.setText("Pause")
            self.timer.start()
            self.isPaused = False

    def updateUI(self):
        self.ui.positionSlider.setValue(self.mediaplayer.get_position() * 1000)

        if not self.mediaplayer.is_playing():
            # no need to call this function if nothing is played
            self.timer.stop()
            if not self.isPaused:
                # after the video finished, the play button stills shows
                # "Pause", not the desired behavior of a media player
                # this will fix it
                self.Stop()

    def handleVlcCheckBox(self, state):
        self.vlcSignal.emit(state)





