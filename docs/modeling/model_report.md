# Reporte del Modelo Final

## Resumen Ejecutivo

## Descripción del Problema

La proliferación de información falsa en línea, especialmente a través de redes sociales y sitios web de noticias no confiables, representa una amenaza creciente para la sociedad. La desinformación puede influir en la opinión pública, generar polarización, e incluso incitar a la violencia.

La verificación manual de noticias es un proceso lento y costoso, que no puede escalar al ritmo al que se produce y difunde la información en línea. Un modelo de detección de fake news permite automatizar este proceso, facilitando la identificación de contenido falso a gran escala.

Por ende, el presente proyecto busca ayudar a resolver esta problemática a través del desarrollo de un modelo que permita clasificar textos como verdaderos o falsos con un grado de precisión confiable. Además, este modelo se enfoca específicamente en noticias en español, un idioma con una creciente presencia en línea pero con menos recursos disponibles para la detección de fake news en comparación con el inglés.

## Descripción del Modelo

El modelo final desarrollado para la detección de fake news en español se basa en la combinación de dos técnicas: CountVectorizer para la extracción de características y Random Forest Classifier para la clasificación. Este modelo se seleccionó por su buen rendimiento en términos de precisión y capacidad de generalización.  Las siguiente son las etapas aplicadas:

1. Recolección y preprocesamiento de datos: Se recopiló un conjunto de datos de noticias en español etiquetadas como verdaderas o falsas tomadas de Kaggle. Los datos se preprocesaron para eliminar ruido, como signos de puntuación y stop words, y se aplicó lematización para reducir las palabras a su raíz.

2. Extracción de características: Se utilizó CountVectorizer para convertir los textos preprocesados en vectores numéricos. Esta técnica crea una matriz donde cada fila representa un documento y cada columna representa una palabra del vocabulario. El valor de cada celda indica la frecuencia de la palabra en el documento.

3. Entrenamiento del modelo: Se dividió el conjunto de datos en dos partes: entrenamiento y prueba. Se utilizó el conjunto de entrenamiento para entrenar un clasificador Random Forest. Este algoritmo crea un conjunto de árboles de decisión, cada uno entrenado en un subconjunto aleatorio de los datos, y combina sus predicciones para obtener una clasificación final.

4. Evaluación del modelo: Se utilizó el conjunto de prueba para evaluar el rendimiento del modelo. Se calculó la métrica del Accuracy para medir la capacidad del modelo para identificar noticias falsas.

## Evaluación del Modelo

En la evaluación del modelo se aplicaron las métricas accuracy, precision, recall, F1-Score y ROC AUC.  Los resultados obtenidos se especifican a continuación:

* Accuracy: 74,25% El modelo predice correctamente el 74.25% de las noticias, ya sean verdaderas o falsas.Si bien no es un mal resultado, indica que hay margen de mejora.
  
* Precision: 78,92% De todas las noticias que el modelo clasificó como falsas, el 78.92% realmente lo eran.
Esto significa que el modelo tiene una tasa de falsos positivos moderada (clasifica algunas noticias verdaderas como falsas).

* Recall: 65,83% De todas las noticias que realmente eran falsas, el modelo identificó correctamente el 65.83%.
Esto significa que el modelo tiene una tasa de falsos negativos más alta (clasifica algunas noticias falsas como verdaderas).

* F1-score: 71,78% Esta medida combina precisión y recall.  El resultado se puede considerar como un rendimiento moderado. 

* ROC AUC: 74,21% El área bajo la curva ROC es moderadamente alta. Indica una capacidad aceptable del modelo para distinguir entre noticias verdaderas y falsas, pero no es tan alta como sería ideal.

  En las siguientes imágenes se pueden apreciar gráficamente los resultados:

![metricas_modelo](https://github.com/user-attachments/assets/06611a41-213c-43b3-ae10-5e2e47c9815b)

![matriz_confusion (1)](https://github.com/user-attachments/assets/75720fd6-0bd6-47ba-9a94-fc8ca35189dd)

## Conclusiones y Recomendaciones

El modelo presenta un rendimiento moderado en la detección de fake news en español.

* Puntos fuertes: El modelo tiene una precisión relativamente buena, lo que significa que cuando clasifica una noticia como falsa, es probable que sea correcta.

* Puntos débiles: El recall es más bajo, lo que indica que el modelo podría estar pasando por alto algunas noticias falsas. Esto es algo a tener en cuenta, ya que podría ser más importante en este contexto detectar todas las noticias falsas, incluso si eso significa tener algunos falsos positivos.

Para mejorar el rendimiento del modelo, es conveniente considerar:

* Ajustar el umbral de probabilidad que usa el modelo para clasificar una noticia como falsa. Esto podría ayudar a aumentar el recall, aunque podría comprometer la precisión.

* Explorar otros algoritmos de clasificación, como Support Vector Machines (SVM) o redes neuronales, para ver si obtienen mejores resultados.

