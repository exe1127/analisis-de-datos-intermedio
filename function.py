import requests
from config import *
from datetime import datetime
import pandas as pd
from pandas import json_normalize


""" def search(city, key):

    # Consulta a la appi
    url = f'{baseUrl}q={city}&appid={key}'

    request = requests.get(url)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code) """


def search2(lat, lon, key, dt):
    # Consulta a la appi
    url = f'{baseUrl}lat={lat}&lon={lon}&dt={dt}&appid={key}&units=metric'

    request = requests.get(url)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code)


def normalize(request,index):
    # Normalizacion de la respuesta de la api
    datecols = ['dt', 'sunrise', 'sunset']
    records = []

    # Utiliza json_normalize para extraer y normalizar los datos
    star = json_normalize(request)
    star = star.drop("data", axis=1)
    weather = json_normalize(request["data"][0]["weather"][0])
    data = json_normalize(request['data'][0])
    data = data.drop("weather", axis=1)

    # Se genera el dataFrame correspondiente
    df = pd.concat([star, data, weather,index], axis=1)

    # Establece el índice del DataFrame en la columna 'id' para evitar errores
    df = df.set_index('index')

    # Convierte las columnas de fechas a objetos de fecha y hora
    df[datecols] = df[datecols].apply(pd.to_datetime)

    return df
