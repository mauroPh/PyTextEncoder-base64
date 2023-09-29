import base64
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Conversor Base64')
        self.setWindowIcon(QIcon('icon.png'))


        self.setGeometry(100, 100, 400, 300)


        self.input_label = QLabel('Texto de entrada:', self)
        self.input_label.move(20, 20)
        self.input_text = QLineEdit(self)
        self.input_text.move(20, 40)
        self.input_text.resize(360, 30)

        self.output_label = QLabel('Texto de saída:', self)
        self.output_label.move(20, 80)
        self.output_text = QLineEdit(self)
        self.output_text.move(20, 100)
        self.output_text.resize(360, 30)
        self.output_text.setReadOnly(True)

        self.convert_button = QPushButton('Converter', self)
        self.convert_button.move(20, 150)
        self.convert_button.clicked.connect(self.convert_text)

        self.clear_button = QPushButton('Limpar', self)
        self.clear_button.move(120, 150)
        self.clear_button.clicked.connect(self.clear_text)

        self.exit_button = QPushButton('Sair', self)
        self.exit_button.move(220, 150)
        self.exit_button.clicked.connect(self.close)

    def convert_text(self):
        input_text = self.input_text.text()

        output_text = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')

        self.output_text.setText(output_text)

    def clear_text(self):
        self.input_text.setText('')
        self.output_text.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_window.show()

    sys.exit(app.exec_())