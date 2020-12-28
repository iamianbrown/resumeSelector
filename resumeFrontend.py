import importlib
import sys
from PyQt5 import QtWidgets
pm = __import__('resumeMainWindow')


def window():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pm.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
window()