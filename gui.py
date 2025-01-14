# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 650)
        MainWindow.setMinimumSize(QtCore.QSize(420, 650))
        MainWindow.setMaximumSize(QtCore.QSize(420, 650))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.power.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.power.setObjectName("power")
        self.volume_2 = QtWidgets.QSlider(parent=self.centralwidget)
        self.volume_2.setGeometry(QtCore.QRect(90, 250, 241, 22))
        self.volume_2.setMaximum(9)
        self.volume_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_2.setObjectName("volume_2")
        self.one = QtWidgets.QPushButton(parent=self.centralwidget)
        self.one.setGeometry(QtCore.QRect(130, 290, 51, 51))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(parent=self.centralwidget)
        self.two.setGeometry(QtCore.QRect(190, 290, 51, 51))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(parent=self.centralwidget)
        self.three.setGeometry(QtCore.QRect(250, 290, 51, 51))
        self.three.setObjectName("three")
        self.four = QtWidgets.QPushButton(parent=self.centralwidget)
        self.four.setGeometry(QtCore.QRect(190, 350, 51, 51))
        self.four.setObjectName("four")
        self.vol_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vol_up.setGeometry(QtCore.QRect(50, 410, 113, 32))
        self.vol_up.setObjectName("vol_up")
        self.channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_up.setGeometry(QtCore.QRect(260, 410, 113, 32))
        self.channel_up.setObjectName("channel_up")
        self.channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_down.setGeometry(QtCore.QRect(260, 470, 113, 32))
        self.channel_down.setObjectName("channel_down")
        self.vol_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vol_down.setGeometry(QtCore.QRect(50, 470, 113, 32))
        self.vol_down.setObjectName("vol_down_2")
        self.mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mute.setGeometry(QtCore.QRect(160, 530, 113, 32))
        self.mute.setObjectName("mute")
        self.volume_num = QtWidgets.QLabel(parent=self.centralwidget)
        self.volume_num.setGeometry(QtCore.QRect(340, 250, 60, 20))
        self.volume_num.setObjectName("volume_num")
        self.power_off_screen = QtWidgets.QLabel(parent=self.centralwidget)
        self.power_off_screen.setGeometry(QtCore.QRect(60, 50, 301, 171))
        self.power_off_screen.setText("")
        self.power_off_screen.setPixmap(QtGui.QPixmap("../images/blacksquare.png"))
        self.power_off_screen.setObjectName("power_off_screen")
        self.channel_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_1.setGeometry(QtCore.QRect(60, 50, 301, 171))
        self.channel_1.setText("")
        self.channel_1.setPixmap(QtGui.QPixmap("../images/cnn.png"))
        self.channel_1.setScaledContents(True)
        self.channel_1.setObjectName("channel_1")
        self.channel_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_2.setGeometry(QtCore.QRect(60, 50, 301, 171))
        self.channel_2.setText("")
        self.channel_2.setPixmap(QtGui.QPixmap("../images/foxnews.png"))
        self.channel_2.setScaledContents(True)
        self.channel_2.setObjectName("channel_2")
        self.channel_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_3.setGeometry(QtCore.QRect(60, 50, 301, 171))
        self.channel_3.setText("")
        self.channel_3.setPixmap(QtGui.QPixmap("../images/nbc.png"))
        self.channel_3.setScaledContents(True)
        self.channel_3.setObjectName("channel_3")
        self.channel_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_4.setGeometry(QtCore.QRect(60, 50, 301, 171))
        self.channel_4.setText("")
        self.channel_4.setPixmap(QtGui.QPixmap("../images/pbs.png"))
        self.channel_4.setScaledContents(True)
        self.channel_4.setObjectName("channel_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.power.setText(_translate("MainWindow", "Power"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.four.setText(_translate("MainWindow", "4"))
        self.vol_up.setText(_translate("MainWindow", "Volume Up"))
        self.channel_up.setText(_translate("MainWindow", "Channel Up"))
        self.channel_down.setText(_translate("MainWindow", "Channel Down"))
        self.vol_down.setText(_translate("MainWindow", "Volume Down"))
        self.mute.setText(_translate("MainWindow", "Mute"))
        self.volume_num.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
