from moduloPiatto import Piatto


class Menu:
    """
    Classe per rappresentare il menu di un ristorante.

    Il menu viene caricato da un file CSV contenente le informazioni sui piatti.
    """
    def __init__(self):
        self.__listaPiatti = []

        menu = open("menu.csv", "r")
        for riga in menu:
            if "idPiatto;NomePiatto;prezzo" != riga.strip():
                listaRiga = riga.strip().split(";")
                piatto = Piatto(listaRiga[0], listaRiga[1], listaRiga[2])
                self.__listaPiatti.append(piatto)
        menu.close()

    def visualizzaMenu(self):
        """
        Visualizza il menu stampando la lista dei piatti disponibili.
        """
        for x in self.__listaPiatti:
            print(x)

    def numeroPiatti(self):
        """
        Restituisce il numero totale di piatti presenti nel menu.

        Returns: Numero di piatti nel menu.
        """
        return len(self.__listaPiatti)

    @staticmethod
    def visualizzaOpzioni():
        """
        Visualizza le opzioni disponibili nel menu principale del sistema di gestione ordini.
        """
        print("""
        1) Visualizzazione del Menu
        2) Registrazione degli Ordini, aggungi piatto a ordine ancora da pagare, elimina piatti
        3) Calcolo del Totale
        4) Riepilogo degli ordini e assegna il pagamento ad un ordine 
        5) Salvataggio degli ordini
        6) Caricamento degli ordini
        7) Uscita
        """)