# Machine Learning Engineering — Trabajo Práctico

## Introducción

El dataset `properati.csv` contiene publicaciones de propiedades en Argentina, con información de ubicación, superficie, ambientes y precio, entre otras variables. El objetivo de este trabajo es predecir el precio de venta de propiedades en Capital Federal, aplicando el ciclo completo de un proyecto de Machine Learning: desde la exploración de los datos hasta la evaluación de distintos modelos.

No hay una única forma correcta de resolver este TP. Se espera que cada alumno tome decisiones propias sobre cómo tratar los datos, y que justifique el porqué de cada una. La corrección va a poner tanto o más foco en el razonamiento detrás de las decisiones que en el resultado final del modelo.

## Parte 1: Exploración, Preprocesamiento y Transformación

### a) Visualización de los datos

Realizá una primera aproximación al dataset apoyándote en visualizaciones, por ejemplo: distribución de precios, comparación de precios por tipo de propiedad, relación entre superficie y precio, mapas o gráficos geográficos, matrices de correlación, o cualquier otro gráfico que consideres útil. Justificá por qué elegiste cada uno y qué te permitió descubrir.

### b) Ingeniería de características

Como mínimo, se espera que trabajes los siguientes puntos:

1. **Datos faltantes o mal ingresados:** identificalos y tomá una decisión justificada sobre cada caso (imputación, eliminación de registros o columnas, etc.).
2. **Columnas a descartar o crear:** identificá columnas que no aportan al análisis, y evaluá si tiene sentido crear nuevas features a partir de las existentes (por ejemplo, derivadas de precio y superficie, de fechas, o de ubicación).
3. **Outliers:** identificalos usando algún método estadístico (Z-Score, rango intercuartílico/IQR) y/o visual (boxplots). Explicá qué representan en este dataset en particular (¿son errores de carga o casos reales?) y justificá si los eliminás, los transformás, o los dejás.
4. **Encoding:** determiná si alguna de las variables categóricas puede convertirse en numéricas usando técnicas como One-Hot Encoding.
5. **Cualquier otra tarea de limpieza que identifiques como necesaria.** Documentala igual que las anteriores.

### c) Descripción de los datos

Resumí qué pudiste descubrir sobre el dataset a partir de los puntos anteriores. Definí también, en esta sección, qué métrica(s) vas a usar para evaluar el desempeño de los modelos (por ejemplo, MAE) y justificá por qué son adecuadas para este problema de regresión en particular.

## Parte 2: Generación y Evaluación de Modelos

### a) Modelos

Dividí el conjunto de datos en entrenamiento/prueba y posteriormente entrená al menos un modelo de Regresión Lineal y otro de Random Forest. Para este último documentá y justificá los hiperparámetros elegidos.

### b) Búsqueda de hiperparámetros

Utilizá GridSearchCV (u otra técnica de búsqueda de hiperparámetros) sobre Random Forest. Compará el rendimiento del mejor modelo encontrado contra la versión sin ajustar. ¿Mejoró el resultado?

### c) Conclusiones

Resumí qué modelo recomendarías para este problema y por qué.
