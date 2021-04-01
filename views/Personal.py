import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem, QFileDialog, QMainWindow
from FormulariosPy.Personal_ui import Ui_Form
from Data.db_favan_py import RegistroTablas, Bd_Personal, Bd_Sucursal, bdLogin
from Reportes.ReportePersonal import generarReporte

# Menu
datos = RegistroTablas()
datos.RTablas()

#-------------------------------------


class Rpersonal(QDialog):
    id = ''
    cedula = ''
    nombre = ''
    apellido = ''
    passwd = ''
    id_suc = ''
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
        self.idSucursal()
        self.idSelectCliente()
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        #label = QLabel(self)
        #pixmap = QPixmap('Formularios/buscar.ico')
        
        #self.ui.label_9.setPixmap(pixmap)
        #self.ui.label_9.resize(10,10)
        #self.ui.label_9.resize(pixmap.width(),pixmap.height())

        
    def idSecuencia(self):
        
        consulta = persona.idSelect()
        valor = len(consulta)
        idValor= 'P0{}'.format(valor+1)
        self.ui.label_10.setText(idValor)
        return idValor


    def idSecuenciaAdmin(self):
        
        consulta = login.idSelectLogin()
        valor = len(consulta)
        idValor= 'admin0{}'.format(valor+1)
        self.ui.label_10.setText(idValor)
        return idValor
            
    def  idSucursal(self):
        l2 = []
        valores = sucursal.idSelect()
        
        for i in valores:
            for datos in i:
                #x = str(datos)
                l2.append(datos)   
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(l2)
        #sfor numero in ram

    def registrar(self):

        self.id = self.idSecuencia()
        self.cedula = self.ui.lineEdit_9.text()
        self.nombre = self.ui.lineEdit_3.text()
        self.apellido = self.ui.lineEdit_5.text()
        self.passwd = self.ui.lineEdit_8.text()
        self.id_suc = self.ui.comboBox.currentText()

        campo = [(self.id,self.cedula,self.nombre,self.apellido,self.passwd,self.id_suc)]
        enti = persona.registro(campo)

        checq = self.ui.checkBox_2.isChecked()
        if checq:
            x= self.idSecuenciaAdmin()
            campo2 = [(x, self.passwd,self.id)]
            login.registro(campo2)
            mensajex= '{} SU USUARIO ADMIN ES: {}'.format(enti, x)
            self.mostrarMensaje(mensajex)

        mensaje = QMessageBox()
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(1)
        mensaje.setText('{}'.format(enti))
        mensaje.exec_()
        self.txt_blanco()
        self.idSecuencia()
        


       


    def actualizar(self):
         
        
        datos=persona.actualiza()
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
            self.ui.lineEdit_9.setEnabled(False)
            self.ui.lineEdit_3.setEnabled(False)
            self.ui.lineEdit_5.setEnabled(False)
            self.ui.lineEdit_8.setEnabled(False)
            self.ui.checkBox_2.setEnabled(False)

            self.ui.lineEdit_6.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            #self.ui.pushButton_3.setEnabled(True)
            #self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton.setEnabled(False)
            self.txt_blanco()
            self.ui.lineEdit_6.setFocus()
        else:
            self.ui.checkBox_2.setEnabled(True)
            

            self.ui.lineEdit_9.setEnabled(True)
            self.ui.lineEdit_3.setEnabled(True)
           
            self.ui.lineEdit_8.setEnabled(True)
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
        datos = persona.consultaIdPersonal(id)
        #self.idSucursal()
          
        for i in datos:
            self.ui.lineEdit_9.setText(i[1])
            self.ui.lineEdit_3.setText(i[2])
            self.ui.lineEdit_5.setText(i[3])
            self.ui.lineEdit_8.setText(i[4])
            self.ui.comboBox.setCurrentText(i[5])
            
            
        

    def devuelveDatosWidgets(self):
        self.id = self.ui.lineEdit_6.text()
        self.cedula = self.ui.lineEdit_9.text()
        self.nombre = self.ui.lineEdit_3.text()
        self.apellido = self.ui.lineEdit_5.text()
        self.passwd = self.ui.lineEdit_8.text()
        self.id_suc = self.ui.comboBox.currentText()

        campo = (self.cedula,self.nombre,self.apellido,self.passwd,self.id_suc,self.id)
        return campo

    def btn_editar(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        self.ui.lineEdit_9.setFocus()
        self.ui.checkBox.setEnabled(True)
        datos = self.devuelveDatosWidgets()
        persona.updatePersonal(datos)
        mensaje= 'Registro Actualizado'

        
        self.mostrarMensaje(mensaje)
        self.txt_blanco()
        self.idSecuencia()
        self.idSucursal()


        

    def btn_eliminar(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        self.ui.lineEdit_9.setFocus()
        self.ui.checkBox.setEnabled(True)
        self.id = self.ui.lineEdit_6.text()
        persona.deletePersonal(self.id)
        mensaje= 'Registro Actualizado'
        self.mostrarMensaje(mensaje)
        self.txt_blanco()
        self.idSecuencia()
        self.idSucursal()

    def btn_reporte(self):
        
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar Reporte Personal","Listado de Personal.pdf","pdf Files (*.pdf)", options=options)
        if fileName != '':
            reporte=generarReporte(fileName)
            self.mostrarMensaje(reporte)
            pass
        

    def mostrarMensaje(self, xmensaje, icono = 1):
        mensaje = QMessageBox()
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(icono)
        mensaje.setText('{}'.format(xmensaje))
        mensaje.exec_()
        
    def txt_blanco(self):
        self.ui.lineEdit_6.setText('')
        self.ui.lineEdit_9.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_5.setText('')
        self.ui.lineEdit_8.setText('')
   

    





persona= Bd_Personal()
sucursal = Bd_Sucursal()
login = bdLogin()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ventana = Rpersonal()
    ventana.show()
    sys.exit(app.exec_())