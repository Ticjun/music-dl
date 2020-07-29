from PySide2.QtCore import QObject, Signal

class Terminal(QObject):
    event = Signal(str)

    def write(self, text):
        text = text.replace("\r", "").replace("\n", "")
        if text == "":
            return
        if "ERROR" in text:
            text = text.replace("ERROR", "")
            text = f"<font color='Red'>{text}</font>"
        if "youtube-dl -U" in text:
            text = f"Update to latest version"
        elif "[ffmpeg]" in text:
            text = text.replace("[ffmpeg]", "")
            text = f"<font color='Blue'>{text}</font>"
        elif "[download]" in text:
            text = text.replace("[download]", "")
            text = f"<font color='Green'>{text}</font>"
        elif "[youtube]" in text:
            text = text.replace("[youtube]", "")
        self.event.emit(text)
