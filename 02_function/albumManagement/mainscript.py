from funzioniAlbum import * 

dataBase= [{'titolo': 'la rosa', 'artista': 'ligaBue', 'anno': 1991, 'genere': 'pop', 'tracce': {('track1', 2.5), ('track2', 5.5), ('track3', 3.5)}},
{'titolo': 'la rosa', 'artista': 'ligaBue', 'anno': 1991, 'genere': 'pop', 'tracce': {('track1', 2.5), ('track2', 5.5), ('track3', 3.5)}}]

uscita= False 

while not uscita:
	print('''
		MENU SCELTA
	premi 1 per aggungere album
	premi 2 per visualizzare tutti gli album
	premi 3 per cercare un album
	premi 4 per rimuovere un album
	premi 5 per uscire''')
	
	scelta= input('	seleziona la funzione desiderata  ')
	
	if scelta== '1':
		album= input('	inserisci il nome del album\n')
		artista= input('	inserisci il nome del artista\n')
		anno= input("	inserisci l'anno dell'album in numeri\n")
		while not anno.isdigit(): 
			anno= input("	inserisci l'anno dell'album in numeri\n")
		anno= int(anno)
		genere= input('	inserisci il genre dell album\n')
		exit= False
		insieme= set()
		while not exit:
			tupla= ()
			traccia= input("	inserisci il nome della traccia oppere premi unvio per uscire dall'immisione dati\n")
			if not traccia:
				exit= True
			else:
				durata= isNumberNotNeg(input("	inserisci la durata della traccia\n"))
				while not durata:
					durata= isNumberNotNeg(input("	inserisci la durata della traccia\n"))
				durata= float(durata)
				traccia= (traccia,)
				durata= (durata,)
				tupla+= traccia
				tupla+= durata
				insieme.add(tupla)
		aggiungiAlbum(dataBase, album, artista, anno, genere, insieme)
		
	elif scelta== '2':
		visualizzaAlbum(dataBase)
		
	elif scelta== '3':
		ricerca = input("	inserisci il nome dell'abum da ceracre\n")
		flag= 0
		for dizio in dataBase:
			if dizio['titolo'].upper()== ricerca.upper():
				print(f"Titolo album: {dizio['titolo']} - artista: {dizio['artista']} - anno: {dizio['anno']} - genere: {dizio['genere']} - tracce: {dizio['tracce']}")
				print('\n')
				flag+=1
		if flag==1:
			print('	Album non trovato\n')
			
	elif scelta== '4':
		album= input("	inserisci il nome dell'album da eliminare\n")
		print('\n')
		eliminaAlbum(dataBase, album)
		
	elif scelta== '5':
		uscita= True
	else:
		print('	hai selezionato una funzione inesistente, utilizza le opzioni indicate nel menu\n')
