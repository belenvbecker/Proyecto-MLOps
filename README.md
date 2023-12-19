<p align="center"><img src="https://i.postimg.cc/PfmCYHBZ/machine-learning.jpg"></p>


<h1 align='center'> Proyecto Individual N°1</h1>

<h2 align='center'> Machine Learning Operations (MLOps)</h2>

<h2 align='center'>Belén Viglioglia Becker, DATAPT05</h2>

---
## **`Tabla de Contenidos`**

- [Introducción](#introducción)
- [Desarrollo](#desarrollo)
    - [ETL](#exploración-transformación-y-carga-etl)
    - [EDA](#análisis-exploratorio-eda)
    - [Sistema de recomendación](#modelo-de-recomendación)
    - [Despliegue de la API](#despliegue-para-la-api)
- [Contacto](#contacto)

- ## **`Links`**
    - [Carpeta con los dataset](./Data/)
    - [Proceso de ETL](./ETL/)
    - [Proceso de EDA](./EDA/)
    - [Modelo de Recomendación](./ModeloML/)
    - [API desplegada en Render](https://belentest.onrender.com/docs)
    - [Link al video](https://youtu.be/V2UOjIHjZ_Y)



    ---

# Introducción

El objetivo de este proyecto es llevar a cabo un estudio de Machine Learning Operations (MLOps) basado en recomendación de juegos a usuarios. Se creó un MVP (Producto Mínimo Viable) que incluye una API desplegada y un modelo de Machine Learning que proporciona recomendaciones de juegos a los usuarios en función de su historial y reseñas. Dicho proyecto se divide en tres etapas principales:

1. **Extracción, Transformación y Carga de datos:** Se extraen los datos relevantes de la base de datos de origen. Luego los transformamos para que sean más adecuados para el análisis, para que al final se carguen nuevamente en la base de destino. Asimismo, se realiza un análisis exploratorio de los datos, incluyendo la exploración de distribuciones y detección de correlaciones y valores atípicos.

2. **Preparación de Datos:** Se preparan los datos para comprender las relaciones entre las variables y crear datasets y modelos sobre ellos. También se establecen funciones para las consultas solicitadas, consumibles a través de una API.

3. **Modelado:** Se despliegan dos modelos de Machine Learning basados en la similitud del conseno a fin de predecir sugerencias personalizadas sobre un determinado tipo de elemento.


# Desarrollo

El desarrollo del proyecto se basa en tres archivos JSON comprimidos (GZIP):

* **steam_games.json.gz** : Contiene información sobre los juegos, como el nombre, las especificaciones, el desarrollador, los precios y los géneros.
* **users_items.json.gz** : Proporciona información sobre cómo los usuarios interactúan con los juegos, incluido el tiempo que pasan jugando.
* **users_reviews.json.gz** : Contiene los comentarios y reseñas que los usuarios hacen sobre los juegos, junto con las recomendaciones y los IDs de usuarios.


### Exploración, Transformación y Carga (ETL)

En primer lugar se realizó el proceso de limpieza, transformación y carga de los datos.

#### `Steam_games`

- Se eliminaron filas completamente nulas y se corrigieron duplicados en el ID.
- Se completaron los datos nulos de la columna title a partir de los datos de la columna app_name.
- Se normalizaron los nombres de los registros que se encuentran en la columna app_name.
- Se completaron los datos nulos de la columna genres a partir de los datos de la columna tags.
- Se completaron los datos nulos de la columna developer a partir de los datos de la columna publisher.
- Se completó con la palabra Otros en publisher y developer cuando tuvieran valores nulos.
- Se normalizaron los nombres de los registros que se encuentran en las columnas publisher y developer.
- En la columna Price se filtraron todos los registros que no sean datos numéricos y se corrigieron. Asimismo
se imputaron los valores nulos.
- Se cambió a formato fecha la columna release_date y se imputaron los valores nulos.
- Se eliminaron los valores nulos restantes de las columnas tags, genres y specs al representar un pequeño porcentaje del total del dataframe.
- Se eliminaron columnas que no se van a utilizar.
- Se exportó para tener el dataset limpio.


#### `User_items`

- Se realizó un explode debido a que la columna de items era una lista de diccionarios.
- Se eliminaron las columnas que no se van a utilizar.
- Se convertió la columna item_id en tipo de dato flotante.
- Se normalizaron los nombres de los registros que se encuentran en la columna item_name.
- Se pasó a horas la columna playtime_forever en donde se pudo observar que posee la cantidad de minutos jugados.
- Se eliminaron los valores nulos restantes al representar un pequeño porcentaje del total del dataframe.
- Se eliminaron los registros que se encuentraban duplicados en las columnas item_id y user_id.
- Se mantuvo en la columna 'playtime_forever' solamente las filas en donde los usuarios hayan jugado más de una hora.
- Se exportó para tener el dataset limpio.


#### `User_reviews`

- Se realizó un explode ya que la columna de review era una lista de diccionarios.
- Se eliminaron las columnas que no se van a utilizar.
- Se eliminaron los valores nulos restantes al representar un pequeño porcentaje del total del dataframe.
- Se convertió la columna item_id en tipo de dato flotante.
- Se creó una nueva columna llamada 'sentiment_analysis' usando análisis de sentimiento y se eliminó la columna de review.
- Se eliminaron los valores duplicados en las columnas 'item_id' y 'user_id'.
- Se exportó para tener el dataset limpio.



### Análisis Exploratorio de datos (EDA)

Una vez que se realizó la limpieza de los 3 dataset, se procedió a efectuar el Análisis Exploratorio de datos(EDA) mediante el cual se confeccionaron gráficos a fin de analizar e investigar los datos y así llegar a comprender las estadísticas, encontrar valores atípicos y orientar un futuro estudio.



### Modelo de Recomendación

Para el desarrollo del modelo de Machine Learning se utilizaron varios datasets. En primera instancia, se llevó a cabo un primer modelo en donde a través de una función a la que se le otorga un Item_id, nos proporciona recomendaciones de 5 juegos similares según el género, el desarrollador y las especificaciones. Luego se implementó el segundo modelo en donde a través de una función a la que se le otorga un User_id, nos proporciona recomendaciones de 5 juegos similares para dicho usuario. También según el género, el desarrollador y las especificaciones. Ambos modelos de recomendaciones se realizaron aplicando la métrica de *similitud del coseno*, una técnica comúnmente empleada para comparar la similitud entre documentos, palabras o cualquier elemento que pueda ser representado como vectores en un espacio multidimensional.



### Despliegue para la API

Se desarrollaron las siguientes funciones, a las cuales se podrá acceder desde la API en la página Render:

- **`PlayTimeGenre( genero : str )`**: Devuelve año con mas horas jugadas para dicho género.

- **`UsersRecommend( año : int )`**: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado..

- **`UserForGenre(género: str)`**: Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

- **`UsersNotRecommend( año : int )`**: Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado.

- **`sentiment_analysis( año : int )`**: Según el año de lanzamiento, devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

- **`recomendacion3(item_id:int)`**: Esta función recomienda 5 juegos dado un ítem_id específico.

- **`recomendacion4(user_id)`**: Esta función recomienda 5 juegos para un user_id especifico.



# <a name="Contacto">Contacto</a>

Si tienes alguna pregunta, sugerencia o simplemente quieres ponerte en contacto conmigo, puedes alcanzarme de las siguientes maneras:

- Correo Electrónico: [belenviglioglia@gmail.com](mailto:belenviglioglia@gmail.com)
- LinkedIn: [Belén Viglioglia Becker](https://www.linkedin.com/in/belen-viglioglia-becker/)


¡Gracias por visitar mi proyecto!


<p align="center"><img src="https://i.postimg.cc/43V7yDtN/descarga.png"></p>