def isNumberNotNeg(digit):
	'''
	Controlla che il parametro inserito sia un numero positivo.
	
	:param digit: è il paramtro inserito
	:return: ritorna il parametro se questo è un parametro 
	:return: ritorna falso se non è un numero positivo
	'''
	lista= []
	lista1= []
	lista2= []
	posizione= 0
	digit= digit
	if digit[0]== '.':
		lista1.append(False)
	for a in digit:
		if a.isdigit():
			lista.append(True)
		elif a=='.':
			lista1.append(True)
		elif a=='-':
			lista2.append(False)
		else:
			lista.append(False)
		posizione+=1
	if len(lista1)>1:
		lista1.append(False)
	if all(lista) and all(lista1) and all(lista2):
		return digit
	return False

def aggiungiAlbum(dataBase, album, artista, anno, genere, insieme):
	'''
	Aggiunge una macchina con tutti i parametri necessarri ad una lista di dizionari.
	
	:param dataBase: punta alla lista di dizionari a quale aggiungere i dati
	:param album: indica il nome dell'album è un valore stringa 
	:param anno: indica l'anno dell'abum è un valore int
	:param genere: indica il genere dell album è un valore stringa
	:param dizionario: rappresenta l'insieme di tuple che deve essere aggiunto 
	'''
	diz={}
	diz['titolo']= album
	diz['artista']= artista
	diz['anno']= anno
	diz['genere']= genere
	diz['tracce']= insieme
	dataBase.append(diz)

def visualizzaAlbum(dataBase):
	'''
	Visualizza il database che è costituito da una lista di dizionari.
	
	:param dataBase: il parametro che indica in quale lista iterare
	'''
	[print(f"Titolo album: {y['titolo']} - artista: {y['artista']} - anno: {y['anno']} - genere: {y['genere']} - tracce: {y['tracce']}") for y in dataBase]
	print('\n')
	
def eliminaAlbum(dataBase, album, erase= False ):
	'''
	Elimina un il primo album trovato in modo case insensitive dal database, costituito da una lista di dizionari, se il parametro erase viene lasciato come da default, mentre se si cambia in False eliminera tutti gli album che contengono quel titolo. 
	
	:param dataBase: indica il database dal quale eliminare il dizionario
	:param album: indica che titolo cercare ed deve essere un valore stinga
	:param erase: 
	'''
	for x in range(len(dataBase)-1,-1,-1):
		if album.upper() == dataBase[x]['titolo'].upper():
			del dataBase[x]
			print(f"Album {album} elimiato \n")
			if not erase:
				return print('	Ho cancellato la prima corrispondenza, per cancellare le eventuali altre chiedi al helpdesck di abilitare il parametro erase\n')
	print('	Non sono state trovate corrispondenze\n')  
		
