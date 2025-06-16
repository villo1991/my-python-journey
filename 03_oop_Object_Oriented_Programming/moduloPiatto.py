class Piatto:
    def __init__(self, id, nome, prezzo):
        """
         Inizializza un oggetto Piatto con id, nome e prezzo.

        :param id: Identificativo univoco del piatto.
        :type id: int
        :param nome: Nome del piatto.
        :type nome: str
        :param prezzo: Prezzo del piatto.
        :type prezzo: float
        """
        self.__id = id
        self.__nome = nome
        self.__prezzo = prezzo

    def getPrezzo(self):
        """
        Restituisce il prezzo del piatto.

        :return: Prezzo del piatto.
        :rtype: float
        """
        return self.__prezzo

    def getNome(self):
        """
        Restituisce il nome del piatto.

        :return: Nome del piatto.
        :rtype: str
        """
        return  self.__nome

    def getId(self):
        """
        Restituisce l'identificativo del piatto.

        :return: ID del piatto.
        :rtype: int
        """
        return self.__id

    def __str__(self):
        return f"   Id piatto {self.__id} - nome piatto {self.__nome} - prezzo piatto {self.__prezzo}"