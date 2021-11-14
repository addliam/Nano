from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from principal import Ui_MainWindow
#from login import Ui_Form
import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.setWindowTitle("Administracion de ventas")
        self.ui.pushButton_productos.setLayoutDirection(Qt.RightToLeft)
        #QPushButton.setLayoutDirection(Qt.RightToLeft)
        self.ui.pushButton_cerrar.clicked.connect(self.close)
        self.ui.pushButton_minimizar.clicked.connect(self.showMinimized)
        self.ui.pushButton_micuenta.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_cuenta))
        self.ui.pushButton_productos.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_productos))
        self.ui.pushButton_empleados.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_empleados))
        self.ui.pushButton_venta.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_venta))
        self.ui.pushButton_reporteventas.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_reporteventas))
    """
    def popWindow(self):
        self.form2 = QtWidgets.QWidget() 
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.form2)
        self.form2.show()
    """ 
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
