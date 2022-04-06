# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from shamir import Shamir
from binascii import hexlify, unhexlify

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = QUiLoader().load('form.ui')
        self.ui.show()
        self.ui.pushButton_create_share.clicked.connect(self.create_shares)
        self.ui.pushButton_combine_share.clicked.connect(self.combine_shares)

    def create_shares(self):
        secret = self.ui.plainTextEdit_Secret.toPlainText().encode()
        l = Shamir.split(3, 5, secret)
        print(l)
        self.ui.plainTextEdit_s1.setPlainText(str(hexlify(l[0][1]))[2:-1])
        self.ui.plainTextEdit_s2.setPlainText(str(hexlify(l[1][1]))[2:-1])
        self.ui.plainTextEdit_s3.setPlainText(str(hexlify(l[2][1]))[2:-1])
        self.ui.plainTextEdit_s4.setPlainText(str(hexlify(l[3][1]))[2:-1])
        self.ui.plainTextEdit_s5.setPlainText(str(hexlify(l[4][1]))[2:-1])
        pass

    def combine_shares(self):
        self.ui.plainTextEdit_cs.setPlainText("NULL")
        shares = []
        if len(self.ui.plainTextEdit_s1.toPlainText()) != 0:
            shares.append((1, unhexlify(self.ui.plainTextEdit_s1.toPlainText().encode())))
        if len(self.ui.plainTextEdit_s2.toPlainText()) != 0:
            shares.append((2, unhexlify(self.ui.plainTextEdit_s2.toPlainText().encode())))
        if len(self.ui.plainTextEdit_s3.toPlainText()) != 0:
            shares.append((3, unhexlify(self.ui.plainTextEdit_s3.toPlainText().encode())))
        if len(self.ui.plainTextEdit_s4.toPlainText()) != 0:
            shares.append((4, unhexlify(self.ui.plainTextEdit_s4.toPlainText().encode())))
        if len(self.ui.plainTextEdit_s5.toPlainText()) != 0:
            shares.append((5, unhexlify(self.ui.plainTextEdit_s5.toPlainText().encode())))
        print(shares)
        secret = Shamir.combine(shares)
        self.ui.plainTextEdit_cs.setPlainText(secret.decode())
        pass


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
