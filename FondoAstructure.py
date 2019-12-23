import pandas as pd
df = pd.read_csv("tabula-portfolio.csv",index_col=0)
names = ['Fondo A', 'Fondo B','Fondo C','Fondo D','Fondo E','Total Millones','% Fondo']
df.iloc[0] = names

df1 = df['A'].str.split(' ',expand=True)
df2 = df['B'].str.split(' ',expand=True)
df3 = df['C'].str.split(' ',expand=True)
df4 = df['D'].str.split(' ',expand=True)
df5 = df['E'].str.split(' ',expand=True)


suma = [df1,df2,df3,df4,df5]
total = pd.concat(suma,axis=1,sort='False')
nombres = ['MM$ A','% Fondo A','MM$ B','% Fondo B','MM$ C','% Fondo C','MM$ D','% Fondo D','MM$ E','% Fondo E']
import numpy as np 

total.iloc[0] = nombres
#total.drop(['INVERSIÓN NACIONAL TOTAL' , 'TOTAL ACTIVOS'],inplace=True)

porcentajes=total[1]
porcentajes.reset_index(level=0, inplace=True)


#porcentajes = porcentajes.drop([19], axis=0)
#porcentajes['Ex o Na'] = ['Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na','Na']
#porcentajes['Ex o Na'][20,:]

#porcentajes.rename(columns={'Index':'Item','1':'Fondo A','1':'Fondo B','1':'Fondo C','1':'Fondo D','1':'Fondo E'})      
#porcentajes.drop(['INVERSIÓN NACIONAL TOTAL','INVERSIÓN EXTRANJERA TOTAL','TOTAL ACTIVOS'],axis=0)      

#['INVERSIÓN NACIONAL TOTAL','INVERSIÓN EXTRANJERA TOTAL','TOTAL ACTIVOS']

#len(porcentajes['% Fondo A'])


porcentajes.set_index('index',inplace=True)

porcentajes = porcentajes.drop(['INVERSIÓN NACIONAL TOTAL','INVERSIÓN EXTRANJERA TOTAL','TOTAL ACTIVOS'])

porcentajes.columns = porcentajes.iloc[0]
#porcentajes = porcentajes.drop('nan')
porcentajes = porcentajes.iloc[1:]
porcentajes = porcentajes.rename_axis(None)
del porcentajes.columns.name



porcentajes.reset_index(level=0, inplace=True)

#porcentajes = porcentajes.rename(index={'RENTA VARIABLE':'RENTA VARIABLE NACIONAL'})
porcentajes.iloc[18:,0] = ['Renta Variable Extranjera','Fondos Mutuos Extranjeros','Activos Alternativos Extranjeros','Otros Extranjeros','Renta Fija Extrajera','Derivados Extranjeros','Otros instrumentos extranjeros']
porcentajes['% Fondo A'] = porcentajes['% Fondo A'].apply(lambda x: x.replace(',','.'))

porcentajes['% Fondo A'] = porcentajes['% Fondo A'].str.rstrip('%').astype('float') / 100.0

from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices = porcentajes['% Fondo A']
labels = porcentajes['index']
plt.pie(slices,labels=labels,autopct='%1.1f%%')

plt.title('AFP Fondo A')
#plt.tight_layout()
plt.show()
