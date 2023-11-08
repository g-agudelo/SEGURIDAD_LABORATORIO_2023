import Clases.Interfaz as Interfaz
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    initialWindow = Interfaz.InitialWindow()
    initialWindow.show()
    sys.exit(app.exec_())