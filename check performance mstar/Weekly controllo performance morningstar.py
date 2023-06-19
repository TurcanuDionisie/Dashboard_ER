import numpy as np
import pandas as pd
import os
import datetime
from datetime import datetime as dt
from datetime import timedelta

directory = r'G:\Analisi e Performance Prodotti\Database & Report\Report Manuali\Morningstar Ranking\Check Performance'
directory_universi = r'I:\Documenti\File PMC\In Corso\Universi di Dettaglio'


#%%

# IL CODICE VIENE LANCIATO OGNI SETTIMANA (venerdì), LO STESSO GIORNO IN CUI L'EXCEL VIENE ESPORTATO DA MORNINGSTAR
os.chdir(directory)
today = datetime.datetime.now()
ms_perf = pd.read_excel('Performance BMED check Mstar_Weekly.xls') # + today.strftime("%Y%m%d") + '.xlsx')
dates = ['1M','3M','YTD','1Y','3Y','5Y']

# FILE ADJUSTMENTS
date_perf = ms_perf.iloc[5:7].dropna(axis=1,how='all')
date_perf.columns = dates
date_perf = date_perf.reset_index(drop=True)
ms_perf.columns = ms_perf.iloc[7]
ms_perf = ms_perf.iloc[10:]
ms_perf = ms_perf.dropna(axis=1,how='all')
ms_perf = ms_perf.dropna(how='all')
colnames = list(ms_perf.columns)
colnames[3:9] = dates
ms_perf.columns = colnames
ms_perf = ms_perf.set_index('ISIN')
ms_perf = ms_perf.iloc[:,:8]
ms_perf[dates] = ms_perf[dates].replace('-', np.nan).apply(pd.to_numeric)

#%% importo performance dagli universi

os.chdir(directory_universi)
ie = pd.read_excel('par - universo mif ch&tm altre classi.xlsx', sheet_name='Quota Rettificata Perf')
it = pd.read_excel('par - universo mgf italiani altre classi.xlsx', sheet_name='Quota Pubb Rettificata')
lu = pd.read_excel('par - universo gamax altre classi sintesi.xlsx', sheet_name='Q.ta Pubblicata Rettificata')
es = pd.read_excel('par - universo mge spagna altre classi.xlsx', sheet_name='Quota Pubb Rettificata')    

# FILE ADJUSTMENTS
ie = ie.iloc[1:] 
ie.iloc[0,0] = 'Date' 
ie.columns = ie.loc[1]
ie = ie.iloc[1:].set_index('Date') 
ie = ie.apply(pd.to_numeric)
ie = ie.replace(0,np.nan)
ie.fillna(method='ffill', inplace=True)

it = it.iloc[2:] #drop first line
it.columns.values[0] = 'Date' 
it = it.set_index('Date') 
it = it.apply(pd.to_numeric)
it = it.replace(0,np.nan)
it.fillna(method='ffill', inplace=True)

lu = lu.iloc[1:] #drop first line
lu.iloc[0,0] = 'Date' 
lu.columns = lu.loc[1]
lu = lu.iloc[1:].set_index('Date') 
lu = lu.apply(pd.to_numeric)
lu = lu.replace(0,np.nan)
lu.fillna(method='ffill', inplace=True)

es = es.iloc[1:]
es.iloc[0,0] = 'Date' 
#colonne sono già a posto ma cambiare nome colonna date
es = es.rename(columns={es.columns[0]: 'Date'})
es = es.iloc[1:].set_index('Date') 
es = es.apply(pd.to_numeric)
es = es.replace(0,np.nan)
es.fillna(method='ffill', inplace=True)

#%% PRENDO PERFORMANCE D'INTERESSE DAGLI UNIVERSI
os.chdir(directory)

#sistemo date_perf
for t in date_perf.columns:
    date_perf[t].iloc[0] = (dt.strptime(date_perf[t].iloc[0], '%d/%m/%Y') - timedelta(days=1) ).strftime('%d/%m/%Y')
    date_perf[t].iloc[1] = (dt.strptime(date_perf[t].iloc[1], '%d/%m/%Y') - timedelta(days=1) ).strftime('%d/%m/%Y')


perf_universi = pd.DataFrame(index = ms_perf.index, columns = dates)

for c in perf_universi.index:
    for t in dates:
        today = dt.strptime(date_perf[t].iloc[1], "%d/%m/%Y")
        ref = dt.strptime(date_perf[t].iloc[0], "%d/%m/%Y")
        
        if c.startswith('IE'):
            if c in ie.columns:
                perf_universi[t].loc[c] = ( ie[c].loc[ie.index[ie.index.get_loc(today, method='ffill')]] / ie[c].loc[ie.index[ie.index.get_loc(ref, method='ffill')]] ) -1
            else:
                perf_universi[t].loc[c] = np.nan

        elif c.startswith('IT'):
            if c in it.columns:
                perf_universi[t].loc[c] = ( it[c].loc[it.index[it.index.get_loc(today, method='ffill')]] / it[c].loc[it.index[it.index.get_loc(ref, method='ffill')]] ) -1
            else:
                perf_universi[t].loc[c] = np.nan
            
        elif c.startswith('LU'):
            if c in lu.columns:
                perf_universi[t].loc[c] = ( lu[c].loc[lu.index[lu.index.get_loc(today, method='ffill')]] / lu[c].loc[lu.index[lu.index.get_loc(ref, method='ffill')]] ) -1
            else:
                perf_universi[t].loc[c] = np.nan
        
        elif c.startswith('ES'):
            if c in es.columns:
                perf_universi[t].loc[c] = ( es[c].loc[es.index[es.index.get_loc(today, method='ffill')]] / es[c].loc[es.index[es.index.get_loc(ref, method='ffill')]] ) -1
            else:
                perf_universi[t].loc[c] = np.nan


#ANNUALIZZO PERFORMANCE A 3Y e 5Y  

delta3y = (dt.strptime(date_perf[dates[4]].iloc[1], '%d/%m/%Y') - dt.strptime(date_perf[dates[4]].iloc[0], '%d/%m/%Y')).days
perf_universi[dates[4]] = (1 + perf_universi[dates[4]])**(365/delta3y) -1 

delta5y = (dt.strptime(date_perf[dates[5]].iloc[1], '%d/%m/%Y') - dt.strptime(date_perf[dates[5]].iloc[0], '%d/%m/%Y')).days
perf_universi[dates[5]] = (1 + perf_universi[dates[5]])**(365/delta5y) -1 


perf_universi.to_excel('python/output/check_perf_universi_weekly.xlsx')
   
#%% CHECK CHE UNIVERSI E MORNINGSTAR ABBIANO STESSI NA

perf_universi.isna().equals(ms_perf[dates].isna())   
#%% CALCOLO DELTA Morningstar vs Universi
os.chdir(directory)

delta = ms_perf[dates]/100 - perf_universi         
# delta = delta.applymap(lambda x: round(x, 4))

delta.to_excel('python/output/Delta Universi vs MStar_weekly.xlsx')
#%%  INVIO EMAIL AUTOMATICA CON LISTA DEI DELTA

import win32com.client as win32

df = delta.replace(0,np.nan)
#solo se superiore alla soglia 
df = df[abs(df) >= 0.0002].dropna(how='all')
#df = df.dropna(axis=1, how='all')

df = df.fillna('')
# Format the DataFrame as percentages with two decimal places
df = df.applymap(lambda x: f"{x*100:.2f}%" if isinstance(x, float) else x)


# Define email parameters
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'monitoraggio.analisi.performance@mediolanum.it'
mail.Subject = 'Segnalazioni delta Performance Universi vs Mstar (Weekly)'

    
if not (df == np.nan).all().all():
    # Add dataframe to email body
    mail.HTMLBody = f'<p>Ciao,</p><p>Questa settimana, da verificare i seguenti delta tra le performance degli Universi e quelle calcolate da Morningstar.</p><p>{df.to_html()}</p>'

else:
    # Add dataframe to email body
    mail.HTMLBody = f'<p>Ciao,</p><p>Questa settimana, non sono risultati delta significativi tra le performance degli Universi e quelle calcolate da Morningstar.</p>'

# Send email
mail.Send()
print('Email sent')