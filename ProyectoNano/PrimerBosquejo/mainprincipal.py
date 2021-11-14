from PyQt5 import QtWidgets, QtCore
from principal import Ui_MainWindow
import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_cuenta.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cuenta))
        self.ui.pushButton_producto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_producto))
        self.ui.pushButton_empleado.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_empleado))
        self.ui.pushButton_venta.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_venta))
        self.ui.pushButton_reporte.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_reporteventa))
        self.ui.pushButton_menu.clicked.connect(self.movermenu)
    def movermenu(self):
        if True:
            width = self.ui.frame_lateral.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QtCore.QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
