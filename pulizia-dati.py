import pandas as pd

# Carica il file Excel
df = pd.read_excel('lavoro1.xlsx')

# Conversione della colonna delle percentuali da testo a valore numerico
df['OBS_VALUE'] = df['OBS_VALUE'].str.replace('%', '').str.replace('.', '').str.replace(',', '.').astype(float) / 100

#i numeri erano formmattati in modo strano (00.00.00)

# Funzione per dividere solo i numeri sopra le migliaia
def divide_sopra_migliaia(x):
    if pd.notna(x):
        if isinstance(x, (int, float)) and x > 1000:
            return x / 100
    return x

# Applica la funzione solo ai valori sopra le migliaia
df['%'] = df['OBS_VALUE'].apply(lambda x: divide_sopra_migliaia(x) if pd.notna(x) else x)


# Salvare il DataFrame
df.to_excel('lavoro.xlsx',index=False)
