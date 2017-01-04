import sys
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
import numpy as np


class MessageProcessorWidget(QWidget):
    messageProcessorSignal = QtCore.pyqtSignal(int)

    def __init__(self, inputModel):
        super(MessageProcessorWidget, self).__init__()
        self.model = inputModel
        self.createUi()

    def createUi(self):
        self.ui = uic.loadUi("QtDesigner/MessageProcessorWidget.ui", self)
        self.ui.messageProcessorCheckBox.stateChanged.connect(self.handleMessageProcessorCheckBox)
        self.ui.show()

    def handleMessageProcessorCheckBox(self, state):
        self.messageProcessorSignal.emit(state)
