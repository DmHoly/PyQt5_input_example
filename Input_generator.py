import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("PyQt Line Edit example (textfield)")

        pybutton = QPushButton('Get all value', self)
        pybutton.clicked.connect(self.Get_all_value)
        pybutton.resize(200,32)
        pybutton.move(80, 60+160)

    def generation_input(self, list):
        self.input_list = []
        ind = 0
        for i in range(len(list)):

            self.nameLabel = QLabel(self)
            self.nameLabel.setText(list[i])
            self.line = QLineEdit(self)
            self.input_list.append(self.line)
            self.line.resize(200, 32)
            self.line.move(80, 20+ind)
            self.nameLabel.move(20, 20+ind)
            ind = ind + 40

    def Get_all_value(self):
        for elt, input in enumerate(self.input_list):

            print(elt, input.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainWin = MainWindow()
    list = ['Value_1', 'Value_2', "Value_3", "Value_4"]
    mainWin.generation_input(list)


    mainWin.show()
    sys.exit( app.exec_())