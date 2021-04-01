import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem, QFileDialog,QMainWindow

#from FormulariosPy.Clientes_ui import Ui_Form as clienteFc
from views.Sucursal import *
from views.Clientes import *
from views.Consultas import *
from views.Personal import *
from views.Login import *
from views.ElegirReporte import *
from views.Fpedido import *
from FormulariosPy.MenuPrincipal_ui import Ui_Form
from Data.db_favan_py import RegistroTablas, Clientes, Consultas


# Menu
datos = RegistroTablas()
datos.RTablas()

#-------------------------------------


class Rmenu(QDialog):

    def __init__(self):
        super().__init__()
      
        
        self.ui = Ui_Form()

        self.ui.setupUi(self)
        self.ui.pushButton_11.clicked.connect(self.btn_abrirCliente)
        self.ui.pushButton_10.clicked.connect(self.btn_abrirSucursal)
        self.ui.pushButton_8.clicked.connect(self.btn_abrirConsultas)
        self.ui.pushButton_4.clicked.connect(self.btn_abrirReportes)
        self.ui.pushButton_7.clicked.connect(self.btn_Salir)
        self.ui.pushButton_9.clicked.connect(self.btn_abritPersonal)
        self.ui.pushButton_3.clicked.connect(self.btn_abrirPedido)
        self.usuarioInicio()


    def usuarioInicio(self):
        #usuario = Plogin()
        #nombre = usuario.enviandoNombre()
        #self.ui.label_19.setText(nombre)
        pass

    def btn_abrirPedido(self):
        ventana = FPedido() #Instancia de clase
        ventana.exec_()#Iniciar
    def btn_abritPersonal(self):
        ventana = Rpersonal() #Instancia de clase
        ventana.exec_()#Iniciar

    def btn_Salir(self):
        self.close()
    def btn_abrirReportes(self):
        ventana = Ereporte() #Instancia de clase
        ventana.exec_()#Iniciar

    def btn_abrirConsultas(self):
            
        ventana = RConsultas() #Instancia de clase
        ventana.exec_()#Iniciar

    def btn_abrirCliente(self):
            
        ventana = RClientes() #Instancia de clase
        ventana.exec_()#Iniciar 
        


    def btn_abrirSucursal(sef):
        ventana = Csucursal() #Instancia de clase
        ventana.exec_()#Iniciar 

        
        #self.hide() 


        

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Rmenu()
    ventana.show()
    sys.exit(app.exec_())




