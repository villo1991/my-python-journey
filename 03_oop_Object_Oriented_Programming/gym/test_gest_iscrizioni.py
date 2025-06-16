from unittest import TestCase

from gest_iscrizioni import Iscrizioni
from datetime import datetime

from gestioneAttivita import Attivita
from soci import Socio

class TestIscrizioni(TestCase):
    def test_agg_socio(self):
        ogg = Socio()
        Id = 2
        nome = "Marco"
        cognome = "Villani"
        data_nascita = datetime(1991,8, 20)
        ogg.setValori(Id, nome, cognome, data_nascita)

        oggIsc = Iscrizioni()
        oggIsc.aggSocio(Id, nome, cognome, data_nascita)

        self.assertEquals(ogg, oggIsc, "l'oggeto creato è diverso")

    def test_carica_socio(self):
        self.fail()

    def test_agg_attività(self):
        self.fail()

    def test_visualizza_soci(self):
        self.fail()

    def test_get_list_soci(self):
        self.fail()

    def test_get_list_attivita(self):
        self.fail()
