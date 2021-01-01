# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resumeMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys, os
from os.path import expanduser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QFileDialog, QApplication)
backend = __import__('resumeBackend')
home = expanduser("~")
os.chdir(home)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 193)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(422, 193))
        MainWindow.setMaximumSize(QtCore.QSize(422, 193))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Resume = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Resume.sizePolicy().hasHeightForWidth())
        self.Resume.setSizePolicy(sizePolicy)
        self.Resume.setTextFormat(QtCore.Qt.RichText)
        self.Resume.setScaledContents(False)
        self.Resume.setAlignment(QtCore.Qt.AlignCenter)
        self.Resume.setObjectName("Resume")
        self.verticalLayout.addWidget(self.Resume)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Add.sizePolicy().hasHeightForWidth())
        self.Add.setSizePolicy(sizePolicy)
        self.Add.setMinimumSize(QtCore.QSize(130, 52))
        self.Add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add.setObjectName("Add")
        self.Add.clicked.connect(self.ShowAddDialog) #link add button to addResume
        self.horizontalLayout_2.addWidget(self.Add)
        self.Replace = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Replace.sizePolicy().hasHeightForWidth())
        self.Replace.setSizePolicy(sizePolicy)
        self.Replace.setMinimumSize(QtCore.QSize(130, 52))
        self.Replace.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Replace.setObjectName("Replace")
        self.horizontalLayout_2.addWidget(self.Replace)
        self.Remove = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Remove.sizePolicy().hasHeightForWidth())
        self.Remove.setSizePolicy(sizePolicy)
        self.Remove.setMinimumSize(QtCore.QSize(130, 52))
        self.Remove.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Remove.setObjectName("Remove")
        self.Remove.clicked.connect(self.ShowDelDialog) #link remove button to delResume
        self.horizontalLayout_2.addWidget(self.Remove)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Description = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Description.sizePolicy().hasHeightForWidth())
        self.Description.setSizePolicy(sizePolicy)
        self.Description.setAlignment(QtCore.Qt.AlignCenter)
        self.Description.setObjectName("Description")
        self.verticalLayout.addWidget(self.Description)
        self.PasteJobDescription = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PasteJobDescription.sizePolicy().hasHeightForWidth())
        self.PasteJobDescription.setSizePolicy(sizePolicy)
        self.PasteJobDescription.setMinimumSize(QtCore.QSize(398, 58))
        self.PasteJobDescription.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PasteJobDescription.setObjectName("PasteJobDescription")
        self.verticalLayout.addWidget(self.PasteJobDescription)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resume Selector"))
        self.Resume.setText(_translate("MainWindow", "Resume"))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.Replace.setText(_translate("MainWindow", "Replace"))
        self.Remove.setText(_translate("MainWindow", "Remove"))
        self.Description.setText(_translate("MainWindow", "Description"))
        self.PasteJobDescription.setText(_translate("MainWindow", "Paste Job Description"))
    
    def ShowAddDialog(self):
        os.chdir(home)
        d = QWidget()
        fileName, ok = QFileDialog.getOpenFileName(d, 'Select a Resume', '','PDF Files (*.pdf)')
        if ok:
            backend.addResume(fileName)

    def ShowDelDialog(self):
        os.chdir(home)
        os.chdir('/../..')
        print(os.getcwd())
        print(__file__)
        os.chdir(__file__)
        print(os.getcwd())
        d = QWidget()




def window():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



window()
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow
    MainWindow.show()
    sys.exit(app.exec_())
'''