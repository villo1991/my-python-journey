from funzioniGestioneAuto import *

dataBase= [{'marca': 'fiat', 'modello': 'qubo', 'anno': 2018, 'targa': 'FR090GT', 'nome': 'Marco', 'cognome': 'Villani', 'cell': 3342817720}]

dataBaseSer= { 'FR090GT': ( 'tagliando', 550.5)}

uscita= False
while not uscita:
	print('''  
	  premi 1 per Registrazione Auto e Clienti
	  premi 2 per Visualizzare tutte le auto e i rispettivi proprietari
	  premi 3 per Registrazione Servizi
	  premi 4 per visualizza i servizi per una determinata targa
	  premi 5 per cerca tutte le auto appartenute ad un cliente
	  premi 6 per uscire 
	''')
	
	menu= input("  inserisci il numero per effettuare l'operazione corrispondente  ")
	menu= controlloNItero(menu)
	
	if menu==1:
		targa= input('	inserisci la targa\n')
		controllo= cercaTarga(dataBase, targa)
		if not controllo:
			marca= input('	inserisci la marca auto\n')
			modello= input('	inserisci il modello\n')
			anno= input("	inserisci l'anno della macchina\n")
			anno= controlloNItero(anno)
			nome= input("	inserisci il nome del proprietario\n")
			cognome= input("	inserisci il cognome del proprietario\n")
			cell= input("	inserisci il numero di telefono\n")
			aggiungiMacchina(dataBase, marca, modello, anno, targa, nome, cognome, cell)
		else:
			print(f'targa {targa} già presente')
	
	elif menu== 2:
		visualizza_auto(dataBase)
	
	elif menu== 3:
		targa= input('	inserisci la targa\n')
		if cercaTarga(dataBase, targa):
			servizio= input("	inserisci il servizio\n")
			prezzo= isNumberNotNeg(input("	inserisci prezzo\n"))
			while not prezzo:
				prezzo= isNumberNotNeg(input("	inserisci prezzo\n"))
			prezzo= float(prezzo)
			registrare_servizio(dataBaseSer, targa, prezzo, servizio)
			print(f"operazione registrata per la macchina targata {targa}")
		else:
			print('	targa non presente')
	
	elif menu==4:
		targa= input('	inserisci la targa\n')
		if dataBaseSer.get(targa):
			visualizzaServiziTarga(dataBaseSer, targa)
		else:
			print('	targa non presente')

	elif menu==5:
		nome= input("	inserisci il nome del proprietario\n")
		cognome= input("	inserisci il nome del proprietario\n")
		risultato= cercaAutoCliente(dataBase, nome, cognome)
		if risultato:
			print(f"Lista delle auto di {nome} {cognome}") 
			visualizza_auto(risultato)
		else:
			print(f'Nessuna auto a nome di {nome} {cognome}')
			
	elif menu==6:
		uscita= True
		
	else:
		print('	hai selezionato una funzione inesistente, utilizza le opzioni indicate nel menu')
