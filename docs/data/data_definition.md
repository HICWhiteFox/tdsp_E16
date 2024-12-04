# Definición de los datos

## Origen de los datos

Los datos utilizados en este proyecto provienen del conjunto de datos "Noticias Falsas en Español" disponible en Kaggle, una plataforma en línea para científicos de datos. 

El dataset específico utilizado se titula "fakes1000.csv" y fue creado por Arsenii Tretiakov. Este dataset contiene una colección de noticias falsas en español, las cuales se obtuvieron por el autor mediante web scraping. Se puede encontrar más información en el dataset original:

Conjunto de datos: Noticias Falsas en Español Autor: Arsenii Tretiakov Plataforma: Kaggle Archivo específico: fakes1000.csv  

https://www.kaggle.com/datasets/arseniitretiakov/noticias-falsas-en-espaol?select=fakes1000.csv] 

## Especificación de los scripts para la carga de datos

Desde el sitio de Kaggle se descargaron localmente los datos disponibles en formato CSV.  Posteriormente, la carga de los datos se realizó mediante un script en Python que utiliza las siguientes librerías:

* csv: Esta librería se emplea para leer el archivo CSV fakes1000.csv que contiene las noticias falsas.

* google.colab.drive: Esta librería permite acceder a Google Drive, donde se almacena el archivo CSV.  

## Referencias a rutas o bases de datos origen y destino

Tal como se especificó en el punto anterior los datos se trabajarán en google colab desde el drive local. Se cuenta con un único archivo origen el cual consolida un total de 1.000 noticias. No se cuenta con diferentes archivos orige

