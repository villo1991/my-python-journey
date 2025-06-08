
libreria = [{'titolo': '1984', 'autore' : 'F. Scott Fitzgerald', 'anno': 1949 , 'genere': 'Fantascienza Sociale'},
		{'titolo': 'Il Grande Gatsby', 'autore' : 'F. Scott Fitzgerald', 'anno': 1925 , 'genere': 'Romanzo'},
		{'titolo': 'Orgoglio e Pregiudizio', 'autore' : 'Jane Austen', 'anno': 1813 , 'genere': 'Romanzo'},
		{'titolo': "Il Signore degli Anelli: La Compagnia dell'Anello", 'autore' : 'J.R.R. Tolkien', 'anno': 1949 , 'genere': 'Avventura'},
		{'titolo': "Cent'anni di Solitudine", 'autore' : 'Gabriel García Márquez', 'anno': 1967 , 'genere': 'Realismo Magico'}
		]
		

genreiLetterari= set()
print(" stampiamo la lista dei generi presenti nel dizionario 'libreria'\n")
for libro in libreria:
	genreiLetterari.add(libro['genere'])
cont=1
for x in genreiLetterari:
	print(f' Genere {cont} = {x}')
	cont+=1

print("\n\n")

anno=[]
for libro in libreria:
	contAnno=[]
	contAnno.append(libro['anno'])
	contAnno.append(libro['titolo'])
	contAnno.append(libro['autore'])
	contAnno.append(libro['genere'])
	tupla= tuple(contAnno)
	anno.append(tupla)
anno.sort()

print('Elenco dei libri odinato per anno e titolo\n')
cont1=1
for x in anno:
	print(f'{cont1}. Anno pubblicazione: {x[0]} - titolo: {x[1]}')
	cont1+=1

print("\n\n")

print(" Stampiamo la lista dei libri presenti nel dizionario 'libreria' scrivendo 'titolo' e 'autore' di ciascuno\n" )
cont2=1
for x in anno:
	print(f'{cont2}. titolo: {x[1]} - autore: {x[2]}')
	cont2+=1

print("\n\n")
tuplaAutori= ()
listaAutori=[]
genreiAutori= set()
print(" stampiamo la lista degli autori presenti nel dizionario 'libreria'\n")
for libro in libreria:
	genreiAutori.add(libro['autore'])
listaAutori= list(genreiAutori)
listaAutori.sort()
tuplaAutori= tuple(listaAutori)
cont3=1
for x in tuplaAutori:
	print(f'{cont3} Autore: {x}') 
	cont3+=1
print("\n\n")

nuovoLibro= input(''' per aggiornare il dizonario premi qualsiasi bottone, se non vuoi aggiornare premi invio\n''')
sensore=0	
while nuovoLibro :
	nuovoLibro= input(''' per aggiornare il dizonario inserisci un nuovo titolo o '.' per finire con l'aggiornamento.\n''')
	if nuovoLibro=='.':
		nuovoLibro= False
	elif nuovoLibro :
		diz= {}
		diz['titolo']= nuovoLibro
		diz['autore']= input("inserisci l'autore\n")
		numero=input("inserisci l'anno in numeri\n")
		while not numero.isdigit():  #licenza poetica ahah
			numero=input("inserisci l'anno in numeri\n") 
		numero= int(numero)
		diz['anno']= numero
		diz['genere']= input("inserisci il genere\n")
		libreria.append(diz)
		sensore+=1

if sensore >= 1:
	anno=[]
	for libro in libreria:
		contAnno=[]
		contAnno.append(libro['titolo'])
		contAnno.append(libro['anno'])
		contAnno.append(libro['autore'])
		contAnno.append(libro['genere'])
		tupla= tuple(contAnno)
		anno.append(tupla)
	anno.sort()
	
	print("Stampo il data base ordinato per titolo libro' \n")
	for x in anno:
		print(f" Titolo libro {x[0]} - anno pubblicazione {x[1]} -  autore {x[2]} - genre {x[3]}")
