
from __future__ import division
from datetime import date
from dateutil.relativedelta import relativedelta
import numpy as np



#Creamos listas para almacenar datos relevantes para presentación de resultados
  
def valbond(paper,formatofechaemi,formatofechaval,tir):
    cortes_ini=[]
    cortes_ini=[]
    cortes_fin=[]
    listadeltadias=[]
    largointerpol=[]
    bombita=[]
    nominal=1
 
    def acronimo(paper):
        if int(paper[5]) != 0:    
            couponrate=int(paper[4:6])/10
        else:
            couponrate=int(paper[4])
        return couponrate

    def fechaemi(formatofechaemi):
        if int(formatofechaemi[3])==0:
            emimonth=int(formatofechaemi[4:5])       
        else:
            emimonth=int(formatofechaemi[3:5])      
        if int(formatofechaemi[0])==0:
            emiday=int(formatofechaemi[1:2])      
        else:          
            emiday=int(formatofechaemi[0:2])
        emiyear=int(formatofechaemi[6:])
        fechaemision=date(emiyear,emimonth,emiday)
        return fechaemision
        
    def fechaval(formatofechaval):
        if int(formatofechaval[3])==0:           
            valmonth=int(formatofechaval[4:5])
        else:          
            valmonth=int(formatofechaval[3:5])       
        if int(formatofechaval[0])==0:
            valday=int(formatofechaval[1:2])
        else:           
            valday=int(formatofechaval[0:2])
            valyear=int(formatofechaval[6:])
        fechaanalisis=date(valyear,valmonth,valday)
        return fechaanalisis      
    
    def fechamat(paper):       
        matday=1       
        if int(paper[6])==0:
            matmonth=int(paper[7:8])           
        else:
            matmonth=int(paper[7])
        matyear=int(paper[8:])+2000
        fechamaturity=date(matyear,matmonth,matday)   
        return fechamaturity   
    
    
    couponrate=acronimo(paper)
    fechaemision=fechaemi(formatofechaemi)       
    fechaanalisis=fechaval(formatofechaval)
    fechamaturity=fechamat(paper)       


    print('La tasa coupon es de:',couponrate)
    print()  

            
    while fechamaturity>fechaemision:      
        fechaemision=fechaemision+relativedelta(months=+6)
        fecha_ini=fechaemision-relativedelta(months=+6)
        if fechaanalisis>fecha_ini and fechaanalisis<fechaemision:           
            cortes_fin.append(fechaemision.isoformat()) #deja las fechas de los cortes finales en la lista
            cortes_ini.append(fecha_ini.isoformat())   #
            listadeltadias.append((fechaemision-fecha_ini).days)
            largointerpol.append((fechaemision-fechaanalisis).days)

        elif fechaanalisis<fecha_ini and fechaanalisis<fechaemision:           
            cortes_fin.append(fechaemision.isoformat())
            cortes_ini.append(fecha_ini.isoformat())
            listadeltadias.append((fechaemision-fecha_ini).days)
            largointerpol.append((fechaemision-fechaanalisis).days)

    miarreglo=np.ones((len(largointerpol)))*(couponrate/200)
    miarreglo[len(miarreglo)-1]=miarreglo[len(miarreglo)-1]+nominal
    miarreglo2=np.asarray(largointerpol)
    print(miarreglo)  
    print()
    for i,j,k in zip(cortes_ini,cortes_fin,miarreglo):
        print(i+"   -   "+j)                   
    print()
    for k in miarreglo2:
        bombita.append(((1+tir)**(-k/365)))
   
    
    print()
    print()
    print("El precio sucio es: ",np.dot(miarreglo,bombita)*100)
    print("El precio limpio es",(np.dot(miarreglo,bombita)*100)-(((couponrate/36500)*(listadeltadias[0]-largointerpol[0])))*100)
