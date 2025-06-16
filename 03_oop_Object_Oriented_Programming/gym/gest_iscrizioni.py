from soci import Socio
from gestioneAttivita import Attivita
from datetime import datetime


class Iscrizioni:
    """
    Classe per gestire le iscrizioni di soci e attività.
    """
    def __init__(self):
        self.__listSoci = []
        self.__listAttivita = []

    def aggSocio(self, id, nome, cognome, data_nascita):
        """Aggiunge un nuovo socio alla lista."""
        newSocio = Socio()
        newSocio.setValori(id, nome, cognome, data_nascita)
        self.__listSoci.append(newSocio)

    def caricaSocio(self,id, nome, cognome, data_nascita, data_iscrizione):
        """Carica un socio con tutti i dati disponibili."""
        newSocio = Socio()
        newSocio.caricaValori(id, nome, cognome, data_nascita, data_iscrizione)
        self.__listSoci.append(newSocio)

    def aggAttività(self, nomeAttivita, descAttivita, giorniAtt ):
        """Aggiunge una nuova attività alla lista."""
        newAttivita = Attivita()
        newAttivita.setAttivita(nomeAttivita, descAttivita, giorniAtt)
        self.__listAttivita.append(newAttivita)

    def aggOggAtt(self, oggetto):
        self.__listAttivita.append(oggetto)

    def aggAttivitaCaricamento(self,newAttivita):
        """
        Aggiunge una nuova attivita alla listaAttivita.

        :param newAttivita: è un oggetto di tipo attivita
        """
        self.__listAttivita.append(newAttivita)

    def visualizzaSoci(self):
        """Restituisce la lista dei soci."""
        return [x for x in self.__listSoci]

    def numeroSoci(self):
        """Restituisce il numero totale di soci."""
        return len(self.__listSoci)

    def visualizzaAttivita(self):
        """Restituisce la lista delle attività."""
        return [x for x in self.__listAttivita]

    def numeroAttivita(self):
        """Restituisce il numero totale di attività."""
        return len(self.__listAttivita)

    def getListSoci(self):
        """Restituisce l'attibuto listSoci."""
        return self.__listSoci

    def getListAttivita(self):
        """Restituisce l'attributo listaAttivita"""
        return self.__listAttivita

def controlloAnno(stringa):
    """
    Controlla che l'anno sia valido (compreso tra 1930 e l'anno attuale).

    :param: è la  stringa che accetta la funzine.
    :return: ritorna il valore stringa trasformato in int
    """
    now = datetime.now()
    annoAttuale = int(now.strftime("%Y"))
    try:
        anno = int(stringa)
        if 1930 <= anno <= annoAttuale:
            return anno
    except ValueError:
            return False

def controlloMese(stringa):
    """
    Controlla che il mese inserito come stringa sia valido.

    :param: è la  stringa che accetta la funzine.
    :return: ritorna il valore stringa trasformato in int.
    """
    try:
        mese = int(stringa)
        if 1 <= mese <= 12:
            return mese
    except ValueError:
            return False

def controlloGionro(stringa, anno, mese):
    """
    Controlla che il giorno sia valido per il mese e l'anno dati.

    :param stringa:è la  stringa che accetta la funzine.
    :param anno: deve essere una quantita numerica int.
    :param mese: deve essere una quantita numerica int.
    :return: ritorna il valore stringa trasformato in int se valido.
    """
    data1 = datetime(anno, mese,1)
    meseS = int(data1.strftime("%m"))+1
    if mese != 12:
        data2 = datetime(anno, meseS,1)
    else:
        data2 = datetime(anno+1, 1, 1)
    deltaGiorni = (data2 - data1).days

    try:
        giorno = int(stringa)
        if 1 <= giorno <= deltaGiorni:
            return giorno
    except ValueError:
            return False

def inserimentoAnno(stringa):  # sistema docstring
    '''
    Valuta se la stringa inserita a video è un in intero positivo, se non lo è continua a riproporre di inserire la stringa finché è valida per la conversione

    :param stringa: stringa da testare
    :return: ritorna il valore della stringa convertito in int
    '''
    BxC = False
    while not BxC:
        Bx = input(stringa)
        BxC = controlloAnno(Bx)
        if BxC:
            Bx = int(Bx)
            return Bx

def inserimentoMese(stringa):  # sistema docstring
    '''
    Valuta se la stringa inserita a video è un in intero positivo, se non lo è continua a riproporre di inserire la stringa finché è valida per la conversione

    :param stringa: stringa da testare
    :return: ritorna il valore della stringa convertito in int
    '''
    BxC = False
    while not BxC:
        Bx = input(stringa)
        BxC = controlloMese(Bx)
        if BxC:
            Bx = int(Bx)
            return Bx

def inserimentoGiorno(stringa, anno, mese):  # sistema docstring
    '''
    Valuta se la stringa inserita a video è un in intero positivo, se non lo è continua a riproporre di inserire la stringa finché è valida per la conversione

    :param stringa: stringa da testare
    :return: ritorna il valore della stringa convertito in int
    '''
    BxC = False
    while not BxC:
        Bx = input(stringa)
        BxC = controlloGionro(Bx, anno, mese)
        if BxC:
            Bx = int(Bx)
            return Bx

def controlloId(stringa,oggetto):
    """
    Controlla che l'ID del socio sia valido.

    :param stringa: Stringa contenente il valore dell'ID da verificare.
    :param oggetto: Oggetto contenente la lista dei soci.
    :return: ID valido se presente, altrimenti False.
    """
    numSoci = oggetto.numeroSoci()
    try:
        ID = int(stringa)
        if 1 <= ID <= numSoci:
            return ID
        elif ID > numSoci:
            print("  Hai inserito un Id troppo grande ")
            return False
    except ValueError:
            return False

def inserimentoId(stringa,oggetto):  # sistema docstring
    '''
    Valuta se la stringa inserita a video è un in intero positivo, se non lo è continua a riproporre di inserire la stringa finché è valida per la conversione

    :param stringa: stringa da testare
    :return: ritorna il valore della stringa convertito in int
    '''
    BxC = False
    while not BxC:
        Bx = input(stringa)
        BxC = controlloId(Bx,oggetto)
        if BxC:
            Bx = int(Bx)
            return Bx

def controlloAtt(stringa,oggetto):
    """
    Controlla se l'attività inserita è valida.

    :param stringa: Il numero dell'attività inserito dall'utente sotto forma di stringa.
    :param oggetto: L'oggetto che contiene il numero totale delle attività.
    :return: Il numero dell'attività se è valido, altrimenti False.
    """
    numAtt = oggetto.numeroAttivita()
    try:
        att = int(stringa)
        if 1 <= att <= numAtt:
            return att
        elif att > numAtt:
            print("  Hai inserito un numero di attività troppo grende ")
            return False
    except ValueError:
            return False

def inserimentoAtt(stringa,oggetto):  # sistema docstring
    '''
    Valuta se la stringa inserita a video è un in intero positivo, se non lo è continua a riproporre di inserire la stringa finché è valida per la conversione

    :param stringa: stringa da testare
    :return: ritorna il valore della stringa convertito in int
    '''
    BxC = False
    while not BxC:
        Bx = input(stringa)
        BxC = controlloAtt(Bx,oggetto)
        if BxC:
            Bx = int(Bx)
            return Bx

def listaTodatetime(stringa):
    """
    Converte una stringa in formato data e ora in un oggetto datetime.

    :param stringa: La data e l'ora in formato stringa, separata da spazio (es. "YYYY-MM-DD HH:MM:SS").
    :return: Un oggetto datetime corrispondente alla data e ora fornite.
    """
    lista = stringa.split(" ")
    lista1 = lista[0].split("-")
    lista2 = lista[1][:8].split(":")
    listaUnione = lista1 + lista2
    return datetime(int(listaUnione[0]),int(listaUnione[1]), int(listaUnione[2]),int(listaUnione[3]),int(listaUnione[4]), int(listaUnione[5]))

def controlloSocio(oggPalestra, nome, cognome,idSocio, data_nascita):
    """
    Controlla che il socio non sia gia presente nell'oggetto palestra.

    :param oggPalestra: rappresente l'oggetto che gestiste le liste della palestra
    :type oggPalestra: oggetto di tipo Iscrizoni
    :param nome: nome socio
    :type nome: str
    :param cognome: cognome socio
    :type cognome: str
    :param idSocio: rappresenta l'id univoco di ogni socio
    :type idSocio: int
    :param data_nascita: è la data di nascita del socio
    :type data_nascita: datetime
    :return: None
    """
    ciclo = True
    listaOggSoci = oggPalestra.getListSoci()
    indice = 0
    sensore = 0
    while ciclo and indice < len(listaOggSoci):
        if nome == listaOggSoci[indice].getNome() and cognome == listaOggSoci[indice].getCognome():
            sensore += 1
            print(f"Socio {nome} {cognome} gia iscritto")
            ciclo = False
        indice += 1

    if sensore == 0:
        print(f"Iscrivo socio {nome} {cognome}")
        oggPalestra.aggSocio(idSocio, nome, cognome, data_nascita)

def controlloAttivita(oggPalestra, nomeAttivita, descrizioneAttivita, giorniSvolgimento):
    """
    Controlla che il attività non sia gia presente nell'oggetto palestra.

    :param oggPalestra: rappresente l'oggetto che gestiste le liste della palestra
    :type oggPalestra: oggetto di tipo Iscrizoni
    :param nomeAttivita: rappresenta il nome attività
    :type nomeAttivita: str
    :param descrizioneAttivita: descive l'attività
    :type descrizioneAttivita: str
    :param giorniSvolgimento: indica i giorni di svolgimento
    :type giorniSvolgimento: str
    :return: None
    """
    ciclo = True
    listaAttivita = oggPalestra.getListAttivita()
    indice = 0
    sensore = 0
    while ciclo and indice < len(listaAttivita):
        if nomeAttivita == listaAttivita[indice].getNomeAttivita():
            sensore += 1
            print(f"Attivita: {nomeAttivita} gia iscritta")
            ciclo = False
        indice += 1

    if sensore == 0:
        print(f"Iscrivo socio {nomeAttivita}")
        oggPalestra.aggAttività(nomeAttivita, descrizioneAttivita, giorniSvolgimento)