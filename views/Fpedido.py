import sys
from datetime import date
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication, QDialog, QMessageBox,QTableWidgetItem
from views.FFactura import *
from views.FFactura import Factura
from FormulariosPy.Formulario_Pedido_ui import Ui_Form
from Data.db_favan_py import Consultas, Pedido


class FPedido(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Pedido1 = Pedido()
    
        FPedido.tablaAdrezo(self)
        self.Pedido1.contar_id()
        self.ui.eliminar_todo.setVisible(False)
        self.ui.cancelar.setVisible(False)
        self.ui.confirmar.setVisible(False)
        self.ui.Siguiente.setVisible(False)
        self.ui.mostrarTodo.clicked.connect(self.tablaAdrezo)
        self.ui.buscar.clicked.connect(self.ConsultaAderezo)
        self.ui.confirmar.clicked.connect(self.calcular_precio)
        self.ui.Siguiente.clicked.connect(self.Siguiente)
        self.ui.asignar.clicked.connect(self.asignar)
        self.ui.eliminar_todo.clicked.connect(self.limpiar)
        self.ui.cancelar.clicked.connect(self.cancelar)
    def cancelar(self):
        self.limpiar()
        self.ui.eliminar_todo.setVisible(False)
        self.calcular_precio()
        self.ui.confirmar.setVisible(True)
        self.ui.cancelar.setVisible(False)
        self.ui.codAderezo.setEnabled(True)  
        self.ui.buscar.setEnabled(True)         
        self.ui.eliminar_todo.setEnabled(True)  
        self.ui.asignar.setEnabled(True)  
        self.ui.tableWidget_Aderezo2.setEnabled(True)  
        self.ui.tableWidget_Aderezo3.setEnabled(True) 
        self.ui.comboBox_tamanio.setEnabled(True)  
        self.ui.comboBox_envace.setEnabled(True)  
    def limpiar(self):
        self.ui.tableWidget_Aderezo3.clear()
        self.ui.confirmar.setVisible(False)
        self.ui.Siguiente.setVisible(False)
        self.ui.eliminar_todo.setVisible(False)

    def asignar(self):
        self.ui.eliminar_todo.setVisible(True)
        self.ui.confirmar.setVisible(True)
        itms = self.ui.tableWidget_Aderezo2.selectedIndexes()
        for it in itms:
            self.ui.tableWidget_Aderezo3.addItem(it.data())

    def Precio_aderezo(self):
        precio=0
        self.Pedido1.LIST_ADEREZO=[]
        if self.ui.tableWidget_Aderezo3.count() > 0:
            for i in range(self.ui.tableWidget_Aderezo3.count()):
                self.Pedido1.LIST_ADEREZO.append(self.ui.tableWidget_Aderezo3.item(i).text())
            for i in self.Pedido1.LIST_ADEREZO:
                Aderezos=Consultas.ConsultaPrecioAderezo(self,i)
                precio= precio + Aderezos[0] 
            self.Pedido1.LIST_ADEREZO=self.Pedido1.listaArreglada()
            return precio
        elif self.ui.tableWidget_Aderezo3.count() ==0:
            self.Pedido1.LIST_ADEREZO="NADA"
            return precio

    def calcular_precio(self):
        self.Pedido1.PRECIO=0
        envase=self.tamanio_envase()
        Aderezos= self.Precio_aderezo()
        self.Pedido1.PRECIO=envase+Aderezos
        self.ui.precio.setText(str(self.Pedido1.PRECIO))
        self.ui.confirmar.setVisible(False)
        self.ui.Siguiente.setVisible(True)
        self.ui.cancelar.setVisible(True)
        self.ui.codAderezo.setEnabled(False)  
        self.ui.buscar.setEnabled(False)    
        self.ui.eliminar_todo.setEnabled(False)  
        self.ui.asignar.setEnabled(False)  
        self.ui.tableWidget_Aderezo2.setEnabled(False)  
        self.ui.tableWidget_Aderezo3.setEnabled(False) 
        self.ui.comboBox_tamanio.setEnabled(False)  
        self.ui.comboBox_envace.setEnabled(False)  

    def datosEnviar(self):
        pass

    def Siguiente(self):
        self.calcular_precio()
        self.Pedido1.registro()
        self.btn_abrirFactura()
        self.ui.confirmar.setVisible(False)
        self.ui.cancelar.setVisible(False)
        self.ui.codAderezo.setEnabled(True)  
        self.ui.buscar.setEnabled(True)   
        self.ui.eliminar_todo.setEnabled(True)  
        self.ui.asignar.setEnabled(True)  
        self.ui.tableWidget_Aderezo2.setEnabled(True)  
        self.ui.tableWidget_Aderezo3.setEnabled(True) 
        self.ui.comboBox_tamanio.setEnabled(True)  
        self.ui.comboBox_envace.setEnabled(True)  
        self.ui.cancelar.setVisible(False)
        self.ui.Siguiente.setVisible(False)


    
    def ConsultaAderezo(self):
        self.ui.tableWidget_Aderezo1.clear()
        self.ui.tableWidget_Aderezo2.clear()
        Aderezos=Consultas.ConsultaAderezo(self,self.ui.codAderezo.text())
        for item in Aderezos:
            L=[item[0]]
            self.ui.tableWidget_Aderezo1.addItems(L)
            L=[item[1]]
            self.ui.tableWidget_Aderezo2.addItems(L)

    def tamanio_envase(self):
        self.Pedido1.TAMANIO = self.ui.comboBox_tamanio.currentText()
        self.Pedido1.ENVASE = self.ui.comboBox_envace.currentText()
        dato= Consultas.consultaTamanio_envase(self,self.Pedido1.TAMANIO,self.Pedido1.ENVASE)
        self.Pedido1.TAMANIO =dato[0]
        self.Pedido1.ENVASE = dato[3]
        precio= dato[2] + dato[5]

        return precio
        
    def btn_abrirFactura(self):       
        self.ventana = Factura() #Instancia de clase
        self.ventana.exec_()
        self.hide()#Iniciar
        
    def tablaAdrezo(self):
        self.ui.tableWidget_Aderezo1.clear()
        self.ui.tableWidget_Aderezo2.clear()
        Aderezos=Consultas.ConsultaAderezo(self,"1234567")
        for item in Aderezos:
            L=[item[0]]
            self.ui.tableWidget_Aderezo1.addItems(L)
            L=[item[1]]
            self.ui.tableWidget_Aderezo2.addItems(L)  


if __name__=='__main__':
    app=QApplication(sys.argv)
    
    GUI= FPedido()
    GUI.show()
    sys.exit(app.exec_())
