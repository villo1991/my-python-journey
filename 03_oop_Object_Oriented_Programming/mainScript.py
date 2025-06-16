#!/usr/bin/env python3
import sys

from classFilm import Film
from classVideoteca import Videoteca
from funzioni import inserimento_intero, verificaFloat
from nomeFile import nomeFile

if len(sys.argv) == 1:
    uscita = False
    magazzino = Videoteca()

    while not uscita:
        choose = input('''
            premi: 
            1_ per Aggiungere un nuovo film alla videoteca
            2_ per Rimuovere un film dalla videoteca
            3_ per Cercare un film per titolo
            4_ per Visualizzare tutti i film disponibili
            5_ per Salvare i dati dei film in un file di testo (videoteca.txt)
            6_ per uscire
            
        ''')

        if choose == '1':
            print(' Inserisci i paramentri richiesti per caricare un film')
            titolo = input("  Inserisci il titolo del film \n")
            anno = inserimento_intero("  Inserisci il l'anno del film \n")
            genere = input("  Inserisci il genere del film \n")
            regista = input("  Inserisci il regista del film \n")
            prezzo = verificaFloat("  Inserisci il prezzo del film \n")
            oggeFilm = Film(titolo, anno, genere, regista, prezzo)
            disponibilita = input(
                "Premi enter/invio per per indicare che non è stato prenotato, altimenti verra registarta la data odierna  ")
            if disponibilita:
                oggeFilm.set_prenota()
            magazzino.add_film(oggeFilm)
            for x in magazzino.get_videoteca():
                print(x)

        elif choose == '2':
            titolo = input("  Inserisci il titolo del film da eliminare  \n")
            risultato = magazzino.del_film(titolo)
            print(f"Risultato: {risultato}")

        elif choose == '3':
            titolo = input("  Inserisci il titolo del film da cercare  \n")
            info = magazzino.get_film(titolo)
            print(info)

        elif choose == '4':
            for x in magazzino.get_videoteca():
                if x.get_disponibilita() == '':
                    print(x)

        elif choose == '5':
            path = nomeFile
            file = open(path, 'w')
            for x in magazzino.get_videoteca():
                file.write(x.stampaFile())
                file.write('\n')
            file.close()

        elif choose == '6':
            uscita = True

        else:
            print('Hai premuto una bottone non compreso nel menu')

if len(sys.argv) > 1:
    modficaPath = sys.argv[1:]
    stringa = ''
    for x in modficaPath:
        stringa += str(x)
        modficaPathText = "'" + stringa + ".txt" + "'"
        modifica = open("nomeFile.py", "w")
        modifica.write("nomeFile = ")
        modifica.write(modficaPathText)
        modifica.close()
