import os.path
import pickle

from Test.test_prenotazioni.DatabaseEntry import *


class DatabasePrenotazioni:
    def __init__(self):
        super(DatabasePrenotazioni, self).__init__()
        self.database_prenotazioni = []

    def aggiungi_data_prenotabile(self, date, attivita, num):
        new_database_entry = DataBaseEntry(date, attivita, num)
        self.database_prenotazioni.append(new_database_entry)
        self.save_data()
        print('data aggiunta')

    def elimina_data_prenotabile(self, data):
        for database_entry in self.database_prenotazioni:
            if database_entry is data:
                self.database_prenotazioni.remove(database_entry)
                self.save_data()

    def visualizza_posti_disponibili(self, attivita):
        for data_prenotabile in self.database_prenotazioni:
            if data_prenotabile.attivita is attivita:
                n_posti = data_prenotabile.n_massimo - data_prenotabile.get_numero_posti_prenotati
                if n_posti > 0:
                    return n_posti
                else:
                    return False

    def visualizza_lista_prenotazioni_per_email(self, email_utente):
        lista_prenotazioni_per_email = []
        for entry in self.get_database_prenotazioni():
            print("ciao")
            lista_email = entry.matrice_clienti[0]
            for email in lista_email:
                if email == email_utente:
                    index = lista_email.index(email)
                    lista_prenotazioni_per_email.append(entry.data.strftime("%d - %m -  %Y") +
                                                        "    " +
                                                        entry.matrice_clienti[1][index] +
                                                        "  " +
                                                        entry.matrice_clienti[2][index] +
                                                        "    " +
                                                        entry.attivita.titolo)
        print(lista_prenotazioni_per_email)
        return lista_prenotazioni_per_email

    def return_last_date(self):
        database = self.get_database_prenotazioni()
        return database[-1].data

    def get_database_prenotazioni(self):
        if os.path.isfile('Test/test_prenotazioni/lista_prenotazioni_salvata.pickle'):
            with open('Test/test_prenotazioni/lista_prenotazioni_salvata.pickle', 'rb') as f:
                self.database_prenotazioni = pickle.load(f)
        return self.database_prenotazioni

    def get_date_per_attivita(self, attivita_selezionata):
        database = self.get_database_prenotazioni()
        lista_date_per_attivita = []
        for entry in database:
            if (entry.attivita.titolo == attivita_selezionata and
                    entry.get_numero_posti_prenotati() < entry.attivita.n_posti):
                lista_date_per_attivita.append(entry.data)
        return lista_date_per_attivita

    def save_data(self):
        with open('Test/test_prenotazioni/lista_prenotazioni_salvata.pickle', 'wb') as f:
            pickle.dump(self.database_prenotazioni, f)
