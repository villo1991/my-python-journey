import pprint
from Cliente import Cliente

class Hotel:
    def __init__(self):
        """
        Crea una lista che accoglierà gli oggetti stanza
        """
        self.__stanze = []

    def get_num_stanze(self):
        """
        :return: ritorna il numero di stanze presenti nella lista
        """
        return len(self.__stanze)

    def aggiungi_stanza(self, stanza):
        """
        Aggunge una stanza alla lista

        :param stanza: aggiunge alla lista __stanze un oggetto che deve essere di tipo Stanza
        """
        self.__stanze.append(stanza)

    def get_ListaS(self):
        """
        :return: Ritorna l'attributo lista __stanze
        """
        return self.__stanze

    def get_stanza(self, i):
        """
        Seleziona una stanza utilizzando un indice che parte da 1 anziche da 0

        :param i: è l'indice che indica la posizione nella lista e il primo indice parte da 1
        :return: ritorna l'oggetto stanza corripondente all'indice nella lista __stanze nel oggetto Hotel
        """
        return self.__stanze[i - 1]

    def lista_iterabile(self, x):
        """
        estrae un getto dalla lista __stanze nel oggetto Hotel indicato dal paramentro

        :param x: rappresenta l'indice di selezione con il primo indiche che parte da 0
        :return: ritorna l'oggetto che appartiene all'indice
        """
        lista = self.get_ListaS()
        oggetto = lista[x]
        return oggetto


def salvaCliente(utente, listaUtenti):  #vecchia funzione di salvataggio
    """
    la funzione ha lo scopo di aggiungere un utente, che è rappresentato da una lista [nome, cognome], alla lista di liste salvata sul file dataBaseClienti.py

    :param utente: è rappresentato da una lista [nome, cognome]
    :param listaUtenti: rappresenta da una lista di liste che raccoglie tutti gli utenti rappresentati con una lista [nome, cognome]
    :return:
    """
    scrittura = open("dataBaseClienti.py", "w")
    listaUtenti.append(utente)
    scrittura.write("listaClienti = ")
    scrittura.write(pprint.pformat(listaUtenti))
    scrittura.close()


def aggiornaOggHotel(cliente, numeroStanze, listaOggetti, h1):
    """
    La funzione ha lo scopo di aggiornare l'oggetto Stanza contenuto nel oggetto Hotel, facendo scegliere le sole stanze libere/ disponibili

    :param cliente: deve essere un oggetto Cliente
    :param numeroStanze: indica il numero di stanze presenti nella struttura
    :param listaOggetti: rappresenta la lista di oggetti Stanza presenti nell'oggetto Hotel
    :param h1: rappresenta l'oggetto Hotel
    """
    controlloSelezione = []
    for x in range(numeroStanze):
        if listaOggetti[x].get_cliente() is None:
            print(f"{x + 1} - {listaOggetti[x]} ")
            controlloSelezione.append(x + 1)
    print()
    if len(controlloSelezione) != 0:
        esegui = True
        while esegui:
            sceltaStanza = inserimento_intero("scegli una stanza tra quelle proposte  ")
            if sceltaStanza in controlloSelezione:
                prenotaStanza = h1.get_stanza(sceltaStanza)
                prenotaStanza.set_cliente(cliente)
                esegui = False
    else:
        print("Non ci sono camere libere")


def aggiornaPrenotazionePerCliente(numeroStanze, listaOggetti,nome, cognome, h1):
    """
    La funzione ha lo scopo di aggiornare l'oggetto Stanza contenuto nel oggetto Hotel, facendo scegliere le sole stanze prenotate da un preciso cliente

    :param numeroStanze: indica il numero di stanze presenti nella struttura
    :param listaOggetti: rappresenta la lista di oggetti Stanza presenti nell'oggetto Hotel
    :param nome: indica il nome del cliente da cercare
    :param cognome: indica il cognome del cliente da cercare
    :param h1: rappresenta l'oggetto Hotel
    """
    controlloSelezione = []
    for x in range(numeroStanze):
        if listaOggetti[x].get_cliente() is not None:
            if listaOggetti[x].get_cliente().get_nome() == nome and listaOggetti[x].get_cliente().get_cognome() == cognome:
                print(f"{x + 1} - {listaOggetti[x]} ")
                controlloSelezione.append(x + 1)
    print()
    if len(controlloSelezione) != 0:
        esegui = True
        while esegui:
            sceltaStanza = inserimento_intero("scegli una stanza tra quelle proposte  ")
            if sceltaStanza in controlloSelezione:
                prenotaStanza = h1.get_stanza(sceltaStanza)
                opzione = input(f"""
                        Premi 1 per annullare la prenotazione del cliente {nome} - {cognome} per la stanza numero {sceltaStanza}
                        premi 2 per assegnare un nuovo cliente alla stanza numero {sceltaStanza}
                        premi 3 per annullare la modifica
                        """)
                if opzione == "1":
                    annulla = None
                    prenotaStanza.set_cliente(annulla)
                    esegui = False
                elif opzione == "2":
                    newName = input('Inserisci il nome del nuovo cliente:  ').lower().strip()
                    NewSurename = input('Inserisci il cognome del nuovo cliente:  ').lower().strip()
                    cliente = Cliente(newName,NewSurename)
                    h1.get_stanza(sceltaStanza).set_cliente(cliente)
                    esegui = False
                elif opzione == "3":
                    esegui = False
    else:
        print(f"Non ci sono prenotazioni attive per il cliente {nome} - {cognome}")

def aggiornaPrenotazionePerStanza(numeroStanze, listaOggetti, h1):
    """
    La funzione ha lo scopo di aggiornare l'oggetto Stanza contenuto nel oggetto Hotel, facendo scegliere le sole stanze prenotate

    :param numeroStanze: indica il numero di stanze presenti nella struttura
    :param listaOggetti: rappresenta la lista di oggetti Stanza presenti nell'oggetto Hotel
    :param h1: rappresenta l'oggetto Hotel
    """
    controlloSelezione = []
    for x in range(numeroStanze):
        if listaOggetti[x].get_cliente() is not None:
            print(f"{x + 1} - {listaOggetti[x]} - {listaOggetti[x].get_cliente()} ")
            controlloSelezione.append(x + 1)
    print()
    if len(controlloSelezione) != 0:
        esegui = True
        while esegui:
            sceltaStanza = inserimento_intero("scegli una stanza tra quelle proposte  ")
            if sceltaStanza in controlloSelezione:
                prenotaStanza = h1.get_stanza(sceltaStanza)
                opzione = input(f"""
                         Premi 1 per annullare la prenotazione della stanza numero {sceltaStanza}
                         premi 2 per assegnare un nuovo cliente alla stanza numero {sceltaStanza}
                         premi 3 per annullare la modifica
                                        """)
                if opzione == "1":
                    annulla = None
                    prenotaStanza.set_cliente(annulla)
                    esegui = False
                elif opzione == "2":
                    newName = input('Inserisci il nome del nuovo cliente:  ').lower().strip()
                    NewSurename = input('Inserisci il cognome del nuovo cliente:  ').lower().strip()
                    cliente = Cliente(newName, NewSurename)
                    h1.get_stanza(sceltaStanza).set_cliente(cliente)
                    esegui = False
                elif opzione == "3":
                    esegui = False
    else:
        print(f"Non ci sono prenotazioni attive per nessuna stanza")

""" # ho commentato per lasciarla da esempio 
def verifica_int_positivo(stringa):
    '''
	verifica che la stringa inserita sia un numero intero positivo maggore di zero

	:param stringa: è il valore stringa da confrontare
	:return: ritorna False se incontra come primo carattere qualsiasi carattere che non sia un numero o un +, mentre ritorna True se c'e al massimo un + come primo cattere e gli altri catteri sono solo cifre numeriche
    '''
    stato = 0
    for c in stringa:
        if (stato == 0):
            if (c == "0"):
                stato = 3
                return False
            elif (c.isdigit()):
                stato = 1
            elif (c in {'+'}):
                stato = 2
            else:
                stato = 3
                return False
        elif (stato == 1):
            if (c.isdigit()):
                stato = 1
            else:
                stato = 3
                return False
        elif (stato == 2):
            if (c.isdigit()):
                stato = 1
            else:
                stato = 3
                return False

    return bool(stato == 1)
"""

def inserimento_intero(stringa):
    '''
    Valuta se la stringa inserita a video è un in intero positivo, se non lo è continua a riproporre di inserire la stringa finché è valida per la conversione

    :param stringa: stringa da testare
    :return: ritorna il valore della stringa convertito in int
    '''
    BxC = False
    while not BxC:
        Bx = input(stringa)
        BxC = verifica_int_positivo(Bx)
        if BxC:
            Bx = int(Bx)
            return Bx

def salvaClienteCsv(utente, file):
    """
    Salva i dati utente nel database CSV

    :param utente: indica i dati dell'utente da salvare
    :param file: indica in quale file salvare
    :return:
    """
    fW = open(file, "a")
    fW.write("\n")
    fW.write(utente)
    fW.close()

def cancellaClienteCsv(utente, file, f): #f è l'oggetto file in lettura per prelevare i dati
    """
    Cancella un utente dal file CSV riscrivendolo e tralasciando la riga dell'utente

    :param utente: utente che deve essere eliminato
    :param file: sarebbe il file database CSV che vine riscritto
    :param f: sarebbe il file database CSV che viene aperto in modalita lettuta esternamente
    """
    listaE = ["Nome;Cognome"]
    f.seek(0)
    ciclo = True
    while ciclo:
        testo = f.readline()
        if utente != testo.strip() :
            listaE.append(testo)
        if testo == "":
            ciclo = False
    f.close()
    fW = open(file, "w")
    for x in range(1,len(listaE)):
        fW.write(listaE[x])
    fW.close()

def verifica_int_positivo(stringa):
    '''
	verifica che la stringa inserita sia un numero intero positivo maggore di zero

	:param stringa: è il valore stringa da confrontare
	:return: ritorna True solo se si inserisce un numero intero positivo maggiore di zero
    '''
    try:
        numStinga = int(stringa)
        if numStinga>0:
            return True
    except ValueError:
        return False
