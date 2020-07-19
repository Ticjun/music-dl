from PySide2.QtCore import QObject, Signal

class Terminal(QObject):
    event = Signal(str)

    def write(self, text):
        text = text.replace("\r", "").replace("\n", "")
        if text == "":
            return
        if "[ffmpeg]" in text:
            text = f"<font color='Blue'>{text}</font>"
        if "[download]" in text:
            text = f"<font color='Green'>{text}</font>"
        self.event.emit(text)
