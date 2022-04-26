# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from inspect import signature
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
import sqlite3

from numpy import sign
import login


class Ui_signup(object):

    # Database Connection
    # def createTable(self):
    #     conn=sqlite3.connect("signup.db")
    #
    #     conn.execute("CREATE TABLE USERS (Username TEXT NOT NULL, Email TEXT , Password TEXT)")
    #     conn.execute("INSERT INTO USERS VALUES(?,?,?)",('Anurag','anurag@gmail.com','anurag1234'))
    #     conn.commit()
    #
    #     result=conn.execute("SELECT * FROM USERS")
    #     for data in result:
    #         print("Username: ",data[0])
    #         print("mail: ",data[1])
    #         print("Pass: ",data[2])
    #
    #     conn.close()

    def signupCheck(self):
        # print("Signup button Clicked")
        username = self.name.text()
        email = self.email.text()
        passwrd = self.passwd.text()
        if self.vaccCheck.isChecked():
            vcc = "True"
        else:
            vcc = "False"
        

        if username=="":
            self.label_33.setText("Enter Your username!")
        elif email=="":
            self.label_33.setText("Enter Your email!")
        elif not email.endswith("@gmail.com"):
            self.label_33.setText("Enter valid email!")
        elif passwrd=="":
            self.label_33.setText("Enter Your passwrd!")
        elif len(passwrd)<6:
            self.label_33.setText("invalid Password!")

        # elif not(email.contains("@")):
        #     self.label_33.setText("Email should contain '@' symbol")


        # INSERT INTO `users` (`id`, `uname`, `mail`, `pass`, `vcc`) VALUES
        # (NULL, 'Anurag', 'anu@gmail.com', '1234', 'True');
        # print("Before Connecting")
        else:
            conn = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="covid tracker"
            )
            # print("Connected")
            query = "INSERT INTO users(uname,mail,pass,vcc) VALUES(%s,%s,%s,%s)"
            values = (username, email, passwrd, vcc)
            # cur = conn.cursor()
            cur = conn.cursor()
            cur.execute(query, values)
            conn.commit()
            # print("Inserted Successfully")
            print("Signed up successfully!")
        # print("Cur")
        # # query="SELECT * FROM `users` where mail='"+email+"'and pass='"+passwrd+"'"
        # query = "SELECT mail,pass from users where mail " \
        #         "like '" + email + "'and pass like '" \
        #         + passwrd + "'"
        #
        # print("Query")
        # cur.execute(query)
        # result=cur.fetchone()
        #
        # if result==None:
        #     print("Incorrect")
        #
        # else:
        #     print("Correct")

    def resetbtn(self):
        
        self.name.setText("")
        self.passwd.setText("")
        self.email.setText("")

    def loginCheck(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = login.Ui_login()
        self.ui.setupUi(self.window)
        self.window.show()
        signup.close()

    def setupUi(self, signup):
        signup.setObjectName("signup")
        signup.resize(640, 600)
        signup.setStyleSheet(
            "background:qlineargradient(spread:pad, x1:1, y1:1, x2:0.347091, y2:0.319, stop:0 rgba(0, 255, 169, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(signup)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -1, 641, 85))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("background:rgb(35, 35, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 221, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:none")
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(170, 120, 271, 41))
        self.name.setStyleSheet("QLineEdit{\n"
                                "    background: #E5C8F3;\n"
                                "    border:2px solid purple;\n"
                                "    border-radius:15px;\n"
                                "}\n"
                                "\n"
                                "QLineEdit:focus{\n"
                                "    border:2px solid #F49D2E;\n"
                                "    background: #F3D7B4;\n"
                                "    border-radius:15px;\n"
                                "}")
        self.name.setObjectName("name")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(170, 220, 271, 41))
        self.email.setStyleSheet("QLineEdit{\n"
                                 "    background: #E5C8F3;\n"
                                 "    border:2px solid purple;\n"
                                 "    border-radius:15px;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:focus{\n"
                                 "    border:2px solid #F49D2E;\n"
                                 "    background: #F3D7B4;\n"
                                 "    border-radius:15px;\n"
                                 "}")
        self.email.setObjectName("email")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 221, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.passwd = QtWidgets.QLineEdit(self.centralwidget)
        self.passwd.setGeometry(QtCore.QRect(170, 320, 271, 41))
        self.passwd.setStyleSheet("QLineEdit{\n"
                                  "    background: #E5C8F3;\n"
                                  "    border:2px solid purple;\n"
                                  "    border-radius:15px;\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:focus{\n"
                                  "    border:2px solid #F49D2E;\n"
                                  "    background: #F3D7B4;\n"
                                  "    border-radius:15px;\n"
                                  "}\n"
                                  "")
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("pass")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 290, 221, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:none")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 90, 81, 31))
        # self.pushButton.clicked.connect(self.resetbtn)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    background-color:none;\n"
                                      "    border:2px solid black;\n"
                                      "    border-radius:15px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color:#E1E7F0;\n"
                                      "    border: 2px solid black;\n"
                                      "    border-radius:15px;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.resetbtn)

        self.vaccCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.vaccCheck.setGeometry(QtCore.QRect(170, 380, 211, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.vaccCheck.setFont(font)
        self.vaccCheck.setStyleSheet("background-color:none")
        self.vaccCheck.setObjectName("vaccCheck")
        self.signupbtn = QtWidgets.QPushButton(self.centralwidget)
        self.signupbtn.setGeometry(QtCore.QRect(250, 420, 111, 51))
        self.signupbtn.setStyleSheet("QPushButton{\n"
                                     "    background-color:#F0BDE6;\n"
                                     "    border: 2px solid black;\n"
                                     "    border-radius:15px;\n"

                                     "\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:#F1D5EB;\n"
                                     "    border: 2px solid black;\n"
                                     "    border-radius:15px;\n"

                                     "}")
        self.signupbtn.setObjectName("signupbtn")

        # Signup button event
        self.signupbtn.clicked.connect(self.signupCheck)
        ###############################

        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(300, 480, 180, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("background-color:none;\ncolor:red;")
        self.label_33.setObjectName("label_33")

        self.Reset = QtWidgets.QLabel(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(40, 500, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.Reset.setFont(font)
        self.Reset.setStyleSheet("background-color:none\n"
                                 "")
        self.Reset.setObjectName("Reset")

        self.slogin = QtWidgets.QPushButton(self.centralwidget)
        self.slogin.setGeometry(QtCore.QRect(30, 530, 131, 41))
        self.slogin.setStyleSheet("QPushButton{\n"
                                  "    background-color:#7AA9F0;\n"
                                  "    border: 2px solid black;\n"
                                  "    border-radius:15px;\n"
                                  
                                  "\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "    background-color:#A8C7F5;\n"
                                  "    border: 2px solid black;\n"
                                  "    border-radius:15px;\n"
                                  
                                  
                                  "}\n"
                                  "\n"
                                  "")
        self.slogin.setObjectName("slogin")
        ################
        self.slogin.clicked.connect(self.loginCheck)
        ##############
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 641, 581))
        self.label_6.setStyleSheet("background-color:none;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.name.raise_()
        self.email.raise_()
        self.label_3.raise_()
        self.label_33.raise_()
        self.passwd.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.vaccCheck.raise_()
        self.signupbtn.raise_()
        self.Reset.raise_()
        self.slogin.raise_()
        signup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(signup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        signup.setMenuBar(self.menubar)

        self.retranslateUi(signup)
        QtCore.QMetaObject.connectSlotsByName(signup)

    def retranslateUi(self, signup):
        _translate = QtCore.QCoreApplication.translate
        signup.setWindowTitle(_translate("signup", "SignUp || Covid Tracker Application"))
        self.label.setText(_translate("signup", "Sign Up"))
        self.label_2.setText(_translate("signup", "Enter Your name"))
        self.label_3.setText(_translate("signup", "Enter Your Email"))
        self.label_4.setText(_translate("signup", "Enter Your Password"))
        self.label_33.setText(_translate("signup", ""))
        self.pushButton.setText(_translate("signup", "Reset"))
        self.vaccCheck.setText(_translate("signup", "Are You Vaccinated??"))
        self.signupbtn.setText(_translate("signup", "Sign Up"))
        self.Reset.setText(_translate("signup", "Already Signed Up?"))
        self.slogin.setText(_translate("signup", "Login Here!!"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    signup = QtWidgets.QMainWindow()
    ui = Ui_signup()
    ui.setupUi(signup)
    signup.show()
    sys.exit(app.exec_())
