import copy


class Videoteca:
    """
    Questa classe gestisce le funzioni di una videoteca
    """

    def __init__(self):
        """
        il costruttore inizalizza una lista che servira a contenere gli oggetti della class Film
        """
        self.__inventario = []

    def add_film(self, film):
        """
        Aggiunge un film alla lista __inventario

        :param film: potenzialmente può aggiungere ogni cosa alla lisata invetario, però in questo caso vogliamo che sia un oggetto Film, perchè altrimenti nei passi successivi il prgramma andrebbe in errore
        """
        self.__inventario.append(film)

    def get_videoteca(self):
        """
        Questa get ritorna la lista __invetario

        :return: ritorna la lista __invetario
        """
        return self.__inventario

    def get_film(self, titolo):
        """
        Ha la funzione di cercare il titolo nella lista __inventario e ritornare l'oggetto corrispondente

        :param titolo: rapprenta una stringa che viene utilizzata per cercare gli oggetti film paragonandola a __titolo
        :return: ritorna l'oggetto Film nel caso in cuoi abbiamo il match altrimenti ritorna stringa con il messaggio "Titolo non trovato"
        """
        for x in self.get_videoteca():
            nome = x.get_titolo()
            if nome == titolo:
                return x
        return "Titolo non trovato"

    def del_film(self, titolo):
        """
        cancella il film con il titolo corrispondente e rutorna anche dei messaggi di controllo

        :param titolo: indica il titolo del film che si vuole cancellare
        :return: ritorna il messaggio film cancellato se trova il film altrimenti ritorna il messaggio nessuna corrispondenza
        """
        for x in range(len(self.__inventario) - 1, -1, -1):
            if self.__inventario[x].get_titolo() == titolo:
                stampa = copy.deepcopy(self.__inventario[x])
                del self.__inventario[x]
                return f" Cancellato il film {stampa}"
        return "Non ho trovato nussuna corrispendeza da cancellare"

    def __str__(self):
        """
        rappresenta come e cosa deve essere stapato quando viene evocato l'oggetto Videoteca

        :return: ritorna la lista __inventario composta da oggetti
        """
        return self.__inventario
