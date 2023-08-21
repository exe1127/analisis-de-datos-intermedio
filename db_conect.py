from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from credenciales_db import *
from sqlalchemy import create_engine

#crear el link de conexion para la base de datos
database_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

#Crear la conexion a la base de datos
engine = create_engine(database_url)