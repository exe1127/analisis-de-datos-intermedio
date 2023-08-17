import requests
from config import *
from datetime import datetime
import pandas as pd
from pandas import json_normalize


def search(city, key):

    # Consulta a la appi
    url = f'{baseUrl}q={city}&appid={key}'

    request = requests.get(url)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code)


def search2(lat, lon, key):
    # Consulta a la appi
    url = f'{baseUrl}lat={lat}&lon={lon}&appid={key}&units=metric'

    request = requests.get(url)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code)


def normalize(request):
    # Normalizacion de la respuesta de la api
    datecols = ['dt', 'sunrise', 'sunset']
    records = []
    # Utiliza json_normalize para extraer y normalizar los datos
    weather = json_normalize(request['weather'])
    coord = json_normalize(request['coord'])
    main = json_normalize(request['main'])
    wind = json_normalize(request['wind'])
    clouds = json_normalize(request['clouds'])
    sys = json_normalize(request['sys'])

    # Crea un registro combinando todos los datos normalizados
    record = {
        'id': request['id'],
        'name': request['name'],
        'cod': request['cod'],
        'dt': pd.to_datetime(request['dt'], unit='s'),
        **weather.iloc[0], **coord.iloc[0], **main.iloc[0], **wind.iloc[0], **clouds.iloc[0], **sys.iloc[0]
    }

    records.append(record)

    # Se genera el dataFrame correspondiente
    result_df = pd.DataFrame(records)

    # Establece el índice del DataFrame en la columna 'id' para evitar errores
    result_df = result_df.set_index('id')

    # Convierte las columnas de fechas a objetos de fecha y hora
    result_df[datecols] = result_df[datecols].apply(pd.to_datetime)

    return result_df
