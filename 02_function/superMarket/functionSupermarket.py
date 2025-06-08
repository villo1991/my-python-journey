def isfloat(valore):
	"""
	Definisce se il valore assegnato alla funzione è un numero
	
	:param valore: valore da verificare
	:return: la funzione ritorna True se il valore in serito è un numero oppere per qualsiasi altro inserimento ritorna False
	"""
	try:
		value=float(valore)
		return True
	except:
		return False
	
def aggiungiProdotto(dizionario,sku, nome, prezzo, qDisponibile):
	'''
	Aggiunge un nuovo prodotto ad un dizionario inserendolo come un dizionario, utilizzando le seguenti chiavi: 'nome', 'prezzo', 'quantita'  
	
	:param dizionario: definisce il dizionario nel quale inserire il nuovo prodotto
	:param sku: rappresenta il codice univoco del prodotto
	:param nome: decrive il protto attraverso un nome comune e puo non essere univoco
	:param prezzo: indica il prezzo e verra converto in float
	:param qDisponibile: indica la quantità che verra caricata a magazzino 
	'''
	newDiz= {}
	newDiz['nome']= nome
	newDiz['prezzo']= prezzo
	newDiz['quantita']= qDisponibile
	dizionario[sku]= newDiz

def rimuoviProdotto(dizionario, sku):
	'''
	Rimuove un articolo dal dizionario indicato, se non presente segnala che può essere eliminata
	
	:param dizionario: definisce il dizionario dal quale eliminare il nuovo prodotto
	:param sku: codice univoco da eliminare
	'''
	if dizionario.get(sku):
		del dizionario[sku]
		print(f'Rimossa la sku {sku}')
	else:
		print(f'  Sku {sku} non presente  ')
		
def visualizzaProd(dizionario):
	"""
	Visualizza i dati del dizionario stampando a video la sku, il nome, il prezzo e la quantita
	
	:param dizionario: definisce il dizionario dal quale stampare i dat
	"""
	[print(f"Sku {x}= {y['nome']} prezzo {y['prezzo']} quantita {y['quantita']}") for x, y in dizionario.items()]
	
def addSkuDiscount(dizionario, insieme, sku):
	"""
	Aggiunge una sku ai prodotti in sconto al 10%, se non presente nel magazzino aggenge il codice, ma evidenzia che non è presente a stock
	
	:param dizionario: indica il dizionario dal quale reperire i dati dei prodotti
	:param insieme: indica l'insime dove aggiungere lo sku
	:param sku: è il codice univoco da aggiungere ai codici sconto 10%
	"""
	if dizionario.get(sku):
		insieme.add(sku)
		print('  Sku aggiunta allo sconto  ')
	else:
		insieme.add(sku)
		print('  Sku aggiunta ai codici sconto, ma sku non presente in sock  ')
		
def rimuoviSconto(insieme, sku):
	"""
	Rimuove la sku dall'insieme dei codici sconto, se non presente vi indica che non era presente
	
	:param insieme: indica l'insime dove togliere lo sku
	:param sku: è il codice univoco da togliere dai codici sconto 10%
	"""
	if sku in insieme:
		insieme.remove(sku)
		print(f'sku {sku} cancellata')
	else:
		print(f'sku {sku} non cancellata perchè non presente')	
		
def controlloPrezzo(prezzo):
	"""
	Controlla e impone di inserire un parametro che sia convertibile in float, quindi un numero qualsiasi. Se il primo inserimento è errato
	chiederà di inserire un numero valido fino a che non lo si inserisce
	
	:param prezz: è il valore che accetta la funzione
	:return: ritorna un valore di tipo float 
	"""
	if isfloat(prezzo):
		prezzo= float(prezzo)    
		return prezzo    
	else:
		while not isfloat(prezzo):
		   prezzo= input('  inserisci il prezzo in numeri\n  ')
		prezzo=float(prezzo)
		return prezzo
		
def controlloQuantita(qDisponibile):
	"""
	Controlla e impone di inserire un parametro che sia un numero intero. Se il primo inserimento è errato
	chiederà di inserire un numero valido fino a che non lo si inserisce
	
	:param qDisponibile: è il valore che accetta la funzione
	:return: ritorna un valore di tipo int
	"""
	while not qDisponibile.isdigit():
		qDisponibile= input('  inserisci la quantità da inserire in intero\n  ')
	qDisponibile= int(qDisponibile)
	return qDisponibile

def registaAcquisti(registroAcq, dizionario, insieme, sku, quantita):
	"""
	Registra l'acquisto nel registro acquisti per una sku presente a nel magazzino sku (dizionario)
	
	:param registroAcq: indica quale sia il registro acquisti, deve essere una lista 
	:param dizionario: indica il dizionario dove trovare i dati delle sku
	:param insieme: indica dove trovare se la sku ha uno sconto
	:param sku:	incica la sku interessata nell'acuisto 
	:param quantita: indica la quantita acquistata
	"""
	a= []
	a.append(sku)
	a.append(quantita)
	b= quantita * dizionario[sku]['prezzo']
	if sku in insieme:
		b= b*0.9
	a.append(b)
	tupla= tuple(a)
	registroAcq.append(tupla)
	
def visualizzaAcqisti(registroAcq):
	"""
	Visuallizza i dati della lista di tuple, che rappresentano un singolo acquisto, stampando a video la sku, la qunatità acquistata e il prezzo totale dell'acuisto

	:param registroAcq: indica quale è la lista da visitare e printare
	"""
	[print(f'dettaglio acquisto: sku {x[0]} - quantità {x[1]} unità - prezzo {x[2]}') for x in registroAcq]

def controlloQuantitaAcqustabile(qDisponibile, sku, wareHouse):
	"""
	Controlla che la quantità richiesta non sia maggiore della quantià presente a stock
	
	:param qDisponibile: è la quantita espressa un valore numerico da controllare
	:parem sku: rappresenta la chiave univoca della sku da cercare a stock
	:param wareHouse: sarebbe il dizionario di dizionari con una chiave univoca, che indentifica un valore dizionario. Al suo interno del valore dizionario deve essereci presente una chiave 'quantita', che ha come valore un valore numerico 
	:return: se la quantità inserita è maggiore della quantita presente nel dizonario restituisce False, se <= restutuisce qDisponibile e se qDisponibile non è un valore numerico restituisce l'errore: TypeError: '<' not supported between instances of 'str' and 'int'
	"""
	a=wareHouse[sku]['quantita']
	if qDisponibile>a:
		print(f'  inserisci una quantità inferiore a {a}')
		return False
	else:
		return qDisponibile
