import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton , QLineEdit
from PyQt5.QtCore import QSize    
from run_class import *

class stack_widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.QtStack = QtWidgets.QStackedLayout()
        self.stack1 = QtWidgets.QWidget()
        self.stack2 = QtWidgets.QWidget()

        self.main_window()
        self.add_run_window()

        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

    def main_window(self):
        self.setMinimumSize(QSize(300,200))
        self.setWindowTitle("Running Log")
        pybutton = QPushButton("Add a run", self)
        pybutton.clicked.connect(self.click_method)
        pybutton.resize(100,32)
        pybutton.move(50, 50)
    
    def add_run_window(self):
        self.setMinimumSize(QSize(300,200))
        self.setWindowTitle("Add a Run")
        save_run_button = QPushButton("Save Run!", self)
        save_run_button.clicked.connect(self.click_method)
        save_run_button.resize(100,32)
        save_run_button.move(50, 50)            
        distance_box = QtWidgets.QLineEdit(self)
    
    def click_method(self):
        self.QtStack.setCurrentIndex(1)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_win = stack_widget()
    main_win.show()
    sys.exit( app.exec_() )