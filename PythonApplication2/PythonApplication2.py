import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
import numpy as np
import Model
import ConfigurationWidget
import VLCWidget
import QssEditorWidget
import MessageProcessorWidget

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = uic.loadUi("QTDesigner/MainWindow.ui", self)
        _dataModel = Model.Model()
        _dataModel.thrustLevel.data = "red"
        _dataModel.coreTemperature.data = "green"
        _dataModel.entropy.data = "blue"
        _dataModel.azimuth.data = "alpha"

        tab1 = ConfigurationWidget.ConfigurationWidget(_dataModel)
        self.ui.tabWidget.addTab(tab1, "M1553 Config")

        tab2 = VLCWidget.VLCWidget(_dataModel)
        self.ui.tabWidget.addTab(tab2, "VLC Video Player")

        tab3 = QssEditorWidget.QssEditorWidget(_dataModel)
        self.ui.tabWidget.addTab(tab3, "QSS Editor")

        tab4 = MessageProcessorWidget.MessageProcessorWidget(_dataModel)
        self.ui.tabWidget.addTab(tab4, "Message Processor")

        tab1.configurationSignal.connect(self.handleConfigurationSignal)
        tab2.vlcSignal.connect(self.handleVlcSignal)
        tab3.qssEditorSignal.connect(self.handleQssEditorSignal)
        #tab4.messageProcessorSignal.connect(self.handleMessageProcessorSignal)
        tab4.messageProcessorSignal.connect(self.ui.messageProcessorCheckBox.setCheckState)

    def handleConfigurationSignal(self, state):
        print("configurationSignal" + str(state))
        self.ui.configurationCheckBox.setCheckState(state)

    def handleMessageProcessorSignal(self, state):
        print("messageProcessorSignal" + str(state))
        self.ui.messageProcessorCheckBox.setCheckState(state)

    def handleQssEditorSignal(self, state):
        print("qssEditorSignal" + str(state))
        self.ui.qssEditorCheckBox.setCheckState(state)

    def handleVlcSignal(self, state):
        print("vlcSignal" + str(state))
        self.ui.vlcCheckBox.setCheckState(state)

if __name__ == "__main__":
    # More generic plumbing -- this is how our app starts up
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
