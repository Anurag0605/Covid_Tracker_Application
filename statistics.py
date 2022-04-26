# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from StatsCount import *
from StatsCount2 import *
import sgraphs
import cgraphs
import home
import precautions 
import latest 
import helpline 
import Vaccination 

class Ui_statistics(object):
    def homep(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = home.Ui_home()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def cgraphsp(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = cgraphs.Ui_cgraphs()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def sgraphsp(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = sgraphs.Ui_sgraphs()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()


    def latestp(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = latest.Ui_latest()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def precs(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = precautions.Ui_precautions()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def statsp(self,event):
        self.window = QtWidgets.QMainWindow()
        self.ui = statistics.Ui_statistics()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()

    def helplinep(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = helpline.Ui_HelpLines()
        self.ui.setupUi(self.window)
        self.window.show()
        # home.close()


    def CMpressed(self):

        import sys
        import io
        import folium  # pip install folium
        from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
        from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

        """
        Folium in PyQt5
        """

        class StatsCount(QWidget):

            def __init__(self):
                super().__init__()
                self.setWindowTitle('Maps || CountryWise')
                self.window_width, self.window_height = 1200, 900

                self.setMinimumSize(self.window_width, self.window_height)

                layout = QVBoxLayout()
                self.setLayout(layout)

                # coordinate = (37.8199286, -122.4782551)
                m = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)
                # save map data to data object
                folium.Marker(location=[20.593683, 78.962883],
                              popup="<h3>India</h3>    <br>    <strong>Total Cases: </strong>6232764372 <br> <strong>Active Cases: </strong>6232764372 <br>    <strong>Total Deaths: </strong>6232764372  <br>  <strong>Total Vaccinations: </strong>6232764372",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[37.090240, -95.712891], popup="USA",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[61.524010, 105.318756], popup="Russia",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[-25.274399, 133.775131], popup="Australia",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[56.130367, -106.346771], popup="Canada",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[35.000074, 104.999927], popup="China",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[36.5748441, 139.2394179], popup="Japan",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[-28.8166236, 24.991639], popup="South Africa",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[30.3308401, 71.247499], popup="Pakistan",
                              tooltip="Click for more information").add_to(m)

                data = io.BytesIO()
                m.save(data, close_file=False)

                webView = QWebEngineView()
                webView.setHtml(data.getvalue().decode())
                layout.addWidget(webView)


            app = QApplication(sys.argv)
            app.setStyleSheet('''
                QWidget {
                    font-size: 35px;
                }
            ''')

            StatsCount = StatsCount()
            StatsCount.show()

            try:
                sys.exit(app.exec_())
            except SystemExit:
                print('Closing Window...')



    def SMpressed(self):

        import sys
        import io
        import folium  # pip install folium
        from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
        from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

        """
        Folium in PyQt5
        """

        class StatsCount2(QWidget):

            def __init__(self):
                super().__init__()
                self.setWindowTitle('Maps || Statewise')
                self.window_width, self.window_height = 1200, 900

                self.setMinimumSize(self.window_width, self.window_height)

                layout = QVBoxLayout()
                self.setLayout(layout)

                # coordinate = (37.8199286, -122.4782551)
                m = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)
                # save map data to data object
                folium.Marker(location=[20.593683, 78.962883],
                              popup="<h3>India</h3>    <br>    <strong>Total Cases: </strong>6232764372 <br> <strong>Active Cases: </strong>6232764372 <br>    <strong>Total Deaths: </strong>6232764372  <br>  <strong>Total Vaccinations: </strong>6232764372",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[37.090240, -95.712891], popup="USA",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[61.524010, 105.318756], popup="Russia",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[-25.274399, 133.775131], popup="Australia",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[56.130367, -106.346771], popup="Canada",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[35.000074, 104.999927], popup="China",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[36.5748441, 139.2394179], popup="Japan",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[-28.8166236, 24.991639], popup="South Africa",
                              tooltip="Click for more information").add_to(m)
                folium.Marker(location=[30.3308401, 71.247499], popup="Pakistan",
                              tooltip="Click for more information").add_to(m)

                data = io.BytesIO()
                m.save(data, close_file=False)

                webView = QWebEngineView()
                webView.setHtml(data.getvalue().decode())
                layout.addWidget(webView)


            app = QApplication(sys.argv)
            app.setStyleSheet('''
                QWidget {
                    font-size: 35px;
                }
            ''')

            StatsCount2 = StatsCount2()
            StatsCount2.show()

            try:
                sys.exit(app.exec_())
            except SystemExit:
                print('Closing Window...')


    def setupUi(self, statistics):
        statistics.setObjectName("statistics")
        statistics.resize(804, 600)
        statistics.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(statistics)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 101, 31))
        self.label_2.setStyleSheet("color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"border:2px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.mousePressEvent=self.homep
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 30, 111, 31))
        self.label_3.setStyleSheet("color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"border:2px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.mousePressEvent=self.precs
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 30, 101, 31))
        self.label_4.setStyleSheet("color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"border:2px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.mousePressEvent=self.latestp
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 30, 111, 31))
        self.label_5.setStyleSheet("color: Black;\n"
"Font-size:15px;\n"
"letter-spacing:1.2px;\n"
"border:2px solid cyan;\n"
"border-radius:10px;\n"
"background:none;\n"
"font-weight:bold;\n"
"color:white;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 71, 81))
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet("background:none")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("cov.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.label_7.setStyleSheet("color:White;\n"
"Font-size:15px;\n"
"letter-spacing:0.5px;\n"
"background:none")
        self.label_7.setObjectName("label_7")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.label_16.setStyleSheet("")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("image (2).png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(680, 10, 61, 61))
        self.label_17.setStyleSheet("background:none;")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("User icon.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(630, 70, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:white;\n"
                                    "font-size:10px;\n"
"background:none;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 80, 381, 51))
        self.label.setStyleSheet("color:White;\n"
"background:none;\n"
"letter-spacing:1px;\n"
"font-size:35px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 100, 101, 41))
        self.pushButton_3.setStyleSheet("QPushButton{border-radius:20px;\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.helplinep)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(280, 140, 251, 20))
        self.label_12.setStyleSheet("background:none;\n"
"border-top:2px solid cyan;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.SMbtn = QtWidgets.QPushButton(self.centralwidget)
        self.SMbtn.setGeometry(QtCore.QRect(130, 290, 151, 61))
        self.SMbtn.setStyleSheet("QPushButton{border-radius:20px;\n"
"font: 12pt \"Times New Roman\";\n"
"    \n"
"    background-color: #db5ad5;\n"
"\n"
"font: 75 10pt \"Times New Roman\";\n"
"font-size:18px;\n"
"color: rgb(0, 0, 0);}\n"
"QPushButton:hover {\n"
"\n"
"    background-color:#e892e4;\n"
"     color: black;\n"
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
        self.SMbtn.setObjectName("SMbtn")

        self.CMbtn = QtWidgets.QPushButton(self.centralwidget)
        self.SMbtn.clicked.connect(self.SMpressed)
        self.CMbtn.setGeometry(QtCore.QRect(130, 390, 151, 61))
        self.CMbtn.setStyleSheet("QPushButton{border-radius:20px;\n"
"font: 12pt \"Times New Roman\";\n"
"    \n"
"    background-color: #db5ad5;\n"
"\n"
"font: 75 10pt \"Times New Roman\";\n"
"font-size:18px;\n"
"color: rgb(0, 0, 0);}\n"
"QPushButton:hover {\n"
"\n"
"    background-color: #e892e4;\n"
"     color: black;\n"
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
        self.CMbtn.setObjectName("CMbtn")
        self.CMbtn.clicked.connect(self.CMpressed)
        self.CGbtn = QtWidgets.QPushButton(self.centralwidget)
        self.CGbtn.setGeometry(QtCore.QRect(550, 390, 141, 61))
        self.CGbtn.setStyleSheet("QPushButton{border-radius:20px;\n"
"font: 12pt \"Times New Roman\";\n"
"    \n"
"    background-color: #59d4a1;\n"
"\n"
"font: 75 10pt \"Times New Roman\";\n"
"font-size:18px;\n"
"color: rgb(0, 0, 0);}\n"
"QPushButton:hover {\n"
"\n"
"    background-color: #91ebc6;\n"
"     color: black;\n"
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
        self.CGbtn.setObjectName("CGbtn")
        self.CGbtn.clicked.connect(self.cgraphsp)
        self.SGbtn = QtWidgets.QPushButton(self.centralwidget)
        self.SGbtn.setGeometry(QtCore.QRect(550, 290, 141, 61))
        self.SGbtn.setStyleSheet("QPushButton{border-radius:20px;\n"
"font: 12pt \"Times New Roman\";\n"
"    \n"
"    background-color: #59d4a1;\n"
"\n"
"font: 75 10pt \"Times New Roman\";\n"
"font-size:18px;\n"
"color: rgb(0, 0, 0);}\n"
"QPushButton:hover {\n"
"\n"
"    background-color: #91ebc6;\n"
"     color: black;\n"
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
        self.SGbtn.setObjectName("SGbtn")
        self.SGbtn.clicked.connect(self.sgraphsp)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 230, 161, 31))
        self.label_8.setStyleSheet("background:none;\n"
"font-size:20px;\n"
"letter-spacing:1px;\n"
"color:white;\n"
"font-weight:bold;\n"
"font-family:Arial;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(540, 230, 161, 31))
        self.label_9.setStyleSheet("background:none;\n"
"font-size:20px;\n"
"letter-spacing:1px;\n"
"color:white;\n"
"font-weight:bold;\n"
"font-family:Arial;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(120, 260, 171, 20))
        self.label_13.setStyleSheet("background:none;\n"
"border-top:2px solid #59d4a1;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 260, 191, 20))
        self.label_14.setStyleSheet("background:none;\n"
"border-top:2px solid #db5ad5;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(420, 180, 2, 371))
        self.line_2.setStyleSheet("background-color:cyan;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_16.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.label_12.raise_()
        self.SMbtn.raise_()
        self.CMbtn.raise_()
        self.CGbtn.raise_()
        self.SGbtn.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.line_2.raise_()
        statistics.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(statistics)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 22))
        self.menubar.setObjectName("menubar")
        statistics.setMenuBar(self.menubar)

        self.retranslateUi(statistics)
        QtCore.QMetaObject.connectSlotsByName(statistics)

    def retranslateUi(self, statistics):
        _translate = QtCore.QCoreApplication.translate
        statistics.setWindowTitle(_translate("statistics", "Statistics"))
        self.label_2.setText(_translate("statistics", "Home"))
        self.label_3.setText(_translate("statistics", "Precaution"))
        self.label_4.setText(_translate("statistics", "Latest"))
        self.label_5.setText(_translate("statistics", "Stats"))
        self.label_7.setText(_translate("statistics", "|| Covid Tracker ||"))
        self.label_18.setText(_translate("statistics", "Welcome, Anurag Yadav"))
        self.label.setText(_translate("statistics", "|| Statistics ||"))
        self.pushButton_3.setText(_translate("statistics", "Help Lines"))
        self.SMbtn.setText(_translate("statistics", "Statewise"))
        self.CMbtn.setText(_translate("statistics", "Countrywise"))
        self.CGbtn.setText(_translate("statistics", "Countrywise"))
        self.SGbtn.setText(_translate("statistics", "Statewise"))
        self.label_8.setText(_translate("statistics", "Show Maps"))
        self.label_9.setText(_translate("statistics", "Show Graphs"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statistics = QtWidgets.QMainWindow()
    ui = Ui_statistics()
    ui.setupUi(statistics)
    statistics.show()
    sys.exit(app.exec_())
