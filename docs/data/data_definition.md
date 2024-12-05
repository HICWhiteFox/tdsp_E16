# Definición de los datos

## Origen de los datos

Los datos utilizados en este proyecto provienen del conjunto de datos "Noticias Falsas en Español" disponible en Kaggle, una plataforma en línea para científicos de datos. 

El dataset específico utilizado se titula "fakes1000.csv" y fue creado por Arsenii Tretiakov. Este dataset contiene una colección de noticias falsas en español, las cuales se obtuvieron por el autor mediante web scraping. Se puede encontrar más información en el dataset original:

Conjunto de datos: Noticias Falsas en Español Autor: Arsenii Tretiakov Plataforma: Kaggle Archivos específicos: fakes1000.csv onlyfakes1000.csv y onlytrue1000.csv  

https://www.kaggle.com/datasets/arseniitretiakov/noticias-falsas-en-espaol?select=fakes1000.csv] 

## Especificación de los scripts para la carga de datos

Desde google colab se realiza la carga de los archivos de Kaggle hacia el repositorio DVC y se actualiza el repositorio del proyecto con los archivos .dvc correspondientes a cada archivo de datos descargado.

Se agrega el google colab utilizado para la carga de los datos y la actualizacion de github y dvc a la carpeta data_acquisition  

## Referencias a rutas o bases de datos origen y destino

Tal como se especificó en el punto anterior los datos se trabajarán en google colab usando dvc y el almacenamiento de los archivos de datos de origen se encuentra en google drive.
Se cuenta con 3 archivos de datos y un total de 3.000 noticias equilibradas entre falsas y verdaderas.
