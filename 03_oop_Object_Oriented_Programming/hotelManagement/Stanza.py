str_optional = ["minibar", "aria condizionata", "televisione"]
prz_optional = [10.00, 13.00, 19.00]

str_costi = ["singola", "matrimoniale", "suite"]
prz_costi = [10.00, 20.00, 30.00]


class Stanza:
    def __init__(self, tipo, optional):
        """
        inizializza l'oggetto Stanza assegnandoli due parametri variabili e uno fisso definito dall'attributo cliente

        :param tipo: deve essere un numero int che indica l'indice della lista prz_costi
        :param optional: deve essere un numero int che indica l'indice della lista prz_optional
        """
        self.__tipo = tipo
        self.__cliente = None
        self.__optional = optional

    def get_cliente(self):
        """
        :return: ritorna il cliente assegnato all'oggetto stanza
        """
        return self.__cliente

    def set_cliente(self, c):
        """
        Assegna un valore all'attributo __cliente

        :param c:  deve essere un oggetto Cliente altrimenti il programma non funziona
        """
        self.__cliente = c

    def get_tipo(self):
        """
        :return: ritorna il membro tipo dell'oggetto Stanza
        """
        return self.__tipo

    def aggiungi_optional(self, i):
        """
        aggunge al parametro __optional un optional

        :param i: deve essere un numero int che rappresenta un indice degli optional indicati nella lista
        """
        self.__optional.add(i)

    def get_prezzo(self):
        """
        Calcola il prezzo giornaliero per la stanza

        :return: ritorna il prezzo totale considerando gli optional
        """
        totale = prz_costi[self.__tipo]
        for ind_prz in self.__optional:
            totale += prz_optional[ind_prz]
        return totale

    def __str__(self):
        """
        :return: Ritorna una lista formattata con tutti i dati necessari per definire lo stato di una stanza
        """
        s1 = f"stanza - tipo:{str_costi[self.__tipo]}, disponibile:{self.__cliente is None}, optional:"
        s2 = f"{[str_optional[i] for i in self.__optional]}, prezzo:{self.get_prezzo()}"
        return s1 + s2
