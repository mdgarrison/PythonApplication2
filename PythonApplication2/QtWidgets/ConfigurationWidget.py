import sys
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyqtgraph as pg
import numpy as np



class ConfigurationWidget(QWidget):
    configurationSignal = QtCore.pyqtSignal(int)

    def __init__(self, inputModel):
        super(ConfigurationWidget, self).__init__()
        self.ui = uic.loadUi("QtDesigner/ConfigurationWidget.ui", self)
        self.ui.configurationCheckBox.stateChanged.connect(self.handleconfigurationCheckBox)
        self.model = inputModel
        inputModel.thrustLevel.dataChanged.connect(self.handleThrustLevelChanged)
        self.ui.show()
        
        print(self.ui.radioButton1.isChecked())
        self.ui.radioButton1.setChecked(True)
        print(self.ui.radioButton1.isChecked())

    def handleconfigurationCheckBox(self, state):
        self.configurationSignal.emit(state)
        self.model.thrustLevel.data = "yellow"
 
    def handleThrustLevelChanged(self):
        print("handleThrustLevelChanged")


