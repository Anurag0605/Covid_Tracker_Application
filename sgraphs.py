# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sgraphs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sgraphs(object):
    def setupUi(self, sgraphs):
        sgraphs.setObjectName("sgraphs")
        sgraphs.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(sgraphs)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 451, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("g1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 451, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("g2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 330, 451, 311))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("g3.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 330, 451, 311))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("g4.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        sgraphs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sgraphs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        sgraphs.setMenuBar(self.menubar)

        self.retranslateUi(sgraphs)
        QtCore.QMetaObject.connectSlotsByName(sgraphs)

    def retranslateUi(self, sgraphs):
        _translate = QtCore.QCoreApplication.translate
        sgraphs.setWindowTitle(_translate("sgraphs", "Graphs ||StateWise (India)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sgraphs = QtWidgets.QMainWindow()
    ui = Ui_sgraphs()
    ui.setupUi(sgraphs)
    sgraphs.show()
    sys.exit(app.exec_())
