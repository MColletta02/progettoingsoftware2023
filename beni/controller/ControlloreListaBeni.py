from beni.model.ListaBeni import *
import pickle
import os


class ControlloreListaBeni:
    def __init__(self):
        super(ControlloreListaBeni, self).__init__()
        self.model = ListaBeni()
        if os.path.isfile('beni/data/lista_beni_salvata.pickle') and os.path.getsize('beni/data/lista_beni_salvata.pickle') > 0:
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as f:
                lista_beni_salvata = pickle.load(f)
                if not self.model.lista_beni:  # Verifica se la lista è vuota
                    self.model.lista_beni = lista_beni_salvata


    def inserisci_bene(self, bene):
        if self.model.aggiungi_bene(bene):
            with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
                pickle.dump(self.model.lista_beni, f)
        self.model.print_lista_beni()

    def elimina_bene(self, bene):
        self.model.elimina_bene(bene)
        with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_beni, f)

    def cerca_bene_per_id(self, id_bene):
        for b in self.model.get_lista_beni():
            if b.id_bene == id_bene:
                return b
        return None

    def cerca_bene_per_nome(self, nome):
        for b in self.model.get_lista_beni():
            if b.nome == nome:
                return b
        return None

    def controlla_nome(self, nome):
        for b in self.model.get_lista_beni():
            if b.nome == nome:
                return False

        return True

    def get_lista_nomi_beni(self):
        self.model.print_lista_beni()
        return self.model.get_lista_nomi_beni()

    def get_lista_beni(self):
        return self.model.get_lista_beni()

    def aggiorna_bene(self, nome_vecchio, nome, immagine, area, descrizione, stato, stato_area, data_di_aggiunta):
        self.model.aggiorna_bene(nome_vecchio, nome, immagine, area, descrizione, stato, stato_area, data_di_aggiunta)
        #self.inserisci_bene(bene)
        #self.elimina_bene(bene_vecchio)
        #with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            #pickle.dump(self.model.lista_beni, f)

    def get_lista_nomi_da_id_o_nome(self,nome_o_id):
        beni_corrispondenti = []

        for bene in sorted(self.get_lista_beni(), key=lambda x: x.id_bene):
            nome_bene = bene.nome.lower()
            id_bene = str(bene.id_bene).lower()

            if nome_o_id in nome_bene or nome_o_id in id_bene:
                beni_corrispondenti.append(bene.nome)
        return beni_corrispondenti


    def get_lista_nomi_per_area(self, area_selezionata):
        if area_selezionata.lower() == "tutte":
            #lista_beni = self.get_lista_beni()
            #sorted(lista_beni, key=lambda x: x.id_bene)
            return [bene.nome for bene in sorted(self.get_lista_beni(), key=lambda x: x.id_bene)]
        beni_per_area = []
        for bene in  sorted(self.get_lista_beni(), key=lambda x: x.id_bene):
            if bene.area == area_selezionata:
                beni_per_area.append(bene.nome)
        return beni_per_area

    def crea_id_bene(self):
        id_bene = len(self.model.lista_beni) + 1
        return id_bene

    def ottieni_path_immagine_bene(self,nome):
        bene = self.cerca_bene_per_nome(nome)
        if bene:
            return bene.immagine
        return None

    def get_bene_by_index(self, index):
        return self.model.get_bene_by_index(index)



    def ottieni_beni_da_file(self):
        try:
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as file:
                beni = pickle.load(file)
                return beni
        except (FileNotFoundError, EOFError):
            return []

    #def filtra_per_stato(self, stato):
        #for b in self.model.get.lista_beni():

