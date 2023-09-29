import base64
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                             QMainWindow, QMessageBox, QPushButton, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Defina o título e o ícone da janela
        self.setWindowTitle('Conversor Base64')
        self.setWindowIcon(QIcon('icon.png'))

        # Defina o tamanho e a posição da janela
        self.setGeometry(100, 100, 600, 450)

        # Crie um widget central e um layout de grade
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout(central_widget)
        grid_layout.setSpacing(10)

        # Crie o rótulo de entrada e a caixa de texto
        self.input_label = QLabel('Texto de entrada:', self)
        grid_layout.addWidget(self.input_label, 0, 0)
        self.input_text = QLineEdit(self)
        grid_layout.addWidget(self.input_text, 1, 0, 1, 2)

        # Crie o rótulo de saída e a caixa de texto
        self.output_label = QLabel('Texto de saída:', self)
        grid_layout.addWidget(self.output_label, 2, 0)
        self.output_text = QLineEdit(self)
        grid_layout.addWidget(self.output_text, 3, 0, 1, 2)
        self.output_text.setReadOnly(True)

        # Crie o botão de codificação
        self.encode_button = QPushButton('Codificar', self)
        grid_layout.addWidget(self.encode_button, 4, 0)
        self.encode_button.clicked.connect(self.encode_text)

        # Crie o botão de decodificação
        self.decode_button = QPushButton('Decodificar', self)
        grid_layout.addWidget(self.decode_button, 4, 1)
        self.decode_button.clicked.connect(self.decode_text)

        # Crie o botão de limpar
        self.clear_button = QPushButton('Limpar', self)
        grid_layout.addWidget(self.clear_button, 5, 0)
        self.clear_button.clicked.connect(self.clear_text)

        # Crie o botão de sair
        self.exit_button = QPushButton('Sair', self)
        grid_layout.addWidget(self.exit_button, 5, 1)
        self.exit_button.clicked.connect(self.confirm_exit)

    def encode_text(self):
        # Obtenha o texto de entrada da caixa de texto
        input_text = self.input_text.text()

        # Converta o texto de entrada para base64
        output_text = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')

        # Atualize a caixa de texto de saída com o texto convertido
        self.output_text.setText(output_text)

    def decode_text(self):
        # Obtenha o texto de entrada da caixa de texto
        input_text = self.input_text.text()

        # Converta o texto de entrada de base64 para texto
        output_text = base64.b64decode(input_text.encode('utf-8')).decode('utf-8')

        # Atualize a caixa de texto de saída com o texto convertido
        self.output_text.setText(output_text)

    def clear_text(self):
        # Exiba uma caixa de diálogo de confirmação
        reply = QMessageBox.question(self, 'Limpar', 'Tem certeza que deseja limpar os campos?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # Se o usuário confirmar, limpe as caixas de texto de entrada e saída
        if reply == QMessageBox.Yes:
            self.input_text.setText('')
            self.output_text.setText('')

    def confirm_exit(self):
        # Exiba uma caixa de diálogo de confirmação
        reply = QMessageBox.question(self, 'Sair', 'Tem certeza que deseja sair do programa?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # Se o usuário confirmar, feche a janela principal
        if reply == QMessageBox.Yes:
            self.close()

if __name__ == '__main__':
    # Crie uma nova instância da classe QApplication
    app = QApplication(sys.argv)

    # Crie uma nova instância da classe MainWindow
    main_window = MainWindow()

    # Mostre a janela principal
    main_window.show()

    # Execute o loop de eventos
    sys.exit(app.exec_())