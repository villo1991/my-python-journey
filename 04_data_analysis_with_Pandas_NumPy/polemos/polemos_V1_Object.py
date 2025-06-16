import pandas as pd
from scipy import stats
from scipy.stats import median_abs_deviation


class Clean_dataframe:
    """
    Classe per la pulizia automatica di un DataFrame caricato da file CSV.
    
    Attributi privati:
        __df (pd.DataFrame): Il DataFrame principale caricato.
        __errore (bool): Flag per indicare eventuali errori nel caricamento del file.
        __colonneNaN34 (pd.Index): Colonne eliminate con più del 34% di valori NaN.
        __righeNaN (pd.Index): Righe eliminate con tutti valori NaN.
        __righeNaN25 (pd.Index): Righe eliminate con più del 25% di NaN.
        __righeDup (pd.Index): Righe duplicate eliminate.
        __colonneNaNStr (pd.Index): Colonne object con ≤ 20% di stringhe sostituite.
        __colonneObjStr (pd.Index): Colonne object con ≥ 40% di stringhe da analizzare.
        __colonneObjNum (pd.Index): Colonne object con 20-40% di stringhe eliminate.
    """

    def __init__(self, nomecsv: str, head: bool = True):
        """
        Inizializza l'oggetto Clean_dataframe caricando un CSV.

        Args:
            nomecsv (str): Percorso del file CSV da caricare.
            head (bool): Se True, stampa le informazioni sul DataFrame.
        """
        try:
            self.__df = pd.read_csv(nomecsv)
            self.__errore = False
            if head:
                self.__df.info()
                print()
        except Exception:
            print("Il file non ha un formato valido o il percorso è inesistente")
            self.__errore = True

        self.__colonneNaN34 = None
        self.__righeNaN = None
        self.__righeNaN25 = None
        self.__righeDup = None
        self.__colonneNaNStr = None
        self.__colonneObjStr = None
        self.__colonneObjNum = None

    def getErrore(self) -> bool:
        """Restituisce True se c'è stato un errore nel caricamento del file, False altrimenti."""
        return self.__errore

    def getDf(self) -> pd.DataFrame:
        """Restituisce il DataFrame attuale."""
        return self.__df

    def deleteDuplicate(self):
        """
        Elimina le righe duplicate dal DataFrame.
        """
        dup = self.__df[self.__df.duplicated()].index
        self.__righeDup = dup
        print(f"Eliminate le seguenti righe duplicate: {self.__righeDup}")
        self.__df.drop_duplicates(inplace=True)

    def deleteNaNLines(self):
        """
        Elimina le righe che contengono solo valori NaN.
        """
        nanRighe = self.__df[self.__df.isna().all(axis=1)].index
        self.__righeNaN = nanRighe
        print(f"Eliminate le seguenti righe tutte NaN: {self.__righeNaN}")
        self.__df.dropna(axis=0, how='all', inplace=True)

    def deleteColumsNaN34(self, soglia: float = 0.34):
        """
        Elimina colonne con una percentuale di NaN superiore alla soglia.

        Args:
            soglia (float): Percentuale massima di NaN ammessa (default 0.34).
        """
        percentuale_col_nan = self.__df.isna().mean()
        colonne = percentuale_col_nan[percentuale_col_nan > soglia].index
        self.__colonneNaN34 = colonne
        print(f"Eliminate le seguenti colonne con più del {int(soglia * 100)}% di NaN: {self.__colonneNaN34}")
        self.__df.drop(columns=colonne, inplace=True)

    def deleteLinesNaN25(self, soglia: float = 0.25):
        """
        Elimina righe con una percentuale di NaN superiore alla soglia.

        Args:
            soglia (float): Percentuale massima di NaN ammessa per riga (default 0.25).
        """
        percentuale_lines_nan = self.__df.isna().mean(axis=1)
        indici = self.__df.index[percentuale_lines_nan > soglia]
        self.__righeNaN25 = indici
        print(f"Eliminate le seguenti righe con più del {int(soglia * 100)}% di NaN: {self.__righeNaN25}")
        self.__df.drop(indici, inplace=True)

    def cleanObjectColumns(self, soglia0: float = 0.2, soglia1: float = 0.4):
        """
        Analizza le colonne object e decide se eliminarle, mantenerle o imputarle.

        Args:
            soglia0 (float): Soglia inferiore per stringhe su colonne numeriche.
            soglia1 (float): Soglia superiore per stringhe su colonne numeriche.
        """
        colonneObject = self.__df.dtypes[self.__df.dtypes == "object"].index
        df1 = self.__df[colonneObject].apply(pd.to_numeric, errors="coerce")
        df2 = df1.isna() & self.__df[colonneObject].notna()

        selezione = df2.loc[:, df2.mean() == 1].columns
        if len(selezione) != 0:
            print(f"Colonne solo stringa escluse dall'analisi: {selezione}")
            df1.drop(columns=selezione.tolist(), inplace=True)
            df2.drop(columns=selezione.tolist(), inplace=True)

        selezione = df2.loc[:, (df2.mean() > soglia0) & (df2.mean() < soglia1)].columns
        if len(selezione) != 0:
            self.__colonneObjNum = selezione
            print(f"Eliminate colonne object con percentuale tra {soglia0} e {soglia1} di valori str: {selezione}")
            self.__df.drop(columns=selezione.tolist(), inplace=True)

        selezione = df2.loc[:, df2.mean() >= soglia1].columns
        if len(selezione) != 0:
            print(f"Colonne da analizzare separatamente (> {soglia1} str): {selezione}")
            self.__colonneObjStr = selezione

        selezione = df2.loc[:, df2.mean() <= soglia0].columns
        if len(selezione) != 0:
            self.__colonneNaNStr = selezione
            self.sostValNaNStr(selezione)

    def cleanColummsNum(self):
        """
        Imputa i valori mancanti per le colonne numeriche.
        """
        colonneObject = self.__df.dtypes[self.__df.dtypes != "object"].index
        self.sostValNaNStr(colonneObject)

    def sostValNaNStr(self, colonne):
        """
        Imputa i valori NaN con media o mediana a seconda della distribuzione.

        Args:
            colonne (iterable): Lista di nomi delle colonne da imputare.
        """
        for x in colonne:
            series = pd.to_numeric(self.__df[x], errors="coerce")
            serieNum = series[series.notna()]
            stat, p = stats.shapiro(serieNum)
            if p > 0.05:
                media = serieNum.mean()
                posNaN = series[series.isna()].index
                self.__df.loc[posNaN, x] = media
            else:
                mediana = serieNum.median()
                posNaN = series[series.isna()].index
                self.__df.loc[posNaN, x] = mediana
            self.__df[x] = pd.to_numeric(self.__df[x])

    def outLier(self, normalizzare: bool = True):
        """
        Elimina gli outlier usando Z-score o MAD a seconda della distribuzione.

        Args:
            normalizzare (bool): Se True, usa Z-score per distribuzioni normali.
        """
        indici_da_eliminare = set()
        colonneObject = self.__df.dtypes[self.__df.dtypes != "object"].index
        for x in colonneObject:
            series = pd.to_numeric(self.__df[x], errors="coerce")
            serieNum = series[series.notna()]
            stat, p = stats.shapiro(serieNum)
            if p > 0.05:
                punteggi_z = stats.zscore(serieNum) if normalizzare else serieNum
                esito = abs(punteggi_z) > 3
            else:
                mediana = serieNum.median()
                mad = median_abs_deviation(serieNum, scale='normal')
                z_robusto = (serieNum - mediana) / mad
                esito = abs(z_robusto) > 3.4

            indici = serieNum[esito].index
            indici_da_eliminare.update(indici)

        self.__df.drop(index=indici_da_eliminare, inplace=True)

    def statistiche(self):
        """Stampa statistiche descrittive del DataFrame."""
        print(self.__df.describe(include="all"))

    def info(self):
        """Mostra le informazioni sul DataFrame."""
        self.__df.info()

    def visualizzaDataframe(self):
        """Stampa il contenuto del DataFrame."""
        print(self.__df)

    def salva(self):
        """
        Salva il DataFrame in un file CSV con nome scelto dall’utente.
        """
        finale = ".csv"
        nomeDataFrameMain = input("Scrivi un nome valido per salvare il file del DataFrame principale senza l'estensione: ")
        nomeDataFrameMainF = nomeDataFrameMain + finale

        try:
            self.__df.to_csv(nomeDataFrameMainF, index=False)
            print("File salvato correttamente.")
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")

    def visualizzaColonneLavorate(self):
        """Stampa un riepilogo delle colonne e righe modificate."""
        print(f"""
        Righe duplicate eliminate: {self.__righeDup}
        Righe tutte NaN eliminate: {self.__righeNaN}
        Righe con >25% NaN eliminate: {self.__righeNaN25}
        Colonne con >34% NaN eliminate: {self.__colonneNaN34}
        Colonne object con 20-40% str eliminate: {self.__colonneObjNum}
        Colonne object con >40% str da analizzare: {self.__colonneObjStr}
        Colonne object con ≤20% str imputate: {self.__colonneNaNStr}
        """)


class Menu:
    """
    Classe per gestire il menu di interazione utente.
    
    Attributi:
        __menu (str): Testo del menu da mostrare.
    """

    def __init__(self):
        """
        Inizializza il menu delle operazioni disponibili.
        """
        self.__menu = """
        Selezionare una delle opzioni da adottare per il DataFrame caricato tramite CSV:
        1. Pulizia delle sole righe tutte NaN e duplicate...
        """
