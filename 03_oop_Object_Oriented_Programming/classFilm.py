from datetime import datetime


class Film:
    """
    La classe Film genra oggetti film che servono per la gestione della classe VideoTeca
    """
    def __init__(self, titolo, anno, genere, regista, prezzo):
        """
        Il costruttore genera un oggetto con i seguenti attributi

        :param titolo: si commentano da soli
        :param anno:
        :param genere:
        :param regista:
        :param prezzo:
        """
        self.__titolo = titolo
        self.__anno = anno
        self.__genere = genere
        self.__regista = regista
        self.__disponibilita = ""
        self.__prezzo = prezzo

    def set_film(self, a, b, c, d, f, g):
        """
        se vogliamo modificare un oggetto film dopo la sua creazione possiamo usare il metodo in oggetto
        :param a: titolo
        :param b: anno
        :param c: genere
        :param d: regista
        :param f: diponibilità
        :param g: prezzo
        """
        self.__titolo = a
        self.__anno = b
        self.__genere = c
        self.__regista = d
        self.__disponibilita = f
        self.__prezzo = g

    def get_titolo(self):
        """
        Accede all'attrubuto __titolo

        :return: ritorna l'attributo __titolo
        """
        return self.__titolo

    def get_disponibilita(self):
        """
        Accede all'attrubuto __disponibilita

        :return: ritorna l'attributo __disponibilita
        """
        return self.__disponibilita

    def set_prenota(self):
        """
        Assegna all'attributo __disponibilita l'oggetto datetime.now()
        """
        adesso = datetime.now()
        self.__disponibilita = adesso

    def stampaFile(self):
        """
        questo metodo permette la stampa in modo formattato dell'oggetto ho creato questo metodo perchè __str__ nella riga 60 del foglio mainVideoT mi dava problemi

        :return: ritorna una stringa formattata con i dati dell'oggetto Film
        """
        if not self.__disponibilita:
            disp = 'si'
        else:
            data = self.__disponibilita
            data = data.strftime("%d/%m/%Y")
            disp = f"NO prenotato il {data}"
        s1 = f"Titolo: {self.__titolo} - Anno: {self.__anno} - Genere: {self.__genere} "
        s2 = f"Regista: {self.__regista} - Prezzo: {self.__prezzo} - Disponibile: {disp}"
        return s1 + s2

    def __str__(self):
        """
        questo metodo permette la stampa in modo formattato dell'oggetto

        :return: ritorna una stringa formattata con i dati dell'oggetto Film
        """
        if not self.__disponibilita:
            disp = 'si'
        else:
            data = self.__disponibilita
            data = data.strftime("%d/%m/%Y")
            disp = f"NO prenotato il {data}"
        s1 = f"Titolo: {self.__titolo} - Anno: {self.__anno} - Genere: {self.__genere} "
        s2 = f"Regista: {self.__regista} - Prezzo: {self.__prezzo} - Disponibile: {disp}"
        return s1 + s2
