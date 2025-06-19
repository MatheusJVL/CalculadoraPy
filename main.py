from mainwindow import MainWindow
from PySide6.QtWidgets import QApplication
from styles import setupTheme
app = QApplication()
window = MainWindow()
setupTheme(app)
window.show()
app.exec()