from moduloMenu import *
from moduloOrdine import *

menu = Menu()
gestoreOrdini = GestoreOrdini()
dataOdierna = datetime.now().strftime("%Y-%m-%d")

uscita = False
while not uscita:
    menu.visualizzaOpzioni()
    scelta = input("Scegli un opzione tra quelle proposte  ")

    if scelta == "1":
        menu.visualizzaMenu()

    elif scelta == "2":
        menu.visualizzaMenu()
        print("\n")
        sceltaTavolo = tavolo()
        sensore = 0
        for indice,x in enumerate(gestoreOrdini.visualizzaListaOrdini()):
            if sceltaTavolo == x.visualizzaId() and x.visualizzaPagamento() == False and dataOdierna == x.getDayOrder():
                sottoMenu = input(f"""
                            premi 1) Per aggiungere un piatto al ordine del tavolo {sceltaTavolo}
                            premi 2) Per eliminare un piatto dell'ordine del tavolo {sceltaTavolo}
                            """)

                if sottoMenu == "1":
                    sensore += 1
                    print(f"Stai modificando l'ordine del tavolo {sceltaTavolo}")
                    ciclo = True
                    while ciclo:
                        seltaPiatto = inserisciPiatto(menu, x)
                        if seltaPiatto == True:
                            ciclo = False
                    x.visualizzaPiatti()

                elif sottoMenu == "2":
                    sensore += 1
                    print(f"Stai eliminando piatti per l'ordine del tavolo {sceltaTavolo}")
                    ciclo = True
                    while ciclo:
                        if len(x.printLista()) != 0:
                            print("Piatti associati all'ordine")
                            ritorno = x.visualizzaPiatti()
                            if ritorno != False:
                                selezionaPiatto = scegliPiattoOrdine(sceltaTavolo, x)
                                x.eliminaPiatto(selezionaPiatto)
                            else:
                                ciclo = False
                        else:
                            del gestoreOrdini.visualizzaListaOrdini()[indice]
                            ciclo = False
                            print(f"Hai eliminato tutti i piatti dell'ordine del tavolo {sceltaTavolo}")

                else:
                    sensore += 1
                    print("Hai fatto una scelta non valida")

        if sensore == 0:
            print(f"Stai creando un novo ordine per il tavolo {sceltaTavolo}")
            ordine = Ordine(sceltaTavolo)
            ciclo = True
            while ciclo:
                seltaPiatto = inserisciPiatto(menu, ordine)
                if seltaPiatto == True:
                    gestoreOrdini.aggOrdine(ordine)
                    ciclo = False
            print(f"Piatti ordinati dal tavolo {sceltaTavolo}")
            ordine.visualizzaPiatti()

    elif scelta == "3":
        print("visualizza il totale di un ordine per un tavolo se è ancora da saldare")
        sceltaTavolo = tavolo()
        sensore = 0
        for x in gestoreOrdini.visualizzaListaOrdini():
            if sceltaTavolo == x.visualizzaId() and x.visualizzaPagamento() == False:
                sensore += 1
                print(x.totaleOrdine())
        if sensore == 0:
            print(f"Il tavolo {sceltaTavolo} nessun ordine da saldare ")

    elif scelta == "4":
        sottoMenu = input("""
            premi 1) Assegna il pagamento del tavolo
            premi 2) Visualizzare tutti gli ordini pagati e non pagati della giornata
            premi 3) Visualizzare tutti gli ordini 
            """)
        if sottoMenu == "1":
            sceltaTavolo = tavolo()
            sensore = 0
            stop = 0
            print(len(gestoreOrdini.visualizzaListaOrdini()))
            while len(gestoreOrdini.visualizzaListaOrdini()) > stop:
                oggOrd = gestoreOrdini.visualizzaListaOrdini()[stop]
                print(oggOrd)
                if sceltaTavolo == oggOrd.visualizzaId() and oggOrd.visualizzaPagamento() == False:
                    oggOrd.assegnaPagamento()
                    sensore += 1
                stop += 1
            if stop == 0:
                print(f"Il tavolo {sceltaTavolo} non ha nessun ordine da saldare ")

        elif sottoMenu == "2":
            for x in gestoreOrdini.visualizzaListaOrdini():
                if dataOdierna == x.getDayOrder():
                    x.printOrder()
                    print()

        elif sottoMenu == "3":
            for x in gestoreOrdini.visualizzaListaOrdini():
                x.printOrder()
                print()
        else:
            print("Hai fatto una scelta non valida")

    elif scelta == "5":
        controllo = 0
        for x in gestoreOrdini.visualizzaListaOrdini():
            pagamento = x.visualizzaPagamento()
            if pagamento == False:
                controllo += 1
        if controllo > 0 :
            scelta = input(f"Attenzione ci sono {controllo} ordini non pagati, potrebbero dare dare problemi. Premi 'yes' ").lower().strip()
            if scelta == "yes":
                salvaOrdinToCSV(gestoreOrdini)

    elif scelta == "6":
        caricaDati(gestoreOrdini)

    elif scelta == "7":
        uscita = True

    else:
        "Hai fatto una scelta non valida"
