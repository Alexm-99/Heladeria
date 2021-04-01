import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem, QFileDialog,QMainWindow
from FormulariosPy.Reportes_ui import Ui_Form
from Reportes.ReporteCliente import generarReporte as reportCliente
from Reportes.ReportePersonal import generarReporte as reportPersonal

class Ereporte(QDialog):

    def __init__(self):
        super().__init__()
      
        
        self.ui = Ui_Form()

        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btn_exportarCliente)
        self.ui.pushButton_2.clicked.connect(self.btn_exportarPersonal)
       

    def btn_exportarCliente(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar Reporte Cliente","Listado de Clientes.pdf","pdf Files (*.pdf)", options=options)
        if fileName != '':
            reporte=reportCliente(fileName)
            self.mostrarMensaje(reporte) 
        self.close()
    def btn_exportarPersonal(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar Reporte Personal","Listado de Personal.pdf","pdf Files (*.pdf)", options=options)
        if fileName != '':
            reporte=reportPersonal(fileName)
            self.mostrarMensaje(reporte) 
        self.close()

    def mostrarMensaje(self, xmensaje):
        mensaje = QMessageBox()
        mensaje.setWindowTitle('Mensaje')
        mensaje.setIcon(1)
        mensaje.setText('{}'.format(xmensaje))
        mensaje.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ereporte()
    ventana.show()
    sys.exit(app.exec_())
