def verifica_int_positivo(stringa):
    '''
	verifica che la stringa inserita sia un numero intero positivo maggore di zero

	:param stringa: è il valore stringa da confrontare
	:return: ritorna False se incontra come primo carattere qualsiasi carattere che non sia un numero o un +, mentre ritorna True se c'e al massimo un + come primo cattere e gli altri catteri sono solo cifre numeriche
    '''
    stato = 0
    for c in stringa:
        if (stato == 0):
            if (c == "0"):
                stato = 3
                return False
            elif (c.isdigit()):
                stato = 1
            elif (c in {'+'}):
                stato = 2
            else:
                stato = 3
                return False
        elif (stato == 1):
            if (c.isdigit()):
                stato = 1
            else:
                stato = 3
                return False
        elif (stato == 2):
            if (c.isdigit()):
                stato = 1
            else:
                stato = 3
                return False

    return bool(stato == 1)


def inserimento_intero(stringa):
    '''
    Valuta se la stringa inserita a video è un in intero positivo, se non lo è continua a riproporre di inserire la stringa finché è valida per la conversione

    :param stringa: stringa da testare
    :return: ritorna il valore della stringa convertito in int
    '''
    BxC = False
    while not BxC:
        Bx = input(stringa)
        BxC = verifica_int_positivo(Bx)
        if BxC:
            Bx = int(Bx)
            return Bx


def verificaFloat(stringa):
    '''
    Valuta se la stringa inserita a video è convertibile in float, se non lo è continua a riproporre di inserire la stringa finché è valida per la conversione

    :param stringa: stringa da testare
    :return: ritorna il valore della stringa convertito in float
    '''
    BxC = False
    while not BxC:
        Bx = input(stringa)
        BxC = verifica_float(Bx)
        if BxC:
            Bx = float(Bx)
            return Bx


def verifica_float(stringa):
    '''
   	verifica che la stringa inserita sia convertible in un float escludendo i numeri che iniziano con un punto e poi continuano con sole cifre

    :param stringa: è il parametro stringa che viene accettato dalla funzione
    :return: ritorna True se il numero è convertibile in float o False se non lo è
    '''
    i = 0
    stato = 0

    while (i < len(stringa)):
        c = stringa[i]
        if (stato == 0):
            if (c.isdigit()):
                stato = 1
            elif (c in {'+', '-'}):
                stato = 2
            else:
                stato = 3
                return False
        elif (stato == 1):
            if (c.isdigit()):
                stato = 1
            elif (c == '.'):
                stato = 4
            else:
                stato = 3
                return False
        elif (stato == 2):
            if (c.isdigit()):
                stato = 1
            else:
                stato = 3
                return False
        elif (stato == 4):
            if (c.isdigit()):
                stato = 5
            else:
                stato = 3
                return False
        elif (stato == 5):
            if (not c.isdigit()):
                stato = 3

        i += 1

    return stato == 1 or stato == 5
