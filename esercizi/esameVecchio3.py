nomeFile = "./../esercizi/GlobalLandTemperaturesByCountry.csv"

class CSVTimeSeriesFile():
    def __init__(self, nome):
        self.nome = nome
        
    def getData(self, paese):
        letto = open(self.nome, "r")
        lista = []
        for riga in letto:
            pulita = riga.strip('\n')
            rigaPulita = pulita.strip(';')
            colonne = rigaPulita.split(',')
            
            if not colonne == ['','',''] and len(colonne) == 3:
                anno = colonne[0]
                temp = colonne[1]
                colonnaPaese = colonne[2]
                if colonnaPaese == paese:
                    lista.append([anno, temp])
        letto.close()
        return lista
        
            
TSF = CSVTimeSeriesFile(nomeFile)
time_serie = TSF.getData("Italy")
print(time_serie)