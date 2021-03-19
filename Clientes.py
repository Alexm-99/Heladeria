import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem, QFileDialog, QMainWindow
from FormulariosPy.Clientes_ui import Ui_Form
from Data.db_favan_py import RegistroTablas, Clientes, Consultas
from Reportes.ReporteCliente import generarReporte
import FormulariosPy.Sucursal_ui as sucursal


#-------------------------------------


class RClientes(QDialog):
    id = ''
    cedula = ''
    nombre = ''
    apellido = ''
    correo = ''
    telefono = ''
    def __init__(self):
        super().__init__()
      
        
        self.ui = Ui_Form()

        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.registrar)
        self.ui.pushButton_5.clicked.connect(self.actualizar)
        self.ui.pushButton_6.clicked.connect(self.btn_idconsulta)
        self.ui.pushButton_3.clicked.connect(self.btn_editar)
        self.ui.pushButton_4.clicked.connect(self.btn_eliminar)
        self.ui.pushButton_2.clicked.connect(self.btn_reporte)
        self.ui.checkBox.stateChanged.connect(self.idSelectCliente)

        self.idSecuencia()
        self.idSelectCliente()
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        #label = QLabel(self)
        #pixmap = QPixmap('Formularios/buscar.ico')
        
        #self.ui.label_9.setPixmap(pixmap)
        #self.ui.label_9.resize(10,10)
        #self.ui.label_9.resize(pixmap.width(),pixmap.height())

        
    def idSecuencia(self):
        
        consulta = cliente1.idSelect()
        valor = len(consulta)
        idValor= 'C{}'.format(valor+1)
        self.ui.label_10.setText(idValor)
        return idValor
            

        #sfor numero in ram
    def registrar(self):

        self.id = self.idSecuencia()
        self.cedula = self.ui.lineEdit.text()
        self.nombre = self.ui.lineEdit_2.text()
        self.apellido = self.ui.lineEdit_3.text()
        self.correo = self.ui.lineEdit_4.text()
        self.telefono = self.ui.lineEdit_5.text()

        campo = [(self.id,self.cedula,self.nombre,self.apellido,self.correo,self.telefono)]
        enti = cliente1.registro(campo)

        mensaje = QMessageBox()
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(1)
        mensaje.setText('{}'.format(enti))
        mensaje.exec_()
        self.txt_blanco()
        self.idSecuencia()
      


       


    def actualizar(self):
         
        
        datos=cliente1.actualiza()
        numcols = len(datos[0])   # ( to get number of columns, count number of values in first row( first row is data[0]))
        numrows = len(datos)   # (to get number of rows, count number of values(which are arrays) in data(2D array))

        self.ui.tableWidget.setColumnCount(numcols)
        self.ui.tableWidget.setRowCount(numrows)
        for row in range(numrows):
            for column in range(numcols):
            # Insertar datos
                self.ui.tableWidget.setItem(row, column, QTableWidgetItem((datos[row][column])))
        
    def idSelectCliente(self):
        chec = self.ui.checkBox.isChecked()
        if chec :
            self.ui.lineEdit.setEnabled(False)
            self.ui.lineEdit_2.setEnabled(False)
            self.ui.lineEdit_3.setEnabled(False)
            self.ui.lineEdit_4.setEnabled(False)
            self.ui.lineEdit_5.setEnabled(False)
            self.ui.lineEdit_6.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            #self.ui.pushButton_3.setEnabled(True)
            #self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton.setEnabled(False)
            self.txt_blanco()
            self.ui.lineEdit_6.setFocus()
        else:
            self.ui.lineEdit.setEnabled(True)
            self.ui.lineEdit_2.setEnabled(True)
            self.ui.lineEdit_3.setEnabled(True)
            self.ui.lineEdit_4.setEnabled(True)
            self.ui.lineEdit_5.setEnabled(True)
            self.ui.lineEdit_6.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)
            #self.ui.pushButton_3.setEnabled(False)
            #self.ui.pushButton_4.setEnabled(False)
            self.ui.pushButton.setEnabled(True)
            

    def btn_idconsulta(self):
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.checkBox.setChecked(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.checkBox.setEnabled(False)
        id = self.ui.lineEdit_6.text()
        datos = consulta.consultaIdCliente(id)
        for i in datos:
            self.ui.lineEdit.setText(i[1])
            self.ui.lineEdit_2.setText(i[2])
            self.ui.lineEdit_3.setText(i[3])
            self.ui.lineEdit_4.setText(i[4])
            self.ui.lineEdit_5.setText(i[5])
            
        

    def devuelveDatosWidgets(self):
        self.id = self.ui.lineEdit_6.text()
        self.cedula = self.ui.lineEdit.text()
        self.nombre = self.ui.lineEdit_2.text()
        self.apellido = self.ui.lineEdit_3.text()
        self.correo = self.ui.lineEdit_4.text()
        self.telefono = self.ui.lineEdit_5.text()

        campo = (self.cedula,self.nombre,self.apellido,self.correo,self.telefono,self.id)
        return campo

    def btn_editar(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        self.ui.lineEdit.setFocus()
        self.ui.checkBox.setEnabled(True)
        datos = self.devuelveDatosWidgets()
        cliente1.updateCliente(datos)
        mensaje= 'Registro Actualizado'
        self.mostrarMensaje(mensaje)
        self.txt_blanco()
        self.idSecuencia()


        

    def btn_eliminar(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        self.ui.lineEdit.setFocus()
        self.ui.checkBox.setEnabled(True)
        self.id = self.ui.lineEdit_6.text()
        cliente1.deleteCliente(self.id)
        mensaje= 'Registro Actualizado'
        self.mostrarMensaje(mensaje)
        self.txt_blanco()
        self.idSecuencia()

    def btn_reporte(self):
        
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar Reporte Cliente","Listado de Clientes.pdf","pdf Files (*.pdf)", options=options)
        if fileName != '':
            reporte=generarReporte(fileName)
            self.mostrarMensaje(reporte)
        
        

    def mostrarMensaje(self, xmensaje):
        mensaje = QMessageBox()
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(1)
        mensaje.setText('{}'.format(xmensaje))
        mensaje.exec_()
        
    def txt_blanco(self):
        self.ui.lineEdit_6.setText('')
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_4.setText('')
        self.ui.lineEdit_5.setText('')

    





cliente1= Clientes()
consulta = Consultas()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ventana = RClientes()
    ventana.show()
    sys.exit(app.exec_())







