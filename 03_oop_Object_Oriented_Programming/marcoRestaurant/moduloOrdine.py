from moduloPiatto import Piatto
from datetime import datetime


class GestoreOrdini():
    """
    Classe per gestire gli ordini di un ristorante.
    """
    def __init__(self):
        """
        Inizializza una lista vuota di ordini
        """
        self.listaOrdini = []

    def aggOrdine(self, oggOrdine):
        """
        Aggiunge un ordine alla lista.

        :param oggOrdine: Oggetto di tipo Ordine da aggiungere alla lista.
        """
        self.listaOrdini.append(oggOrdine)

    def visualizzaOrdini(self):
        """
        Aggiunge un ordine alla lista.

        :param oggOrdine: Oggetto di tipo Ordine da aggiungere alla lista.
        """
        for x in self.listaOrdini:
            print(x)
            x.visualizzaPiatti()

    def visualizzaListaOrdini(self):
        """
        Restituisce la lista degli ordini.

        :return: Lista degli ordini.
        """
        return self.listaOrdini


class Ordine():
    """
    Classe che rappresenta un ordine effettuato da un tavolo.
    """
    def __init__(self, IdTavolo):
        """
        Inizializza un nuovo ordine.

        :param IdTavolo: Identificativo numerico del tavolo.
        """
        self.__idTavolo = IdTavolo
        self.__piatti = []
        self.__pagamento = False
        self.__numeroOrdine = datetime.now()

    def assegnaPagamento(self):
        """
        Imposta lo stato dell'ordine come pagato.
        """
        self.__pagamento = True

    def setPagamento(self, valore):
        """
        Imposta manualmente lo stato di pagamento.

        :param valore: Booleano che indica se l'ordine è pagato o meno.
        """
        self.__pagamento = valore

    def numeroOrdine(self, valore):
        """
        Imposta manualmente la data e ora dell'ordine.

        :param valore: Oggetto datetime rappresentante la data e ora.
        """
        self.__numeroOrdine = valore

    def aggPiatto(self, piatto):
        """
        Aggiunge un piatto all'ordine.

        :param piatto: Oggetto di tipo Piatto da aggiungere all'ordine.
        """
        self.__piatti.append(piatto)

    def eliminaPiatto(self, numero):
        """
        Elimina un piatto dall'ordine dato il suo indice.

        :param numero: Indice del piatto da rimuovere.
        """
        del self.__piatti[numero]

    def printLista(self):
        """
        Restituisce la lista dei piatti ordinati.

        :return: Lista di oggetti Piatto.
        """
        return self.__piatti

    def visualizzaPiatti(self):
        """
        Stampa l'elenco dei piatti nell'ordine.
        """
        for c in range(len(self.__piatti)):
            print(f"{c} : {self.__piatti[c]} ")

    def visualizzaId(self):
        """
        Restituisce l'identificativo del tavolo.

        :return: Identificativo numerico del tavolo.
        """
        return self.__idTavolo

    def visualizzaPagamento(self):
        """
        Restituisce lo stato del pagamento dell'ordine.

        :return: Booleano che indica se l'ordine è stato pagato.
        """
        return self.__pagamento

    def getDayOrder(self):
        """
        Restituisce la data dell'ordine in formato stringa (YYYY-MM-DD).

        :return: Stringa rappresentante la data dell'ordine.
        """
        return self.__numeroOrdine.strftime("%Y-%m-%d")

    def getDateTime(self):
        """
        Restituisce la data e ora completa dell'ordine.

        :return: Oggetto datetime dell'ordine.
        """
        return self.__numeroOrdine

    def totaleOrdine(self):
        """
        Calcola il totale dell'ordine sommando i prezzi dei piatti.

        :return: Totale dell'ordine come float.
        """
        prezzo =0
        for x in self.__piatti:
            prezzo += x.getPrezzo()
        return prezzo

    def printOrder(self):
        """
        Stampa i dettagli dell'ordine.
        """
        print(f"""id tavolo {self.__idTavolo} - pagamento {self.__pagamento}""")
        for x in self.__piatti:
            print(x)

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa dell'ordine.

        :return: Stringa con id tavolo e stato del pagamento.
        """
        return f"""id tavolo {self.__idTavolo} - pagamento {self.__pagamento}"""


def tavolo():
    """
    Chiede all'utente di inserire un numero di tavolo compreso tra 1 e 10.

    :return : Numero del tavolo scelto dall'utente.
    """
    ciclo = True
    while ciclo:
        try:
            numero = int(input("inserisci il numero del tavolo compreso da 1 a 10  "))
            if 1 <= numero <= 10:
                ciclo = False
                return numero
            else:
                print(f"Il numero inserito {numero} non rappresenta un tavolo presente")
        except ValueError:
            print("Hai inserito una stringa non convertibile in intero")


def scegliPiattoOrdine(sceltaTavolo, oggOrdine):
    """
    Permette all'utente di selezionare un piatto dal tavolo per eliminarlo dall'ordine.

    :param sceltaTavolo: Numero del tavolo per cui si sta modificando l'ordine.
    :type sceltaTavolo: int
    :param oggOrdine: Oggetto che gestisce l'ordine, contenente la lista dei piatti ordinati.
    :type oggOrdine: Ordine
    :return: Numero del piatto da eliminare se valido, altrimenti False se l'utente esce.
    :rtype: int or bool
    """
    ciclo1 = True
    while ciclo1:
        try:
            numero = input(f"Piatti ordinati dal tavolo {sceltaTavolo}, selezione il numero corrispondente per eliminare il piatto o digita 'exit' per uscire ")
            if numero == "exit":
                return False
            numero = int(numero)
            if 0 <= numero <= len(oggOrdine.printLista()):
                ciclo1 = False
                return numero
            else:
                print(f"Il numero inserito {numero} non rappresenta un piatto presente")
        except ValueError:
            print("Hai inserito una stringa non convertibile in intero")


def inserisciPiatto(oggMenu, oggOrdine ):
    """
    Permette all'utente di inserire un piatto nell'ordine, selezionandolo da un menu.

    :param oggMenu: Oggetto che gestisce il menu dei piatti disponibili.
    :type oggMenu: Menu
    :param oggOrdine: Oggetto che gestisce l'ordine e la lista dei piatti ordinati.
    :type oggOrdine: Ordine
    :return: True se l'utente ha concluso l'ordinazione, False se non ci sono corrispondenze.
    :rtype: bool
    """
    fileMenu = open("menu.csv", "r")
    ciclo1 = True
    while ciclo1:
        try:
            numero = int(input(f"inserisci id del piatto compreso da 1 a {oggMenu.numeroPiatti()} se premi 0 esci dall'ordinazione\n"))
            if numero == 0:
                fileMenu.close()
                return True
            elif 1 <= numero <= oggMenu.numeroPiatti():
                sensore = 0
                loop = True
                fileMenu.seek(0)
                fileMenu.readline()
                while loop:
                    riga = fileMenu.readline()
                    listaRiga = riga.strip().split(";")
                    if int(listaRiga[0]) == numero:
                        sensore += 1
                        nome = listaRiga[1]
                        prezzo = float(listaRiga[2])
                        piatto = Piatto(numero, nome, prezzo)
                        oggOrdine.aggPiatto(piatto)
                        loop = False
                    elif riga =="":
                        loop = False
                if sensore == 0:
                    print("nessuna corrispondenza ")  # solo per controllo
                    fileMenu.close()
            else:
                print(f"Il numero inserito {numero} non rappresenta un piatto presente")
        except ValueError:
            print("Hai inserito una stringa non convertibile in intero")


def salvaOrdinToCSV(ogg):
    """
    Salva gli ordini correnti in un file CSV chiamato "databaseOrdini.csv".

    :param ogg: Oggetto che gestisce gli ordini da salvare nel file.
    :type ogg: GestoreOrdini
    :return: None
    :rtype: None
    """
    leggiOrdini = open("databaseOrdini.csv", "r")
    riga = leggiOrdini.readline()
    if riga == "":
        fileOrdini = open("databaseOrdini.csv", "w")
        fileOrdini.write("idTavolo;listaPiatti;pagamento;numeroOrdine(datetime)\n")
        fileOrdini.close()
    fileOrdini = open("databaseOrdini.csv", "a")
    for x in ogg.visualizzaListaOrdini():
        fileOrdini.write(f"{x.visualizzaId()};")
        for c in x.printLista():
            fileOrdini.write(f"{c.getId()}-")
            fileOrdini.write(f"{c.getNome()}-")
            fileOrdini.write(f"{c.getPrezzo()}-")
        fileOrdini.write(f";{x.visualizzaPagamento()};")
        fileOrdini.write(f"{x.getDateTime()}\n")
    fileOrdini.close()


def caricaDati(oggGestore):
    """
    Carica gli ordini salvati nel file CSV "databaseOrdini.csv" e li inserisce nell'oggetto GestoreOrdini.

    :param oggGestore: Oggetto che gestisce la lista degli ordini.
    :type oggGestore: GestoreOrdini
    :return: None
    :rtype: None
    """
    leggiOrdini = open("databaseOrdini.csv", "r")
    if not leggiOrdini.readline():
        print("File databaseOrdini.csv è vuolto")
        leggiOrdini.close()
    else:
        leggiOrdini.seek(0)
        leggiOrdini.readline()
        for riga in leggiOrdini:
            lRiga = riga.strip().split(";")
            idTavolo = int(lRiga[0])
            oggOrdi = Ordine(idTavolo)
            listaPiatti = lRiga[1][:-1].split("-")
            listaDiListe = []
            for x in range(0, len(listaPiatti), 3):
                newLista = []
                newLista.append(listaPiatti[0 + x])
                newLista.append(listaPiatti[1 + x])
                newLista.append(listaPiatti[2 + x])
                listaDiListe.append(newLista)

            for x in listaDiListe:
                idPiatto = int(x[0])
                descrizioneP = x[1]
                prezzoPiatto = float(x[2])
                oggPiatto = Piatto(idPiatto, descrizioneP, prezzoPiatto)
                oggOrdi.aggPiatto(oggPiatto)
            statoPagamento = lRiga[2]
            if statoPagamento == "False":
                statoPagamento = False
            else:
                statoPagamento = True
            oggOrdi.setPagamento(statoPagamento)
            tempoDateTime = listaTodatetime(lRiga[3])
            oggOrdi.numeroOrdine(tempoDateTime)
            oggGestore.aggOrdine(oggOrdi)
            oggGestore.visualizzaListaOrdini()
        print("File caricato corretamente")
        leggiOrdini.close()

def listaTodatetime(stringa):
    """
    Converte una stringa in formato data e ora in un oggetto datetime.

    :param stringa: La data e l'ora in formato stringa, separata da spazio (es. "YYYY-MM-DD HH:MM:SS").
    :return: Un oggetto datetime corrispondente alla data e ora fornite.
    """
    lista = stringa.split(" ")
    lista1 = lista[0].split("-")
    lista2 = lista[1][:8].split(":")
    lista3 = list(lista[1][9:])
    listaUnione = lista1 + lista2 + lista3
    return datetime(int(listaUnione[0]),int(listaUnione[1]), int(listaUnione[2]),int(listaUnione[3]),int(listaUnione[4]), int(listaUnione[5]), int(listaUnione[6]))