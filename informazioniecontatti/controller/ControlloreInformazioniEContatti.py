from informazioniecontatti.model.InformazioniEContatti import *
import pickle
import os


class ControlloreInformazioniEContatti:

    def __init__(self):
        super(ControlloreInformazioniEContatti, self).__init__()
        self.model = InformazioniEContatti()
        if os.path.isfile('informazioniecontatti/data/informazioni_salvate.pickle'):
            with open('informazioniecontatti/data/informazioni_salvate.pickle', 'rb') as f:
                informazioni_salvate = pickle.load(f)
            self.model.aggiorna_informazioni(informazioni_salvate)

        with open('informazioniecontatti/data/informazioni_salvate.pickle', 'wb') as f:
            pickle.dump(self.model.informazioni, f)

        if os.path.isfile('informazioniecontatti/data/contatti_salvati.pickle'):
            with open('informazioniecontatti/data/contatti_salvati.pickle', 'rb') as f:
                contatti_salvati = pickle.load(f)
            self.model.aggiorna_contatti(contatti_salvati)

        with open('informazioniecontatti/data/contatti_salvati.pickle', 'wb') as f:
            pickle.dump(self.model.contatti, f)

    def get_informazioni(self):
        return self.model.get_informazioni()

    def get_contatti(self):
        print("x")
        return self.model.get_contatti()

    def aggiorna_informazioni(self, informazioni_aggiornate):
        with open('informazioniecontatti/data/informazioni_salvate.pickle', 'wb') as f:
            pickle.dump(informazioni_aggiornate, f)

    def aggiorna_contatti(self, contatti_aggiornati):
        with open('informazioniecontatti/data/contatti_salvati.pickle', 'wb') as f:
            pickle.dump(contatti_aggiornati, f)
