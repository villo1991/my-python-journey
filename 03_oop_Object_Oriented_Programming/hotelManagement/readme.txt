L'applicazione viene eseguita tramite il file appPrenotazioni.py, che si serve di ogetti e funzioni definiti sui seguenti moduli:

1_ file Cliente.py: contiene l'oggetto Cliente, che gestisce le anagrafiche dei clienti
2_ file Stanza.py: contiene l'oggetto Stanza, che gestisce i paramentri di una stanza definiti dai seguenti parametri:
   tipologia stanza, optional stanza e se è associato un oggetto Cliente all'attributo cliente
3_ file Hotel.py: contiene l'oggetto Hotel, che gestisce e rappresenta lo stato del hotel,
   inoltre sono presenti delle funzioni, che si occupano di interagire con database per salvare e caricare i dati a sistema

Restano da descivere i tre file:
1_ file dataBaseStanze.py: contiene il numero e gli attributi di ogni stanza, da passare all'oggetto Hotel
2_ file dataBaseClienti.py: contiene i dati dei clieni che hanno penottato
3_ file dataBasePrenotazioneStanza.py: permette il salvataggio dei clienti, che hanno prenotato la stanza al momento dell'
   esecuzione del programma avendo poi la possibilità di recuperare i dati


tipologia;optional
1;0,2
2;1
0;2
1;
2;0,1,2
0;1
1;0
2;
0;0,2
1;1



Nome;Cognome
antonello;villani
marisa;cignoli


antonello;villani
marisa;cignoli
marco giuseppe;villani
giovanni;favetti
federico;silva
federica;silva