import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from Data.db_favan_py import RegistroTablas, Consultas
from FormulariosPy.Consultas_ui import Ui_Form

class RConsultas(QDialog):
 
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()

        self.ui.setupUi(self)
        self.ui.comboBox.currentIndexChanged.connect(self.tablas)
        self.ui.pushButton.clicked.connect(self.nombreCampos)
      
        #self.ui.comboBox.addItems(['CLIENTES','PERSONAL'])
    def tablas(self):
        caja = self.ui.comboBox.currentText()
        if caja == 'CLIENTES':
            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.addItems(['ID','CEDULA'])
            self.ui.checkBox.setVisible(True)
        else:
            self.ui.checkBox.setVisible(False)
            
       


    def nombreCampos(self):
        caja = self.ui.comboBox.currentText()
        chec = self.ui.checkBox.isChecked()
        self.txtLine = self.ui.lineEdit.text()
        #Consulta cliente sin factura
        if caja == 'CLIENTES' and chec == False:
            print('Iniciando {}... '.format(caja))
            self.encabezado = ['ID', 'CÉDULA','NOMBRE', 'APELLIDO','CORREO','TELÉFONO']
            self.clienteId(self.encabezado,self.txtLine)
        #Consulta Cliente con factura
        if caja == 'CLIENTES' and chec == True:
            print('Iniciando {}... '.format(caja))
            self.encabezado = ['FACTURA', 'ID CLIENTE','CEDULA', 'CLIENTE','IVA','DESCUENTO','TOTAL','FECHA']
            self.clienteIdFactura(self.encabezado,self.txtLine)               

        if caja == 'PERSONAL':
            print('Iniciando {}... '.format(caja))
            self.encabezado = ['ID', 'CÉDULA','NOMBRE', 'APELLIDO','SUCURSAL']
            self.personalId(self.encabezado,self.txtLine)
            
            
        elif caja == 'FACTURA':
            print('Iniciando {}... '.format(caja))
        elif caja == 'HELADO':
            print('Iniciando {}... '.format(caja))
        elif caja == 'SUCURSAL':
            print('Iniciando {}... '.format(caja))
    
    def validarStringLista(self, datos):
        l2=[]
        ind=-1
        for datosx in datos:
            dt = list(datosx)
            for valorL in datosx:
                ind+=1
                if isinstance(valorL, float) or isinstance(valorL, int):
                    vdt= str(valorL)
                    dt[ind]=str(vdt)
            l2.append(dt)
            ind=-1
        return l2  
   
    def llenarTabla(self, datos,encabezado):
        
        try:
            numcols = len(datos[0])   # ( to get number of columns, count number of values in first row( first row is data[0]))
            numrows = len(datos)   # (to get number of rows, count number of values(which are arrays) in data(2D array))
            
            self.ui.tableWidget.setColumnCount(numcols)
            self.ui.tableWidget.setRowCount(numrows)
            for row in range(numrows):
                for column in range(numcols):
                # Insertar datos
                    self.ui.tableWidget.setItem(row, column, QTableWidgetItem((datos[row][column])))
            self.ui.tableWidget.setHorizontalHeaderLabels(encabezado)
        except:
            x='Dato Incorrecto'
            mensaje = QMessageBox()
            mensaje.setWindowTitle('Mensaje')
            mensaje.setIcon(1)
            mensaje.setText('{}'.format(x))
            mensaje.exec_()

    def personalId(self, encabezado, identificador):
        opcion = self.ui.comboBox_2.currentText()
        if opcion == 'ID':         
            datos=consulta.consultaIdPersonal(self, identificador)
           
            self.llenarTabla(datos,encabezado)
            
        elif opcion == 'CEDULA':
            datos=consulta.consultaCedPersonal(self,identificador)
            self.llenarTabla(datos,encabezado)


        


    def clienteId(self, encabezado, identificador):
        opcion = self.ui.comboBox_2.currentText()
        if opcion == 'ID':  
            
            datos=consulta.consultaIdCliente(self,identificador)
            self.llenarTabla(datos,encabezado)
            
        elif opcion == 'CEDULA':
            datos=consulta.consultaCedCliente(self,identificador)
            self.llenarTabla(datos,encabezado)


        elif opcion == 'NOMBRE':
            pass

    def clienteIdFactura(self, encabezado, identificador):
        opcion = self.ui.comboBox_2.currentText()
        if opcion == 'ID':  
            
            datos=consulta.consultaIdClienteFactura(self,identificador)
            
            datos=self.validarStringLista(datos)


            

            self.llenarTabla(datos,encabezado)
            
        elif opcion == 'CEDULA':
            pass
    


consulta= Consultas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ventana = RConsultas()
    ventana.show()
    sys.exit(app.exec_())



