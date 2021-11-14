from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from login import Ui_Form
from mainprincipal import mywindow
import sys

class form(QtWidgets.QWidget):
    def __init__(self):
        super(form,self).__init__()
        self.ui = Ui_Form()
        #self.setWindowTitle("Inicio de sesion")
        self.ui.setupUi(self)
        self.ui.pushButton_cerrarlogin.clicked.connect(self.close)
        self.ui.pushButton_ingresar.clicked.connect(self.iniciarSesion)
        
    def iniciarSesion(self):
        user = self.ui.lineEdit_user.text()
        password = self.ui.lineEdit_password.text()
        if user == "PP3001" and password == "12345678":
            self.mostrarPrincipal()
            return True
        else:
            self.errorAcceso()
            return False
        
    def errorAcceso(self):
        self.ui.label_error.setText("La contraseña es incorrecta.\nVuelve a intentarlo")

    def mostrarPrincipal(self):
        self.miventanaprincipal = mywindow()
        self.miventanaprincipal.show()

        

app = QtWidgets.QApplication([])
application = form()
application.show()
sys.exit(app.exec())