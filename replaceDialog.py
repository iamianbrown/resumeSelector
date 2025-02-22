# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'replaceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_replaceDialog(object):
    def __init__(self, replaceDialog, filename):
        self.setupUi(replaceDialog, filename)
    def setupUi(self, replaceDialog, filename):
        replaceDialog.setObjectName("replaceDialog")
        replaceDialog.resize(330, 177)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(replaceDialog.sizePolicy().hasHeightForWidth())
        replaceDialog.setSizePolicy(sizePolicy)
        replaceDialog.setMinimumSize(QtCore.QSize(330, 113))
        replaceDialog.setMaximumSize(QtCore.QSize(330, 113))
        self.verticalLayout = QtWidgets.QVBoxLayout(replaceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(replaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(306, 32))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(replaceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(replaceDialog, filename)
        self.buttonBox.accepted.connect(replaceDialog.accept)
        self.buttonBox.rejected.connect(replaceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(replaceDialog)

    def retranslateUi(self, replaceDialog, filename):
        _translate = QtCore.QCoreApplication.translate
        replaceDialog.setWindowTitle(_translate("replaceDialog", "Overwrite Resume"))
        self.label.setText(_translate("replaceDialog", "A resume with the name  '" + filename + "' already exists. Would you like to replace it?"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    replaceDialog = QtWidgets.QDialog()
    ui = Ui_replaceDialog(replaceDialog, 'loop')
    
    replaceDialog.show()

    
    sys.exit(app.exec_())
