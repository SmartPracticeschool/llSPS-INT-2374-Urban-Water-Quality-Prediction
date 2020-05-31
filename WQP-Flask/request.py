import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Temp':28.7, 'D.O. (mg/l)':6.4, 'CONDUCTIVITY (µmhos/cm)':189, 'B.O.D. (mg/l)':2,'NITRATENAN N+ NITRITENANN (mg/l)':0.1,'FECAL COLIFORM (MPN/100ml)':4500, 'TOTAL COLIFORM (MPN/100ml)Mean':5500})

print(r.json())



