import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication, QDialog, QMessageBox,QTableWidgetItem
from views.Clientes import *
from FormulariosPy.Formulario_Factura_ui import Ui_Form
from Data.db_favan_py import Consultas, Facturas, Detalle_Factura,Pedido

class Factura(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.factura1=Facturas()
        self.Detalle_Fac=Detalle_Factura()
        #pedido1=Pedido()
        self.ultimo_pedido()
        self.calculartotal()
        self.ui.Facturar.setVisible(False)
        self.ui.Fecha.setText(self.factura1.FECHA)
        self.factura1.ID_FACTURA=self.factura1.contar_id()
        self.ui.n_pedido.setText(self.factura1.ID_FACTURA)
        #self.ui.Facturar.clicked.connect(self.facturar)
        self.ui.buscar.clicked.connect(self.buscarCliente)
        self.ui.radioButton_2.clicked.connect(self.consumidorF)
        self.ui.radioButton.clicked.connect(self.afiliado)
        self.ui.aggCantidad.clicked.connect(self.calculartotal)
        self.ui.Facturar.clicked.connect(self.facturar)
        self.ui.cancelar.clicked.connect(self.cancelar)
        self.ui.insertar.clicked.connect(self.insertar)

    def insertar(self):
        ventana = RClientes() #Instancia de clase
        ventana.exec_()#Iniciar 

    def cancelar(self):
        self.hide()
    def facturar(self):
        self.factura1.registro()
        self.Detalle_Fac.ID_FACTURA=self.factura1.ID_FACTURA
        self.Detalle_Fac.ID_DETALLE_FAC=self.Detalle_Fac.contar_id()
        self.Detalle_Fac.registro()
        self.llenarTabla()
        mensaje = QMessageBox()
        mensaje.setWindowTitle('Factura realizada')
        mensaje.setIcon(1)
        mensaje.setText('{}'.format("Factura Realizada!"))
        mensaje.exec_()
        self.hide()
    
        
        #Detalle_Factura
    def llenarTabla(self):
            self.ui.tableWidget.setRowCount(1)
            self.ui.tableWidget.setColumnCount(5)
            encabezado=['Cod. Helado','Detalle','Cantidad','P.U.P',' TOTAL']
            self.ui.tableWidget.setHorizontalHeaderLabels(encabezado)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(self.Detalle_Fac.ID_HELADO)))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(self.ui.envase.text()+", "+self.ui.tamanio.text()+", "+str(self.ui.listview.count())+" aderezos"))
            self.ui.tableWidget.setItem(0,2, QTableWidgetItem(self.ui.cantidad.text()))
            self.ui.tableWidget.setItem(0,3, QTableWidgetItem(str(self.Detalle_Fac.SUBTOTAL)))
            self.ui.tableWidget.setItem(0,4, QTableWidgetItem(str(self.Detalle_Fac.TOTAL)))

    def calculartotal (self):
        cantidad=float(self.ui.cantidad.text())
        subtotale=cantidad * self.Detalle_Fac.SUBTOTAL
        self.ui.subtotal.setText(str(subtotale))
        self.ui.descuento.setText(str(self.Detalle_Fac.DESCUENTO))
        self.ui.descuento_2.setText(str((self.Detalle_Fac.DESCUENTO*subtotale)/100))
        self.Detalle_Fac.IVA=(subtotale* 12)/100
        self.ui.iva.setText(str(self.Detalle_Fac.IVA))
        self.Detalle_Fac.TOTAL=subtotale-float(self.ui.descuento_2.text()) + self.Detalle_Fac.IVA
        self.ui.total.setText(str(self.Detalle_Fac.TOTAL))


    def ultimo_pedido(self):
        id_helado=Consultas.consultar_ultimo_H(self)
        self.ui.codigo.setText(str(id_helado[0]))
        datos=Consultas.cosultaNomAde(self,id_helado[2],id_helado[1])
        self.ui.envase.setText(datos[1])
        self.ui.tamanio.setText(datos[0])  
        listADR=str(id_helado[4])

        itms=listADR.split(",")
        for it in itms:
            self.ui.listview.addItem(it)
        self.Detalle_Fac.SUBTOTAL=id_helado[5]
        self.ui.subtotal.setText(str(self.Detalle_Fac.SUBTOTAL))
        self.Detalle_Fac.ID_FACTURA=self.factura1.ID_FACTURA
        self.Detalle_Fac.ID_HELADO= self.ui.codigo.text()

    def afiliado(self):
        if self.ui.rucCliente.text()=="":
            self.ui.Facturar.setVisible(False)
        self.ui.rucCliente.setEnabled(True)
        self.ui.buscar.setEnabled(True)
        self.ui.comboBox_tamanio.setEnabled(True)
        self.Detalle_Fac.DESCUENTO=10
        self.ui.descuento.setText(str(self.Detalle_Fac.DESCUENTO))
        Factura.calculartotal(self)  
    def consumidorF(self):
        self.ui.Facturar.setVisible(True)
        self.factura1.ID_CLIENTE="Consumidor Final"
        self.ui.rucCliente.setEnabled(False)
        self.ui.comboBox_tamanio.setEnabled(False)
        self.ui.buscar.setEnabled(False)
        self.Detalle_Fac.DESCUENTO=0
        self.ui.descuento.setText(str(self.Detalle_Fac.DESCUENTO))
        self.ui.groupBox.setVisible(True)
        self.ui.label.setVisible(False)
        self.ui.label_2.setVisible(False)        
        Factura.calculartotal(self)

    def buscarCliente(self):
        if self.ui.rucCliente.text()=="":
            self.ui.groupBox.setVisible(True)
            self.ui.label_2.setVisible(True)
            self.ui.Facturar.setVisible(False)
        else:
            if self.ui.comboBox_tamanio.currentText()=="ID":
                cliente=Consultas.consulta_cliente_id(self,self.ui.rucCliente.text())
                self.factura1.ID_CLIENTE= self.ui.rucCliente.text()
                self.ui.id.setVisible(False)
                self.ui.cedula.setVisible(True)
            else:
                cliente=Consultas.consulta_cliente_ced(self,self.ui.rucCliente.text())
                self.ui.cedula.setVisible(False)
                self.ui.id.setVisible(True)

            if  cliente == None:
                self.ui.Facturar.setVisible(False)
                self.ui.groupBox.setVisible(True)
                self.ui.label.setVisible(True)
                self.ui.label_2.setVisible(False)
                #self.factura1.ID_CLIENTE= self.ui.rucCliente.text()
                
            else:
                self.ui.Facturar.setVisible(True)
                if self.ui.comboBox_tamanio.currentText()=="ID":
                    self.factura1.ID_CLIENTE= self.ui.rucCliente.text()
                elif self.ui.comboBox_tamanio.currentText()=="CEDULA":
                    factura1.ID_CLIENTE=cliente[0]
                self.ui.groupBox.setVisible(False)
                self.ui.label.setVisible(False)
                self.ui.label_2.setVisible(False)
                self.ui.cedCliente.setText(str(cliente[0]))
                self.ui.NomApeCliente.setText(str(cliente[1]))
                self.ui.mailCliente.setText(str(cliente[2]))
                self.ui.telfCliente.setText(str(cliente[3]))
                
            
if __name__=='__main__':
    app=QApplication(sys.argv)
    factura1=Facturas()
    pedido1=Pedido()
    GUI= Factura()
    GUI.show()
    sys.exit(app.exec_())


        