import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
import Clases.Funciones as Funciones

class InitialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        user=os.getlogin()
        self.setWindowTitle('Ventana Inicial')
        self.setGeometry(0, 0, 1850, 950)

        # Cargar el GIF como un QPixmap
        pixmap = QPixmap(os.getcwd()+'\\Recursos\\BGVentanaPrincipalMinas.jpg')  # Reemplaza 'ruta_del_video.gif' con la ruta de tu JPG

        # Crear un QLabel para mostrar el QPixmap
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, self.width(), self.height())

        main_layout = QVBoxLayout()

        btn1 = QPushButton('Escaenar código del estudiante', self)
        btn1.setStyleSheet('''
            background-color: #E3902A;
            color: white;
            border-radius: 10px;
            padding: 20px;
            border: 3px solid white;
            margin 3px;
        ''')
        btn1.setFont(QFont("Roboto", 22, QFont.Bold))
        btn1.clicked.connect(self.openQRCodeReaderLab)

        btn1.setGeometry(600, 700, 650, 100)

    def openQRCodeReaderLab(self):
        self.hide()
        self.qrCodeReader = QRCodeReader.Lab()
        self.qrCodeReader.closed.connect(self.showInitialWindow)
        self.qrCodeReader.show()  
    
    def showInitialWindow(self):
        self.show()

class QRCodeReader(QWidget):
    class Lab(QWidget):
        closed = pyqtSignal()
        def __init__(self):
            super().__init__()
            user=os.getlogin()
            self.setGeometry(250, 250, 1280, 720)
            self.setWindowTitle('Lector de Código QR - Carné institucional')

            # Cargar el GIF como un QMovie
            pixmap = QPixmap(os.getcwd()+'\\Recursos\\BGAmpere.jpg')  # Reemplaza 'ruta_del_video.gif' con la ruta de tu video GIF

            # Crear un QLabel para mostrar el QPixmap
            label = QLabel(self)
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)
            label.setScaledContents(True)
            label.setGeometry(0, 0, self.width(), self.height())

            self.btn = QPushButton('Leer código QR - Carné institucional', self)
            self.btn.setGeometry(320, (self.height() - 120) // 2, 700, 120)
            self.btn.setFont(QFont("Roboto", 21, QFont.Bold))
            self.btn.setStyleSheet('''
                background-color: #1E90FF;
                color: white;
                border-radius: 10px;
                padding: 20px;
                border: 3px solid white;
                margin 3px;
            ''')
            self.btn.setMinimumHeight(60)  # Ajusta la altura del botón

            self.btn.clicked.connect(self.openSecondWindow)

        def openSecondWindow(self):
            self.secondWindow = SecondWindow()
            self.secondWindow.show()
            self.secondWindow.btnYes.clicked.connect(self.executeYesCode)
            self.secondWindow.btnNo.clicked.connect(self.executeNoCode)

        def executeYesCode(self):
            Funciones.base_dato()
            resultado=Funciones.buscarbd()
            QMessageBox.information(self, 'Resultado', resultado)
            QApplication.quit()

        def executeNoCode(self):
            resultado=Funciones.buscarbd()
            QMessageBox.information(self, 'Resultado', resultado)
            QApplication.quit()
        
        def closeEvent(self, event):
            self.closed.emit()
            event.accept()
            self.btn.clicked.connect(self.openSecondWindow)

        def openSecondWindow(self):
            self.secondWindow = SecondWindow()
            self.secondWindow.show()
            self.secondWindow.btnYes.clicked.connect(self.executeYesCode)
            self.secondWindow.btnNo.clicked.connect(self.executeNoCode)

        def executeYesCode(self):
            Funciones.base_dato()
            resultado=Funciones.buscarbd()
            QMessageBox.information(self, 'Resultado', resultado)
            QApplication.quit()

        def executeNoCode(self):
            resultado=Funciones.buscarbd()
            QMessageBox.information(self, 'Resultado', resultado)
            QApplication.quit()
        
        def closeEvent(self, event):
            self.closed.emit()
            event.accept()
     
class SecondWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Base de datos')
        self.setGeometry(300, 300, 400, 200)

        main_layout = QVBoxLayout()

        label1 = QLabel('¿Actualizar base de datos?')
        label1.setStyleSheet('font-size: 15px;')
        label1.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(label1)

        button_layout = QHBoxLayout()

        self.btnYes = QPushButton(self)
        self.btnYes.setText('Sí, por favor')
        self.btnYes.setStyleSheet('background-color: #55D6BE; color: white; font-weight: bold;')

        self.btnNo = QPushButton(self)
        self.btnNo.setText('No')
        self.btnNo.setStyleSheet('background-color: #991C1C; color: white; font-weight: bold;')

        button_layout.addWidget(self.btnYes)
        button_layout.addWidget(self.btnNo)

        main_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        label3 = QLabel('NOTA: Recuerde preguntarle al estudiante cuándo expidió el certificado.')
        label3.setAlignment(Qt.AlignCenter)
        label3.setStyleSheet('font-weight: bold; font-style: bold;')
        main_layout.addWidget(label3)