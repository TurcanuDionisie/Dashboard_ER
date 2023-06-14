import pandas as pd
import numpy as np
import os
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import math

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash import dash_table
from dash import ctx
import dash_bootstrap_components as dbc
from PIL import Image
from io import BytesIO
import requests

#%%

directory = r'G:\Analisi e Performance Prodotti\Prodotti\Analisi Offerta di Prodotto\Presidenza Funds Performance & Positioning\2023\2023.06\python'
os.chdir(directory)

#%% INPUT

data_confronto = ['1M','3M','YTD','1Y','30/06/2022','3Y','5Y']


#%% CARICAMENTO DATI SOTTOSTANTI E NON VARIABILI

#  QUOTA NETTA
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


# QUOTA LORDA
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

# NAV

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

#  BMK
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
    
    
# CATEGORIA
file_path = "I:/Documenti/File PMC/In Corso/par - universo categoria morningstar.xlsx" 
sheet_name = "Cat MStar utilizzate"
cat_morningstar = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
cat_morningstar = cat_morningstar.iloc[2:]


cat_morningstar = cat_morningstar.apply(pd.to_numeric) 


#FILE DECODIFICA ALL 

codifiche_all = pd.read_excel('Analisi ER netto_lordo_V2.xlsx', sheet_name='codifica').set_index('Isin')

codifiche = codifiche_all[(codifiche_all ['BMK'] == 'SI')]
#LORDO

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
#NETTO
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


#%% DASHBOARD: LAYOUT

app = dash.Dash(__name__, 
                title ='DashBoard ER')
server = app.server

# Add the following line to set the favicon

#use href="/assets/favicon.ico" to get favicon from local folder (named 'assets' and subdirectory) instead of github

#FAVICON
app.index_string = '''
    <!DOCTYPE html>
    <html>
        <head>           
            <link rel="shortcut icon" href="https://raw.githubusercontent.com/marzowill96/Monitoraggio_Analisi_Performance/main/favicon.ico"  type="image/x-icon">
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
'''

# Define app layout
app.layout = html.Div([
  
    #TITOLO
    html.Div([
        html.H1('DashBoard ER'),
        html.H2('by Monitoraggio & Analisi Prodotti di Investimento', style={'color': 'black', 'font-style': 'italic', 'font-weight': 'normal','font-size': '1.85vh', 'margin-left': '0px','margin-bottom':'20px'})

    ],style={'margin': 'auto', 'justify-content': 'center','display': 'flex', 'align-items': 'flex-end'}),
    
    # TABELLA INPUT
    html.Div([
    html.Table([
        html.Tr([
            html.Th('Data Primo Versamento (Fine Mese)', style={'text-align': 'center','backgroundColor': 'royalblue',
            'color': 'white', 'fontSize':'0.75vw'}),
            html.Th('Importo (Min. €30.000)', style={'text-align': 'center','backgroundColor': 'royalblue',
            'color': 'white', 'fontSize':'0.75vw'}),
            html.Th('Durata', style={'text-align': 'center','backgroundColor': 'royalblue',
            'color': 'white', 'fontSize':'0.75vw'}),
            html.Th('Importo Rata Totale', style={'text-align': 'center','backgroundColor': 'royalblue',
            'color': 'white', 'fontSize':'0.75vw'}),
        ], style={'border': '1px solid black'}),
        
        html.Tr([
            html.Td(dcc.Dropdown(
                id='start_date',
                options=[{'label': date, 'value': date} for date in dates],
                value=dates[0]), style={'text-align': 'center','border': '1px solid black', 'fontSize':'0.75vw'}),
            html.Td(dcc.Input(
                id='importo',
                type='number',
                min=30000,style={'position': 'sticky', 'top': '0'} ), style={'text-align': 'center','border': '1px solid black', 'fontSize':'0.75vw'}),
           html.Td(dcc.RadioItems(
               id='durata_months',
               options=[{'label': i, 'value': i} for i in [36, 48, 60]],
               value=36,
               labelStyle={'display': 'inline-block', 'margin-right': '10px'},
               style={'display': 'inline-block', 'margin':'0px'} ), style={'text-align': 'center','border': '1px solid black', 'fontSize':'0.75vw'}),
           html.Td(html.Div(id='installment-amount', style={'display': 'inline-block'}), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'})
           
        ],style={'border': '1px solid black'}),
        # ],style={'width': '60%', 'table-layout': 'adaptive','marginTop': '50px', 'marginLeft': '100px','border': '1px solid black'}),

        html.Tr([
            html.Th('Comparto', style={'text-align': 'center','backgroundColor': 'royalblue',
            'color': 'white','fontSize':'0.75vw'}),
            html.Th('Ripartizione (0% - 100%)', style={'text-align': 'center','backgroundColor': 'royalblue',
            'color': 'white','fontSize':'0.75vw'}),
            html.Th('Soglia Automatic Step-Out', style={'text-align': 'center','backgroundColor': 'royalblue',
            'color': 'white','fontSize':'0.75vw'}),
            html.Th('Importo Rata', style={'text-align': 'center','backgroundColor': 'royalblue',
            'color': 'white','fontSize':'0.75vw'})            
        ], style={'border': '1px solid black'}),
        # table rows
        html.Tr([
            html.Td(dcc.Dropdown(id='fondo1', options=[{'label': fondo, 'value': fondo} for fondo in nomi], value='-'), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            
            html.Td(dcc.Input(id='input1', type='number',min=0, value = 0), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            html.Td(dcc.Dropdown(id='step_out1', options=[
                                          {'label': '-', 'value': '-'},
                                          {'label': '10%', 'value': '10%'},
                                          {'label': '20%', 'value': '20%'}], value = '-'), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            html.Td(id='rata1', style={'text-align': 'center','border': '1px solid black'})

        ],style={'border': '1px solid black'}),
        html.Tr([
            html.Td(dcc.Dropdown(id='fondo2', options=[{'label': fondo, 'value': fondo} for fondo in nomi], value='-'), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            html.Td(dcc.Input(id='input2', type='number',min=0, value = 0), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            html.Td(dcc.Dropdown(id='step_out2', options=[
                                          {'label': '-', 'value': '-'},
                                          {'label': '10%', 'value': '10%'},
                                          {'label': '20%', 'value': '20%'}], value = '-'), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            html.Td(id='rata2', style={'text-align': 'center','border': '1px solid black',})

        ]),
        html.Tr([
            html.Td(dcc.Dropdown(id='fondo3', options=[{'label': fondo, 'value': fondo} for fondo in nomi], value='-'), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            html.Td(dcc.Input(id='input3', type='number',min=0, value = 0), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            html.Td(dcc.Dropdown(id='step_out3', options=[
                                          {'label': '-', 'value': '-'},
                                          {'label': '10%', 'value': '10%'},
                                          {'label': '20%', 'value': '20%'}], value = '-'), style={'text-align': 'center','border': '1px solid black','fontSize':'0.75vw'}),
            html.Td(id='rata3', style={'text-align': 'center','border': '1px solid black'})

        ],style={'border': '1px solid black'}),
    ],style={'width': '60%', 'table-layout': 'adaptive','marginTop': '50px','border': '1px solid black'})

    ], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '10px'}), 
    
    
    
    
    #MESSAGGIO ROSSO/VERDE SOTTO TABELLA
    html.Div(id='output',style={'margin': 'auto', 'justify-content': 'center','display': 'flex'}),
    
    # BOTTONI PER FILTRO
    html.Div([
        html.Div([
            html.Button('Look Through Comparto 1', id='btn-nclicks-1', style={'margin-right': '20px', 'fontSize':'0.75vw'}),
            html.Button('Look Through Comparto 2', id='btn-nclicks-2', style={'margin-right': '20px', 'fontSize':'0.75vw'}),
            html.Button('Look Through Comparto 3', id='btn-nclicks-3', style={'margin-right': '20px', 'fontSize':'0.75vw'}),
            html.Button('Complessivo', id='btn-nclicks-all', style={'fontSize':'0.75vw'})
        ], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '30px'})
    ]),
    
    #GRAFICI GROSSI
    html.Div(children=[
    dcc.Graph(id='grafico_iis', style={'height': '70%', 'width': '100%', 'display': 'block'}, config={'displayModeBar': False}),   
    dcc.Graph(id='istogramma', style={'height': '30%', 'width': '100%', 'display': 'block', 'margin-top': '0px'}, config={'displayModeBar': False})
    ], style={'height': '1000px','justify-content': 'center'}),           
    
    
    #TABELLA RISULTATI
    html.Div([dash_table.DataTable(
            id='stats',
            columns=[
                {"name": [" ", "Nome"], "id": "nome"},
                {"name": ["Performance", "IIS"], "id": "perfiis"},
                {"name": ["Performance", "PIC"], "id": "perfpic"},
                {"name": ["Performance", "Effetto Strategia"], "id": "perfstra"},
                {"name": ["Performance", "Prezzo Iniziale"], "id": "perfprin"},
                {"name": ["Performance", "Prezzo Finale"], "id": "perfprfin"},   
                {"name": ["Performance", "Prezzo Medio"], "id": "perfprmed"}, 
                {"name": ["Performance", "Rimbalzo per parità IIS"], "id": "perfrimbiis"}, 
                {"name": ["Performance", "Rimbalzo per parità PIC"], "id": "perfrimbpic"}, 
                {"name": ["Volatilità", "IIS"], "id": "voliis"},
                {"name": ["Volatilità", "PIC"], "id": "volpic"},
                {"name": ["Volatilità", "Effetto Strategia"], "id": "volstra"},
                {"name": ["Max Draw-Down", "IIS"], "id": "mddiis"},
                {"name": ["Max Draw-Down", "PIC"], "id": "mddpic"},
                {"name": ["Max Draw-Down", "Effetto Strategia"], "id": "mddstra"},
            ],
            data=None,
            merge_duplicate_headers=True,
            style_table={                
                'margin': 'auto',  
            },
            style_header={
                'backgroundColor': 'royalblue',
                'color': 'white',
                'fontWeight': 'bold',
                'text-align': 'center'
            },
            style_cell={'textAlign': 'center', 'fontSize':'0.75vw'}
        )
                
    ],style={'justify-content': 'center','text-align': 'center', 'width':'100%','marginTop':'40px'}
),



html.Div(
    [
        html.Div(
            [
                html.Div([
                    
                    dash_table.DataTable(
                        id='step_in',
                        columns=[{"name": i, "id": i} for i in step_in_df],
                        data=None,
                        editable=False,
                        style_table={
                            'maxWidth': '10%',
                            'margin': 'auto',
                            'marginLeft': '20px',
                            'marginTop': '20px'  # add margin to the top
                        },
                        style_header={
                            'backgroundColor': 'royalblue',
                            'color': 'white',
                            'fontWeight': 'bold',
                            'text-align': 'center'
                        },
                        style_cell={'textAlign': 'center', 'fontSize':'0.75vw'}
                    )],
                    className="six columns",
                    style={"display": "inline-block",'text-align': 'center'}
                ),
                html.Div(
                    dash_table.DataTable(
                        id='step_out',
                        columns=[{"name": i, "id": i} for i in step_out_df],
                        data=None,
                        editable=False,
                        style_table={
                            'maxWidth': '10%',
                            'margin': 'auto',
                            'marginLeft': '20px',
                            'marginTop': '20px',
                            
                            # add margin to the top
                        },
                        style_header={
                            'backgroundColor': 'royalblue',
                            'color': 'white',
                            'fontWeight': 'bold',
                            'text-align': 'center'
                        },
                        style_cell={'textAlign': 'center', 'fontSize':'0.75vw'}
                    ),
                    className="six columns",
                    style={"display": "inline-block",'text-align': 'center'}
                ),
            ],
            style={"display": "flex", 'text-align': 'center','justify-content': 'center','width':'100%','marginTop':'20px'}
        )
    ]
),

     # 3 GRAFICI PICCOLI
     html.Div(children=[html.H1("Prezzo vs Prezzo Medio di Carico vs Prezzo Medio", style={"font-size": "0.9vw","text-align": "center"}),
                        dcc.Graph(id='pmc1', style={'width': '33%','height':'80%', 'display': 'inline-block'},config={'displayModeBar': False}),
                        dcc.Graph(id='pmc2', style={'width': '33%', 'height':'80%','display': 'inline-block'},config={'displayModeBar': False}),
                        dcc.Graph(id='pmc3', style={'width': '33%', 'height':'80%','display': 'inline-block'},config={'displayModeBar': False})
                        ], style={'height': '300px', 'margin': 'auto', 'justify-content': 'center','marginTop':'40px'})
    
     ]) 

#%% 

# Define callbacks
@app.callback(
    Output('amount-error', 'children'),
    Input('importo', 'value')
)
def check_amount(amount):
    if amount is not None and amount < 30000:
        return 'Minimo investito deve essere almeno €30.000'


@app.callback(
    [Output('grafico_iis', 'figure'),
     Output('istogramma', 'figure'),
     Output('stats', 'data'),
     Output('step_in', 'data'),
     Output('step_out', 'data'),
     Output('pmc1', 'figure'),
     Output('pmc2', 'figure'),
     Output('pmc3', 'figure')],
    [Input('start_date', 'value'),
     Input('importo', 'value'),
     Input('durata_months', 'value'),
     Input('fondo1', 'value'),
     Input('fondo2', 'value'),
     Input('fondo3', 'value'),
     Input('input1', 'value'),
     Input('input2', 'value'),
     Input('input3', 'value'),
     Input('step_out1', 'value'),
     Input('step_out2', 'value'),
     Input('step_out3', 'value'),
     Input('btn-nclicks-1', 'n_clicks'),
     Input('btn-nclicks-2', 'n_clicks'),
     Input('btn-nclicks-3', 'n_clicks'),
     Input('btn-nclicks-all', 'n_clicks'),
     ]
)

def motore(start_date, importo, durata_months, fondo1, fondo2, fondo3, input1, input2, input3, step_out1, step_out2, step_out3, btn1, btn2, btn3, btnall ):




