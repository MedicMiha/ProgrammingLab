nomeFile = "./../esercizi/GlobalLandTemperaturesByCountry.csv"

class CSVTimeSeriesFile():
    def __init__(self, nome):
        self.nome = nome
        
    def getData(self, paese):
        letto = open(self.nome, "r")
        
        for riga in letto:
            rigaPulita = riga.strip('\n')
            #print(rigaPulita)
            colonne = rigaPulita.split(',')
            #print(colonne[1])
            print(f"num colonne: {len(colonne)} | colonne: {colonne}")
            '''if len(colonne) == 3:
                continue
                
            anno = colonne[0]
            temp = colonne[1]
            colonnaPaese = colonne[2]
            
            if temp == '':
                continue
            
            #print(colonnaPaese)
            if colonnaPaese == paese:
                print(anno)'''
           
        letto.close() 
            
TSF = CSVTimeSeriesFile(nomeFile)
time_serie = TSF.getData("Italia")
