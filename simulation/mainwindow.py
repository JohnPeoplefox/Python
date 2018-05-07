# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.display = QtWidgets.QGraphicsView(self.centralwidget)
        self.display.setObjectName("display")
        self.horizontalLayout.addWidget(self.display)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.frame = QtWidgets.QFrame(self.splitter_2)
        self.frame.setMinimumSize(QtCore.QSize(120, 200))
        self.frame.setMaximumSize(QtCore.QSize(120, 10000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 77, 112))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_start = QtWidgets.QPushButton(self.layoutWidget)
        self.button_start.setObjectName("button_start")
        self.verticalLayout.addWidget(self.button_start)
        self.button_stop = QtWidgets.QPushButton(self.layoutWidget)
        self.button_stop.setObjectName("button_stop")
        self.verticalLayout.addWidget(self.button_stop)
        self.button_pause = QtWidgets.QPushButton(self.layoutWidget)
        self.button_pause.setObjectName("button_pause")
        self.verticalLayout.addWidget(self.button_pause)
        self.button_resume = QtWidgets.QPushButton(self.layoutWidget)
        self.button_resume.setObjectName("button_resume")
        self.verticalLayout.addWidget(self.button_resume)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.horizontalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.button_pause.setText(_translate("MainWindow", "Pause"))
        self.button_resume.setText(_translate("MainWindow", "Resume"))

