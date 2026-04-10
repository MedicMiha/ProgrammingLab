import os

class CSVTimeSeriesFiles():
    def __init__(self, nomeFile):
        self.nome = nomeFile
        try:
            letto = open(self.nome, "r")
            letto.close()
        except:
            raise ExamException("Erroe: file nn esiste")
        
    def getData(self):
        letto = open(self.nome, "r")
        liste = []
        #print(letto.read())
        for riga in letto:
            #print(riga)
            rigaPulita = riga.strip('\n')
            
            if rigaPulita != 'dt,LandAverageTemperature':
                lista = rigaPulita.split(",")
                liste.append(lista)
                #print(lista)
        letto.close()
        return liste

def compute_variations(time_series, primoAnno, ultimoAnno, N):
    datiAnnuali = {}
    medieAnnuali = {}
    mediaMobile = {}
    somma = 0.0
    differenza = {}
    if int(ultimoAnno) - int(primoAnno) < int(N):
        raise ExamException("Errore: finestra troppo grande")
    for riga in time_series:
        data = riga[0]
        media = riga[1]
        #print(data)
        dataStrip = data.split('/')
        #print(dataStrip)
        anno = dataStrip[0]
        mese = dataStrip[1]
        if int(anno) >= int(primoAnno) and int(anno) <= int(ultimoAnno):
            #print(anno)
            if not anno in datiAnnuali.keys():
                datiAnnuali[anno] = [media]
                medieAnnuali[anno] = media
            else:
                datiAnnuali[anno].append(media)
                medieAnnuali[anno] = str((float(medieAnnuali[anno]) + float(media))/ 2)
        #print(anno)
        #print(mese)
        
    for anno in medieAnnuali:
        #print(anno)
        if int(anno) >= int('1900')+int(N):
            somma = somma + float(media)
            mediaMobile[anno] = str(somma / int(N))
            #print(mediaMobile[anno])
            
    for anno in mediaMobile:
        differenza[anno] = str(float(medieAnnuali[anno]) - float(mediaMobile[anno]))
    
    #return datiAnnuali
    #return medieAnnuali
    #return mediaMobile
    return differenza

class ExamException():
    pass



nome = "./../esercizi\GlobalTemperatures.csv"
tsf = CSVTimeSeriesFiles(nome)
time_series = tsf.getData()

print(compute_variations(time_series=time_series, primoAnno='1989', ultimoAnno='2002', N='4'))

