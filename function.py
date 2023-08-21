import requests
from config import *
from datetime import datetime
import pandas as pd
from pandas import json_normalize
import json


def search(lat, lon, key):
    # Consulta a la appi
    url = f'{baseUrl}lat={lat}&lon={lon}&appid={key}&units=metric'

    request = requests.get(url)

    if request.status_code == 200:
        # Restornar el resultado como un JSON
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code)


def normalize(request):
    # Normalizacion de la respuesta de la api

    extracted_data = []

    for item in request['list']:
        # Extraer los datos y crear una nueva lista de objetos
        main_data = item['main']
        extracted_item = {
            'dt': datetime.fromtimestamp(item['dt']),
            'city_name': request['city']['name'],
            'temp': main_data['temp'],
            'feels_like': main_data['feels_like'],
            'temp_min': main_data['temp_min'],
            'temp_max': main_data['temp_max'],
            'pressure': main_data['pressure'],
            'sea_level': main_data['sea_level'],
            'grnd_level': main_data['grnd_level'],
            'humidity': main_data['humidity'],
            'temp_kf': main_data['temp_kf']
        }
        extracted_data.append(extracted_item)

    # Crear el DataFrame a partir de la información extraída
    df = pd.DataFrame(extracted_data)

    return df
