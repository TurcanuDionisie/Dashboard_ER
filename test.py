import pandas as pd
import numpy as np


podio = pd.read_excel(r'C:\Users\Dionisie.Turcanu\Documents\GitHub\Top_performer\dati_podio.xlsx', sheet_name='x dashboard')

podio= podio.set_index('isin')


tab = pd.DataFrame(index = ['rk_net','rk_gross','er_net','er_gross','perf'], columns=['Categoria','1M','3M','YTD','1Y','2022','2021','2020'])


dettaglio_fondo = 'IE00B1P83V78'


for t in ['1M','3M','YTD','1Y','2022','2021','2020']:
    tab[t].loc['rk_net'] = str(np.array(int(round(podio['net_'+t].loc[dettaglio_fondo]*100,0))))
    tab[t].loc['rk_gross'] = str(np.array(int(round(podio['gross_'+t].loc[dettaglio_fondo]*100,0))))
    tab[t].loc['er_net'] = str(np.array(float(round(podio['ernetto_'+t].loc[dettaglio_fondo]*100,2)))) +'%'
    tab[t].loc['er_gross'] = str(np.array(float(round(podio['erlordo_'+t].loc[dettaglio_fondo]*100,2)))) +'%'
    tab[t].loc['perf'] = str(np.array(float(round(podio['perf_'+t].loc[dettaglio_fondo]*100,2)))) +'%'



tab['Categoria'].loc['rk_net'] = "CIAO"

tab['Categoria'].loc['rk_gross'] = podio['NOME_CAT'].loc[dettaglio_fondo]


tab = tab.rename(index={'rk_net':'Net Rank',
                        'rk_gross':'Gross Rank',
                        'er_net':'ER Net',
                        'er_gross':'ER Gross',
                        'perf':'Perf. Absolute',
                        })

tabs = [{
     "cat": tab["Categoria"].loc[i],
     "type": i,
     "m1": tab["1M"].loc[i],
     "m3": tab["3M"].loc[i],
     "ytd": tab["YTD"].loc[i],
     "y1": tab["1Y"].loc[i],
     "_2022_": tab["2022"].loc[i],
     "_2021_": tab["2021"].loc[i],
     "_2020_": tab["2020"].loc[i],
     
 }for i in tab.index] 
