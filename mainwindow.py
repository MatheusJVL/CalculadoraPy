from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QMessageBox
from variables import ICON_PATH
from PySide6.QtGui import QIcon
from display import Display, Info
import sys
from styles import ButtonsGrid


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent)
        self._window = self
        self.cw = QWidget()
        self.box_lay = QVBoxLayout()

        self.cw.setLayout(self.box_lay)
        self.setCentralWidget(self.cw)


        self.setWindowTitle('Calculadora')

        icon = QIcon(str(ICON_PATH))
        self.setWindowIcon(icon)

        self.info = Info()  
        self.addWidgetQvlayout(self.info)

        self.display = Display()
        self.addWidgetQvlayout(self.display)

        # botoes
        self.buttonGrid = ButtonsGrid(self.display, self.info, self._window)
        self.box_lay.addLayout(self.buttonGrid)

        self.adjustFixedSize()
    
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetQvlayout(self, widget):
        self.box_lay.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    display = Display()
    window.addWidgetQvlayout(display)
    window.show()
    app.exec()