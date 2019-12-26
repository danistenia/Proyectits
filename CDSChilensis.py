

df = pd.read_excel('T:\ControlFinanciero\TREATS\DVAR\Data Science\CDS.xlsx',usecols=[0,1,2],skipfooter=11)

df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=[25,5])

x = df['Date']
y = df['CDS 1 YR']
z = df['CDS 2 YR']

plt.plot(x,y,linewidth=4)
plt.plot(x,z,linewidth=3)
plt.axvline(x=df['Date'][50],linestyle='--',color='r')

plt.axhline(y=27,linestyle='--',color='r')
plt.axvline(x=df['Date'][12],linestyle='-',color='g')




#print(df)

plt.title('CDS 1 year and 2 year')
plt.xlabel('Meses-Periodos')
plt.ylabel('CDS Spread')



plt.legend(['CDS 1 YR','CDS 2 YR'])
plt.tick_params(axis='y',which='both',labelleft='off',labelright='on')
plt.show()
#print(df['Date'])



