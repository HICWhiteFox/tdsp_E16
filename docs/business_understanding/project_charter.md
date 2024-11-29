# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

[DETECCIÓN DE FAKE NEWS EN ESPAÑOL]

## Objetivo del Proyecto

[Desarrollar un modelo de Machine Learning capaz de identificar noticias falsas en español con una alta precisión, utilizando técnicas de Procesamiento del Lenguaje Natural (PLN) para analizar el contenido textual y detectar patrones lingüísticos que indiquen la falsedad de la información]

## Alcance del Proyecto

[El proyecto se enfocará en desarrollar un modelo de Machine Learning capaz de clasificar noticias en español como "verdaderas" o "falsas". Se utilizarán técnicas de Procesamiento de Lenguaje Natural para analizar características del texto y se emplearán difernetes algoritmos para encontrar el que mejor se adapte a la tarea.]

### Datos Disponibles:

[Dataset disponible en la plataforma Kaggle en el siguiente enlace: https://www.kaggle.com/datasets/arseniitretiakov/noticias-falsas-en-espaol/data

Cuenta en total con 2.000 noticias, de las cuales 1.000 son falsas y 1.000 son verdaderas. Es decir, el conjunto de datos se encuentra balanceado.

Consta de dos columnas: la clase (fake / true) y la noticia la cual está en idioma español.]

### Resultados Esperados:

[-Desarrollo de un modelo de Machine Learning con una precisión mínima del 85% en la detección de noticial falsas en español.

-Identificación de patrones linguísticos y características textuales más relevantes para la detección de fake news en español. Por ejemplo, detectar si las fake news se caracterizan por un lenguaje emocional, datos no verificados o una estructura patrón.

-Propuesta de un prototipo de aplicación web que permita ingresar nuevas noticias y obtener una predicción sobre su veracidad.]

### Criterios de Éxito:

[Precisión del modelo: alcanar una precisión mínima del 85% en la detección de noticias falsas en español Este criterio se evaluará utilizando métricas de evaluación precisión, recall, F1-Score y matriz de confusión.

Robustez del modelo: el modelo debe ser capaz de detectar la veracidad de nuevas noticias incluidas al conjuno de datos y mantener un buen rendimiento. Para esto es clave evaluar el modelo en un conjunto de datos que no sea incluido en el entrenamiento.]


## Metodología

[Para el desarrollo del proyecto se aplicará la metodología Cross Industry Standard Process for Data Mining (CRISPDM), la cual consta de las siguientes fases:

Entendimiento del negocio: definir el problema de la desinformación y sus consecuencias. Establecer los objetivos del proyecto. Definir los criterios de éxito.

Preparación de los datos: Limpieza de los datos. Preprocesamiento del texto. Creación de características. Creación de bases de entrenamiento y prueba.

Modelado: Selección de algoritmos de machine learning (Naive Bayes, SVM, redes neuronales). Entrenamiento del modelo. Ajuste de hiperparámetros. Evaluación de modelos.

Evaluación: Evaluación en conjunto de datos independiente con las métricas establecidas. Comparación de modelos. Selección de modelo más adecuado.

Despliegue: Implementación de modelo para detección de nuevas noticias.]

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y recopilación de datos | 1 semana | del 23 al 28 de noviembre |
| Preprocesamiento, análisis exploratorio | 1 semana | del 29 de noviembre al 5 de diciembre |
| Modelamiento y extracción de características | 1 semana | del 6 de diciembre al 12 de diciembre |
| Evaluaciónde modelos | 0.5 semana | del 13 de diciembre al 17 de diciembre |
| Despliegue | 0.5 semana | del 19 de diciembre al 21 de diciembre  |

## Equipo del Proyecto

[CLAUDIA LORENA CAÑON DIAZ - clcanond@unal.edu.co | GLORIA ISABEL RINCÓN TORRES - glrincont25@gmail.com]



