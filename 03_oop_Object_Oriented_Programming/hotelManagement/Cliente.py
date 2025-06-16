class Cliente:
    def __init__(self, nome, cognome):
        """
        Il costruttore assegna ai due parametri i valori passando per il metodo imposta_anagrafica()

        :param nome: definisce il nome del cliente
        :param cognome: definisce il cognome del cliente
        """
        self.__cognome = None
        self.__nome = None
        self.imposta_anagrafica(nome, cognome)

    def imposta_anagrafica(self, nome, cognome):
        """
        assegna i valori ai parametri nome e cognome, che sono attributi privati

        :param nome: nome cliente
        :param cognome: cognome cliente
        """
        self.__nome = nome
        self.__cognome = cognome

    def get_nome(self):
        """
        :return: Ritorna il nome del cliente
        """
        return self.__nome

    def get_cognome(self):
        """
        :return: Ritorna il cognome del cliente
        """
        return self.__cognome

    def __str__(self):
        """
        :return: ritorna una lista formattata con il nome e il cognome del cliente
        """
        return f"cliente - nome:{self.__nome}, cognome:{self.__cognome}"
