# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaAggiungiPrenotazione.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from prenotazioni.Controller.ControlloreInserisciPrenotazione import *
from attivita.controller.ControlloreListaAttivita import *


class Ui_Form(object):
    def __init__(self, utente_attivo):
        super(Ui_Form, self).__init__()
        self.utente_attivo = utente_attivo
        self.controller = ControlloreInserisciPrenotazione()
        self.lista_attivita = ControlloreListaAttivita().get_lista_attivita()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(322, 164)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 20, 321, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Label_nome = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_nome.setFont(font)
        self.Label_nome.setObjectName("Label_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_nome)
        self.nomeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nomeLineEdit.setObjectName("nomeLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nomeLineEdit)
        self.Label_cognome = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_cognome.setFont(font)
        self.Label_cognome.setObjectName("Label_cognome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_cognome)
        self.cognomeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cognomeLineEdit.setObjectName("cognomeLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cognomeLineEdit)
        self.Label_attivita = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_attivita.setFont(font)
        self.Label_attivita.setObjectName("Label_attivita")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_attivita)
        self.attivitaComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.attivitaComboBox.setObjectName("attivitaComboBox")
        self.attivitaComboBox.addItem("Seleziona un'attivitá")

        # popola la combobox delle attivita
        for attivita in self.lista_attivita:
            self.attivitaComboBox.addItem(attivita.titolo)

        self.attivitaComboBox.setCurrentIndex(0)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.attivitaComboBox)
        self.Label_date = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_date.setFont(font)
        self.Label_date.setObjectName("Label_date")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_date)
        self.datePrenotabiliComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.datePrenotabiliComboBox.setObjectName("datePrenotabiliComboBox")
        self.datePrenotabiliComboBox.addItem('Seleziona una data')
        self.datePrenotabiliComboBox.setCurrentIndex(0)
        if self.attivitaComboBox.currentText() == "Seleziona un'attivitá":
            self.datePrenotabiliComboBox.setEditable(False)

        def mostra_date_per_attivita():
            self.datePrenotabiliComboBox.clear()
            print(self.attivitaComboBox.currentText())
            lista_date = self.controller.get_data_prenotazione_per_attivita(self.attivitaComboBox.currentText())
            for data in lista_date:
                self.datePrenotabiliComboBox.addItem(data.strftime("%Y -%m -%d") +
                                                     "    " +
                                                     str(self.controller.get_posti_disponibili_per_data(data)))

        # Assuming you have an instance of Ui_Form called ui
        self.attivitaComboBox.currentTextChanged.connect(mostra_date_per_attivita)

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.datePrenotabiliComboBox)
        self.pushButton_prenota = QtWidgets.QPushButton(Form)
        self.pushButton_prenota.setGeometry(QtCore.QRect(110, 130, 101, 23))
        self.pushButton_prenota.setObjectName("pushButton_prenota")

        self.pushButton_prenota.clicked.connect(lambda: show_popup_if_form_not_filled())

        def is_form_filled():
            if (self.nomeLineEdit.text().strip() == "" or
                    self.cognomeLineEdit.text().strip() == "" or
                    self.attivitaComboBox.currentText() == "Seleziona un'attivitá" or
                    self.datePrenotabiliComboBox.currentText() == 'Seleziona una data'):
                return False
            return True

        def show_popup_if_form_not_filled():
            if not is_form_filled():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Per favore compila tutti i campi")
                msg.setWindowTitle("Incomplete Form")
                msg.exec_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "InserisciPrenotazione"))
        self.Label_nome.setText(_translate("Form", "Nome:"))
        self.Label_cognome.setText(_translate("Form", "Cognome:"))
        self.Label_attivita.setText(_translate("Form", "Attività:"))
        self.Label_date.setText(_translate("Form", "Date prenotabili:"))
        self.pushButton_prenota.setText(_translate("Form", "Prenota attività"))


def show_vista_aggiungi_prenotazione(utente_attivo):
    ui = Ui_Form(utente_attivo)
    ui.setupUi(Form)
    Form.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()

# sys.exit(app.exec_())
