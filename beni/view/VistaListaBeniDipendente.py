import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from beni.controller.ControlloreListaBeni import *
from beni.view.VistaInserisciBene import *
from beni.view.VistaBene import *



class Ui_VistaListaBeniDipendente(object):

    def __init__(self, utente_attivo):
        super(Ui_VistaListaBeniDipendente, self).__init__()
        self.controller = ControlloreListaBeni()
        self.utente_attivo = utente_attivo
        self.list_model = None
    def setupUi(self, VistaListaBeniDipendente):
        VistaListaBeniDipendente.setObjectName("VistaListaBeniDipendente")
        VistaListaBeniDipendente.resize(858, 646)
        self.centralwidget = QtWidgets.QWidget(VistaListaBeniDipendente)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(650, 80, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 581, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 70, 211, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(170, 70, 191, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 20, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 120, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        if self.utente_attivo.is_dipendente:
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 101, 31))
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(170, 110, 101, 31))
            self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 180, 871, 431))
        self.listView.setObjectName("listView")
        VistaListaBeniDipendente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VistaListaBeniDipendente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 22))
        self.menubar.setObjectName("menubar")
        VistaListaBeniDipendente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VistaListaBeniDipendente)
        self.statusbar.setObjectName("statusbar")
        VistaListaBeniDipendente.setStatusBar(self.statusbar)
        def popola_listview():
            #lista_beni = self.controller.get_lista_beni()
            bene_names = list(self.controller.get_lista_nomi_beni())
            #bene_names = list(set(bene.nome for bene in lista_beni))
            #for item in bene_names:
                #print(type(item), item)
            if bene_names:
                self.list_model = QtCore.QStringListModel(bene_names)
                self.listView.setModel(self.list_model)
            else:
                self.listView.setModel(None)



        popola_listview()

        self.lineEdit.setPlaceholderText("Inserisci Nome")
        if self.utente_attivo.is_dipendente:
            self.lineEdit.setPlaceholderText("Inserisci Nome o ID")


        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.doubleClicked.connect(lambda: self.item_clicked())
        self.pushButton.clicked.connect(self.ricerca_bene)
        if self.utente_attivo.is_dipendente:
            self.pushButton_2.clicked.connect(lambda: show_inserisci_bene(self.utente_attivo,self.update_ui))


        self.retranslateUi(VistaListaBeniDipendente)
        QtCore.QMetaObject.connectSlotsByName(VistaListaBeniDipendente)


    def retranslateUi(self, VistaListaBeniDipendente):
        _translate = QtCore.QCoreApplication.translate
        VistaListaBeniDipendente.setWindowTitle(_translate("VistaListaBeniDipendente", "Vista lista beni"))
        self.comboBox.setItemText(0, _translate("VistaListaBeniDipendente", "Area Geologica"))
        self.comboBox.setItemText(1, _translate("VistaListaBeniDipendente", "Area Zoologica"))
        self.comboBox.setItemText(2, _translate("VistaListaBeniDipendente", "Area Paleontologica"))
        self.comboBox.setItemText(3, _translate("VistaListaBeniDipendente", "Area esposizione temporanee"))
        self.comboBox.setItemText(4, _translate("VistaListaBeniDipendente", "Science room"))
        self.checkBox.setText(_translate("VistaListaBeniDipendente", "Beni Disponibili"))
        self.checkBox_2.setText(_translate("VistaListaBeniDipendente", "Beni Non Disponibili"))
        self.pushButton.setText(_translate("VistaListaBeniDipendente", "Ricerca"))
        self.label.setText(_translate("VistaListaBeniDipendente", "LISTA DEI BENI"))
        if self.utente_attivo.is_dipendente:
            self.pushButton_2.setText(_translate("VistaListaBeniDipendente", "Inserisci Bene"))
            self.pushButton_3.setText(_translate("VistaListaBeniDipendente", "Stato Aree"))


    def update_ui(self):
        # lista_beni = self.controller.get_lista_beni()
        bene_names = list(self.controller.get_lista_nomi_beni())
        # bene_names = list(set(bene.nome for bene in lista_beni))
        if bene_names:
            self.list_model = QtCore.QStringListModel(bene_names)
            self.listView.setModel(self.list_model)
        else:
            self.listView.setModel(None)

    def item_clicked(self):
        index = self.listView.currentIndex()
        if index.isValid():
            nome_bene = self.list_model.data(index, QtCore.Qt.DisplayRole)
            #url = self.controller.ottieni_path_immagine_bene(nome_bene)
            bene = self.controller.cerca_bene_per_nome(nome_bene)
            show_vista_bene(self.utente_attivo, bene, self.update_ui)
        else:
            print("Nessun elemento selezionato")

    def ricerca_bene(self):
        testo_ricerca = self.lineEdit.text().lower()
        beni_corrispondenti = self.controller.get_lista_nomi_da_id_o_nome(testo_ricerca)

        if beni_corrispondenti:
            self.list_model = QtCore.QStringListModel(beni_corrispondenti)
            self.listView.setModel(self.list_model)
        else:
            self.listView.setModel(None)




    def show_popup(self, n, text):
        msg = QMessageBox()
        if n == 0:
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Errore")
            msg.setText(text)
        elif n == 1:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Errore")
            msg.setText(text)
        x = msg.exec_()




def show_listabeni_dipendente(utente_attivo):
    ui = Ui_VistaListaBeniDipendente(utente_attivo)
    ui.setupUi(VistaListaBeniDipendente)
    VistaListaBeniDipendente.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaListaBeniDipendente = QtWidgets.QMainWindow()

#sys.exit(app.exec_())
