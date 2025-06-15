def controlloNItero(qDisponibile):
	"""
	Controlla e impone di inserire a tastiera un parametro che sia un numero intero. Se il primo inserimento è errato
	chiederà di inserire un numero valido fino a che non lo si inserisce.
	
	:param qDisponibile: è il valore che accetta la funzione
	:return: ritorna un valore di tipo int
	"""
	while not qDisponibile.isdigit():
		qDisponibile= input('  inserisci un numro intero\n  ')
	qDisponibile= int(qDisponibile)
	return qDisponibile

def aggiungiMacchina(dataBase, marca, modello, anno, targa, nome, cognome, cell):
	'''
	Aggiunge una macchina con tutti i parametri necessarri ad una lista di dizionari.
	
	:param dataBase: punta alla lista di dizionari a quale aggiungere i dati
	:param marca: indica la marca della macchina è un valore stringa 
	:param modello: indica il modello della macchina è un valore stringa
	:param anno: indica l'anno della macchina è un valore int
	:param targa: indica la targa della macchina è un valore stringa
	:param nome: indica il nome del proprietario della macchina è un valore stringa
	:param cognome: indica la cognome del proprietario della macchina è un valore stringa
	:param cell: è il numero di telefono del proprietario
	'''
	diz={}
	diz['marca']= marca
	diz['modello']= modello
	diz['anno']= anno
	diz['targa']= targa
	diz['nome']= nome
	diz['cognome']= cognome
	diz['cell']= cell
	dataBase.append(diz)
	
def visualizza_auto(dataBase):
	'''
	Visualizza tutte le auto presenti nel database.
	
	:param dataBase: punta alla lista di dizionari per il quale visualizzare i dati
	'''
	[print(f"Marca: {y['marca']} - modello: {y['modello']} - anno: {y['anno']} - targa: {y['targa']} - nome: {y['nome']} - cognome: {y['cognome']}") for y in dataBase]
	
def registrare_servizio(dataBaseSer, targa, prezzo, servizio):
	'''
	Aggiunge un servizio con tutti i parametri necessarri ad un dizionario.
	
	:param dataBaseSer: punta al data base che in questo caso deve essere un dizonario
	:param targa: indica la targa della macchina è un valore stringa
	:param prezzo: indica il prezzo del servizo è un valore float
	:param servizio: indica che servizo è stato fatto alla macchina è un valore stringa
	'''
	tupla=()
	servizio= (servizio,)
	prezzo= (prezzo,)
	tupla+= servizio
	tupla+= prezzo
	dataBaseSer[targa]= tupla	
	
def cercaTarga(dataBase, targa):
	'''
	Cerca una targa nel database.
	
	:param dataBase: punta alla lista di dizionari per il quale visualizzare i dati
	:param targa: indica la targa della macchina è un valore stringa
	:return: ritorna True appena trova il primo match di riceraca
	:return: ritorna False appena trova il primo match di riceraca
	'''
	i= 0 
	while i< len(dataBase):	
		if dataBase[i]['targa'].upper() == targa.upper():
			return True
		i+= 1 
	return False 
	
def isNumberNotNeg(digit):
	'''
	Controlla che il parametro inserito sia un numero positivo.
	
	:param digit: è il paramtro inserito
	:return: ritorna il parametro se questo è una stringa convertibile in numeri
	:return: ritorna falso se non è un numero positivo
	'''
	lista= []
	lista1= []
	lista2= []
	posizione= 0
	digit= digit
	if digit == "":
		return False
	elif digit[0]== '.':
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
	else:
		return False
		
def visualizzaServiziTarga(dataBaseSer, targa):
	'''
	Visualizza tutti i servizi fatti per una data targa.
	
	:param dataBaseSer: punta al data base che in questo caso deve essere un dizonario
	:param targa: indica la targa della macchina per la quale cercare i valori è un valore stringa
	'''
	[print(f"{targa} - servizio: {y[0]} - costo: {y[1]}") for x, y in dataBaseSer.items() if targa.upper()== x.upper()]

def cercaAutoCliente(dataBase, nome, cognome):
	'''
	Cerca tutte le auto di un cliente confrontando nome e cognome e stocca i risultati in una lista di dizionari.
	
	:param dataBase: punta alla lista di dizionari per il quale visualizzare i dati
	:param nome: indica il nome del proprietario della macchina è un valore stringa
	:param cognome: indica la cognome del proprietario della macchina è un valore stringa
	:return: se trova dei match con nome e cognome ritorna una lista di dizonari
	:return: se trova dei match con nome e cognome ritorna una lista di dizonari
	'''
	lista=[]
	for x in dataBase:
		diz= {}
		flagNome= False
		flagCognome= False
		if x['nome'].upper() == nome.upper():
			flagNome= True
		if x['cognome'].upper() == cognome.upper():
			flagCognome= True
		if flagNome and flagCognome:
			diz['marca']= x['marca']
			diz['modello']= x['modello']
			diz['anno']= x['anno']
			diz['targa']= x['targa']
			diz['nome']= nome
			diz['cognome']= cognome
			lista.append(diz)
	if len(lista)>0:
		return lista
	return False
