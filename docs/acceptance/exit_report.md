# Informe de salida

## Resumen Ejecutivo

El proyecto se centró en el desarrollo de un modelo de Machine Learning capaz de detectar noticias falsas en español. Para ello, se utilizaron diversas técnicas de preprocesamiento de texto, extracción de características y modelado. A continuación, se describen los logros obtenidos.

## Resultados del proyecto

* Se desarrolló un modelo de Machine Learning con una precisión moderada para la detección de fake news en español a partir de fragmentos de noticias.
* Se implementaron técnicas de preprocesamiento como tokenización, lematización, eliminación de stopwords y transformación a minúsculas de los textos con el fin de garantizar un mejor desempeño de los modelos.
* En la etapa de extracción de características se usaron dos métodos: bolsa de palabras y embedding con word2vec.  La técnica countvectorizer permitió mejores resultados para el caso de negocio. 
* En la etapa de modelamiento se implementaron diferentes tipos de modelos buscando el mejor desempeño en las métricas de desempeño.  Se probaron modelos como random forest, regresión logística, Xgboost y red neuronal con TensorFlow. 

Finalmente el mejor desempeño se obtuvo con Random Forest a partir de un embedding con CountVectorizer que permitió alcanzar las métricas que presenta la imagen:

![metricas_modelo (2)](https://github.com/user-attachments/assets/02794cec-4501-4c00-b463-4057af0e2c3a)

El modelo puede ser mejorado, no obstante con estos resultados puede ser empleado para casos de clasificación binaria de textos cortos, por ejemplo en detección de Tweets falsos o verdaderos. 


## Lecciones aprendidas

* El primer desafio encontrado estuvo relacionado con la estructuración de los textos.  En la fuente de los datos, las noticias no estaban completas sino que fueron previamente acotadas a las primeras 50 palabras aproximadamente.  Por ende, no se pudieron llevar a cabo la construcción de otras variables tales como longitud de las noticias, uso de mayúsculas, uso de signos de puntuación que permitieran complementar y mejorar el desempeño de los modelos.

* Como lección aprendida y recomendación, se sugiere contar con textos completos en su formato original para construir otras variables que puedan enriquecer el modelo. 

## Impacto del proyecto

Este tipo de modelos, como se mencionó pueden ser útiles para clasificación binaria de textos (2 categorías, tipo true/false) y es un buen ejercicio académico para el aprendizaje de las metodologías ágiles para el desarrollo de proyectos de machine learning.

## Conclusiones

Por medio del presente proyecto se logra una comprensión detallada de los pasos para desarrollar de manera estructurada un proyecto de Machine Learning desde la obtención de los datos hasta el despliegue final. Así mismo, en su particularidad el modelo permite realizar clasificación binaria (en dos categorías) de fragmentos de noticias en español para determinar si son veraces o falsas.   Al no poder contar con los textos completos puede resultar desafiante obtener un alto desempeño, no obstante a través del embedding con Contvectorizer y un modelo de Random Forest es posible lograr un buen clasificador. 
