import pandas as pd
import os
import matplotlib as plt
import numpy as np
directory = r'G:\Analisi e Performance Prodotti\Prodotti\Analisi Offerta di Prodotto\Presidenza Funds Performance & Positioning\2023\2023.06\python'
os.chdir(directory)


#ciao 123#ciao 123#ciao 123#ciao 123#ciao 123#ciao 123#ciao 123


#ciao 123
# %% QUOTA NETTA
file_path = "I:/Documenti/File PMC/In Corso/a&p - universo mgf italiani.xlsx" 
sheet_name = "Quota Pubb Rettificata"
qpubb_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qpubb_MGF = qpubb_MGF.iloc[2:]

#ciao 

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


# %% FILE DECODIFICA ALL 

codifiche_all = pd.read_excel('Analisi ER netto_lordo_V2.xlsx', sheet_name='codifica').set_index('Isin')

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
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])
    
nav_netto_all = nav_netto.copy()
# %% CALCOLO PERFORMANCE
ret_quota_netta = quota_netta.pct_change()[1:]
ret_quota_lorda = quota_lorda.pct_change()[1:]
ret_bmk = bmk.pct_change()[1:]
ret_categoria = cat_morningstar.pct_change()[1:]

#filtro per data inizio
ret_quota_netta = ret_quota_netta[ret_quota_netta.index >= "06/30/2022"]
ret_quota_lorda = ret_quota_lorda[ret_quota_lorda.index >= "06/30/2022"]
ret_bmk = ret_bmk[ret_bmk.index >= "06/30/2022"]
ret_categoria = ret_categoria[ret_categoria.index >= "06/30/2022"]

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

#CATEGORIA
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
ret = ret_quota_lorda[isin][ret_quota_lorda.index >= '06/30/2022']

nav_lordo = nav_lordo_all[isin].copy()
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_bmk[map_dict[i]]

ret_pond = ret * nav_lordo[isin][nav_lordo.index >= '06/30/2022']
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= '06/30/2022']
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
#%% LORDO FIXED INCOME
codifiche = codifiche_all[(codifiche_all['BMK'] == 'SI') & (codifiche_all['Asset class'] == 'FixedIncome')]


decodifica_bmk = codifiche[['serve per BMK']]
map_dict = decodifica_bmk.to_dict().get('serve per BMK')

isin = codifiche[(codifiche['BMK'] == 'SI')].index
ret = ret_quota_lorda[isin][ret_quota_lorda.index >= '06/30/2022']

nav_lordo = nav_lordo_all[isin].copy()
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_bmk[map_dict[i]]

ret_pond = ret * nav_lordo[isin][nav_lordo.index >= '06/30/2022']
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= '06/30/2022']
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
ret = ret_quota_lorda[isin][ret_quota_lorda.index >= '06/30/2022']

nav_lordo = nav_lordo_all[isin].copy()
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_bmk[map_dict[i]]

ret_pond = ret * nav_lordo[isin][nav_lordo.index >= '06/30/2022']
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= '06/30/2022']
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
ret = ret_quota_lorda[isin][ret_quota_lorda.index >= '06/30/2022']

nav_lordo = nav_lordo_all[isin].copy()
for t in nav_lordo.index:
    nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_bmk[map_dict[i]]

ret_pond = ret * nav_lordo[isin][nav_lordo.index >= '06/30/2022']
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= '06/30/2022']
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
ret = ret_quota_netta[isin][ret_quota_netta.index >= '06/30/2022']

nav_netto = nav_netto_all[isin].copy()
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_categoria[map_dict[i]]

ret_pond = ret * nav_netto[isin][nav_netto.index >= '06/30/2022']
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_netto[isin][nav_netto.index >= '06/30/2022']
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
ret = ret_quota_netta[isin][ret_quota_netta.index >= '06/30/2022']

nav_netto = nav_netto_all[isin].copy()
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_categoria[map_dict[i]]

ret_pond = ret * nav_netto[isin][nav_netto.index >= '06/30/2022']
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_netto[isin][nav_netto.index >= '06/30/2022']
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
ret = ret_quota_netta[isin][ret_quota_netta.index >= '06/30/2022']

nav_netto = nav_netto_all[isin].copy()
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_categoria[map_dict[i]]

ret_pond = ret * nav_netto[isin][nav_netto.index >= '06/30/2022']
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_netto[isin][nav_netto.index >= '06/30/2022']
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
ret = ret_quota_netta[isin][ret_quota_netta.index >= '06/30/2022']

nav_netto = nav_netto_all[isin].copy()
for t in nav_netto.index:
    nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

alfa = ret.copy()
for i in ret.columns:
    alfa[i] = ret_categoria[map_dict[i]]

ret_pond = ret * nav_netto[isin][nav_netto.index >= '06/30/2022']
ret_pond = ret_pond.sum(axis=1)
alfa_pond = alfa * nav_netto[isin][nav_netto.index >= '06/30/2022']
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





# %% DETTAGLIO FONDI


nome_fondi = codifiche_all[(codifiche_all['CAT'] == 'SI') | (codifiche_all['BMK'] == 'SI')] 


ret_quota_netta = quota_netta.pct_change()[1:]
ret_quota_lorda = quota_lorda.pct_change()[1:]
ret_bmk = bmk.pct_change()[1:]
ret_categoria = cat_morningstar.pct_change()[1:]


date_picker = "01/01/2023"
dettaglio_fondo = 'IE00B9CQ9016'


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
    er_lordo = cum_quota_lorda - cum_bmk



if(dettaglio_fondo in (nome_fondi_netto.index)):
    cum_quota_netta = cum_quota_netta[dettaglio_fondo]
    cum_categoria = cum_categoria[nome_fondi_netto['serve per CAT M*'].loc[dettaglio_fondo]]
    er_netto = cum_quota_netta - cum_categoria

#%%


podio = pd.read_excel('230510 - Analisi MAP - Elementi per il podio  v2 APRILE 23.xlsx', sheet_name ='x dashboard')
podio= podio.set_index('isin')


tab = pd.DataFrame(index = ['rk_net','rk_gross','er_net','er_gross','perf'], columns=['Categoria','1M','3M','YTD','1Y','2022','2021','2020'])

for t in ['1M','3M','YTD','1Y','2022','2021','2020']:
    tab[t].loc['rk_net'] = np.array(round(podio['net_'+t].loc[dettaglio_fondo],2))
    tab[t].loc['rk_gross'] = np.array(round(podio['gross_'+t].loc[dettaglio_fondo],2))
    tab[t].loc['er_net'] = np.array(round(podio['ernetto_'+t].loc[dettaglio_fondo],2))
    tab[t].loc['er_gross'] = np.array(round(podio['erlordo_'+t].loc[dettaglio_fondo],2))
    tab[t].loc['perf'] = np.array(round(podio['perf_'+t].loc[dettaglio_fondo],2))

tab['Categoria'].loc['rk_net'] = nome_fondi['Asset class'].loc[dettaglio_fondo]

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


# %% EXCEL

dataframes = [er_lordo,er_netto, er_lordo_fi,er_lordo_ma, er_lordo_eq, er_netto_fi,er_netto_ma,er_netto_eq]


serie_unite = pd.concat(dataframes, ignore_index=False, axis=1)

serie_unite.columns = ["er_lordo","er_netto","er_lordo_fi","er_lordo_ma","er_lordo_eq","er_netto_fi","er_netto_ma","er_netto_eq"]
file_name = "er_netto_lordo_finale.xlsx"
serie_unite.to_excel(file_name)

dataframes = [pesi_er_lordo,pesi_er_netto, pesi_er_lordo_fi,pesi_er_lordo_ma, pesi_er_lordo_eq, pesi_er_netto_fi,pesi_er_netto_ma,pesi_er_netto_eq]


serie_unite = pd.concat(dataframes, ignore_index=False, axis=1)

serie_unite.columns = ["pesi_er_lordo","pesi_er_netto","pesi_er_lordo_fi","pesi_er_lordo_ma","pesi_er_lordo_eq","pesi_er_netto_fi","pesi_er_netto_ma","pesi_er_netto_eq"]
file_name = "pesi_finale.xlsx"
serie_unite.to_excel(file_name)

