# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Myth-Busterseidvvj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from home import *
from statistics import *
from precautions import *
from latest import *
from login import *


class Ui_myth(object):
    def homep(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_home()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def latestp(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_latest()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def precs(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_precautions()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def statsp(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_statistics()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def setupUi(self, myth):
        if not myth.objectName():
        myth.setObjectName("myth")
        myth.resize(801, 605)
        myth.setStyleSheet(u"background-color: white;")
        self.centralwidget = QtWidgets.QWidget(myth)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 50, 101, 31))
        self.label_2.setStyleSheet(u"color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"border:2px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.mousePressEvent=self.homep
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 50, 111, 31))
        self.label_3.setStyleSheet(u"color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"border:2px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 50, 101, 31))
        self.label_4.setStyleSheet(u"color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"border:2px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 50, 111, 31))
        self.label_5.setStyleSheet(u"color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"border:2px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 10, 91, 41))
        self.pushButton.setStyleSheet("QPushButton{border-radius:20px;\n"
"font: 12pt \"Times New Roman\";\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"font: 75 10pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(170, 170, 255);\n"
"}{\n"
"    background: blue;\n"
"    border:2px solid black;\n"
"    border-radius:15px;\n"
"    color:#fff;\n"
"    font-size: 15px;\n"
"    letter-spacing: 2px;\n"
"    font-family: \'Lato\';\n"
"    font-weight: 200;}\n"
" \n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 80, 101, 41))
        self.pushButton_2.setStyleSheet("QPushButton{border-radius:20px;\n"
"font: 12pt \"Times New Roman\";\n"
"    \n"
"    background-color: rgb(255, 98, 101);\n"
"\n"
"font: 75 10pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);}\n"
"QPushButton:hover {\n"
"\n"
"    background-color: rgb(255, 0, 4);\n"
"     color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(170, 170, 255);\n"
"}\n"
"{    background: #F8B97A;\n"
"    border:2px solid black;\n"
"    border-radius:15px;\n"
"    color:Black;\n"
"    font-size: 15px;\n"
"    letter-spacing: 0.5px;\n"
"    font-family: \'Lato\';\n"
"    font-weight: 200;}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 10, 71, 81))
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet(u"background:none")
        self.label_6.setPixmap(QPixmap(u"cov.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(False)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 90, 141, 31))
        self.label_7.setStyleSheet(u"color:White;\n"
"Font-size:15px;\n"
"letter-spacing:0.5px;\n"
"background:none")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 0, 801, 581))
        self.label_16.setStyleSheet(u"")
        self.label_16.setPixmap(QPixmap(u"image (2).png"))
        self.label_16.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 100, 191, 31))
        self.label.setStyleSheet(u"color: Black;\n"
"Font-size:25px;\n"
"letter-spacing:1.2px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 160, 411, 51))
        self.label_8.setStyleSheet(u"color: Black;\n"
"Font-size:12px;\n"
"letter-spacing:1.2px;\n"
"border:1px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 220, 271, 161))
        self.label_9.setStyleSheet(u"color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_9.setPixmap(QPixmap(u"../m2.png"))
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(430, 160, 371, 41))
        self.label_10.setStyleSheet(u"color: Black;\n"
"Font-size:12px;\n"
"letter-spacing:1.2px;\n"
"border:1px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 380, 331, 31))
        self.label_12.setStyleSheet(u"color: Black;\n"
"Font-size:12px;\n"
"letter-spacing:1.2px;\n"
"border:1px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 420, 211, 141))
        self.label_13.setStyleSheet(u"color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_13.setPixmap(QPixmap(u"../m3.jpg"))
        self.label_13.setScaledContents(True)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(470, 380, 241, 31))
        self.label_14.setStyleSheet(u"color: Black;\n"
"Font-size:12px;\n"
"letter-spacing:1.2px;\n"
"border:1px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(490, 420, 191, 141))
        self.label_15.setStyleSheet(u"color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_15.setPixmap(QPixmap(u"../m4.png"))
        self.label_15.setScaledContents(True)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(510, 210, 201, 151))
        self.label_11.setPixmap(QPixmap(u"../m1.png"))
        self.label_11.setScaledContents(True)
        myth.setCentralWidget(self.centralwidget)
        self.label_16.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_11.raise_()
        self.menubar = QMenuBar(myth)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 26))
        myth.setMenuBar(self.menubar)

        self.retranslateUi(myth)

        QMetaObject.connectSlotsByName(myth)
    # setupUi

    def retranslateUi(self, myth):
        myth.setWindowTitle(QCoreApplication.translate("myth", u"myth", None))
        self.label_2.setText(QCoreApplication.translate("myth", u"Home", None))
        self.label_3.setText(QCoreApplication.translate("myth", u"Precaution", None))
        self.label_4.setText(QCoreApplication.translate("myth", u"Latest", None))
        self.label_5.setText(QCoreApplication.translate("myth", u"Stats", None))
        self.pushButton.setText(QCoreApplication.translate("myth", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("myth", u"Help Lines", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("myth", u"|| Covid Tracker ||", None))
        self.label_16.setText("")
        self.label.setText(QCoreApplication.translate("myth", u"Myth-Busters", None))
        self.label_8.setText(QCoreApplication.translate("myth", u"Can Covid-19 be transmitted through goods produced \n"
"in countries where there is ongoing transmission?", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("myth", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("myth", u"Can Covid-19 be transmitted through mosquitoes?", None))
        self.label_12.setText(QCoreApplication.translate("myth", u"Can digital thermometers be 100% effective \n"
"in detecting Covid-19 patients?", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("myth", u"Can Pneumonia vaccine prevent \n"
"Covid-19?", None))
        self.label_15.setText("")
        self.label_11.setText("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myth = QtWidgets.QMainWindow()
    ui = Ui_myth()
    ui.setupUi(myth)
    myth.show()
    sys.exit(app.exec_())
