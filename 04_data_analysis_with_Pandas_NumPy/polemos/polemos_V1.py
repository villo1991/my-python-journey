from polemos_V1_Object import Clean_dataframe, Menu

#C:\Users\villa\Downloads\wine+quality\winequality-red.csv
#"wdbc_corrupted.csv"
if __name__ == "__main__":
    menu = Menu()
    ciclo = True
    while ciclo:
        percorsoFile = input(" Inserisci il percorso assoluto o relativo del file .CSV che vuoi analizzare:  ")
        dataFrame = Clean_dataframe(percorsoFile)
        ciclo = dataFrame.getErrore()

    uscita = False
    while not uscita:
        menu.visulizzaMenu()
        scelta = input("Scegli una opzione proposta nel menu:  ")

        if scelta == '1':
            dataFrame.deleteNaNLines()
            dataFrame.deleteDuplicate()

        elif scelta == '2':
            dataFrame.deleteLinesNaN25()

        elif scelta == '3':
            dataFrame.deleteColumsNaN34()

        elif scelta == '4':
            dataFrame.cleanObjectColumns()

        elif scelta == '5':
            dataFrame.cleanColummsNum()

        elif scelta == '6':
            print("Funzione sperimentale. Da usare con cautela funziona solo su data set normalmente distribuiti o con solo alcune fetaures distribuite non normalmente")
            dataFrame.outLier()

        elif scelta == '7':
            dataFrame.info()
            print()
            dataFrame.visualizzaDataframe()

        elif scelta == '8':
            dataFrame.statistiche()

        elif scelta == '9':
            dataFrame.visualizzaColonneLavorate()

        elif scelta == '10':
            dataFrame.salva()

        elif scelta == '11':
            uscita = True

        else:
            print("Hai selezionato una scelta inesistente")
