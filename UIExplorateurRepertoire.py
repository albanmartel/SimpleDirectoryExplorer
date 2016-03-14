# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alban/Documents/programmationPython/video/ExplorateurRepertoire.ui'
#
# Created: Mon Mar 14 10:39:49 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Forms(object):
    def setupUi(self, Forms):
        Forms.setObjectName("Forms")
        Forms.resize(344, 344)
        Forms.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Forms)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Forms)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Forms)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Forms)
        QtCore.QMetaObject.connectSlotsByName(Forms)

    def retranslateUi(self, Forms):
        _translate = QtCore.QCoreApplication.translate
        Forms.setWindowTitle(_translate("Forms", "Explorateur de Document"))
        self.pushButton_3.setText(_translate("Forms", "Ok"))
        self.pushButton_4.setText(_translate("Forms", "Prev."))
        self.pushButton_5.setText(_translate("Forms", "Parent"))
        self.pushButton_6.setText(_translate("Forms", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Forms = QtWidgets.QWidget()
    ui = Ui_Forms()
    ui.setupUi(Forms)
    Forms.show()
    sys.exit(app.exec_())

