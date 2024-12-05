# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Para el entrenamiento del modelo se cuenta con un dataset denominado "fakes1000" el cual contiene 1.000 noticias falsas y 1.000 noticias verdaderas.  Está configurado con dos variables: la categoría a la que pertenece la noticia (class), una variable de tipo categórico y el texto de la noticia (Text), una variable de texto, que corresponde a un fragmento de aproximadamente 40 palabras en promedio. No hay valores faltantes.  El dataset no presenta desbalance de clases, ambas categorías cuentan con la misma cantidad de registros (1.000 noticias falsas, 1.000 noticias verdaderas).

## Resumen de calidad de los datos

Como se anotó, el dataset no contiene valres faltantes y cuenta con dos variables, el texto y la clase, por ende no hay variables adicionales con las cuales efectuar análisis de correlación.  La variable clase, por su parte, se encuentra balanceada, por lo que no será necesario aplicar técnicas de balanceo. 

Al efectuar el análisis exploratorio se identifica que cada texto es un fragmento de la noticia que en promedio, para ambas clases, cuenta con 40 +/- 14 palabras. 

Al realizar una clasificación del idioma de los textos, se identifica que en su gran mayoría son catalogados como español, no obstante, 31 son categorizados como otros idiomas.  Se efectúa una revisión manual de estos textos y se puede concluir que si están en español pero contienen algunas palabras en otro idioma que son parte del contexto de la noticia por lo que se espera no generen algún problema en el modelo y por ende se mantendrán dentro del corpus. 

## Variable objetivo

El proyecto busca como objetivo desarrollar un modelo para predecir si una noticia es falsa o verdadera, por lo tanto, la variable objetivo es la clase: true (1) y false (0).  Como se mencionó las clases se encuentran balanceadas. 

## Variables individuales

El dataset no cuenta con variables adicionales al texto y la clase. 
