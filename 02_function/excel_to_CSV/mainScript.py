# il programma deve legggere i file di una specificva cartella oppure puo usare l'opzione os.walk() andare in profondità. Una volta indivuduato il file lo converte
# converte da excel a CSV

"""
1_ chiede all'utente di inserire la carella di lavro
2_ controllo che esista e chiedo se si vuole analizzare solo quella cartella o anche le sotto carelle
3_ creo una cartella nuova con una certa rinomina che accolga tutti i file
4_

"""
import os, datetime, openpyxl, csv

verifica = False

while not verifica:
    directory = input(
        "digita o incolla in nome della directori sulla quale lavorare non necessario usare il doppo \n")
    directory = rf"{directory}"
    verifica = os.path.exists(directory)
    absolutePath = os.path.abspath(directory)

uscita = False
while not uscita:
    scelta = input("""
            premi 1 per analizzare solo la cartella indicata 
            premi 2 per analizzare tutte le sotto cartelle
            premi 3 per uscire 
            """)
    if scelta == "1":
        folder = os.listdir(absolutePath)
        if len(folder) > 0:
            pathNewDirectory = input("""insreisci in nome della nuova directory dove salavre i file convertiti o 
                non inserire niente e sarà creata la directory = C:\\Users\\villo\Desktop\\film\\conversione_data_odierna
            """)
            if pathNewDirectory == "":
                oggettoTime = datetime.datetime.now()
                stringaData = oggettoTime.strftime("%d_%m_%Y")
                pathNewDirectory = f"C:\\Users\\villo\Desktop\\film\\conversione{stringaData}"
                os.makedirs(pathNewDirectory, exist_ok=True)
                controllo = True
                os.chdir(pathNewDirectory)
            else:
                try:
                    os.makedirs(pathNewDirectory)
                    os.chdir(pathNewDirectory)
                    controllo = True
                except Exception as e:
                    print(e)
                    controllo = False

            if controllo == True:
                for x in folder:
                    if x.endswith(".xlsx"):
                        correzione = os.path.join(absolutePath, x)
                        wb = openpyxl.load_workbook(correzione, read_only=True)
                        nomeWoorkbook = os.path.splitext(os.path.basename(correzione))[0]
                        # nomeWoorkbook = x[:-5]
                        listaRinomina = []
                        for sheetName in wb.sheetnames: # cicliamo sui tutti i fogli che compongono il workbook trattandoli come oggetti
                            nomefoglio = sheetName.title()
                            mixNome = nomeWoorkbook + str(nomefoglio)+".csv"
                            listaRinomina.append(mixNome)
                        sheet = wb.worksheets

                        for y in range(len(sheet)):
                            file = open(listaRinomina[y], mode="a", newline="", encoding="utf-8")
                            writer = csv.writer(file)  # Creiamo un oggetto writer che utilizzeremo per scivere sul file
                            # for rowNum in y.iter_rows(values_only=True):
                            for row in sheet[y].values:  #questo è il metodo più veloce
                                writer.writerow(row)
                            """
                            for row in sheet[y].iter_rows(values_only=True):   #molto comodo e flessibile fa la setssa cosa di sheet[y].values, perchè con il parametro (values_only=True) accede alla riga e preleva solo i valori e non gli oggetti
                                writer.writerow(row)"""                        # ha una velocità inferiore sheet[y].values di 5/10 %
                            """for rowNum in range(1, sheet[y].max_row + 1):
                                rowData = []
                                        # rowData = [y.cell(row=rowNum, column=colNum).value for colNum in range(1, y.max_column + 1)]
                                for colNum in range(1, sheet[y].max_column + 1):
                                    rowData.append(sheet[y].cell(row=rowNum, column=colNum).value)
                                writer.writerow(rowData)"""
                            file.close()
        else:
            print("La cartella è vuota")
        uscita = True

    elif scelta == "2":
        pathNewDirectory = input("""insreisci in nome della nuova directory dove salavre i file convertiti o 
                        non inserire niente e sarà creata la directory = C:\\Users\\villo\Desktop\\film\\conversione_data_odierna
                    """)
        if pathNewDirectory == "":
            oggettoTime = datetime.datetime.now()
            stringaData = oggettoTime.strftime("%d_%m_%Y")
            pathNewDirectory = f"C:\\Users\\villo\Desktop\\film\\conversione{stringaData}"
            os.makedirs(pathNewDirectory, exist_ok=True)
            controllo = True
            os.chdir(pathNewDirectory)
        else:
            try:
                os.makedirs(pathNewDirectory)
                os.chdir(pathNewDirectory)
                controllo = True
            except Exception as e:
                print(e)
                controllo = False
        if controllo:
            for dirpath, dirnames, filenames in os.walk(absolutePath):
                print(f"stiamo analizzando i file nella directory {dirpath}")
                for x in filenames:
                    if x.endswith(".xlsx"):
                        correzione = os.path.join(absolutePath, x)
                        wb = openpyxl.load_workbook(correzione, read_only=True)
                        nomeWoorkbook = os.path.splitext(os.path.basename(correzione))[0]
                        # nomeWoorkbook = x[:-5]
                        listaRinomina = []
                        for sheetName in wb.sheetnames:  # cicliamo sui tutti i fogli che compongono il workbook trattandoli come oggetti
                            nomefoglio = sheetName.title()
                            mixNome = nomeWoorkbook + str(nomefoglio) + ".csv"
                            listaRinomina.append(mixNome)
                        sheet = wb.worksheets

                        for y in range(len(sheet)):
                            file = open(listaRinomina[y], mode="a", newline="", encoding="utf-8")
                            writer = csv.writer(file)  # Creiamo un oggetto writer che utilizzeremo per scivere sul file
                            # for rowNum in y.iter_rows(values_only=True):
                            for row in sheet[y].values:  # questo è il metodo più veloce
                                writer.writerow(row)

    elif scelta == "3":
        uscita = True
    else:
        print("Hai premuto un bottone differente dal menu proposto")
