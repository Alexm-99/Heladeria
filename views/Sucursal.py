import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem,QFileDialog
from FormulariosPy.Sucursal_ui import Ui_Form
from Data.db_favan_py import RegistroTablas, Consultas, Bd_Sucursal



class Csucursal(QDialog):

    id = ''
    ciudad = ''
    direccion = ''
 
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
        self.ui.checkBox.stateChanged.connect(self.idSelectSucursal)

        self.idSecuencia()
        self.idSelectSucursal()
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_2.setVisible(False)
        #label = QLabel(self)
        #pixmap = QPixmap('Formularios/buscar.ico')
        
        #self.ui.label_9.setPixmap(pixmap)
        #self.ui.label_9.resize(10,10)
        #self.ui.label_9.resize(pixmap.width(),pixmap.height())

        
    def idSecuencia(self):
        
        consulta = sucursal.idSelect()
        valor = len(consulta)
        idValor= 'SU0{}'.format(valor+1)
        self.ui.label_10.setText(idValor)
        return idValor
            

        #sfor numero in ram
    def registrar(self):

        self.id = self.idSecuencia()
        self.ciudad = self.ui.lineEdit_7.text()
        self.direccion = self.ui.lineEdit_10.text()
       

        campo = [(self.id,self.ciudad,self.direccion)]
        enti = sucursal.registro(campo)

        mensaje = QMessageBox()
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(1)
        mensaje.setText('{}'.format(enti))
        mensaje.exec_()
        self.txt_blanco()
        self.idSecuencia()
        


       


    def actualizar(self):
         
        
        datos=sucursal.actualiza()
        numcols = len(datos[0])   # ( to get number of columns, count number of values in first row( first row is data[0]))
        numrows = len(datos)   # (to get number of rows, count number of values(which are arrays) in data(2D array))

        self.ui.tableWidget.setColumnCount(numcols)
        self.ui.tableWidget.setRowCount(numrows)
        for row in range(numrows):
            for column in range(numcols):
            # Insertar datos
                self.ui.tableWidget.setItem(row, column, QTableWidgetItem((datos[row][column])))
        
    def idSelectSucursal(self):
        chec = self.ui.checkBox.isChecked()
        if chec :
           
            self.ui.lineEdit_10.setEnabled(False)
            self.ui.lineEdit_7.setEnabled(False)
            self.ui.lineEdit_6.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            #self.ui.pushButton_3.setEnabled(True)
            #self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton.setEnabled(False)
            self.txt_blanco()
            self.ui.lineEdit_6.setFocus()
        else:
        
            self.ui.lineEdit_10.setEnabled(True)
            self.ui.lineEdit_7.setEnabled(True)
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
        datos = sucursal.consultaIdSucursal(id)
        for i in datos:
            self.ui.lineEdit_7.setText(i[1])
            self.ui.lineEdit_10.setText(i[2])
            
            
        

    def devuelveDatosWidgets(self):
        self.id = self.ui.lineEdit_6.text()
        self.ciudad = self.ui.lineEdit_7.text()
        self.direccion = self.ui.lineEdit_10.text()
        

        campo = (self.ciudad,self.direccion,self.id)
        return campo

    def btn_editar(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        self.ui.lineEdit_7.setFocus()
        self.ui.checkBox.setEnabled(True)
        datos = self.devuelveDatosWidgets()
        sucursal.updateSucursal(datos)
        mensaje= 'Registro Actualizado'
        self.mostrarMensaje(mensaje)
        self.txt_blanco()
        self.idSecuencia()
        

    
        

    def btn_eliminar(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        self.ui.lineEdit_7.setFocus()
        self.ui.checkBox.setEnabled(True)
        self.id = self.ui.lineEdit_6.text()
        sucursal.deleteSucursal(self.id)
        mensaje= 'Registro Actualizado'
        self.mostrarMensaje(mensaje)
        self.txt_blanco()
        self.idSecuencia()

    def btn_reporte(self):
        
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar Reporte Cliente","Listado de Clientes.pdf","pdf Files (*.pdf)", options=options)
        if fileName != '':
            pass
            #reporte=generarReporte(fileName)
            #self.mostrarMensaje(reporte)
        
        
    def mostrarMensaje(self, xmensaje):
        mensaje = QMessageBox()
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(1)
        mensaje.setText('{}'.format(xmensaje))
        mensaje.exec_()

    def txt_blanco(self):
        self.ui.lineEdit_6.setText('')
        self.ui.lineEdit_7.setText('')
        self.ui.lineEdit_10.setText('')
       
        
#consulta = Consultas()
sucursal = Bd_Sucursal()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ventana = Csucursal()
    ventana.show()
    sys.exit(app.exec_())