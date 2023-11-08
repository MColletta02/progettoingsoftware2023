# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaAttivita_PROVA.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from attivita.controller.ControlloreListaAttivita import *
import sys


class Ui_Vista_attivita(object):

    def __init__(self, attivita_selezionata):
        super(Ui_Vista_attivita).__init__()
        self.controller = ControlloreListaAttivita()
        self.attivita_selezionata = attivita_selezionata

    def setupUi(self, Vista_attivita):
        Vista_attivita.setObjectName("Vista_attivita")
        Vista_attivita.resize(397, 210)
        self.verticalLayoutWidget = QtWidgets.QWidget(Vista_attivita)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Titolo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titolo.setFont(font)
        self.label_Titolo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titolo.setObjectName("label_Titolo")
        self.verticalLayout.addWidget(self.label_Titolo)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_5)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.label_Titolo.hide()
        self.retranslateUi(Vista_attivita)
        QtCore.QMetaObject.connectSlotsByName(Vista_attivita)

    def retranslateUi(self, Vista_attivita):
        _translate = QtCore.QCoreApplication.translate
        Vista_attivita.setWindowTitle(_translate("Vista_attivita", self.attivita_selezionata.titolo))
        self.label.setText(_translate("Vista_attivita", "Descrizione:"))
        self.label_2.setText(_translate("Vista_attivita", "Prezzo:"))
        self.label_3.setText(_translate("Vista_attivita", "Giorno:"))
        self.label_4.setText(_translate("Vista_attivita", "Orario:"))
        self.label_5.setText(_translate("Vista_attivita", "Posti massimi:"))
        self.plainTextEdit.setPlainText(_translate('Vista_attivita', self.attivita_selezionata.descrizione))
        self.plainTextEdit_2.setPlainText(_translate("Vista_attivita", self.attivita_selezionata.prezzo))
        self.plainTextEdit_3.setPlainText(_translate("Vista_attivita", self.attivita_selezionata.giorno_della_settimana))
        self.plainTextEdit_4.setPlainText(_translate("vista_attivita", self.attivita_selezionata.orario))
        self.plainTextEdit_5.setPlainText(_translate("vista_attivita", str(self.attivita_selezionata.n_posti)))


def show_attivita(attivita_selezionata):
    ui = Ui_Vista_attivita(attivita_selezionata)
    ui.setupUi(Vista_attivita)
    Vista_attivita.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
Vista_attivita = QtWidgets.QWidget()

