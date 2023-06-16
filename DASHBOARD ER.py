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
url = 'https://raw.githubusercontent.com/TurcanuDionisie/Dashboard_ER/main/'


#%% CARICAMENTO DATI SOTTOSTANTI E NON VARIABILI

#  QUOTA NETTA
file_path = url+ "universo_mgf_italiani.xlsx" 
sheet_name = "Quota Pubb Rettificata"
qpubb_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qpubb_MGF = qpubb_MGF.iloc[2:]


file_path = url+"universo_ch_mif_sintesi.xlsx" 
sheet_name = "Q.ta Pubblicata"
qpubb_CH_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qpubb_CH_MIF.columns = qpubb_CH_MIF.iloc[1]
qpubb_CH_MIF = qpubb_CH_MIF[2:]


file_path = url+"universo_mbb_mif_sintesi.xlsx" 
sheet_name = "Q.ta Pubblicata"
qpubb_MBB_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qpubb_MBB_MIF.columns = qpubb_MBB_MIF.iloc[1]
qpubb_MBB_MIF = qpubb_MBB_MIF[2:]


file_path = url+"universo_gamax_sintesi.xlsx" 
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
file_path = url+ "universo_mgf_italiani.xlsx" 
sheet_name = "Quota Lorda Opz 2"
qlorda_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qlorda_MGF = qlorda_MGF.iloc[2:]


file_path = url+"universo_ch_mif_sintesi.xlsx" 
sheet_name = "Q.ta BMK"
qlorda_CH_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qlorda_CH_MIF.columns = qlorda_CH_MIF.iloc[1]
qlorda_CH_MIF = qlorda_CH_MIF[2:]


file_path = url+"universo_mbb_mif_sintesi.xlsx"  
sheet_name = "Q.ta BMK"
qlorda_MBB_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
qlorda_MBB_MIF.columns = qlorda_MBB_MIF.iloc[1]
qlorda_MBB_MIF = qlorda_MBB_MIF[2:]


file_path = url+"universo_gamax_sintesi.xlsx" 
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

file_path = url+ "universo_mgf_italiani.xlsx" 
sheet_name = "NAV Totale"
nav_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
nav_MGF.columns = nav_MGF.iloc[0]
nav_MGF = nav_MGF.iloc[2:]

file_path = url+"universo_ch_mif_sintesi.xlsx" 
sheet_name = "NAV Totale"
nav_CH_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
nav_CH_MIF.columns = nav_CH_MIF.iloc[0]
nav_CH_MIF = nav_CH_MIF[2:]
nav_CH_MIF = nav_CH_MIF.drop(nav_CH_MIF.columns[-1], axis=1)

file_path = url+"universo_mbb_mif_sintesi.xlsx" 
sheet_name = "NAV Totale"
nav_MBB_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
nav_MBB_MIF.columns = nav_MBB_MIF.iloc[0]
nav_MBB_MIF = nav_MBB_MIF[2:]
nav_MBB_MIF = nav_MBB_MIF[nav_MBB_MIF.columns[:-1]]

file_path = url+"universo_gamax_sintesi.xlsx"  
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
file_path = url+ "universo_mgf_italiani.xlsx" 
sheet_name = "BMK_SERIE_STO"
bmk_MGF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
bmk_MGF.columns = bmk_MGF.iloc[0]
bmk_MGF = bmk_MGF[3:]


file_path = url+"universo_ch_mif_sintesi.xlsx" 
sheet_name = "BMK"
bmk_CH_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
bmk_CH_MIF.columns = bmk_CH_MIF.iloc[0]
bmk_CH_MIF = bmk_CH_MIF[1:]


file_path = url+"universo_mbb_mif_sintesi.xlsx" 
sheet_name = "BMK"
bmk_MBB_MIF = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
bmk_MBB_MIF.columns = bmk_MBB_MIF.iloc[0]
bmk_MBB_MIF = bmk_MBB_MIF[1:]


file_path = url+"universo_gamax_sintesi.xlsx" 
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
file_path = url+"universo_categoria_morningstar.xlsx" 
sheet_name = "Cat MStar utilizzate"
cat_morningstar = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)
cat_morningstar = cat_morningstar.iloc[2:]


cat_morningstar = cat_morningstar.apply(pd.to_numeric) 


#FILE DECODIFICA ALL 

codifiche_all = pd.read_excel(url+'codifiche.xlsx', sheet_name='codifica').set_index('Isin')

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


#%% ELEMENTI PER LA DASHBOARD
nome_fondi = codifiche_all[(codifiche_all['CAT'] == 'SI') | (codifiche_all['BMK'] == 'SI') & (codifiche_all['posizionamento'] == 'SI')] 

from datetime import timedelta

today = dt.today()
first_day_of_month = dt(today.year, today.month, 1)
last_day_of_previous_month = first_day_of_month - timedelta(days=1)

end_of_previous_month = last_day_of_previous_month.strftime('%Y-%m-%d')

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
    # html.Div([
        html.Div(html.H1('DashBoard ER'), style={'margin-left': '20px', 'justify-content': 'center','display': 'flex', 'align-items': 'flex-end'}),
        html.Div(html.H2('by Monitoraggio & Analisi Prodotti di Investimento', 
                 style={'margin-top':'-10px','color': 'black', 'font-style': 'italic', 'font-weight': 'normal','font-size': '1.85vh', 'margin-left': '0px','margin-bottom':'20px', 'justify-content': 'center'}),
                 style={'margin-left': '20px', 'justify-content': 'center','display': 'flex', 'align-items': 'flex-end'}),

    # ],style={'margin-left': '20px', 'justify-content': 'center','display': 'flex', 'align-items': 'flex-end'}),
    
    # TABELLA INPUT
    html.Div([
        
        #FILTRO DATA
        html.Div(
            [   
                dcc.DatePickerSingle(
                    id='date_picker',
                    date=None
                ),
                html.Div(id='date_error')
            ]
        ),
        

        
        #FILTRO SOCIETA
        html.Div(
        style={'text-align': 'center', 'margin-left': '30px'},  # Added style to center align the content
        children=[
            html.H2('SOCIETA', style={'color': 'black', 'font-style': 'italic', 'font-weight': 'normal', 'font-size': '1.85vh', 'margin-left': '0px', 'margin-bottom': '20px'}),
            dcc.RadioItems(
                id='societa',
                options=[{'label': i, 'value': i} for i in ['ALL', 'MIF+GAMAX', 'MGF']],
            )
        ]
    ),

        #FILTRO ASSET CLASS
        html.Div(
        style={'text-align': 'center', 'margin-left': '30px'},  # Added style to center align the content
        children=[
            html.H2('ASSET CLASS', style={'color': 'black', 'font-style': 'italic', 'font-weight': 'normal', 'font-size': '1.85vh', 'margin-left': '0px', 'margin-bottom': '20px'}),
            dcc.RadioItems(
                id='asset_class',
                options=[{'label': i, 'value': i} for i in ['ALL', 'Equity', 'Fixed Income','Multi Asset']],
            )
        ]
    ),

        #FILTRO RANKING SI/NO
        html.Div(
        style={'text-align': 'center', 'margin-left': '30px'},  # Added style to center align the content
        children=[
            html.H2('RANKING', style={'color': 'black', 'font-style': 'italic', 'font-weight': 'normal', 'font-size': '1.85vh', 'margin-left': '0px', 'margin-bottom': '20px'}),
            dcc.RadioItems(
                id='ranking',
                options=[{'label': i, 'value': i} for i in ['ALL','SI', 'NO']],
            )
        ]
    ),
        #FILTRO MEDIA SI/NO
        html.Div(
        style={'text-align': 'center', 'margin-left': '30px'},  # Added style to center align the content
        children=[
            html.H2('MEDIA', style={'color': 'black', 'font-style': 'italic', 'font-weight': 'normal', 'font-size': '1.85vh', 'margin-left': '0px', 'margin-bottom': '20px'}),
            dcc.RadioItems(
                id='media',
                options=[{'label': i, 'value': i} for i in ['Semplice', 'Ponderata per NAV']],
            )
        ]
    ),
        

    ], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '10px'}),
    
    
    #GRAFICI GROSSI
    html.Div([
        dcc.Graph(id='grafico_er', style={'height': '100%', 'width': '100%'}) # questo è il componente in cui il grafico verrà visualizzato
    ],style={'height': '700px','justify-content': 'center'}),          
    
    
    html.Div([
        html.H1('Dettaglio Fondo')
    ],style={'margin-left': '20px', 'justify-content': 'center','display': 'flex', 'align-items': 'flex-end'}),
    
    
    #FILTRO DETTAGLIO FONDO
    html.Div(
        style={'text-align': 'center', 'margin-left': '30px'},  # Added style to center align the content
        children=[
            dcc.Dropdown(
                id='dettaglio_fondo',
                options=[{'label': nome_fondi["Nome 2"].loc[fondo], 'value': fondo} for fondo in nome_fondi.index],
                style={'width': '70%','height':'80%', 'display': 'inline-block'}
                ),
            
            html.Div('Dati al: ' + end_of_previous_month, style={'margin-top':'20px'}),
            dash_table.DataTable(
                    id='tabella',
                    columns=[
                        {"name": ["Category"], "id": "cat"},
                        {"name": ["Type"], "id": "type"},
                        {"name": ["1M"], "id": "m1"},
                        {"name": ["3M"], "id": "m3"},
                        {"name": ["YTD"], "id": "ytd"},
                        {"name": ["1Y"], "id": "y1"},   
                        {"name": ["2022"], "id": "_2022_"}, 
                        {"name": ["2021"], "id": "_2021_"},
                        {"name": ["2020"], "id": "_2020_"},

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
        ]
    ),
    
    
    
    #GRAFICI GROSSI
    html.Div([
        dcc.Graph(id='grafico_dettaglio') # questo è il componente in cui il grafico verrà visualizzato
    ], style={'margin-top':'20px'} ),  
    

 ]) 


@app.callback(
    Output('date_error', 'children'),
    [Input('date_picker', 'date')]
)
def update_output(date):
    if date is not None:
        return f"The selected date is {date}"
    else:
        return "Please select a date."
    

@app.callback(
    Output('grafico_er', 'figure'),
    [Input('date_picker', 'date'),
      Input('societa', 'value'),
      Input('asset_class', 'value'),
      Input('ranking', 'value'),
      Input('media', 'value'),
      ]
)

def motore(date_picker, societa, asset_class, ranking, media):
    
    if date_picker is not None and societa is not None and asset_class is not None and ranking is not None and media is not None:
        
        print(date_picker)
        print(societa)
        print(asset_class)
        print(ranking)
        print(media)
        
        

        ret_quota_netta = quota_netta.pct_change()[1:]
        ret_quota_lorda = quota_lorda.pct_change()[1:]
        ret_bmk = bmk.pct_change()[1:]
        ret_categoria = cat_morningstar.pct_change()[1:]

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



        
        # SOCIETA: ['ALL', 'MIF+GAMAX', 'MGF']
        if societa == 'ALL' :
            soc = ['MIF','GAMAX','MGF']
        elif societa == 'MIF+GAMAX' :
            soc = ['MIF','GAMAX']
        elif societa == 'MGF' :
            soc = ['MGF']
        
        # SOCIETA: ['ALL', 'MIF+GAMAX', 'MGF']
        if asset_class == 'ALL' :
            ac = ['Equity','FixedIncome','MultiAsset']
        elif asset_class == 'Equity' :
            ac = ['Equity']
        elif asset_class == 'Fixed Income' :
            ac = ['FixedIncome']
        elif asset_class == 'Multi Asset':
            ac = ['MultiAsset']
        
       # RANKING ['ALL','SI','NO']
        if ranking == 'ALL' :
            rk = ['SI','NO']
        elif ranking == 'SI' :
            rk = ['SI']
        elif ranking == 'NO' :
            rk = ['NO']

       

        codifiche = codifiche_all[(codifiche_all['BMK'] == 'SI') & (codifiche_all['SGR'].isin(soc)) & (codifiche_all['Asset class'].isin(ac)) & (codifiche_all['posizionamento'].isin(rk))]


        decodifica_bmk = codifiche[['serve per BMK']]
        map_dict = decodifica_bmk.to_dict().get('serve per BMK')

        isin = codifiche[(codifiche['BMK'] == 'SI')].index
        ret = ret_quota_lorda[isin][ret_quota_lorda.index >= date_picker]

        nav_lordo = nav_lordo_all[isin].copy()
        for t in nav_lordo.index:
            nav_lordo.loc[t] = nav_lordo.loc[t]/sum(nav_lordo.loc[t])

        alfa = ret.copy()
        for i in ret.columns:
            alfa[i] = ret_bmk[map_dict[i]]
            
        ret_pond = None
        
        if media == 'Semplice':
            ret_pond = ret * 1/len(ret)
            ret_pond = ret_pond.sum(axis=1)
            alfa_pond = alfa * 1/len(alfa)
            alfa_pond = alfa_pond.sum(axis=1)
            
        if media == 'Ponderata per NAV':
            ret_pond = ret * nav_lordo[isin][nav_lordo.index >= date_picker]
            ret_pond = ret_pond.sum(axis=1)
            alfa_pond = alfa * nav_lordo[isin][nav_lordo.index >= date_picker]
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


        codifiche = codifiche_all[(codifiche_all['CAT'] == 'SI') & (codifiche_all['SGR'].isin(soc)) & (codifiche_all['Asset class'].isin(ac)) & (codifiche_all['posizionamento'].isin(rk))]


        decodifica_bmk = codifiche[['serve per CAT M*']]
        map_dict = decodifica_bmk.to_dict().get('serve per CAT M*')

        isin = codifiche[(codifiche['CAT'] == 'SI')].index
        ret = ret_quota_netta[isin][ret_quota_netta.index >= date_picker]

        nav_netto = nav_netto_all[isin].copy()
        for t in nav_netto.index:
            nav_netto.loc[t] = nav_netto.loc[t]/sum(nav_netto.loc[t])

        alfa = ret.copy()
        for i in ret.columns:
            alfa[i] = ret_categoria[map_dict[i]]
        
        ret_pond = None
        if media == 'Semplice':
            ret_pond = ret * 1/len(ret)
            ret_pond = ret_pond.sum(axis=1)
            alfa_pond = alfa * 1/len(alfa)
            alfa_pond = alfa_pond.sum(axis=1)
            
        if media == 'Ponderata per NAV':
            ret_pond = ret * nav_netto[isin][nav_netto.index >= date_picker]
            ret_pond = ret_pond.sum(axis=1)
            alfa_pond = alfa * nav_netto[isin][nav_netto.index >= date_picker]
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
        
        
          
    
        
        #GRAFICO AGGREGATO
        
        
        er_graph = go.Figure()
        er_graph.add_trace(go.Scatter(x=er_netto.index, y=er_netto, mode='lines', name='ER Netto', line=dict(color='lightsteelblue'),hovertemplate='(%{x}, %{y:.2f}%)'))
        er_graph.add_trace(go.Scatter(x=er_lordo.index,y=er_lordo, mode='lines', name='ER Lordo', line=dict(color='midnightblue'),hovertemplate='(%{x}, %{y:.2f}%)'))
        
        # er_graph.update_layout(legend=dict(orientation="h", yanchor="top", y=1.07, xanchor="center", x=0.15, font=dict(size=15)),
        #                        title={'text':f'Dettaglio ER dati al '+str(er_netto.index[1]), 'font':{'size': 24}, 'x': 0.5,'y': 0.95, 'xanchor': 'center','yanchor': 'top'},
        #                        plot_bgcolor='white',xaxis=dict(showgrid=False),yaxis=dict(showgrid=True, gridcolor='lightgrey', 
        #                        gridwidth=1, tickwidth=2, tickformat='%'))
        
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
                'text':f'Dettaglio ER dal '+ str(er_netto.index[0].strftime("%Y-%m-%d")) + ' al ' + str(er_netto.index[-1].strftime("%Y-%m-%d")),
                'font': {'size': 24},
                'x': 0.5,
                'y': 0.95,
                'xanchor': 'center',
                'yanchor': 'top'
            },
        plot_bgcolor='white',
        xaxis=dict(showgrid=False),
        yaxis=dict(
            showgrid=True,
            gridcolor='lightgrey',
            gridwidth=1,
            tickwidth=2,
            tickformat=',.2%',  # Rounded to 2 decimals and displayed as percentage
            
        )
        )

            
        
        return er_graph
    else:
        return {}
    
    
    
    
@app.callback(
    [Output('grafico_dettaglio', 'figure'),
    Output('tabella', 'data')],
    [Input('dettaglio_fondo', 'value'),
     Input('date_picker', 'date')]
)

def motoreDettaglio(dettaglio_fondo, date_picker):
    
    if dettaglio_fondo is not None and date_picker is not None:
        
            
        ret_quota_netta = quota_netta.pct_change()[1:]
        ret_quota_lorda = quota_lorda.pct_change()[1:]
        ret_bmk = bmk.pct_change()[1:]
        ret_categoria = cat_morningstar.pct_change()[1:]
        
        
        
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
            
        
    
    
        # GRAFICO DETTAGLIO FONDO
        fondo_graph = go.Figure()
        
        if(dettaglio_fondo in (nome_fondi_netto.index)):
            fondo_graph.add_trace(go.Scatter(x=er_netto.index, y=er_netto, mode='lines', name='ER Netto', line=dict(color='lightsteelblue'), hovertemplate='(%{x}, %{y:.2f}%)'))
        
        if(dettaglio_fondo in (nome_fondi_lordo.index)):
            fondo_graph.add_trace(go.Scatter(x=er_lordo.index,y=er_lordo, mode='lines', name='ER Lordo', line=dict(color='midnightblue'), hovertemplate='(%{x}, %{y:.2f}%)'))
        
        
        fondo_graph.update_layout(legend=dict(orientation="h", yanchor="top", y=1.07, xanchor="center", x=0.15, font=dict(size=15)), 
                                  title={'text':f'Dettaglio ER dal '+ str(er_netto.index[0].strftime("%Y-%m-%d")) + ' al ' + str(er_netto.index[-1].strftime("%Y-%m-%d")) , 
                                'font':{'size': 24}, 'x': 0.5,'y': 0.95, 'xanchor': 'center','yanchor': 'top'},
                                plot_bgcolor='white',xaxis=dict(showgrid=False),yaxis=dict(showgrid=True, gridcolor='lightgrey', 
                                gridwidth=1, tickwidth=2, tickformat=',.2%'))
        
        
        
        podio = pd.read_excel(url+'dati_podio.xlsx', sheet_name ='x dashboard')
        podio= podio.set_index('isin')

        
        tab = pd.DataFrame(index = ['rk_net','rk_gross','er_net','er_gross','perf'], columns=['Categoria','1M','3M','YTD','1Y','2022','2021','2020'])
        
        for t in ['1M','3M','YTD','1Y','2022','2021','2020']:
            tab[t].loc['rk_net'] = str(np.array(round(podio['net_'+t].loc[dettaglio_fondo]*100,2))) +'%'
            tab[t].loc['rk_gross'] = str(np.array(round(podio['gross_'+t].loc[dettaglio_fondo]*100,2))) +'%'
            tab[t].loc['er_net'] = str(np.array(round(podio['ernetto_'+t].loc[dettaglio_fondo]*100,2))) +'%'
            tab[t].loc['er_gross'] = str(np.array(round(podio['erlordo_'+t].loc[dettaglio_fondo]*100,2))) +'%'
            tab[t].loc['perf'] = str(np.array(round(podio['perf_'+t].loc[dettaglio_fondo]*100,2))) +'%'
        
        tab['Categoria'].loc['rk_net'] = nome_fondi['Asset class'].loc[dettaglio_fondo]
        
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
        
        return fondo_graph, tabs
    
    else:
        return {}


if __name__ == '__main__':
    app.run_server()

