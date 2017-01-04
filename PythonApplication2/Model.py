from PyQt5 import QtCore
import DataItem

class Model(QtCore.QObject):
    def __init__(self):
        super(Model, self).__init__()

        self.thrustLevel = DataItem.DataItem()
        self.coreTemperature = DataItem.DataItem()
        self.entropy = DataItem.DataItem()
        self.azimuth = DataItem.DataItem()
