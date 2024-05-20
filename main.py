from PyQt5.QtGui import QFont
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QDialog, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt, QEvent
from art import text2art
from random import choice

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.text_input = QLineEdit(self)
        self.UI()

    def UI(self):
        self.setWindowTitle('art app')
        self.setGeometry(300, 300, 300, 200)
        self.btn1 = QPushButton('example', self)
        self.btn1.setGeometry(50, 50, 100, 30)
        self.btn1.clicked.connect(self.btn_1_clc)
        self.btn2 = QPushButton('text', self)
        self.btn2.setGeometry(50, 100, 100, 30)
        self.btn2.clicked.connect(self.btn_2_clc)
        self.btn3 = QPushButton('Btn_3', self)
        self.btn3.setGeometry(50, 150, 100, 30)
        self.btn3.clicked.connect(self.btn_3_clc)
        self.show()

    def keyPressEvent(self, event: QEvent):
        if event.key() == Qt.Key_Q:
            self.destroy()

    def btn_1_clc(self):
        dialog = QDialog()
        dialog.setWindowTitle('Art')
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setFont(QFont("Courier", 12))
        chars = ['good','bad','cool','nice','fine']
        random_string = choice(chars)
        art_text = text2art(random_string)
        text_edit.setText(art_text)
        layout.addWidget(text_edit)
        dialog.setLayout(layout)
        dialog.resize(800, 600)
        dialog.exec_()

    def btn_2_clc(self):
        dialog = QDialog()
        dialog.setWindowTitle('Art')
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setFont(QFont("Courier", 12))
        user_text = self.text_input.text() 
        if not user_text:
            chars = ['good','bad','cool','nice','fine']
            random_string = choice(chars)
        else:
            random_string = user_text
        art_text = text2art(random_string)
        text_edit.setText(art_text)
        layout.addWidget(text_edit)
        dialog.setLayout(layout)
        dialog.resize(800, 600)
        self.text_input.setGeometry(10, 10, 200, 30)
        dialog.exec_()

    def btn_3_clc(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
