import sys
from PyQt5.QtWidgets import QApplication, QDialog
from views.Login import Plogin


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ventana = Plogin()
    ventana.show()
    sys.exit(app.exec_())