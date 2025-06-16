from datetime import datetime
from gest_iscrizioni import *

palestra = Iscrizioni()

uscita = False

while not uscita:
    choose = input('''
                premi: 
                1_ per Aggiungere socio  OK
                2_ per Aggiungere attività OK
                3_ per Iscrivere soci ad attività ok
                4_ per Visualizzare soci  OK
                5_ per Visualizzare iscrizioni OK 
                6_ per Visualizzare attività OK
                7_ per Salvataggio dell'intero archivio
                8_ per caricamento dell'intero archivio
                9_ per uscire

            ''')
    if choose == '1':
        ciclo = True
        nome = None
        cognome = None
        while ciclo:
            print(' Inserisci i dati del cliente')
            nome = input('  Inserisci il nome :  ').lower().strip()
            cognome = input('  Inserisci il cognome :  ').lower().strip()
            utente = nome + ";" + cognome
            ciclo = len(nome) == 0 or len(cognome) == 0 or ";" in nome or ";" in cognome

        annoNascita = inserimentoAnno("  Inserisci l'anno di nascita  ")
        meseNascita = inserimentoMese("  Inserisci il mese di nascita  ")
        giornoNascita = inserimentoGiorno("  Inserisci il giorno di nascita  ", annoNascita, meseNascita)
        data_nascita = datetime(annoNascita, meseNascita, giornoNascita)
        idSocio = palestra.numeroSoci() + 1
        if palestra.numeroSoci() == 0:
            print("Socio aggiunto")
            palestra.aggSocio(idSocio, nome, cognome, data_nascita)# aggunge il socio all'oggetto palestra
        else:
            controlloSocio(palestra, nome, cognome, idSocio, data_nascita)

    elif choose == '2':
        ciclo = True
        while ciclo:
            nomeAttivita = input("  Inserisci il nome dell'attività  ").lower()
            if not ";" in nomeAttivita:
                ciclo = False
        ciclo = True
        while ciclo:
            descrizioneAttivita = input("  Inserisci breve descizione attività  ").lower()
            if not ";" in descrizioneAttivita:
                ciclo = False
        ciclo = True
        while ciclo:
            giorniSvolgimento = input(
                "  Inserisci i giorni utilizzando queste diciture per indicare i giorni L,MA,ME,G,V,S,D  ")
            if not ";" in giorniSvolgimento:
                ciclo = False

        if palestra.getListAttivita() == 0:
            print("Aggiungo attività")
            palestra.aggAttività(nomeAttivita, descrizioneAttivita, giorniSvolgimento)
        else:
            controlloAttivita(palestra, nomeAttivita, descrizioneAttivita, giorniSvolgimento)

    elif choose == '3':
        selezione = input(''' Premi: 
                        1_ per Selezionare socio da iscrivere in base all'Id
                        2_ per Selezionare socio da iscrivere in base a nome e cognome
                         ''')

        if selezione == "1":
            if palestra.numeroSoci() > 0 and palestra.numeroAttivita() > 0:
                IdSocio = inserimentoId("  Inserisci l'Id cliente  ", palestra)
                print(" Elenco attività: ")
                n = 1
                for x in palestra.getListAttivita():
                    print(f"{n}_ {x.visualizzaDatiAtt()}")
                    n += 1

                sceltaAttivita = inserimentoAtt(
                    " Seleziona una attivita con un numero compreso in qelle proposte nel elenco sopra  ", palestra)

                oggSocio = palestra.visualizzaSoci()[IdSocio - 1]
                oggAttivita = palestra.visualizzaAttivita()[sceltaAttivita - 1]

                oggAttivita.iscriviSocio(oggSocio)
            else:
                print("Non sono presenti soci o attività")

        elif selezione == "2":
            if palestra.numeroSoci() > 0 and palestra.numeroAttivita() > 0:
                ciclo = True
                nome = None
                cognome = None
                while ciclo:
                    print(' Inserisci i dati del cliente')
                    nome = input('  Inserisci il nome :  ').lower().strip()
                    cognome = input('  Inserisci il cognome :  ').lower().strip()
                    utente = nome + ";" + cognome
                    ciclo = len(nome) == 0 or len(cognome) == 0 or ";" in nome or ";" in cognome

                for x in palestra.getListSoci():
                    sensore = 0
                    if nome == x.getNome() and cognome == x.getCognome():
                        sensore += 1
                        scelta = input(
                            f"Premi yes per aggiungere il cliente {nome} {cognome} ad una attivita, altrimenti qulasisi altro tasto per annullare ").strip().lower()
                        if scelta == "yes":
                            print(" Elenco attività: ")
                            n = 1
                            for x in palestra.getListAttivita():
                                print(f"{n}_ {x.visualizzaDatiAtt()}")
                                n += 1

                            sceltaAttivita = inserimentoAtt(
                                " Seleziona una attivita con un numero compresa in qelle proposte nel elenco sopra  ",
                                palestra)
                            oggAttivita = palestra.visualizzaAttivita()[sceltaAttivita - 1]
                            oggAttivita.iscriviSocio(x)
                        if sensore == 0:
                            print(f"Nessuna corrispondenza per {nome} {cognome}")

            else:
                print("Non sono presenti soci o attività")

    elif choose == '4':
        for x in palestra.visualizzaSoci():
            print(x)

    elif choose == '5':
        for x in palestra.getListAttivita():
            print(x.visualizzaDatiAtt())
            for y in x.visualizzaPartecipanti():
                print(y)

    elif choose == '6':
        for x in palestra.getListAttivita():
            print(x.visualizzaDatiAtt())

    elif choose == '7':
        archivioSoci = open("archivioSoci.csv", "w")
        archivioSoci.write("Id;Nome;Cognome;Data di nascita;Data iscizione\n")
        for x in palestra.getListSoci():
            archivioSoci.write(f"{x.getId()};")
            archivioSoci.write(f"{x.getNome()};")
            archivioSoci.write(f"{x.getCognome()};")
            archivioSoci.write(f"{x.getDataNascita()};")
            archivioSoci.write(f"{str(x.getDataIscrizione())}")  # valutare se usare strftime
            archivioSoci.write("\n")
        archivioSoci.close()

        archivioAttivita = open("archivioAttivita.csv", "w")
        archivioAttivita.write("Nome Attivita;Descizione attivita;Giorni attivita;Lista iscritti\n")
        for x in palestra.getListAttivita():
            archivioAttivita.write(f"{x.getNomeAttivita()};")
            archivioAttivita.write(f"{x.getDescAttivita()};")
            if len(x.getIscitti()) == 0:
                archivioAttivita.write(f"{x.getGiorniAttivita()}")
            else:
                archivioAttivita.write(f"{x.getGiorniAttivita()};")
            for y in x.getIscitti():
                archivioAttivita.write(f"{y.getId()},")
                archivioAttivita.write(f"{y.getNome()},")
                archivioAttivita.write(f"{y.getCognome()},")
                archivioAttivita.write(f"{y.getDataNascita()},")
                archivioAttivita.write(f"{str(y.getDataIscrizione())},")
            archivioAttivita.write("\n")
        archivioAttivita.close()

    elif choose == '8':
        conferma = input(
            "Atenzione se premi 'yes' verranno svutati i dati attuali dell'oggetto Iscrizioni e caricati quelli in archivio ").strip().lower()
        if conferma == "yes":
            for x in range(len(palestra.getListSoci()) - 1, -1, -1):
                del palestra.getListSoci()[x]
            for x in range(len(palestra.getListAttivita()) - 1, -1, -1):
                del palestra.getListAttivita()[x]

            archivioSoci = open("archivioSoci.csv", "r")
            archivioSoci.readline()
            ciclo = True
            while ciclo:
                riga = archivioSoci.readline()
                if riga != "":
                    Lriga = riga.split(";")
                    idSocio = int(Lriga[0])
                    nome = Lriga[1]
                    cognome = Lriga[2]
                    data_nascita = listaTodatetime(Lriga[3])
                    dataIscrizione = listaTodatetime(Lriga[4])
                    palestra.caricaSocio(idSocio, nome, cognome, data_nascita, dataIscrizione)
                elif riga == "":
                    ciclo = False

            archivioAttivita = open("archivioAttivita.csv", "r")
            archivioAttivita.seek(0)
            archivioAttivita.readline()
            ciclo = True
            indice = 0
            while ciclo:
                riga = archivioAttivita.readline()
                if riga != "":
                    Lriga = riga.split(";")
                    nomeAttivita = Lriga[0]
                    descrizioneAttivita = Lriga[1]
                    giorniAttivita = Lriga[2]
                    #nuovaAttivita = palestra.aggAttività(nomeAttivita, descrizioneAttivita, giorniAttivita)
                    nuovaAttivita = Attivita()
                    nuovaAttivita.setAttivita(nomeAttivita, descrizioneAttivita, giorniAttivita)
                    palestra.aggAttivitaCaricamento(nuovaAttivita)
                    listaCrostruttore = Lriga[3][:-1].split(",")
                    listaDiListe = []
                    listaOgg = []
                    newLista = []
                    indice = 0
                    for x in range(len(listaCrostruttore) // 5):
                        newLista = []
                        newLista.append(listaCrostruttore[0 + indice])
                        newLista.append(listaCrostruttore[1 + indice])
                        newLista.append(listaCrostruttore[2 + indice])
                        newLista.append(listaCrostruttore[3 + indice])
                        newLista.append(listaCrostruttore[4 + indice])
                        indice += 5
                        listaDiListe.append(newLista)

                    listaSoci = []
                    for x in listaDiListe:
                        idSocio = int(x[0])
                        nome = x[1]
                        cognome = x[2]
                        data_nascita = listaTodatetime(x[3])
                        dataIscrizione = listaTodatetime(x[4])
                        newSocio = Socio()
                        newSocio.caricaValori(idSocio, nome, cognome, data_nascita, dataIscrizione)
                        listaSoci.append(newSocio)
                        print(type(newSocio))
                        print(newSocio)

                    for x in listaSoci:
                        nuovaAttivita.iscriviSocio(x)


                elif riga == "":
                    ciclo = False

    elif choose == '9':
        uscita = True
    else:
        print('Hai premuto una bottone non compreso nel menu')
