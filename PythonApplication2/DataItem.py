from PyQt5 import QtCore

class DataItem(QtCore.QObject):
    dataChanged = QtCore.pyqtSignal()

    def __init__(self):
        super(DataItem, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if (self._data != value):
            self._data = value
            self.dataChanged.emit()

