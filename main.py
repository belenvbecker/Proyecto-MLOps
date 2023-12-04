import pandas as pd 
from fastapi import FastAPI
from os import path
import pyarrow.parquet as pq


app = FastAPI()

@app.get('/userforgenres/{genero}')
def UserForGenre(genero):
    #df = pd.read_parquet('./Data/Data-Funciones/df-userforgenre.parquet')
    df = pd.read_csv('./Data/Data-Funciones/Funciones1.csv.gz', compression='gzip')

    df_genero= df.groupby(['user_id', 'año']).sum().reset_index()

    df_genero = df_genero[df_genero['genres'].str.contains(genero)]

    # Encontrar al usuario con la máxima cantidad de playtime
    usuario_max_playtime = df_genero.loc[df_genero['playtime_forever'].idxmax()]['user_id']

    # Filtrar el DataFrame original por usuario y género
    df_usuario_genero = df[(df['user_id'] == usuario_max_playtime)]
    # Agrupar por año y sumar el tiempo de juego
    poranio = df_usuario_genero.groupby('año')['playtime_forever'].sum().to_dict()

    # Crear un diccionario con la información
    dicc = {
        'usuario': usuario_max_playtime,
        'años': poranio
    }

    return dicc