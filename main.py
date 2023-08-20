
import pandas as pd
from function import *
import datetime
if __name__ == '__main__':
    # Obtener del archivo txt la key
    with open('credenciales.txt', 'r') as f:
        key = f.read()

    coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58",
                 "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

    list = []
    tiempo_actual = datetime.datetime.now()

    # Realizamos la primera busqueda por nombre de la ciudad

    for coords in coordList:
        # Separamos los elementos del arrregolo en longitud y latitud
        lat, lon = coords.split('&')
    # Extraemos los valores numéricos de latitud y longitud después de "lat=" y "lon="
        lat = float(lat.split('=')[1])
        lon = float(lon.split('=')[1])
        for i in range(0, 4):
            tiempo_unix = int(
                (tiempo_actual-datetime.timedelta(days=i)).timestamp())
    # Realizamos la segunda busqueda por latitud y longitud de la ciudad
            list.append(search2(lat, lon, key, tiempo_unix))

    # Se genera la normalizacion de la lista obtenida en las busquedas
    normalized_data = [normalize(entry) for entry in list]

    # Se consolida en un dataFrame
    consolidated_df = pd.concat(normalized_data)
