def addContact( rubrica , nome, numero):
	if rubrica.get(nome):
		print(f'  Il nome {nome} è gia presente vuoi aggiornare il numero {rubrica[nome]} con il numero {numero}')
		print('  premi invio pre annullare o qualsisi altro tasto per aggiornare')
		if input('  '):
			rubrica[nome] = numero
			print('aggiornato')
	else:
		rubrica[nome] = numero


def visCont(rubrica):
	print(f'lista contatti in rubrica')
	for nome , numero in rubrica.items():
		print(f'contatto: {nome} ha il numero {numero}') 
	

def cercaCont(rubrica, nome):
	return rubrica.get(nome, 'Nome non trovato')
	

def rimuoviContatto(rubrica, nome):
	if rubrica.get(nome): 
		del rubrica[nome]
	else:
		print('contatto non presente')
	visCont(rubrica)
	

def numeriUnici(rubrica):
	insieme= set()
	for numero in rubrica.values():
		insieme.add(numero)
	return insieme

"-------------------------------------------------------------------------"
rubrica={
		'marco': 3342817720, 'fra': 455646464, 'gio': 45998915, 'andrea': 3342817720,
		'ele': 545454646, 'eri': 455646464
		}

addContact(rubrica, 'marco', 33664984)
print('\n\n\n')
visCont(rubrica)
print('\n\n\n')
print(cercaCont(rubrica, 'marco'))
print('\n\n\n')
print(cercaCont(rubrica, 'luca'))
print('\n\n\n')
rimuoviContatto(rubrica, 'luca')
print('\n\n\n')
print(numeriUnici(rubrica))
