from __future__ import division
import pandas as pd
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta
from sympy import symbols,Eq, solve
 
#Este proyecto se hizo con el fin de crear una Zero Yield Curve a partir de los contratos swaps transados en el mercado chileno.
#El objetivo era crear un shock de 1bp en cada uno de los tenors desde 6m hasta 10yrs, con el fin de medir la sensibilidad de la cartera
#al shock de un bp en la curva. 
#Son 20 escenarios, si gustas puedes editarla y generar una curva de una iteración para tener la curva zero, guardé pero ni printié la curva zero compuesta, esta calculada con convención lineal. 


dficap=pd.read_excel(‘ruta del excel’)
dficap['Promedios'] = (dficap['Mid'] + dficap['Mid'] + dficap['Mid'])/3
dficap['Promedios'].tolist()
columnas=['6M','1Y','1.5Y','2Y','2.5Y','3Y','3.5Y','4Y','4.5Y','5Y','5.5Y','6Y','6.5Y','7Y','7.5Y','8Y','8.5Y','9Y','9.5Y','10Y']

 
for vargas,t in zip(range(0,20),columnas):

    dficap.iloc[vargas,5]=dficap.iloc[vargas,5] + 0.01
    fechaanalisis=date(2019,9,24)
    fechamaturity=fechaanalisis+relativedelta(days=+3600)
    fechapivot=date(2019,9,24)
    days=[]
    dfdiscount=[]  
    DaysReal=dficap['DaysReal']
    tasaszero=dficap['Promedios'][0:3].tolist()
    i=4
    tasaszero=dficap['Promedios'][0:3].tolist()
    tasascompuestas=dficap['Promedios'][3:]
    lineales=[] 

    for zero,day in zip(tasaszero[0:3],DaysReal[0:3]):

        monto = (((1+zero/100)**(day/360))-1)*36000/day
        lineales.append(monto)
    while fechamaturity>fechapivot:  

        fechapivot+=relativedelta(months=+6)
        a=fechapivot-relativedelta(months=+6)
        days.append((fechapivot-a).days)
        dias=fechapivot-fechaanalisis
        dfdiscount.append(dias.days)
  
    for i in range(4,21):
        cupones=[]       
        descontaos=[]
        for y in days[0:i]:

            a=((tasascompuestas[i-1])/100)*(y/360)
            cupones.append(a)
        

        cupones[len(cupones)-1]=cupones[len(cupones)-1]+1
        last = cupones[len(cupones)-1]       
        cupones.pop(i-1)            
        for z,alfa,cupones in zip(dfdiscount[0:i-1],tasaszero[0:i-1],cupones[0:i-1]):
            vector=cupones/((1+alfa/100)**(z/360))
            descontaos.append(vector)
        #print(descontaos)      
        x=symbols('x')
        ecuacion=Eq(sum(np.asarray(descontaos))-1+(last/((1+x)**(dfdiscount[i-1]/360))))          
        resultado=solve(ecuacion,x,rational=False)  
        chor=((((1+resultado[0])**(DaysReal[i-1]/360))-1)*360/DaysReal[i-1])*100
        lineales.append(chor)  
        tasaszero.append(resultado[0]*100)
    

    print(t)
    dficap.iloc[vargas,5]=dficap.iloc[vargas,5] - 0.01   
    dficap[t] = lineales

               



print(dficap)

 
