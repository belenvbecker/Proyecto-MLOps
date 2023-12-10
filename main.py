import pandas as pd 
from fastapi import FastAPI
from os import path
import pyarrow.parquet as pq
import joblib 


app = FastAPI()

df1 = pd.read_csv('./Data/Data-Funciones/F_user_genre.csv.gz', compression='gzip')

@app.get('/playtimegenre/{genero}')
def PlayTimeGenre(genero):
    df = pd.read_csv('./Data/Data-Funciones/Funciones1.csv.gz', compression='gzip')
    
    # Se filtra el DataFrame para el género específico
    df_genero = df[df['genres'].str.contains(genero, case=False, na=False)]

    # Se agrupa por año y calcula las horas jugadas
    horas_por_año = df_genero.groupby('año')['playtime_forever'].sum()

    # Se encuentra el año con más horas jugadas
    año_max_horas = horas_por_año.idxmax()

    # Se crea el diccionario de retorno
    resultado = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero, año_max_horas)}

    return resultado


@app.get('/userrecommend/{año}')
def UsersRecommend(year: int):
    df = pd.read_csv('./Data/Data-Funciones/Funciones2.csv.gz', compression='gzip')    

    df_filtrado = df['app_name'][(df['año'] == year) & (df['recommend'] == True) & (df['sentiment_analysis'].isin([1, 2]))].value_counts().reset_index().head(3)
    resultado = [{"Puesto {}:{}".format(i + 1, row['app_name'])} for i, row in df_filtrado.iterrows()]
    return resultado


@app.get('/sentiment_analysis/{year}')
def sentiment_analysis1(año: int):
    df = pd.read_csv('./Data/Data-Funciones/Funciones2.csv.gz', compression='gzip')
    # Filtrar el DataFrame para el año dado
    df_filtrado = df[df['año'] == año]
    #Cuenta los comentarios positivos
    Positivos = df_filtrado[df_filtrado['sentiment_analysis']==2]['sentiment_analysis'].count()
    # Cuenta los comentarios negativos
    Negativos = df_filtrado[df_filtrado['sentiment_analysis']==0]['sentiment_analysis'].count()
    # Cuenta los comentarios neutrales
    Neutrales = df_filtrado[df_filtrado['sentiment_analysis']==1]['sentiment_analysis'].count()
    # Devolver conteos en un diccionario

    return {
        'Negative': str(int(Negativos)),
        'Positive': str(int(Positivos)),
        'Neutral':str(int(Neutrales))
        }



@app.get('/userforgenres/{genero}')
def UserForGenre2(genero):
    # Filtrar el DataFrame por el género dado
    global df1
    #df = pd.read_csv('./Data/Data-Funciones/F_user_genre.csv.gz', compression='gzip')

    df_genero = df1[df1['genres'].str.contains(genero)] 
    df_horas = df_genero.groupby('user_id')['playtime_forever'].sum().reset_index()


    # Encontrar el usuario con más horas jugadas para ese género
    usuario_max_playtime = df_horas.loc[df_horas['playtime_forever'].idxmax()]['user_id']


    # Filtrar el DataFrame por el usuario con más horas jugadas en ese género
    df_usuario_max = df_genero[df_genero['user_id'] == usuario_max_playtime]
    df_horas_anio = df_usuario_max.groupby('año')['playtime_forever'].sum().reset_index()

    #horas_anio = [{'Año': row['año'], 'Horas': row['playtime_forever']} for _, row in df_horas_anio.iterrows()]
    horas_anio = [{'Año': str(row['año']), 'Horas': str(row['playtime_forever'])} for _, row in df_horas_anio.iterrows()]

    salida = {'Usuario con más horas jugadas para ' + 'Action': usuario_max_playtime, 'Horas jugadas': horas_anio}
    return salida



@app.get("/recomendacion1")
def recomendacion3(item_id:int):
    #Cargar el modelo entrenado desde el archivo pickle
    with open('Modelo1.pkl', 'rb') as file:
       modelo = joblib.load(file)

    Modelo1 = pd.read_csv('./Modelo1.csv.gz', compression='gzip')
    
    if item_id not in Modelo1['id'].tolist():
       return {"Respuesta": "No se encontraron resultados para la búsqueda realizada"}

    def get_recommendations(idx, cosine_sim=modelo):
       idx = Modelo1[Modelo1['id'] == item_id].index[0]
       sim_scores = list(enumerate(cosine_sim[idx]))
       sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
       sim_scores = sim_scores[1:6]  # Top 5 juegos similares
       game_indices = [i[0] for i in sim_scores]
       return Modelo1['app_name'].iloc[game_indices].tolist()

    #Obtener el índice del item_id
   # 

    recommendations = get_recommendations(item_id)
    return {"Recomendaciones": recommendations}

   