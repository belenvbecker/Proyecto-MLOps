import pandas as pd 
from fastapi import FastAPI
from os import path
import pyarrow.parquet as pq


app = FastAPI()

#@app.get('/playtimegenre/{genero}')
#def PlayTimeGenre(genero):
    # Acceder al DataFrame 
    #df = pd.read_csv('./Data/Data-Funciones/Funciones1.csv.gz', compression='gzip')
    
    
    # Se filtra el DataFrame para el género específico
    #df_genero = df[df['genres'].str.contains(genero, case=False, na=False)]

    # Se agrupa por año y calcula las horas jugadas
    #horas_por_año = df_genero.groupby('año')['playtime_forever'].sum()

    # Se encuentra el año con más horas jugadas
    #año_max_horas = horas_por_año.idxmax()

    # Se crea el diccionario de retorno
    #resultado = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero, año_max_horas)}

    #return resultado

@app.get('/userrecommend/{año}')
def UsersRecommend(año):
    df = pd.read_csv('./Data/Data-Funciones/Funciones2.csv.gz', compression='gzip')
    # Filtrar el DataFrame para el año y las recomendaciones positivas (True) y los sentimientos 1 y 2
    df_filtrado = df[(df['año'] == año) & (df['recommend'] == True) & (df['sentiment_analysis'].isin([1, 2]))]

    # Contar la frecuencia de cada juego
    juegos_frecuencia = df_filtrado['app_name'].value_counts().reset_index() #Ver user id (carga diferente)

    # Renombrar las columnas
    juegos_frecuencia.columns = ['app_name', 'count']

    # Seleccionar los tres juegos más recomendados
    top3_juegos = juegos_frecuencia.head(3)

    # Crear la lista de diccionarios para el resultado
    #resultado = [{"Puesto {}: {}".format(i + 1, juego): count} for i, (juego, count) in enumerate(top3_juegos.values)]
    resultado = [{"Puesto {}".format(i + 1): juego} for i, (juego, _) in enumerate(top3_juegos.values)]
    return resultado

@app.get('/sentiment_analysis/{año}')
def UsersRecommend(year):
    df = pd.read_csv('./Data/Data-Funciones/Funciones2.csv.gz', compression='gzip')    

    df_filtrado = df[(df['año'] == year) & (df['recommend'] == True) & (df['sentiment_analysis'].isin([1, 2]))]
    df_grouped = df_filtrado.groupby(['user_id', 'app_name']).size().reset_index(name='counts')
    juegos_frecuencia = df_grouped['app_name'].value_counts().reset_index() 
    df_top3 = juegos_frecuencia.head(3)
    resultado = [{"Puesto {}".format(i + 1): juego} for i, (juego, count) in enumerate(df_top3.values)]
    return resultado



#@app.get('/userforgenres/{genero}')
#def UserForGenre(genero):
    #df = pd.read_parquet('./Data/Data-Funciones/df-userforgenre.parquet')
    #df = pd.read_csv('./Data/Data-Funciones/Funciones1.csv.gz', compression='gzip')

    #df_genero= df.groupby(['user_id', 'año']).sum().reset_index()

    #df_genero = df_genero[df_genero['genres'].str.contains(genero)]

    # Encontrar al usuario con la máxima cantidad de playtime
    #usuario_max_playtime = df_genero.loc[df_genero['playtime_forever'].idxmax()]['user_id']

    # Filtrar el DataFrame original por usuario y género
    #df_usuario_genero = df[(df['user_id'] == usuario_max_playtime)]
    # Agrupar por año y sumar el tiempo de juego
    #poranio = df_usuario_genero.groupby('año')['playtime_forever'].sum().to_dict()

    # Crear un diccionario con la información
    #dicc = {
        #'usuario': usuario_max_playtime,
        #'años': poranio
    #}

    #return dicc