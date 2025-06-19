from PySide6.QtWidgets import QPushButton
from variables import MEDIUM_TEXT


class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_TEXT)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')
