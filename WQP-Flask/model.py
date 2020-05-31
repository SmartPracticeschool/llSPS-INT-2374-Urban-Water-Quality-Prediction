# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

data=pd.read_csv('Water.csv',encoding='ISO-8859-1',low_memory=False)

#Data Preprocessing
data['STATION CODE'].fillna(data['STATION CODE'].mean(),inplace=True)
data['PH'].fillna(data['PH'].mean(),inplace=True)
data['CONDUCTIVITY (µmhos/cm)'].fillna(data['CONDUCTIVITY (µmhos/cm)'].mean(),inplace=True)
data['D.O. (mg/l)'].fillna(data['D.O. (mg/l)'].mean(),inplace=True)
x=['LOCATIONS','STATE']
data[x]=data[x].fillna(data.mode().iloc[0])
data['B.O.D. (mg/l)'] = pd.to_numeric(data['B.O.D. (mg/l)'],errors='coerce')
data['NITRATENAN N+ NITRITENANN (mg/l)'] = pd.to_numeric(data['NITRATENAN N+ NITRITENANN (mg/l)'],errors='coerce')
data['FECAL COLIFORM (MPN/100ml)'] = pd.to_numeric(data['FECAL COLIFORM (MPN/100ml)'],errors='coerce')
data['TOTAL COLIFORM (MPN/100ml)Mean'] = pd.to_numeric(data['TOTAL COLIFORM (MPN/100ml)Mean'],errors='coerce')
data['TOTAL COLIFORM (MPN/100ml)Mean'].fillna(60, inplace=True)
data['FECAL COLIFORM (MPN/100ml)'].fillna(17, inplace=True)
data['NITRATENAN N+ NITRITENANN (mg/l)'].fillna(1.42, inplace=True)
data['B.O.D. (mg/l)'].fillna(1.5, inplace=True)
data['Temp'] = pd.to_numeric(data['Temp'],errors='coerce')
data['Temp'].fillna(30,inplace=True)


X=data.iloc[:,3:10].values
Y=data.iloc[:,-1].values

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.ensemble import RandomForestRegressor
rig=RandomForestRegressor(n_estimators=100,random_state=0)

#Fitting model with trainig data
rig.fit(X,Y)

# Saving model to disk
pickle.dump(rig, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

a=model.predict([[27.2,5.6,200.0,1.5,0.1,3000.1,5000.5]])
if 6.6<a<7.4:
    print("Water is Potable with PH value :",a)
else:
    print("Contaminated water with PH value :",a)


