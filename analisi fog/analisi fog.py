import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
directory = r'C:\Users\william.marzo\OneDrive - Banca Mediolanum SPA\Desktop\analisi fog'
os.chdir(directory)

#%%

df = pd.read_excel("dati_FOG.xlsx", sheet_name="Quota Rettificata")
df = df[2:]
df = df.rename(columns={'Unnamed: 0': 'date'})

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

 
# Usiamo resample per selezionare l'ultimo giorno di ogni mese
end_of_month = df.resample('M').last()
ret = end_of_month.pct_change().dropna()


min2022 = ret[ret.index < "2022"]
magg2010 = ret[ret.index > "1988"]

 

 
final_2011_5y = pd.DataFrame(columns=magg2010.index, index=range(0,60+1))
final_2011_10y= pd.DataFrame(columns=magg2010.index, index=range(0,120+1))


for j in range(len(magg2010)):
    start = j
    
    if len(magg2010.iloc[start:]) > 60:
        end = j + 60
    else:
        end = j+len(magg2010.iloc[start:])
        
    temp = magg2010.iloc[start:end]
    
    #5 anni = 60 mesi
    cum = [1]
    for i in range(len(temp)):
        cum.append(cum[-1] * (1 + temp.iloc[i][0]))
        
    cum=pd.Series(cum)
    cum = cum.reindex(final_2011_5y.index, fill_value=np.NaN)
    final_2011_5y[temp.index[0]] = cum


for j in range(len(magg2010)):
    start = j
    
    if len(magg2010.iloc[start:]) > 120:
        end = j + 120
    else:
        end = j+len(magg2010.iloc[start:])
        
    temp = magg2010.iloc[start:end]
    
    #5 anni = 60 mesi
    cum = [1]
    for i in range(len(temp)):
        cum.append(cum[-1] * (1 + temp.iloc[i][0]))
        
    cum=pd.Series(cum)
    cum = cum.reindex(final_2011_10y.index, fill_value=np.NaN)
    final_2011_10y[temp.index[0]] = cum


#%%% CON COMIISIONI DI GESTIONE 0,50% ANNUO

df = pd.read_excel("dati_FOG.xlsx", sheet_name="Quota Lorda 2")
df = df[2:]
df = df.rename(columns={'Unnamed: 0': 'date'})

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

 
# Usiamo resample per selezionare l'ultimo giorno di ogni mese
end_of_month = df.resample('M').last()
ret = end_of_month.pct_change().dropna()


min2022 = ret[ret.index < "2022"]
magg2010 = ret[ret.index > "1988"]

final_2011_5y_com = pd.DataFrame(columns=magg2010.index, index=range(0,60+1))
final_2011_10y_com= pd.DataFrame(columns=magg2010.index, index=range(0,120+1))


for j in range(len(magg2010)):
    start = j
    
    if len(magg2010.iloc[start:]) > 60:
        end = j + 60
    else:
        end = j+len(magg2010.iloc[start:])
        
    temp = magg2010.iloc[start:end]
    
    #5 anni = 60 mesi
    cum = [1]
    for i in range(len(temp)):
        cum.append(cum[-1] * (1 + temp.iloc[i][0] - 0.005/12))
        
    cum=pd.Series(cum)
    cum = cum.reindex(final_2011_5y_com.index, fill_value=np.NaN)
    final_2011_5y_com[temp.index[0]] = cum


for j in range(len(magg2010)):
    start = j
    
    if len(magg2010.iloc[start:]) > 120:
        end = j + 120
    else:
        end = j+len(magg2010.iloc[start:])
        
    temp = magg2010.iloc[start:end]
    
    #5 anni = 60 mesi
    cum = [1]
    for i in range(len(temp)):
        cum.append(cum[-1] * (1 + temp.iloc[i][0]- 0.005/12))
        
    cum=pd.Series(cum)
    cum = cum.reindex(final_2011_10y_com.index, fill_value=np.NaN)
    final_2011_10y_com[temp.index[0]] = cum

plt.plot(final_2011_10y)
#%% esporto file su excel

final_2011_5y.columns=final_2011_5y.columns.date
final_2011_10y.columns=final_2011_10y.columns.date
final_2011_5y_com.columns=final_2011_5y_com.columns.date
final_2011_10y_com.columns=final_2011_10y_com.columns.date




from openpyxl import load_workbook




# Your DataFrame creation and manipulation code here




# The name of the Excel file you want to append to

file_name = "Simulazioni FOG 1988_2023_corrette.xlsx"




# Load the existing Excel file using openpyxl

book = load_workbook(file_name)




# Create an ExcelWriter object with the loaded book

writer = pd.ExcelWriter(file_name, engine='openpyxl')

writer.book = book




# Write the DataFrame to the Excel file, to a new sheet named 'Sheet2'

final_2011_5y.to_excel(writer, sheet_name='5Y_no_commissioni')
final_2011_5y_com.to_excel(writer, sheet_name='5Y_commissioni')
final_2011_10y.to_excel(writer, sheet_name='10Y_no_commissioni')
final_2011_10y_com.to_excel(writer, sheet_name='10Y_commissioni')



# Save the changes

writer.save()
writer.close()




#%%
count_positive = pd.DataFrame(columns=final_2011_5y.columns, index=[0])

for c in final_2011_5y.columns:
    count_positive[c].iloc[0] = final_2011_5y[c].dropna().iloc[-1]

positive_rate = len(count_positive.iloc[0][count_positive.iloc[0] > 1]) / len(count_positive.columns)


final_2011_5y.iloc[-1][final_2011_5y.iloc[-1]>0] / final_2011_5y.iloc[-1]
