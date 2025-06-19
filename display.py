from PySide6.QtWidgets import QLineEdit, QPushButton
from PySide6.QtCore import Qt
from variables import BIG_TEXT, DEFAULT_MARGIN, MINIMUN_WIDTH, SMALL_TEXT, MEDIUM_TEXT
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from variables import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_TEXT}px')
        self.setMinimumHeight(BIG_TEXT * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setTextMargins(*[DEFAULT_MARGIN for _ in range(4)])
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
            KEYS.Key_P,
        ]

        if isEnter:
            
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            
            self.clearPressed.emit()
            return event.ignore()

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()
        
        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        if isNumOrDot(text):
            print(
                'inputPressed pressionado, sinal emitido', type(self).__name__
            )
            self.inputPressed.emit(text)
            return event.ignore()

        
class Info(QLabel):
    def __init__(self, text=None):
        super().__init__(text)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_TEXT}')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

    