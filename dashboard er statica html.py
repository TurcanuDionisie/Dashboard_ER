import pandas as pd
import os
import matplotlib as plt
import numpy as np
import datetime
import warnings

import io
import base64
import matplotlib.pyplot as plt
import plotly.graph_objects as go

warnings.filterwarnings("ignore")

current_date = datetime.date.today()
year = current_date.year
month = current_date.month

directory = r'\\med-fls-031\GesFondi\Analisi e Performance Prodotti\Prodotti\Analisi Offerta di Prodotto\Presidenza Funds Performance & Positioning\{year:04d}\{year:04d}.{month:02d}\python'.format(year=year, month=month)
url = 'https://raw.githubusercontent.com/TurcanuDionisie/Dashboard_ER/main/'

os.chdir(directory)

from datetime import datetime, timedelta

def last_end_of_month():
    # Get today's date
    today = datetime.today()
    
    # Subtract one day to get to the previous month
    previous_month = today.replace(day=1) - timedelta(days=1)
    
    # Return the end of the previous month in the desired format
    return previous_month.strftime('%Y-%m-%d')

date = last_end_of_month()
date = date.replace('-','_')


#%% DATA INIZIO E DATA FINE
data_inizio = '30/12/2022'
data_fine = '29/09/2023'

# %% QUOTA NETTA
file_path = "I:/Documenti/File PMC/In Corso/a&p - universo mgf italiani.xlsx" 
sheet_name = "Quota Pubb Rettificata"
qpubb_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qpubb_MGF = qpubb_MGF.iloc[2:]



file_path = "I:/Documenti/File PMC/In Corso/par - universo ch mif sintesi.xlsx" 
sheet_name = "Q.ta Pubblicata"
qpubb_CH_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qpubb_CH_MIF.columns = qpubb_CH_MIF.iloc[1]
qpubb_CH_MIF = qpubb_CH_MIF[2:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo mbb mif sintesi.xlsx" 
sheet_name = "Q.ta Pubblicata"
qpubb_MBB_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qpubb_MBB_MIF.columns = qpubb_MBB_MIF.iloc[1]
qpubb_MBB_MIF = qpubb_MBB_MIF[2:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo gamax sintesi.xlsx" 
sheet_name = "Q.ta Pubblicata Rettificata"
qpubb_GAMAX = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qpubb_GAMAX.columns = qpubb_GAMAX.iloc[1]
qpubb_GAMAX = qpubb_GAMAX[2:]



dataframes = [qpubb_MGF, qpubb_CH_MIF, qpubb_MBB_MIF, qpubb_GAMAX]

quota_netta = dataframes[0]  # iniziamo con il primo DataFrame

# uniamo tutti gli altri DataFrames
for df in dataframes[1:]:
    quota_netta = quota_netta.merge(df, left_index=True, right_index=True, how='inner')


quota_netta = quota_netta.apply(pd.to_numeric)


# %% QUOTA LORDA
file_path = "I:/Documenti/File PMC/In Corso/a&p - universo mgf italiani.xlsx" 
sheet_name = "Quota Lorda Opz 2"
qlorda_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qlorda_MGF = qlorda_MGF.iloc[2:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo ch mif sintesi.xlsx" 
sheet_name = "Q.ta BMK"
qlorda_CH_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qlorda_CH_MIF.columns = qlorda_CH_MIF.iloc[1]
qlorda_CH_MIF = qlorda_CH_MIF[2:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo mbb mif sintesi.xlsx" 
sheet_name = "Q.ta BMK"
qlorda_MBB_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qlorda_MBB_MIF.columns = qlorda_MBB_MIF.iloc[1]
qlorda_MBB_MIF = qlorda_MBB_MIF[2:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo gamax sintesi.xlsx" 
sheet_name = "Q.ta BMK"
qlorda_GAMAX = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qlorda_GAMAX.columns = qlorda_GAMAX.iloc[1]
qlorda_GAMAX = qlorda_GAMAX[2:]


dataframes = [qlorda_MGF, qlorda_CH_MIF, qlorda_MBB_MIF, qlorda_GAMAX]

quota_lorda = dataframes[0]  # iniziamo con il primo DataFrame

# uniamo tutti gli altri DataFrames
for df in dataframes[1:]:
    quota_lorda = quota_lorda.merge(df, left_index=True, right_index=True, how='inner')
    
        
quota_lorda = quota_lorda.apply(pd.to_numeric)    

#%% NAV

file_path = "I:/Documenti/File PMC/In Corso/a&p - universo mgf italiani.xlsx" 
sheet_name = "NAV Totale"
nav_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
nav_MGF.columns = nav_MGF.iloc[0]
nav_MGF = nav_MGF.iloc[2:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo ch mif sintesi.xlsx" 
sheet_name = "NAV Totale"
nav_CH_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
nav_CH_MIF.columns = nav_CH_MIF.iloc[0]
nav_CH_MIF = nav_CH_MIF[2:]
nav_CH_MIF = nav_CH_MIF.drop(nav_CH_MIF.columns[-1], axis=1)

file_path = "I:/Documenti/File PMC/In Corso/par - universo mbb mif sintesi.xlsx" 
sheet_name = "NAV Totale"
nav_MBB_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
nav_MBB_MIF.columns = nav_MBB_MIF.iloc[0]
nav_MBB_MIF = nav_MBB_MIF[2:]
nav_MBB_MIF = nav_MBB_MIF[nav_MBB_MIF.columns[:-1]]

file_path = "I:/Documenti/File PMC/In Corso/par - universo gamax sintesi.xlsx" 
sheet_name = "NAV Totale"
nav_GAMAX = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
nav_GAMAX.columns = nav_GAMAX.iloc[0]
nav_GAMAX = nav_GAMAX[2:]
nav_GAMAX = nav_GAMAX.drop(nav_GAMAX.columns[-1], axis=1)


dataframes = [nav_MGF, nav_CH_MIF, nav_MBB_MIF, nav_GAMAX]

df_nav = dataframes[0]  # iniziamo con il primo DataFrame

# uniamo tutti gli altri DataFrames
for df in dataframes[1:]:
    df_nav = df_nav.merge(df, left_index=True, right_index=True, how='inner')


df_nav = df_nav.apply(pd.to_numeric)



# %% BMK
file_path = "I:/Documenti/File PMC/In Corso/a&p - universo mgf italiani.xlsx" 
sheet_name = "BMK_SERIE_STO"
bmk_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
bmk_MGF.columns = bmk_MGF.iloc[0]
bmk_MGF = bmk_MGF[3:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo ch mif sintesi.xlsx" 
sheet_name = "BMK"
bmk_CH_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
bmk_CH_MIF.columns = bmk_CH_MIF.iloc[0]
bmk_CH_MIF = bmk_CH_MIF[1:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo mbb mif sintesi.xlsx" 
sheet_name = "BMK"
bmk_MBB_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
bmk_MBB_MIF.columns = bmk_MBB_MIF.iloc[0]
bmk_MBB_MIF = bmk_MBB_MIF[1:]


file_path = "I:/Documenti/File PMC/In Corso/par - universo gamax sintesi.xlsx" 
sheet_name = "BMK"
bmk_GAMAX = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
bmk_GAMAX.columns = bmk_GAMAX.iloc[2]
bmk_GAMAX = bmk_GAMAX[3:]


dataframes = [bmk_MGF, bmk_CH_MIF, bmk_MBB_MIF, bmk_GAMAX]

bmk = dataframes[0]  # iniziamo con il primo DataFrame

# uniamo tutti gli altri DataFrames
for df in dataframes[1:]:
    bmk = bmk.merge(df, left_index=True, right_index=True, how='inner')
    

bmk = bmk.apply(pd.to_numeric)        
    
    
# %% CATEGORIA
file_path = "I:/Documenti/File PMC/In Corso/par - universo categoria morningstar.xlsx" 
sheet_name = "Cat MStar utilizzate"
cat_morningstar = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
cat_morningstar = cat_morningstar.iloc[2:]


cat_morningstar = cat_morningstar.apply(pd.to_numeric) 

#%% OMOGEINIZZO LE DATE TRA PERFORMANCE FONDI, NAV, BMK, GROSS/NET

common_dates = quota_netta.index.intersection(quota_lorda.index).intersection(df_nav.index).intersection(bmk.index).intersection(cat_morningstar.index)

quota_netta = quota_netta.loc[common_dates]
quota_lorda = quota_lorda.loc[common_dates]
df_nav = df_nav.loc[common_dates]
bmk = bmk.loc[common_dates]
cat_morningstar = cat_morningstar.loc[common_dates]

# %% FILE DECODIFICA ALL 

codifiche_all = pd.read_excel(url+'codifiche.xlsx', sheet_name='codifica').set_index('Isin')

codifiche = codifiche_all[(codifiche_all ['BMK'] == 'SI')]
#%% LORDO

nav_per_isin = codifiche[['serve per BMK','BMK','CAT']]
nav_per_isin['ISIN AGGREGAZIONE LORDO'] = None
nav_per_isin['ISIN AGGREGAZIONE NETTO'] = None

nav_dict = {i : {'NAV NETTO':pd.Series(),'NAV LORDO':pd.Series() } for i in nav_per_isin.index}

for i in nav_dict:
    if nav_per_isin['BMK'].loc[i] == 'SI':
        nav_per_isin['ISIN AGGREGAZIONE LORDO'].loc[i] = i
    elif nav_per_isin['BMK'].loc[i] == 'NO':
        beta = nav_per_isin['serve per BMK'][nav_per_isin['serve per BMK'] == nav_per_isin['serve per BMK'].loc[i]].index
        
        if beta[beta!=i].empty:
            pass
        else:
            nav_per_isin['ISIN AGGREGAZIONE LORDO'].loc[i] = beta[beta!=i].values[0]
              
    if nav_per_isin['CAT'].loc[i] == 'SI':
        nav_per_isin['ISIN AGGREGAZIONE NETTO'].loc[i] = i
    elif nav_per_isin['CAT'].loc[i] == 'NO':
        beta = nav_per_isin['serve per BMK'][nav_per_isin['serve per BMK'] == nav_per_isin['serve per BMK'].loc[i]].index
        
        if beta[beta!=i].empty:
            pass
        else:
            nav_per_isin['ISIN AGGREGAZIONE NETTO'].loc[i] = beta[beta!=i].values[0]

nav_per_isin = nav_per_isin[['ISIN AGGREGAZIONE NETTO', 'ISIN AGGREGAZIONE LORDO']].replace(np.nan,'ESCLUSO')


codifiche['NAV AGG LORDO'] = codifiche['Serve per NAV'] 
codifiche['NAV AGG NETTO'] = codifiche['Serve per NAV'] 

for i in nav_dict:
    for k in ['NETTO','LORDO']:
           nav_dict[i]['NAV ' + k] = df_nav[codifiche['NAV AGG '+k].loc[i]]
           
  
#LORDO            
nav_lordo = pd.DataFrame(columns=codifiche.index)            
er_pond_lordo = pd.DataFrame(columns=codifiche[codifiche['BMK'] == 'SI'].index) 

for i in nav_lordo.columns:    
    nav_lordo[i] = nav_dict[i]['NAV LORDO']   
    
for k in codifiche[codifiche['BMK'] == 'NO'].index:
    nav_lordo[codifiche['ISIN AGGREGAZIONE LORDO'].loc[k]] += nav_dict[k]['NAV LORDO']       

nav_lordo = nav_lordo.replace(np.nan,0)
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

nav_lordo_all = nav_lordo.copy()
#%% NETTO
codifiche = codifiche_all[(codifiche_all['CAT'] == 'SI')]

nav_per_isin = codifiche[['serve per BMK','BMK','CAT']]
nav_per_isin['ISIN AGGREGAZIONE LORDO'] = None
nav_per_isin['ISIN AGGREGAZIONE NETTO'] = None

nav_dict = {i : {'NAV NETTO':pd.Series(),'NAV LORDO':pd.Series() } for i in nav_per_isin.index}

for i in nav_dict:
    if nav_per_isin['BMK'].loc[i] == 'SI':
        nav_per_isin['ISIN AGGREGAZIONE LORDO'].loc[i] = i
    elif nav_per_isin['BMK'].loc[i] == 'NO':
        beta = nav_per_isin['serve per BMK'][nav_per_isin['serve per BMK'] == nav_per_isin['serve per BMK'].loc[i]].index
        
        if beta[beta!=i].empty:
            pass
        else:
            nav_per_isin['ISIN AGGREGAZIONE LORDO'].loc[i] = beta[beta!=i].values[0]
              
    if nav_per_isin['CAT'].loc[i] == 'SI':
        nav_per_isin['ISIN AGGREGAZIONE NETTO'].loc[i] = i
    elif nav_per_isin['CAT'].loc[i] == 'NO':
        beta = nav_per_isin['serve per BMK'][nav_per_isin['serve per BMK'] == nav_per_isin['serve per BMK'].loc[i]].index
        
        if beta[beta!=i].empty:
            pass
        else:
            nav_per_isin['ISIN AGGREGAZIONE NETTO'].loc[i] = beta[beta!=i].values[0]

nav_per_isin = nav_per_isin[['ISIN AGGREGAZIONE NETTO', 'ISIN AGGREGAZIONE LORDO']].replace(np.nan,'ESCLUSO')


codifiche['NAV AGG LORDO'] = codifiche['Serve per NAV'] 
codifiche['NAV AGG NETTO'] = codifiche['Serve per NAV'] 

for i in nav_dict:
    for k in ['NETTO','LORDO']:
           nav_dict[i]['NAV ' + k] = df_nav[codifiche['NAV AGG '+k].loc[i]]
#NETTO            
nav_netto = pd.DataFrame(columns=codifiche[codifiche['CAT'] == 'SI'].index)            
er_pond_netto = pd.DataFrame(columns=codifiche[codifiche['CAT'] == 'SI'].index) 

for i in nav_netto.columns:    
    nav_netto[i] = nav_dict[i]['NAV NETTO']   
    
for k in codifiche[codifiche['CAT'] == 'NO'].index:
    nav_netto[codifiche['ISIN AGGREGAZIONE NETTO'].loc[k]] += nav_dict[k]['NAV NETTO']  
    
nav_netto = nav_netto.replace(np.nan,0)
nav_netto.loc['2023-06-30'].to_excel('NAV_NETTO_30062023.xlsx') # esporto i NAV netto

for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])
    
nav_netto_all = nav_netto.copy()

nav_netto_all.loc['2023-06-30'].to_excel('weights_NAV_NETTO_30062023.xlsx') #corrisponde alla colonna weight del file netto

# %% CALCOLO PERFORMANCE
ret_quota_netta = quota_netta.pct_change()[1:]
ret_quota_lorda = quota_lorda.pct_change()[1:]
ret_bmk = bmk.pct_change()[1:]
ret_categoria = cat_morningstar.pct_change()[1:]

#filtro per data inizio
ret_quota_netta = ret_quota_netta[ret_quota_netta.index >= data_inizio]
ret_quota_lorda = ret_quota_lorda[ret_quota_lorda.index >= data_inizio]
ret_bmk = ret_bmk[ret_bmk.index >= data_inizio]
ret_categoria = ret_categoria[ret_categoria.index >= data_inizio]

#%% calcolo cumulative da data inizio

#NETTA
cum_quota_netta = pd.DataFrame(columns=ret_quota_netta.columns, index = ret_quota_netta.index)
cum_quota_netta.iloc[0] = 1
for i in range(1,len(cum_quota_netta)):
    cum_quota_netta.iloc[i] = cum_quota_netta.iloc[i-1] * ( 1 + ret_quota_netta.iloc[i])
cum_quota_netta = cum_quota_netta -1
    
#LORDA    
cum_quota_lorda = pd.DataFrame(columns=ret_quota_lorda.columns, index = ret_quota_lorda.index)
cum_quota_lorda.iloc[0] = 1
for i in range(1,len(cum_quota_lorda)):
    cum_quota_lorda.iloc[i] = cum_quota_lorda.iloc[i-1] * ( 1 + ret_quota_lorda.iloc[i])
cum_quota_lorda = cum_quota_lorda -1

#BMK
cum_bmk = pd.DataFrame(columns=ret_bmk.columns, index = ret_bmk.index)
cum_bmk.iloc[0] = 1
for i in range(1,len(cum_bmk)):
    cum_bmk.iloc[i] = cum_bmk.iloc[i-1] * ( 1 + ret_bmk.iloc[i])
cum_bmk = cum_bmk -1

#CATEGORIA MSTAR
cum_categoria = pd.DataFrame(columns=ret_categoria.columns, index = ret_categoria.index)
cum_categoria.iloc[0] = 1
for i in range(1,len(cum_categoria)):
    cum_categoria.iloc[i] = cum_categoria.iloc[i-1] * ( 1 + ret_categoria.iloc[i])
cum_categoria = cum_categoria -1



#%% all LORDO
codifiche = codifiche_all[(codifiche_all['BMK'] == 'SI')]


decodifica_bmk = codifiche[['serve per BMK']]
map_dict = decodifica_bmk.to_dict().get('serve per BMK')

isin = codifiche[(codifiche['BMK'] == 'SI')].index
ret = ret_quota_lorda[isin][ret_quota_lorda.index >= data_inizio]

nav_lordo = nav_lordo_all[isin].copy()
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_bmk[map_dict[i]]

ret_pond = ret * nav_lordo[isin][nav_lordo.index >= data_inizio]
ret_pond_singoli = ret_pond.copy()
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= data_inizio]
alfa_pond_singoli = alfa_pond.copy()
alfa_pond = alfa_pond.sum(axis=1)

cum_ret = pd.Series(index = ret_pond.index)
cum_ret.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_ret.iloc[i] = cum_ret.iloc[i-1] * ( 1 + ret_pond.iloc[i])
cum_ret = cum_ret -1



cum_alfa = pd.Series(index = alfa_pond.index)
cum_alfa.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_alfa.iloc[i] = cum_alfa.iloc[i-1] * ( 1 + alfa_pond.iloc[i])
cum_alfa = cum_alfa -1


er_lordo = cum_ret - cum_alfa
pesi_er_lordo = nav_lordo.iloc[-1]


# #ANALISI ER PONDERATO SINGOLI PER I TOP CONTRIBUTORS AL PONDERATO AGGREGATO
# cum_ret_singoli = ret_pond_singoli.copy()
# first_valid_indices = cum_ret_singoli.apply(pd.Series.first_valid_index)

# for i in ret_pond_singoli.columns:
#     singolo = pd.Series(cum_ret_singoli[i])
#     cum_ret_singoli[i].loc[first_valid_indices[i]] = 1
#     for t in range(1,len(pd.Series(cum_ret_singoli[i])):
#         cum_ret_singoli[i].iloc[t] = cum_ret_singoli[i].iloc[t-1] * ( 1 + ret_pond_singoli[i].iloc[t])
#     cum_ret_singoli[i] = cum_ret_singoli[i] -1





#%% LORDO FIXED INCOME
codifiche = codifiche_all[(codifiche_all['BMK'] == 'SI') & (codifiche_all['Asset class'] == 'FixedIncome')]


decodifica_bmk = codifiche[['serve per BMK']]
map_dict = decodifica_bmk.to_dict().get('serve per BMK')

isin = codifiche[(codifiche['BMK'] == 'SI')].index
ret = ret_quota_lorda[isin][ret_quota_lorda.index >= data_inizio]

nav_lordo = nav_lordo_all[isin].copy()
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_bmk[map_dict[i]]

ret_pond = ret * nav_lordo[isin][nav_lordo.index >= data_inizio]
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= data_inizio]
alfa_pond = alfa_pond.sum(axis=1)

cum_ret = pd.Series(index = ret_pond.index)
cum_ret.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_ret.iloc[i] = cum_ret.iloc[i-1] * ( 1 + ret_pond.iloc[i])
cum_ret = cum_ret -1


cum_alfa = pd.Series(index = alfa_pond.index)
cum_alfa.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_alfa.iloc[i] = cum_alfa.iloc[i-1] * ( 1 + alfa_pond.iloc[i])
cum_alfa = cum_alfa -1


er_lordo_fi = cum_ret - cum_alfa
pesi_er_lordo_fi = nav_lordo.iloc[-1]
#%% LORDO MULTI ASSET
codifiche = codifiche_all[(codifiche_all['BMK'] == 'SI') & (codifiche_all['Asset class'] == 'MultiAsset')]


decodifica_bmk = codifiche[['serve per BMK']]
map_dict = decodifica_bmk.to_dict().get('serve per BMK')

isin = codifiche[(codifiche['BMK'] == 'SI')].index
ret = ret_quota_lorda[isin][ret_quota_lorda.index >= data_inizio]

nav_lordo = nav_lordo_all[isin].copy()
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_bmk[map_dict[i]]

ret_pond = ret * nav_lordo[isin][nav_lordo.index >= data_inizio]
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= data_inizio]
alfa_pond = alfa_pond.sum(axis=1)

cum_ret = pd.Series(index = ret_pond.index)
cum_ret.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_ret.iloc[i] = cum_ret.iloc[i-1] * ( 1 + ret_pond.iloc[i])
cum_ret = cum_ret -1


cum_alfa = pd.Series(index = alfa_pond.index)
cum_alfa.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_alfa.iloc[i] = cum_alfa.iloc[i-1] * ( 1 + alfa_pond.iloc[i])
cum_alfa = cum_alfa -1


er_lordo_ma = cum_ret - cum_alfa
pesi_er_lordo_ma = nav_lordo.iloc[-1]
#%% LORDO EQUITY
codifiche = codifiche_all[(codifiche_all['BMK'] == 'SI') & (codifiche_all['Asset class'] == 'Equity')]


decodifica_bmk = codifiche[['serve per BMK']]
map_dict = decodifica_bmk.to_dict().get('serve per BMK')

isin = codifiche[(codifiche['BMK'] == 'SI')].index
ret = ret_quota_lorda[isin][ret_quota_lorda.index >= data_inizio]

nav_lordo = nav_lordo_all[isin].copy()
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_bmk[map_dict[i]]

ret_pond = ret * nav_lordo[isin][nav_lordo.index >= data_inizio]
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= data_inizio]
alfa_pond = alfa_pond.sum(axis=1)

cum_ret = pd.Series(index = ret_pond.index)
cum_ret.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_ret.iloc[i] = cum_ret.iloc[i-1] * ( 1 + ret_pond.iloc[i])
cum_ret = cum_ret -1


cum_alfa = pd.Series(index = alfa_pond.index)
cum_alfa.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_alfa.iloc[i] = cum_alfa.iloc[i-1] * ( 1 + alfa_pond.iloc[i])
cum_alfa = cum_alfa -1


er_lordo_eq = cum_ret - cum_alfa
pesi_er_lordo_eq = nav_lordo.iloc[-1]
# %% ALL NETTO
codifiche = codifiche_all[(codifiche_all['CAT'] == 'SI')]


decodifica_bmk = codifiche[['serve per CAT M*']]
map_dict = decodifica_bmk.to_dict().get('serve per CAT M*')

isin = codifiche[(codifiche['CAT'] == 'SI')].index
ret = ret_quota_netta[isin][ret_quota_netta.index >= data_inizio]

nav_netto = nav_netto_all[isin].copy()
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_categoria[map_dict[i]]

ret_pond = ret * nav_netto[isin][nav_netto.index >= data_inizio]
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_netto[isin][nav_netto.index >= data_inizio]
alfa_pond = alfa_pond.sum(axis=1)

cum_ret = pd.Series(index = ret_pond.index)
cum_ret.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_ret.iloc[i] = cum_ret.iloc[i-1] * ( 1 + ret_pond.iloc[i])
cum_ret = cum_ret -1


cum_alfa = pd.Series(index = alfa_pond.index)
cum_alfa.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_alfa.iloc[i] = cum_alfa.iloc[i-1] * ( 1 + alfa_pond.iloc[i])
cum_alfa = cum_alfa -1


er_netto = cum_ret - cum_alfa
pesi_er_netto = nav_netto.iloc[-1]
# %% NETTO FIXED INCOME
codifiche = codifiche_all[(codifiche_all['CAT'] == 'SI') & (codifiche_all['Asset class'] == 'FixedIncome')]


decodifica_bmk = codifiche[['serve per CAT M*']]
map_dict = decodifica_bmk.to_dict().get('serve per CAT M*')

isin = codifiche[(codifiche['CAT'] == 'SI')].index
ret = ret_quota_netta[isin][ret_quota_netta.index >= data_inizio]

nav_netto = nav_netto_all[isin].copy()
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_categoria[map_dict[i]]

ret_pond = ret * nav_netto[isin][nav_netto.index >= data_inizio]
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_netto[isin][nav_netto.index >= data_inizio]
alfa_pond = alfa_pond.sum(axis=1)

cum_ret = pd.Series(index = ret_pond.index)
cum_ret.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_ret.iloc[i] = cum_ret.iloc[i-1] * ( 1 + ret_pond.iloc[i])
cum_ret = cum_ret -1


cum_alfa = pd.Series(index = alfa_pond.index)
cum_alfa.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_alfa.iloc[i] = cum_alfa.iloc[i-1] * ( 1 + alfa_pond.iloc[i])
cum_alfa = cum_alfa -1


er_netto_fi = cum_ret - cum_alfa
pesi_er_netto_fi = nav_netto.iloc[-1]
# %% NETTO MULTIASSET
codifiche = codifiche_all[(codifiche_all['CAT'] == 'SI') & (codifiche_all['Asset class'] == 'MultiAsset')]


decodifica_bmk = codifiche[['serve per CAT M*']]
map_dict = decodifica_bmk.to_dict().get('serve per CAT M*')

isin = codifiche[(codifiche['CAT'] == 'SI')].index
ret = ret_quota_netta[isin][ret_quota_netta.index >= data_inizio]

nav_netto = nav_netto_all[isin].copy()
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_categoria[map_dict[i]]

ret_pond = ret * nav_netto[isin][nav_netto.index >= data_inizio]
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_netto[isin][nav_netto.index >= data_inizio]
alfa_pond = alfa_pond.sum(axis=1)

cum_ret = pd.Series(index = ret_pond.index)
cum_ret.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_ret.iloc[i] = cum_ret.iloc[i-1] * ( 1 + ret_pond.iloc[i])
cum_ret = cum_ret -1


cum_alfa = pd.Series(index = alfa_pond.index)
cum_alfa.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_alfa.iloc[i] = cum_alfa.iloc[i-1] * ( 1 + alfa_pond.iloc[i])
cum_alfa = cum_alfa -1


er_netto_ma = cum_ret - cum_alfa
pesi_er_netto_ma = nav_netto.iloc[-1]
# %% NETTO Equity
codifiche = codifiche_all[(codifiche_all['CAT'] == 'SI') & (codifiche_all['Asset class'] == 'Equity')]


decodifica_bmk = codifiche[['serve per CAT M*']]
map_dict = decodifica_bmk.to_dict().get('serve per CAT M*')

isin = codifiche[(codifiche['CAT'] == 'SI')].index
ret = ret_quota_netta[isin][ret_quota_netta.index >= data_inizio]

nav_netto = nav_netto_all[isin].copy()
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_categoria[map_dict[i]]

ret_pond = ret * nav_netto[isin][nav_netto.index >= data_inizio]
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_netto[isin][nav_netto.index >= data_inizio]
alfa_pond = alfa_pond.sum(axis=1)

cum_ret = pd.Series(index = ret_pond.index)
cum_ret.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_ret.iloc[i] = cum_ret.iloc[i-1] * ( 1 + ret_pond.iloc[i])
cum_ret = cum_ret -1


cum_alfa = pd.Series(index = alfa_pond.index)
cum_alfa.iloc[0] = 1
for i in range(1,len(cum_ret)):
    cum_alfa.iloc[i] = cum_alfa.iloc[i-1] * ( 1 + alfa_pond.iloc[i])
cum_alfa = cum_alfa -1


er_netto_eq = cum_ret - cum_alfa
pesi_er_netto_eq = nav_netto.iloc[-1]

#%% unisco netto e lordo per macroragruppamenti

all_funds = pd.DataFrame()
all_funds['Net Perf vs Cat M*'] = er_netto
all_funds['Gross Perf vs SAA'] = er_lordo
all_funds = all_funds[all_funds.index <= data_fine]

eq_funds = pd.DataFrame()
eq_funds['Net Perf vs Cat M*'] = er_netto_eq
eq_funds['Gross Perf vs SAA'] = er_lordo_eq
eq_funds = eq_funds[eq_funds.index <= data_fine]

fi_funds = pd.DataFrame()
fi_funds['Net Perf vs Cat M*'] = er_netto_fi
fi_funds['Gross Perf vs SAA'] = er_lordo_fi
fi_funds = fi_funds[fi_funds.index <= data_fine]

ma_funds = pd.DataFrame()
ma_funds['Net Perf vs Cat M*'] = er_netto_ma
ma_funds['Gross Perf vs SAA'] = er_lordo_ma
ma_funds = ma_funds[ma_funds.index <= data_fine]
#%% PER SINGOLO FONDO
nome_fondi = codifiche_all[(codifiche_all['CAT'] == 'SI') | (codifiche_all['BMK'] == 'SI')] 
names_isin_dict = nome_fondi['Nome 2'].to_dict()
isin_names_dict = nome_fondi.set_index('Nome 2')['Isin.1'].to_dict()

ret_quota_netta = quota_netta.pct_change()[1:]
ret_quota_lorda = quota_lorda.pct_change()[1:]
ret_bmk = bmk.pct_change()[1:]
ret_categoria = cat_morningstar.pct_change()[1:]

er_funds_dict = {}

date_picker = data_inizio


for isin in names_isin_dict.keys():

    dettaglio_fondo = isin
    
    
    #filtro per data inizio
    ret_quota_netta = ret_quota_netta[ret_quota_netta.index >= date_picker]
    ret_quota_lorda = ret_quota_lorda[ret_quota_lorda.index >= date_picker]
    ret_bmk = ret_bmk[ret_bmk.index >= date_picker]
    ret_categoria = ret_categoria[ret_categoria.index >= date_picker]
    
    
    #NETTA
    cum_quota_netta = pd.DataFrame(columns=ret_quota_netta.columns, index = ret_quota_netta.index)
    cum_quota_netta.iloc[0] = 1
    for i in range(1,len(cum_quota_netta)):
        cum_quota_netta.iloc[i] = cum_quota_netta.iloc[i-1] * ( 1 + ret_quota_netta.iloc[i])
    cum_quota_netta = cum_quota_netta -1
        
    #LORDA    
    cum_quota_lorda = pd.DataFrame(columns=ret_quota_lorda.columns, index = ret_quota_lorda.index)
    cum_quota_lorda.iloc[0] = 1
    for i in range(1,len(cum_quota_lorda)):
        cum_quota_lorda.iloc[i] = cum_quota_lorda.iloc[i-1] * ( 1 + ret_quota_lorda.iloc[i])
    cum_quota_lorda = cum_quota_lorda -1
    
    #BMK
    cum_bmk = pd.DataFrame(columns=ret_bmk.columns, index = ret_bmk.index)
    cum_bmk.iloc[0] = 1
    for i in range(1,len(cum_bmk)):
        cum_bmk.iloc[i] = cum_bmk.iloc[i-1] * ( 1 + ret_bmk.iloc[i])
    cum_bmk = cum_bmk -1
    
    #CATEGORIA
    cum_categoria = pd.DataFrame(columns=ret_categoria.columns, index = ret_categoria.index)
    cum_categoria.iloc[0] = 1
    for i in range(1,len(cum_categoria)):
        cum_categoria.iloc[i] = cum_categoria.iloc[i-1] * ( 1 + ret_categoria.iloc[i])
    cum_categoria = cum_categoria -1
    
        
    nome_fondi_lordo = nome_fondi[nome_fondi['BMK'] == 'SI']
    
    nome_fondi_netto = nome_fondi[nome_fondi['CAT'] == 'SI']
    
       
    if(dettaglio_fondo in (nome_fondi_lordo.index)):
        cum_quota_lorda = cum_quota_lorda[dettaglio_fondo]
        cum_bmk = cum_bmk[nome_fondi_lordo['serve per BMK'].loc[dettaglio_fondo]]
        er_fund_lordo = cum_quota_lorda - cum_bmk
        
    if(dettaglio_fondo in (nome_fondi_netto.index)):
        cum_quota_netta = cum_quota_netta[dettaglio_fondo]
        cum_categoria = cum_categoria[nome_fondi_netto['serve per CAT M*'].loc[dettaglio_fondo]]
        er_fund_netto = cum_quota_netta - cum_categoria
    
    # UNIFICO DATE
    common_dates = er_fund_netto.index.intersection(er_fund_lordo.index)
    er_fund_netto = er_fund_netto.loc[common_dates]
    er_fund_lordo = er_fund_lordo.loc[common_dates]
    
    er_fund = pd.DataFrame()
    er_fund['Net Perf vs Cat M*'] = er_fund_netto
    er_fund['Gross Perf vs SAA'] = er_fund_lordo
    er_fund = er_fund[er_fund.index <= data_fine]
    
    
    er_funds_dict[isin] = er_fund
    

result_dict = {key1: er_funds_dict[value1] for key1, value1 in isin_names_dict.items()}



#%%
dictionary = {'All Funds (NAV weighted)': all_funds, 'Equity Funds (NAV weighted)': eq_funds, 'Fixed Income Funds (NAV weighted)': fi_funds, 'Multi Asset Funds (NAV weighted)': ma_funds }
dictionary.update(result_dict)

# Function to create a sample Plotly figure and return it as an HTML div
def create_plot(i):
    er_graph = go.Figure()
    er_graph.add_trace(go.Scatter(x=dictionary[i].index, y=dictionary[i]['Net Perf vs Cat M*'], mode='lines', name='Net Perf vs Cat M*', line=dict(color='lightsteelblue'), hovertemplate='(%{x}, %{y:.3%})'))
    er_graph.add_trace(go.Scatter(x=dictionary[i].index, y=dictionary[i]['Gross Perf vs SAA'], mode='lines', name='Gross Perf vs SAA', line=dict(color='midnightblue'), hovertemplate='(%{x}, %{y:.3%})'))

    er_graph.update_layout(
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.07,
            xanchor="center",
            x=0.15,
            font=dict(size=15)
        ),
        title={
            'text': f'Dettaglio ER dal ' + str(dictionary[i].index[0].strftime("%Y-%m-%d")) + ' al ' + str(dictionary[i].index[-1].strftime("%Y-%m-%d")),
            'font': {'size': 24},
            'x': 0.5,
            'y': 0.95,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        paper_bgcolor='rgba(0,0,0,0)',  # Set the overall background to transparent
        plot_bgcolor='rgba(0,0,0,0)',  # Set the plotting area background to transparent
        xaxis=dict(showgrid=False),
        yaxis=dict(
            showgrid=True,
            gridcolor='lightgrey',
            gridwidth=1,
            tickwidth=2,
            tickformat=',.2%',  # Rounded to 2 decimals and displayed as a percentage
            zerolinecolor='lightcoral',
            zerolinewidth=1
        )
    )

    # Convert the Plotly figure to an HTML div
    plot_div = er_graph.to_html(full_html=False)

    return plot_div

# Create the HTML content with a search bar
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>100 Charts</title>
    <style>
        .chart-title {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Chart Search</h1>
    <form id="search-form" action="#">
        <label for="search-input">Search:</label>
        <input type="text" id="search-input" oninput="searchCharts()">
    </form>
    <ul id="chart-list">
"""

for chart_name in dictionary.keys():
    html_content += f'<li class="chart-item"><a href="#{chart_name}">{chart_name}</a></li>'

html_content += """
    </ul>
</body>
<script>
    function searchCharts() {
        var input = document.getElementById('search-input').value.toLowerCase();
        var chartList = document.getElementById('chart-list');
        var chartItems = chartList.getElementsByClassName('chart-item');
        
        for (var i = 0; i < chartItems.length; i++) {
            var chartName = chartItems[i].innerText.toLowerCase();
            if (chartName.includes(input)) {
                chartItems[i].style.display = 'block';
            } else {
                chartItems[i].style.display = 'none';
            }
        }
    }
</script>
</html>
"""



for i in dictionary.keys():
    plot_data = create_plot(i)
    html_content += f"""
    <h2 id="{i}">{i}</h2>
    {plot_data}
    """

html_content += """
</body>
</html>
"""


# Save the HTML content to a file
with open("charts.html", "w") as file:
    file.write(html_content)

print("HTML file 'charts.html' has been created.")


