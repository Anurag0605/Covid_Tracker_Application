# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cgraphs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cgraphs(object):
    def setupUi(self, cgraphs):
        cgraphs.setObjectName("cgraphs")
        cgraphs.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(cgraphs)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 451, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("cg1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 451, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("cg2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 330, 451, 311))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("cg3.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 330, 451, 311))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("g4.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        cgraphs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cgraphs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        cgraphs.setMenuBar(self.menubar)

        self.retranslateUi(cgraphs)
        QtCore.QMetaObject.connectSlotsByName(cgraphs)

    def retranslateUi(self, cgraphs):
        _translate = QtCore.QCoreApplication.translate
        cgraphs.setWindowTitle(_translate("cgraphs", "Graphs ||CountryWise"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cgraphs = QtWidgets.QMainWindow()
    ui = Ui_cgraphs()
    ui.setupUi(cgraphs)
    cgraphs.show()
    sys.exit(app.exec_())
