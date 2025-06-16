from Cliente import Cliente
from Stanza import Stanza
from Hotel import *
from datetime import datetime

uscita = False

fileClienti = "dataBaseClienti.csv"
h1 = Hotel()
dataStanze = open("dataBaseStanze.csv", "r")
dataStanze.readline()
ciclo = True
while ciclo:
    riga = dataStanze.readline()
    if riga != "":  # credo che si possa eliminare il != perchè quando riga = "" è gia False, giusto?
        lR = riga.split(";")
        lR0 = int(lR[0])
        lR1 = lR[1].split(",")
        lR2 = set()
        for x in lR1:
            newX = x.strip()
            if newX != "":
                lR2.add(int(newX))
        ST = Stanza(lR0, lR2)
        h1.aggiungi_stanza(ST)
    else:
        ciclo = False
numeroStanze = h1.get_num_stanze()
listaOggetti = h1.get_ListaS()

while not uscita:
    choose = input('''
                premi: 
                1_ per inserimento e rimozione clienti dall'archivio
                2_ per nuova prenotazione
                3_ per modifica/rimozione prenotazione già esistente
                4_ per visualizzare l'elenco delle sole camere disponibili
                5_ per salvataggio dell'intero archivio su file ( Salvataggio dei dati dell'oggetto Hotel)
                6_ per caricamento dell'intero archivio su file
                7_ per visualizzare il conto per una determinata stanza
                8_ per uscire

            ''')
    if choose == '1':
        ciclo = True
        while ciclo:
            print(' Inserisci il nome e il cognome del cliente')
            nome = input('Inserisci il nome :  ').lower().strip()
            cognome = input('Inserisci il cognome :  ').lower().strip()
            utente = nome + ";" + cognome
            ciclo = len(nome) == 0 or len(cognome) == 0 or ";" in nome or ";" in cognome

        sensore = 0
        f = open(fileClienti, "r")
        f.seek(0)
        riga = f.readline()
        if len(riga) != 0:
            f.seek(0)
            f.readline()
            uscita1 = False
            while not uscita1:
                riga = f.readline()
                lR = riga.split(";")
                if riga != "":
                    ricNome = lR[0].lower()
                    ricCognome = lR[1].lower().strip()
                if riga == "":
                    uscita1 = True
                elif nome == ricNome and cognome == ricCognome:
                    sensore += 1
                    scelta = input(
                        "Cliente già presente. Vuoi cancellare il cliente? Premi yes per procedere con l'eliminazione   ").lower()
                    if scelta == 'yes':
                        cancellaClienteCsv(utente, fileClienti, f)
            if sensore == 0:
                print(f"Aggiungo il cliente {nome} - {cognome}")
                salvaClienteCsv(utente, fileClienti)
                f.close()

        else:
            print("Test1")
            fW = open("dataBaseClienti.csv", "a")#non so se farlo che compila la prima riga con le intestazioni o no
            fW.write("Nome;Cognome")
            fW.write("\n")
            fW.write(utente)
            fW.close()
        f.close()


    elif choose == '2':
        ciclo = True
        while ciclo:
            print(' Inserisci il nome e il cognome del cliente che deve prenotare')
            nome = input('Inserisci il nome :  ').lower().strip()
            cognome = input('Inserisci il cognome :  ').lower().strip()
            utente = nome + ";" + cognome
            ciclo = len(nome) == 0 or len(cognome) == 0 or ";" in nome or ";" in cognome

        f = open(fileClienti, "r")
        f.seek(0)  # questo è di troppo ma voglio essere sicuro
        f.readline()
        riga = f.readline()
        if len(riga) != 0:
            sensore = 0
            f.seek(0)
            f.readline()
            uscita1 = False
            while not uscita1:
                riga = f.readline()
                lR = riga.split(";")
                print(lR)
                if riga != "":
                    ricNome = lR[0].lower()
                    ricCognome = lR[1].lower().strip()
                if riga == "":
                    uscita1 = True
                elif nome == ricNome and cognome == ricCognome:
                    sensore += 1
            f.close()
            if sensore == 1:
                print(" Cliente già presente")
                cliente = Cliente(nome, cognome)
                print(" Stanze disponibili")
                aggiornaOggHotel(cliente, numeroStanze, listaOggetti, h1)
            elif sensore > 1:  # controllo aggiuntivo se abbiamo qualche rindondanza nel data base
                print(" Cliente presente più volte in database")
                cliente = Cliente(nome, cognome)
                print(" Stanze disponibili")
                aggiornaOggHotel(cliente, numeroStanze, listaOggetti, h1)
            else:
                print(f" Cliente non è in anagrafica aggiungo {nome} - {cognome}.  ")
                # salvaCliente(utente, listaUtenti)
                salvaClienteCsv(utente, fileClienti)
                cliente = Cliente(nome, cognome)
                print("Stanze disponibili")
                aggiornaOggHotel(cliente, numeroStanze, listaOggetti, h1)
        else:
            print(f"Il database è vuoto aggiungo {nome} - {cognome}.  ")
            # salvaCliente(utente, listaUtenti)
            salvaClienteCsv(utente, fileClienti)
            cliente = Cliente(nome, cognome)
            print("Stanze disponibili")
            aggiornaOggHotel(cliente, numeroStanze, listaOggetti, h1)
            f.close()

    elif choose == '3':
        print(""" Premi:
            1 per modificare la prenotazione cercando per cliente
            2 per selezionare la stanza""")
        metodo = input("Scegli l'opzione  ")
        if metodo == "1":
            print(' Inserisci il nome e il cognome del cliente per il quale deve essere modificata la prenotazione')
            nome = input('Inserisci il nome :  ').lower().strip()
            cognome = input('Inserisci il cognome :  ').lower().strip()
            aggiornaPrenotazionePerCliente(numeroStanze, listaOggetti, nome, cognome, h1)
        elif metodo == "2":
            aggiornaPrenotazionePerStanza(numeroStanze, listaOggetti, h1)
        else:
            print("Hai premuto il tasto sbagliato")

    elif choose == '4':
        controlloSelezione = []
        for x in range(numeroStanze):
            if listaOggetti[x].get_cliente() is None:
                print(f"{x + 1} - {listaOggetti[x]} ")
                controlloSelezione.append(x + 1)
        print()
        if len(controlloSelezione) == 0:
            print("Non ci sono camere libere")

    elif choose == '5':
        dataStanze = open("dataBasePrenotazioniStanza.csv", "w")
        now = str(datetime.now())
        dataStanze.write(f"DataSalvataggio;'{now}'\n")
        for x in listaOggetti:
            if x.get_cliente() is None:
                nome = None
                cognome = None
                dataStanze.write(f"{nome};{cognome}\n")
            else:
                nome = x.get_cliente().get_nome()
                cognome = x.get_cliente().get_cognome()
                dataStanze.write(f"{nome};{cognome}\n")
        dataStanze.close()

    elif choose == '6':
        dataStanze = open("dataBasePrenotazioniStanza.csv", "r")
        visualizzaData = dataStanze.readline()
        lVisualizzaData = visualizzaData.split(';')
        print(f"Data salvatggio: {lVisualizzaData[1][1:11]}")
        ciclo = True
        indice = 0
        while ciclo:
            riga = dataStanze.readline()
            if riga != "":
                lR = riga.split(';')
                aggNome = lR[0]
                aggCognome = lR[1]
                if aggNome == "None":
                    cliente = None
                    listaOggetti[indice].set_cliente(cliente)
                else:
                    cliente = Cliente(aggNome, aggCognome)
                    h1.lista_iterabile(indice).set_cliente(cliente)
            if riga == "":
                ciclo = False
            indice += 1

    elif choose == '7':
        esegui = True
        while esegui:
            sceltaStanza = inserimento_intero(
                f"scegli una stanza tra 1 e {numeroStanze}  ")
            if sceltaStanza in range(1, numeroStanze + 1):
                prenotaStanza = h1.get_stanza(sceltaStanza)
                print(prenotaStanza.get_prezzo())
                esegui = False

    elif choose == '8':
        uscita = True
    else:
        print('Hai premuto una bottone non compreso nel menu')
