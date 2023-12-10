from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_trainingWindow(object):
    def setupUi(self, trainingWindow):
        trainingWindow.setObjectName("trainingWindow")
        trainingWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(trainingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(180, 10, 392, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        trainingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(trainingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        trainingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(trainingWindow)
        self.statusbar.setObjectName("statusbar")
        trainingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(trainingWindow)
        QtCore.QMetaObject.connectSlotsByName(trainingWindow)

    def retranslateUi(self, trainingWindow):
        _translate = QtCore.QCoreApplication.translate
        trainingWindow.setWindowTitle(_translate("trainingWindow", "Training Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trainingWindow = QtWidgets.QMainWindow()
    ui = Ui_trainingWindow()
    ui.setupUi(trainingWindow)
    trainingWindow.show()
    sys.exit(app.exec_())
