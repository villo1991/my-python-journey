inventario = {
				'vino': (5.5 , 50) , 'tappi': (0.20, 500),
				'bottigle': ( 0.25 , 90 ),'lips stick':( 11 , 5)
			}


for key in inventario.keys():
	print('       ',key,'=',inventario[key])


var= input('''				per aggiornare il dizonario premi qualsiasi bottone, se non vuoi aggiornare premi invio\n''')
		
while var :
	var= input('''				per aggiornare il dizonario inserisci un nuovo prodotto o 'stop' per finire con l'aggiornamento. 
				Se la chiave è già presente ti verrà mostartato il prezzo e le quantità presenti, 
				quindi potrai aggiornarle separatamete\n''')
	
	prodotto = inventario.get(var, 'corrispondenza non trovata')
	if prodotto == 'corrispondenza non trovata':
		lista= []
		prezzo=float(input("				inserisci il prezzo del nuovo articolo\n"))
		lista.append(prezzo)
		quantita= int(input("				inserisci la quantità del nuovo articolo\n"))
		lista.append(quantita)
		listaTupla= tuple(lista)
		inventario[var]= listaTupla

  if prodotto != 'corrispondenza non trovata' and var !='stop':
    print(inventario[var])

  if var=='stop':
	  var= False
		
cancel= input('''				per cancellare un prodotto o i prodotti dal dizonario premi qualsiasi bottone,
				se non vuoi cancellare premi invio\n''')
				
while cancel:
	cancel= input('''				inserisci una chiave esistente per cancellare i valori asocciati, 
					scrivi 'stop' per uscire dalla pulizia\n''')
	
  if cancel == 'stop':
		cancel= False
    continue
		
	comando= inventario.get(cancel, 'corrispondenza non trovata')
	if comando== 'corrispondenza non trovata':
		print('				hai inserito una chiave inesistente, iserisci una chiave valida')
		print('				chiavi esistenti')
		for key in inventario.keys():
			print('					',key)
		continue
	
  else:
		cancellare= input(f"				se premi 'yes' cacelli {comando}, se preni 'no' annulli l'operazione\n")
		if cancellare == 'yes':
			valore= inventario.pop(cancel)
			print(f'				cancellati i dati nella key {cancel}')
		elif cancellare== 'no':
			continue
valoreTot=0

for value in inventario.values():
	 prezzo=value[0]
	 numero= value[1]
	 prezzoPerNumero=prezzo*numero
	 valoreTot+=prezzoPerNumero
print("				il valore totale dell'inventario e di: \n  				", valoreTot)

for key in inventario.keys():
	print('       ',key,'=',inventario[key])
