import sys
from PyQt5 import QtWidgets, QtCore
from ui import Ui_Form
from math import ceil, sqrt


class Calc(QtWidgets.QMainWindow):
    display = '0'
    buffer = '0'
    memory = '0'
    operator = ''
    new_operation = False

    def __init__(self):
        super(Calc, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label.setText(self.display)
        # Connection buttons block
        self.ui.pushButton_0.clicked.connect(self.button_0)
        self.ui.pushButton_1.clicked.connect(self.button_1)
        self.ui.pushButton_2.clicked.connect(self.button_2)
        self.ui.pushButton_3.clicked.connect(self.button_3)
        self.ui.pushButton_4.clicked.connect(self.button_4)
        self.ui.pushButton_5.clicked.connect(self.button_5)
        self.ui.pushButton_6.clicked.connect(self.button_6)
        self.ui.pushButton_7.clicked.connect(self.button_7)
        self.ui.pushButton_8.clicked.connect(self.button_8)
        self.ui.pushButton_9.clicked.connect(self.button_9)
        self.ui.pushButton_plus.clicked.connect(self.button_plus)
        self.ui.pushButton_minus.clicked.connect(self.button_minus)
        self.ui.pushButton_mult.clicked.connect(self.button_mult)
        self.ui.pushButton_div.clicked.connect(self.button_div)
        self.ui.pushButton_percent.clicked.connect(self.button_percent)
        self.ui.pushButton_sqrt.clicked.connect(self.button_sqrt)
        self.ui.pushButton_c.clicked.connect(self.button_c)
        self.ui.pushButton_mrc.clicked.connect(self.button_mrc)
        self.ui.pushButton_answer.clicked.connect(self.button_answer)

    def button_0(self):
        self.set_number('0')

    def button_1(self):
        self.set_number('1')

    def button_2(self):
        self.set_number('2')

    def button_3(self):
        self.set_number('3')

    def button_4(self):
        self.set_number('4')

    def button_5(self):
        self.set_number('5')

    def button_6(self):
        self.set_number('6')

    def button_7(self):
        self.set_number('7')

    def button_8(self):
        self.set_number('8')

    def button_9(self):
        self.set_number('9')

    def button_plus(self):
        self.operation('+')

    def button_minus(self):
        self.operation('-')

    def button_mult(self):
        self.operation('*')

    def button_div(self):
        self.operation('/')

    def button_percent(self):
        self.display = str(ceil(int(self.buffer) * int(self.display) / 100))
        self.ui.label.setText(self.display)

    def button_sqrt(self):
        self.operation('**')
        self.button_answer()

    def button_answer(self):
        if self.operator == '**':
            try:
                answer = str(ceil(sqrt(int(self.buffer))))
                self.ui.label.setText(answer)
                self.operator = ''
                self.new_operation = True
            except ValueError:
                self.ui.label.setText('Error')
        elif self.operator:
            try:
                answer = str(ceil(eval(self.buffer + self.operator + self.display)))
                self.display = answer
                if len(self.display) < 10 or len(self.display) <= 11 and self.display[0] == '-':
                    self.ui.label.setText(self.display)
                    self.operator = ''
                    self.new_operation = True
                else:
                    self.ui.label.setText('Error')
            except ZeroDivisionError:
                self.ui.label.setText('Error')

    def button_c(self):
        self.display = '0'
        self.buffer = '0'
        self.operator = None
        self.ui.label.setText(self.display)

    def button_mrc(self):
        if self.display != 'Error':
            if self.memory == '0' and self.display != self.memory:
                self.memory = self.display
                self.ui.label_mem.setText('M')
                self.new_operation = True
            elif self.memory != '0' and self.display != self.memory:
                self.display = self.memory
                self.ui.label.setText(self.display)
            elif self.memory != '0' and self.memory == self.display:
                self.memory = '0'
                self.ui.label_mem.setText('')

    def set_number(self, number):
        if self.ui.label.text() != 'Error':
            if self.new_operation:
                self.display = number
                self.new_operation = False
            else:
                if len(self.display) < 10 or len(self.display) <= 11 and self.display[0] == '-':
                    if self.display != '0':
                        self.display += number
                    else:
                        self.display = number
            self.ui.label.setText(self.display)

    def operation(self, operator):
        if self.ui.label.text() != 'Error':
            if self.operator != '':
                self.button_answer()
            self.buffer = self.ui.label.text()
            self.operator = operator
            self.new_operation = True

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_0:
            self.button_0()
        if event.key() == QtCore.Qt.Key_1:
            self.button_1()
        if event.key() == QtCore.Qt.Key_2:
            self.button_2()
        if event.key() == QtCore.Qt.Key_3:
            self.button_3()
        if event.key() == QtCore.Qt.Key_4:
            self.button_4()
        if event.key() == QtCore.Qt.Key_5:
            self.button_5()
        if event.key() == QtCore.Qt.Key_6:
            self.button_6()
        if event.key() == QtCore.Qt.Key_7:
            self.button_7()
        if event.key() == QtCore.Qt.Key_8:
            self.button_8()
        if event.key() == QtCore.Qt.Key_9:
            self.button_9()
        if event.key() == QtCore.Qt.Key_Plus:
            self.button_plus()
        if event.key() == QtCore.Qt.Key_Minus:
            self.button_minus()
        if event.key() == QtCore.Qt.Key_Asterisk:
            self.button_mult()
        if event.key() == QtCore.Qt.Key_Slash:
            self.button_div()
        if event.key() == QtCore.Qt.Key_Q:
            self.button_sqrt()
        if event.key() == QtCore.Qt.Key_P:
            self.button_percent()
        if event.key() == QtCore.Qt.Key_Enter:
            self.button_answer()
        if event.key() == QtCore.Qt.Key_Escape:
            self.button_c()
        if event.key() == QtCore.Qt.Key_M:
            self.button_mrc()
        event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec_())
