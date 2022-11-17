import requests
import json
from datetime import datetime


Momentos = []
Temperaturas = []
Dias = []

appid = "a3a7114576a3b54a0a02aee0bb777dea"

#Generamos el link de nuestra ciudad y aplicamos el método request.get para hacer la solicitud http a OpenWeather
page=requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=41.389&lon=2.159&exclude=minutely,hourly&units=metric&appid="+appid)

#Convertimos la cadena JSON obtenida en un diccionario de Python utilizando el método json.loads()
Clima_INFO = json.loads(page.content)


for x, y in Clima_INFO.items():
    #Buscamos donde comienza la información de temperaturas de cada día, esto se sabe pues 
    #Cada día diferente inicia con la clave "daily"
    if x == "daily":
        for i in y[1:5]:
            Fecha = int(i['dt'])

            Actual = datetime.utcfromtimestamp(Fecha).strftime("%Y-%m-%d")
            Dias.append(Actual)

            for key in i['temp']:
                Momentos.append(key)
            
                Temperaturas.append(i['temp']['day'])
                Temperaturas.append(i['temp']['eve'])
                Temperaturas.append(i['temp']['night'])
                Temperaturas.append(i['temp']['min'])
                Temperaturas.append(i['temp']['max'])

temp_max_min = {"Dia 1":[Temperaturas[1], Temperaturas[2]], 
"Dia 2":[Temperaturas[7], Temperaturas[8]], 
"Dia 3":[Temperaturas[14], Temperaturas[13]],
"Dia 4":[Temperaturas[19], Temperaturas[20]]}

print("Temperaturas máximas y mínimas: ")
print(temp_max_min)