import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem, QFileDialog, QMainWindow
from views.Menu import *
from FormulariosPy.Login_ui import Ui_Dialog
from Data.db_favan_py import RegistroTablas, Bd_Personal, Consultas, bdLogin


# Menu
datos = RegistroTablas()
datos.RTablas()

#-------------------------------------


class Plogin(QDialog):
    usuario = ''
    passwd = ''
    
    def __init__(self):
        super().__init__()
      
        
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.salir)

        self.ui.pushButton.clicked.connect(self.iniciar)



    def iniciar(self):
        id = self.ui.lineEdit.text()
        datos = login.verificarInicio(id)
        for i in datos:
            self.usuario= i[0]
            self.passwd = i[1]
        txt_usu = self.ui.lineEdit.text()
        txt_pass = self.ui.lineEdit_2.text()
        if txt_usu=='' or txt_pass =='' :
            mensaje = 'Datos en blanco'
            self.mostrarMensaje(mensaje, 3)
        elif self.usuario == txt_usu and self.passwd == txt_pass:
            mensaje ='Bienvenido'
            self.mostrarMensaje(mensaje)
            
            ventana = Rmenu() #Instancia de clase
            
            
            self.close()
            ventana.exec_()#Iniciar 
            #sys.exit(app.exec_())
            
        else:
            mensaje = 'Error en los datos'
            self.mostrarMensaje(mensaje, 3)


    def salir(self):
        self.close()

    def mostrarMensaje(self, xmensaje, icono = 1):
        mensaje = QMessageBox()
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(icono)
        mensaje.setText('{}'.format(xmensaje))
        mensaje.exec_()

login = bdLogin()
