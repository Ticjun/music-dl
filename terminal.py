from PySide2.QtCore import QObject, Signal

class Terminal(QObject):
    event = Signal(str)

    def write(self, text):
        self.event.emit(str(text))
