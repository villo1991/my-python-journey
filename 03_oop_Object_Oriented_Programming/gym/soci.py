from datetime import datetime

class Socio:
    """
    Classe che rappresenta un socio, con informazioni personali e di iscrizione.
    """
    def __init__(self):
        """
        Inizializza un oggetto Socio con valori predefiniti.
        L'ID, il nome, il cognome e la data di nascita sono inizializzati a None.
        La data di iscrizione è impostata al momento della creazione dell'istanza.
        """
        self.__id = None
        self.__nome = None
        self.__cognome = None
        self.__data_nascita = None  #quando verrà inserita usremo un datetime per avere un indicatore su cui operare
        self.__data_iscrizione = datetime.now()

    def setValori(self, id, nome, cognome, data_nascita):
        """
        Imposta i valori del socio.

        :param id: Identificativo univoco del socio.
        :param nome: Nome del socio.
        :param cognome: Cognome del socio.
        :param data_nascita: Data di nascita del socio (tipo datetime).
        """
        self.__id = id
        self.__nome = nome
        self.__cognome = cognome
        self.__data_nascita = data_nascita

    def caricaValori(self, id, nome, cognome, data_nascita, data_iscrizione):
        """
        Carica tutti i valori del socio, inclusa la data di iscrizione.

        :param id: Identificativo univoco del socio.
        :param nome: Nome del socio.
        :param cognome: Cognome del socio.
        :param data_nascita: Data di nascita del socio (tipo datetime).
        :param data_iscrizione: Data di iscrizione del socio (tipo datetime).
        """
        self.__id = id
        self.__nome = nome
        self.__cognome = cognome
        self.__data_nascita = data_nascita
        self.__data_iscrizione = data_iscrizione

    def getId(self):
        """
        Restituisce l'ID del socio.

        :return: ID del socio.
        """
        return self.__id

    def getNome(self):
        """
        Restituisce il nome del socio.

        :return:Nome del socio.
        """
        return self.__nome

    def getCognome(self):
        """
        Restituisce il cognome del socio

        :return: Cognome del socio.
        """
        return self.__cognome

    def getDataNascita(self):
        """
        Restituisce la data di nascita del socio.

        :return: Data di nascita del socio (tipo datetime).
        """
        return self.__data_nascita

    def getDataIscrizione(self):
        """
        Restituisce la data di iscrizione del socio.

        :return: Data di iscrizione del socio (tipo datetime).
        """
        return self.__data_iscrizione

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa dell'oggetto Socio.

        :return: Stringa contenente i dati del socio.
        """
        return (f""" dati socio: {self.__nome} - {self.__cognome}.
        id: {self.__id} - data nascita: {self.__data_nascita.strftime("%d-%m-%Y")} - data iscrizione: {self.__data_iscrizione.strftime("%d-%m-%Y")}""")

    