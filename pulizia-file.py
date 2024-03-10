import pandas as pd

# importo file

df = pd.read_excel('Opinioni su ruoli tradizionali - regione.xlsx')
#tramite il file json, costruisco un dizionario per fare le sostituizioni nel file excel
# dizionario di sostituzione
sostituzioni_area = {
    'IT': 'Italia',
    'ITC': 'Nord-ovest',
    'ITC1': 'Piemonte',
    'ITC2': "Valle d'Aosta / Vallée d'Aoste",
    'ITC3': 'Liguria',
    'ITC4': 'Lombardia',
    'ITD': 'Nord-est',
    'ITD1': 'Provincia Autonoma Bolzano / Bozen',
    'ITD2': 'Provincia Autonoma Trento',
    'ITD3': 'Veneto',
    'ITD4': 'Friuli-Venezia Giulia',
    'ITD5': 'Emilia-Romagna',
    'ITDA': 'Trentino Alto Adige / Südtirol',
    'ITE': 'Centro',
    'ITE1': 'Toscana',
    'ITE2': 'Umbria',
    'ITE3': 'Marche',
    'ITE4': 'Lazio',
    'ITF': 'Sud',
    'ITF1': 'Abruzzo',
    'ITF2': 'Molise',
    'ITF3': 'Campania',
    'ITF4': 'Puglia',
    'ITF5': 'Basilicata',
    'ITF6': 'Calabria',
    'ITG1': 'Sicilia',
    'ITG2': 'Sardegna'
}



# i valori nella colonna desiderata
sostituzioni_stereotipo = {
'MISUCWOR': "per l'uomo, più che per la donna, è molto importante avere successo nel lavoro",
"MLESHOUS": "gli uomini sono meno adatti ad occuparsi delle faccende domestiche",
'MPRFAM': "è soprattutto l'uomo che deve provvedere alle necessità economiche della famiglia",
'MTAKEDE': "è l'uomo che deve prendere le decisioni più importanti riguardanti la famiglia",
'PRIOMEN': "in condizioni di scarsità di lavoro, i datori di lavoro dovrebbero dare la precedenza agli uomini rispetto alle donne"}

sostituzioni_titolo_studio= {
'CLF_ML':  'laurea o diploma universitario',
'NP': 'licenza di scuola elementare, nessun titolo di studio',
'ALL': 'ALL',
'LSE': 'licenza di scuola media inferiore o di avviamento professionale',
'USE_IF': 'diploma di istruzione secondaria di II grado o di qualifica professionale (corso di 3-4 anni) compresi IFTS'
}

sostituzione_grado_accordo = {
'NOANSW': 'non risponde',
'SOMAGR': "abbastanza d'accordo",
'SOMDISAG': "poco d'accordo",
'STRAGR': "molto d'accordo",
'STRODIS': "per niente d'accordo",
'TOT': "TOT"}

sostituzione_stereotipi_violenza = {
"HUSFNVIO":"se un marito/compagno obbliga la moglie/compagna ad avere un rapporto sessuale contro la sua volontà, non è una violenza",
"OACVIF":"spesso le accuse di violenza sessuale sono false",
'SEWNRAP': "le donne serie non vengono violentate",
'WABLAVO': "le donne che non vogliono un rapporto sessuale riescono a evitarlo",
'WOFSREM':"di fronte a una proposta sessuale le donne spesso dicono no ma in realtà intendono sì",
"WPROVSEX":"le donne possono provocare la violenza sessuale con il loro modo di vestire",
"WSVADRE":"se una donna subisce una violenza sessuale quando è ubriaca o è sotto l'effetto di droghe è almeno in parte responsabile"
}


df['Stereotipi sui ruoli di genere, comportamenti nella coppia'] = df['Stereotipi sui ruoli di genere, comportamenti nella coppia'].map(sostituzioni_stereotipo)
df['Area'] = df['Area'].map(sostituzioni_area)
df['Grado di accordo'] = df['Grado di accordo'].map(sostituzione_grado_accordo)

df2 = pd.read_excel('Opinioni su violenza sessuale-eta.xlsx')
df2['Area']= df2['Area'].map(sostituzioni_area)
df2['Grado di accordo'] = df2['Grado di accordo'].map(sostituzione_grado_accordo)
df2['Stereotipi sulla violenza sessuale'] = df2['Stereotipi sulla violenza sessuale'].map(sostituzione_stereotipi_violenza)

df3 = pd.read_excel('Opinioni su violenza sessuale - istruzione.xlsx')
df3['AREA']= df3['AREA'].map(sostituzioni_area)
df3['Grado di accordo'] = df3['Grado di accordo'].map(sostituzione_grado_accordo)
df3['Stereotipi sulla violenza sessuale'] = df3['Stereotipi sulla violenza sessuale'].map(sostituzione_stereotipi_violenza)
df3['Livello di istruzione'] = df3['Livello di istruzione'].map(sostituzioni_titolo_studio)

df4= pd.read_excel('Opinioni-violenza-sessuale-regione.xlsx')
df4['Area'] = df4['Area'].map(sostituzioni_area)
df4['Grado di accordo'] = df4['Grado di accordo'].map(sostituzione_grado_accordo)
df4['Stereotipi sulla violenza sessuale'] = df4['Stereotipi sulla violenza sessuale'].map(sostituzione_stereotipi_violenza)
#Salvo file excel
#df4.to_excel('Opinioni violenza sex regioni puliti.xlsx')
#df2.to_excel('Opinioni su violenza sessuale eta-puliti.xlsx', index=False)
#df.to_excel('Opinioni-ruoli-tradizionali-regione-cleaned.xlsx', index=False) 
#df3.to_excel('Opinioni violenza sessuale-istruzione-puliti.xlsx', index=False)

sostituzione_comportamenti = {
    "HABCONTR": "un uomo controlla abitualmente il cellulare, l'attività sui social network della moglie/compagna",
    "NSMOCC": "in una relazione di coppia è normale che ci scappi uno schiaffo ogni tanto",
    "SLGIROC": "un ragazzo schiaffeggia la sua fidanzata perché ha civettato/flirtato con un altro uomo"
}

sostituzione_grado_accettabilit = {
    "ACUNDCIR": 'in certe circostanze accettabile',
    "ALWACC":"sempre accettabile",
    "NEVACC":"mai accettabile",
    "NOANSW": "non risponde",
    "TOT": "TOT"
}

df5= pd.read_excel('Accettabilità-violenza-.xlsx')
df5['Area'] = df5['Area'].map(sostituzioni_area)
df5['Comportamento nella coppia'] = df5['Comportamento nella coppia'].map(sostituzione_comportamenti)
df5['Grado di accettabilità'] = df5['Grado di accettabilità'].map(sostituzione_grado_accettabilit)
df5.to_excel('Accettabilità violenza-regioni-pulito.xlsx', index= False)


df7= pd.read_excel('Accettabilità violenza nella coppia-livello.xlsx')
df7['Area'] = df7['Area'].map(sostituzioni_area)
df7['Comportamento nella coppia'] = df7['Comportamento nella coppia'].map(sostituzione_comportamenti)
df7['Grado di accettabilità'] = df7['Grado di accettabilità'].map(sostituzione_grado_accettabilit)
df7['Livello di istruzione'] = df7['Livello di istruzione'].map(sostituzioni_titolo_studio)
df7.to_excel('Accettabilità violenza nella coppia-livello-pulito.xlsx', index= False)


df6 = pd.read_excel('Accettabilità violenza nella coppia-eta.xlsx')
df6['Area'] = df6['Area'].map(sostituzioni_area)
df6['Comportamento nella coppia'] = df6['Comportamento nella coppia'].map(sostituzione_comportamenti)
df6['Grado di accettabilità'] = df6['Grado di accettabilità'].map(sostituzione_grado_accettabilit)
df6.to_excel('Accettabilità violenza-età-pulito.xlsx', index= False)

