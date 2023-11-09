#IMPORTAMOS LA LIBRERIA QUE VAMOS A USAR
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
import Clases.Funciones as Funciones
#CREAMOS LA VENTANA PRINCIPAL 
class InitialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana Inicial')
        self.setGeometry(0, 0, 1850, 950)

        # Cargar el GIF como un QPixmap
        pixmap = QPixmap(os.getcwd()+'\\Recursos\\BGAmpere.jpg')  # Reemplaza 'ruta_del_video.gif' con la ruta de tu JPG

        # Crear un QLabel para mostrar el QPixmap
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, self.width(), self.height())

        main_layout = QVBoxLayout()

        btn1 = QPushButton('Escanear código del estudiante', self)
        btn1.setStyleSheet('''
            background-color: #E3902A;
            color: white;
            border-radius: 10px;
            padding: 20px;
            border: 3px solid white;
            margin 3px;
        ''')
        btn1.setFont(QFont("Roboto", 22, QFont.Bold))
        btn1.clicked.connect(self.openSecondWindow)

        btn1.setGeometry(600, 700, 650, 100)
    #CREACION DEL EVENTO PARA ACCEDER A LA SEGUNDA VENTANA   
    def openSecondWindow(self):
        self.secondWindow = SecondWindow()
        self.secondWindow.show()
        self.secondWindow.btnYes.clicked.connect(self.executeYesCode)
        self.secondWindow.btnNo.clicked.connect(self.executeNoCode)
    
    def showInitialWindow(self):
        self.show()
        
    def executeYesCode(self):
        Funciones.base_dato()
        resultado=Funciones.buscarbd()
        QMessageBox.information(self, 'Resultado', resultado)
        QApplication.quit()
    def executeNoCode(self):
        resultado=Funciones.buscarbd()
        QMessageBox.information(self, 'Resultado', resultado)
        QApplication.quit()
    #CIERRE DE LA SEGUNDA VENTANA
    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
        self.btn.clicked.connect(self.openSecondWindow)
    #CREACION DEL EVENTO PARA CERRAR
    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
             
#CREACION DE LA VENTANA PARA PREGUNTAR SI SE DESEA ACTUALIZAR LA BASE DE DATOS O NO   
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