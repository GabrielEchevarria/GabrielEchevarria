# Interactuar con la API de Mercado Libre


import requests
from datetime import datetime
import os
import json

hoy = datetime.today()
nombreapi='trends'
region='MLA'
formato='json'
aniomes=hoy.strftime('%Y%m')

url=f'https://api.mercadolibre.com/{nombreapi}/{region}/MLA1051'

r = requests.get(url)
a=r.json()

path=nombreapi+formato+aniomes
if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)

with open(path+'/'+nombreapi+'.'+formato, 'w') as outfile:
    json.dump(a, outfile)
