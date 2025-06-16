#dizDescAttivita = {"sumo" : {"desc": "buttare fuori in nemico dal ring", "giorni": "L,MA,ME,G,V,S,D"}}
#dizDescAttivita[self.__nomeAttivita].get("desc", "attività da inseite nel data base")
#dizDescAttivita[self.__nomeAttivita].get("giorni", "attività da inseite nel data base")

class Attivita:
    """
    Classe che rappresenta un'attività con nome, descrizione, giorni di svolgimento e iscritti.
    """
    def __init__(self):
        """
        Inizializza un oggetto Attivita con valori predefiniti.
        Il nome, la descrizione e i giorni dell'attività sono inizializzati a None.
        La lista degli iscritti è inizialmente vuota.
        """
        self.__nomeAttivita = None
        self.__descAttivita = None
        self.__giorniAtt = None
        self.__iscritti = []

    def setAttivita(self,nomeAttivita, descAttivita, giorniAtt):
        """
        Imposta i valori dell'attività.

        :param nomeAttivita: Nome dell'attività.
        :param descAttivita: Descrizione dell'attività.
        :param giorniAtt: Giorni in cui si svolge l'attività.
        """
        self.__nomeAttivita = nomeAttivita
        self.__descAttivita = descAttivita
        self.__giorniAtt = giorniAtt

    def getNomeAttivita(self):
        """
        Restituisce il nome dell'attività.

        :return: Nome dell'attività.
        """
        return self.__nomeAttivita

    def getDescAttivita(self):
        """
        Restituisce la descrizione dell'attività.

        :return: Descrizione dell'attività.
        """
        return self.__descAttivita

    def getGiorniAttivita(self):
        """
        Restituisce i giorni in cui si svolge l'attività.

        :return: Giorni dell'attività.
        """
        return self.__giorniAtt

    def getIscitti(self):
        """
        Restituisce la lista degli iscritti all'attività.

        :return: Lista degli iscritti.
        """
        return self.__iscritti

    def iscriviSocio(self, iscritto):
        """
        Aggiunge un socio alla lista degli iscritti all'attività.

        :param iscritto: Nome del socio da iscrivere.
        """
        self.__iscritti.append(iscritto)

    def visualizzaPartecipanti(self):
        """
        Restituisce una lista dei partecipanti iscritti all'attività.

        :return: Lista dei partecipanti.
        """
        return [partecipante for partecipante in self.__iscritti]

    def visualizzaDatiAtt(self):
        """
        Restituisce una stringa con i dati principali dell'attività.

        :return: Stringa contenente nome, descrizione e giorni dell'attività.
        """
        return f"Nome attività: {self.__nomeAttivita} - Descrizone: {self.__descAttivita} - Giorni:{self.__giorniAtt}"

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa dell'oggetto Attivita, includendo gli iscritti.

        :return: Stringa contenente nome, descrizione, giorni e iscritti all'attività.
        """
        return f"""Nome attività: {self.__nomeAttivita} - Descrizone: {self.__descAttivita} - Giorni:{self.__giorniAtt}
               {[x for x in self.__iscritti]}"""


