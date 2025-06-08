from funzioniSupermercato import *

wareHouse= {'0001': {'nome': 'pasta', 'prezzo': 1.5, 'quantita': 5},
			'0002': {'nome': 'pasto', 'prezzo': 1.8, 'quantita': 6},
			'0003': {'nome': 'paste', 'prezzo': 2.5, 'quantita': 7}
			}

promozione= set()

registroAcq= []
'----------------------------------------------'
a= True 
while a:
	print('''  
	  premi 1 per inserire un sku
	  premi 2 per modificare lo sku
	  premi 3 per per eliminare uno sku
	  premi 4 per visulizzare gli sku
	  premi 5 per inserire un sku in promozione
	  premi 6 per togliere un sku dalla promozione
	  premi 7 per effettuare un acquisto
	  premi 8 per visualizzare il registro acquisti
	  premi 9 per uscire 
	''')
	
	a= input("  inserisci il numero per effettuare l'operazione corrispondente  ")
	a= 	controlloQuantita(a)

	if a==1:
		sku= input('  inserisci il codice univoco del nuovo prodotto\n  ')
		if wareHouse.get(sku):
			print('  articolo già presente \n  ')
		else:
			nome= input('  inserisci il nome prodotto\n  ')
			prezzo= input('  inserisci il prezzo in numeri\n  ')
			prezzo= controlloPrezzo(prezzo)
			qDisponibile= input('  inserisci la quantità da inserire in intero\n  ')
			qDisponibile= controlloQuantita(qDisponibile)
			aggiungiProdotto(wareHouse, sku, nome, prezzo, qDisponibile)
		print('----------------------\n')
		
	elif a==2:
		sku= input("  inserisci lo sku da modificare\n  ")
		if wareHouse.get(sku):
			nome= input('  aggiorna il nome prodotto\n  ')
			prezzo= input('  aggiorna il prezzo in numeri\n  ')
			prezzo= controlloPrezzo(prezzo)
			qDisponibile= input('  aggiorna la quantità da inserire in intero\n  ')
			qDisponibile= controlloQuantita(qDisponibile)
			aggiungiProdotto(wareHouse, sku, nome, prezzo, qDisponibile)
		else:
			print('  sku non trovata\n  ')
		print('----------------------\n')
		
	elif a==3:
		sku= input('  inserisci la sku da rimuovere\n  ')
		rimuoviProdotto(wareHouse, sku)
		print('----------------------\n')
	
	elif a==4:
		visualizzaProd(wareHouse)
		print('----------------------\n')

	elif a==5:
		sku= input('  inserisci lo sku da aggiungere alle promozioni\n  ')
		addSkuDiscount(wareHouse, promozione, sku)
		print('----------------------\n')

	elif a==6:
		sku= input('  inserisci lo sku da eliminare dalle promozioni\n  ')
		rimuoviSconto(promozione, sku)
		print('----------------------\n')

	elif a==7:
		sku= input('  inserisci la sku da acquistare\n  ')
		if wareHouse.get(sku):
			quantita= True
			while type(quantita) is bool:
				quantita= input('  inserisci la quantità acquistata\n  ')
				quantita= controlloQuantita(quantita)
				quantita= controlloQuantitaAcqustabile(quantita, sku, wareHouse)
			registaAcquisti(registroAcq, wareHouse, promozione, sku, quantita)
			wareHouse[sku]['quantita']= wareHouse[sku]['quantita'] - quantita
		else:
			print('  sku non presente a magazzino  ')
		print('----------------------\n')

	elif a==8:
		visualizzaAcqisti(registroAcq)
		print('----------------------\n')
	
	elif a==9:
		a= False
		
	else:
		print('Hai premuto un bottone fuori dal menu')
