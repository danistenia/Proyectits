from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.dates as mdates





df = pd.read_excel('T:/retail.xlsx')
plt.style.use('bmh')


fig, axs = plt.subplots(2,2)


df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m')

#df['Date'] = mdates.DateFormatter('%Y-%m-%d')


p = df['Date'][0:200]

    
q = df['Falabella'][0:200]
r = df['Ripley'][0:200]
s = df['Cencosud'][0:200]
t = df['La polar'][0:200]




axs[0,0].plot(p,q,label='Falabella',color='r')
axs[0,0].set_title('Falabella',color='k')
axs[0,0].axvline(x=df['Date'][49],linestyle='-',color='k',linewidth=2)



axs[0,1].plot(p,r,label='Ripley',color='g')
axs[0,1].set_title('Ripley',color='k')
axs[0,1].axvline(x=df['Date'][49],linestyle='-',color='k',linewidth=2)



axs[1,0].plot(p,s,label='Cencosud',color='b')
axs[1,0].set_title('Cencosud',color='k')
axs[1,0].axvline(x=df['Date'][49],linestyle='-',color='k',linewidth=2)



axs[1,1].plot(p,t,label='La polar',color='y')
axs[1,1].set_title('La polar',color='k')
axs[1,1].axvline(x=df['Date'][49],linestyle='-',color='k',linewidth=2)




plt.show()
