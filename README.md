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
    - [Link al video] 



    ---

# Introducción

El objetivo de este proyecto es llevar a cabo un estudio de Machine Learning Operations (MLOps) basado en recomendación de juegos a usuarios. Se creó un MVP (Producto Mínimo Viable) que incluye una API desplegada y un modelo de Machine Learning que proporciona recomendaciones de juegos a los usuarios en función de su historial y reseñas. Dicho proyecto se divide en tres etapas principales:

1. **Extracción, Transformación y carga de datos:** Se extraen los datos relevantes de la base de datos de origen. Luego los transformamos para que sean más adecuados para el análisis, para que al final se carguen nuevamente en la base de destino. Asimismo, se realiza un análisis exploratorio de los datos, incluyendo la exploración de distribuciones y detección de correlaciones y valores atípicos.

2. **Preparación de Datos:** Se preparan los datos para comprender las relaciones entre las variables y crear datasets y modelos sobre ellos. También se establecen funciones para las consultas solicitadas, consumibles a través de una API.

3. **Modelado:** Se despliegan dos modelos de Machine Learning basados en la similitud del conseno a fin de predecir sugerencias personalizadas sobre un determinado tipo de elemento.



