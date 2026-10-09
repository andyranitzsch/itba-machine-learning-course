# Clase 5 - Evaluación y ajuste de modelos

## Pagina 1

Machine Learning

---

## Pagina 2

CLASE 4
Algoritmos de machine learning
Repaso

---

## Pagina 3

Tipos de problemas: repaso
Antes de elegir un algoritmo, hay que saber qué queremos que el modelo responda
● Clasificación: la respuesta es una categoría (¿sobrevivió al Titanic o no?)
● Regresión: la respuesta es un número (¿cuánto va a costar una casa?)
● Clustering: no hay respuesta correcta, se buscan grupos parecidos (¿qué clientes se comportan similar?)

---

## Pagina 4

Regresión Lineal
Regresión Lineal: es un algoritmo de aprendizaje supervisado donde se busca entrenar un modelo capaz de 
predecir el valor de una variable continua
Modelo
ENTRADAS 
 edad
 género
 peso
SALIDA 
 altura

---

## Pagina 5

Regresión Lineal

---

## Pagina 6

Regresión Logística
Regresión Logística: es un algoritmo de aprendizaje supervisado donde se busca entrenar un modelo capaz de 
predecir una categoría
Modelo
ENTRADAS 
 ingresos
 deuda actual
 historial de pagos
SALIDA 

aprobado / 
rechazado

---

## Pagina 7

Regresión Logística

---

## Pagina 8

KNN
K-Vecinos más cercanos (KNN): es un algoritmo de aprendizaje supervisado que predice basándose en los K 
casos más parecidos que ya conoce, sin construir ninguna fórmula ni árbol de antemano.
k = 5
x
y

---

## Pagina 9

K-Means
K-Means: es un algoritmo de aprendizaje no supervisado que agrupa datos parecidos entre sí en K grupos 
(clusters), sin que nadie le diga de antemano a qué grupo pertenece cada dato.
● Caso de uso: sistema de recomendación que sugiere películas basándose en lo que vieron y clasificaron 
usuarios con gustos parecidos
Pasos
1. Elegir el K: cuántos grupos se desean buscar
2. El algoritmo tira 2 centros al azar en el espacio
3. Asigna a cada punto al centro más cercano
4. Recalcula el centro como el promedio de los puntos que quedaron asignados a él
5. Repite los pasos 3 y 4 cada vez

---

## Pagina 10

K-Means
x
y

---

## Pagina 11

K-Means
x
y

---

## Pagina 12

K-Means
x
y

---

## Pagina 13

Árboles de decisión
Árboles de decisión: son algoritmos de aprendizaje supervisado que con simples reglas de decisión aplicadas 
sobre los datos les permite generar predicciones
¿Pronóstico?
Soleado Nublado Lluvia
¿Humedad?
Juego (siempre) ✓
¿Viento?
Alta Normal Fuerte Débil
No juego ✗ Juego ✓ No juego ✗ Juego ✓

---

## Pagina 14

Árboles de decisión
¿Es hora pico?
¿Distancia > 10km? ¿Distancia > 10km?
Sí No Sí No
$8000 $4500 $5500 $2000
Sí No

---

## Pagina 15

Random Forest
Random Forest: es un algoritmo de ensemble que entrena muchos árboles de decisión distintos entre sí, y 
combina sus resultados — para clasificación, vota la mayoría; para regresión, promedia.
1. Se eligen N árboles se quieren entrenar
2. Para cada árbol se toma una muestra al azar
3. Se entrena el árbol completo con esas reglas
4. Se repite el proceso N veces, generando N árboles distintos
5. Para un caso nuevo, se le pregunta a los 100 árboles y votan (clasificación) o promedian (regresión)

---

## Pagina 16

Random Forest
Médico 1
Gripe
Médico 2
Alergia
Médico 3
Gripe
Médico 4
Alergia
Médico 5
Gripe
Voto mayoritario
3 contra 2
Diagnóstico
Gripe

---

## Pagina 17

XGBoost
XGBoost: es un algoritmo de ensemble que entrena árboles en secuencia, donde cada árbol nuevo se enfoca 
específicamente en corregir los errores que cometió el conjunto de árboles anterior.
1. El primer árbol hace una predicción básica
2. El segundo árbol se centra en los casos donde el primer árbol se equivocó
3. Así sucesivamente

---

## Pagina 18

Selección del algoritmo
La selección del algoritmo es una decisión que implica un análisis de tradeoffs. La elección dependerá del 
rendimiento esperado y de las limitaciones de negocio y de tecnología.
Criterios para tomar una decisión:
● Rendimiento: priorizar los algoritmos que maximicen las métricas de evaluación
● Explicabilidad: hace referencia a si se puede entender cómo el modelo llegó a una decisión
● Complejidad: generalmente es inversamente proporcional a la explicabilidad
● Dimensionalidad de los datos: el volumen de datos y cantidad de features influyen en la elección
● Costo y tiempo: se debe considerar el costo y justificar si vale la pena con el nivel de precisión deseado

---

## Pagina 19

CLASE 5
Evaluación y ajuste de modelos

---

## Pagina 20

Entendimiento del dominio
Flujo del aprendizaje automático
1
Recolección de datos2
Análisis Exploratorio3
Procesamiento de datos4
Entrenamiento del modelo5
Evaluación del modelo6
Ajuste del modelo7
¿Cumple con el objetivo?
Aumento de característicasAumento de datos No
Hoy

---

## Pagina 21

Agenda de hoy
01
Métricas de 
regresión
02
Métricas de 
clasificación
03
Cross Validation
04
Hyperparameter 
Tuning

---

## Pagina 22

Métricas de
Regresión

---

## Pagina 23

MSE
La error cuadrático medio (MSE)  es una métrica de regresión que indica el promedio de las diferencias entre el 
valor real y el predicho, elevadas al cuadrado
N: número de datos
yi: dato conocido
ŷi: dato predicho

---

## Pagina 24

MSE
Gráfico: CodificandoBits
MSE =
6
(17-16)² + (15-17)² + (16-20)² + …
MSE =                             5.83 (°C)²

---

## Pagina 25

MSE
Gráfico: CodificandoBits
MSE =
6
… + (21-19)² + (18-2)² + (17-18)² 
MSE =                             47 (°C)²

---

## Pagina 26

RMSE
La raíz cuadrada del error cuadrático medio (RMSE)  es una métrica de regresión que calcula el promedio de las 
diferencias entre el valor real y el predicho elevadas al cuadrado, y luego le aplica la raíz cuadrada para volver a 
las unidades originales
N: número de datos
yi: dato conocido
ŷi: dato predicho

---

## Pagina 27

RMSE
Gráfico: CodificandoBits
RMSE =
6
(17-16)² + (15-17)² + (16-20)² + …
RMSE =                                  2.41 (°C)

---

## Pagina 28

RMSE
Gráfico: CodificandoBits
RMSE =
6
… + (21-19)² + (18-2)² + (17-18)² 
RMSE =                                  6.85 (°C)

---

## Pagina 29

MAE
La error absoluto medio (MAE)  es una métrica de regresión que indica el promedio de las diferencias absolutas 
entre el valor real y el predicho
N: número de datos
yi: dato conocido
ŷi: dato predicho

---

## Pagina 30

MAE
Gráfico: CodificandoBits
MAE =
6
|17-16| + |15-17| + |16-20| + …
MAE =                             2.17 (°C)

---

## Pagina 31

MAE
Gráfico: CodificandoBits
MAE =
6
     … + |21-18| + |18-2| + |17-18|
MAE =                             4.33 (°C)

---

## Pagina 32

R2
La coeficiente de determinación (R2)  es una métrica de regresión que mide la variabilidad explicada del 
modelo
● Indica que tan "bueno" es el modelo prediciendo datos reales
● Va de 0 a 1

---

## Pagina 33

Métricas de
Clasificación

---

## Pagina 34

Accuracy
El accuracy  es una métrica de clasificación que mide la proporción de predicciones correctas sobre el total de 
predicciones hechas
accuracy   =
número de aciertos
cantidad total de datos

---

## Pagina 35

Accuracy
accuracy   =
8
10
real predicho
accuracy   = 0.8

---

## Pagina 36

Matriz de confusión
La matriz de confusión es una métrica de clasificación que permite ver que tan confundido está nuestro 
modelo, mostrando tanto los aciertos como los desaciertos para cada una de las categorías 
Real
Verdadero Positivo
Predicho Es
Falso Negativo
Verdadero Negativo
Falso Positivo

---

## Pagina 37

Matriz de confusión
89 1
9 1
reales
predichos

---

## Pagina 38

Matriz de confusión
89 1
2 8
reales
predichos
88 2
1 9
reales
predichos
73 17
6 4
reales
predichos
Modelo 1 Modelo 2
Modelo 3

---

## Pagina 39

Precision
El precision es una métrica de clasificación que mide la proporción de predicciones positivas correctas sobre el 
total de predicciones positivas realizadas por el modelo
● De todo lo clasificado como positivo, ¿qué es realmente positivo?
Precision  =
TP
TP + FP

---

## Pagina 40

Precision
Precision  =
89
89 + 1
89 2
1 8
reales
predichos
Precision  = 0,99

---

## Pagina 41

Recall
El recall es una métrica de clasificación que mide la proporción de casos positivos reales que el modelo logró 
identificar correctamente sobre el total de casos positivos reales que existían
● De todo lo que es realmente positivo, ¿qué proporción fue clasificada como positivo?
Recall     =
TP
TP + FN

---

## Pagina 42

Recall
Precision  =
89
89 + 2
89 2
1 8
reales
predichos
Precision  = 0,97

---

## Pagina 43

Precision vs. Recall
¿Cuál es mejor?
● Precision: Si nos interesa minimizar la cantidad de falsos positivos ("anormales" detectados como 
"normales")
● Recall: si nos interesa minimizar la cantidad de falsos negativos ("normales" detectados como 
"anormales")
Precision  =
TP
TP + FP
Recall  =
TP
TP + FN

---

## Pagina 44

F-Score
El F-Score es una métrica de clasificación que combina la Precisión y el Recall en un solo número
De todo lo que es realmente positivo, ¿qué proporción fue clasificada como positivo?
β = 0:     nos quedamos con el precision
β = 0.5:  se da más importancia al recall
β = 1:      F1-Score, precision y recall tienen igual importancia

---

## Pagina 45

Cross
Validation

---

## Pagina 46

Cross-Validation
La validación cruzada es una técnica de evaluación de modelos que consiste en dividir los datos de 
entrenamiento en múltiples partes para entrenar y probar el modelo varias veces, asegurando que los 
resultados sean estables y no dependan de una sola división de datos.

---

## Pagina 47

Cross-Validation
Dolor de pecho Buena circulación 
sanguínea
Arterias obstruidas Peso Enfermedad 
cardíaca
No No No 125 No
Sí Sí Sí 180 Sí
Sí Sí No 210 No
Sí Sí No 100 Sí
No Sí Sí 120 No
Sí No No 95 Sí
Train (80%)
Test (20%)

---

## Pagina 48

Dolor de pecho Buena circulación 
sanguínea
Arterias obstruidas Peso Enfermedad 
cardíaca
No No No 125 No
Sí Sí Sí 180 Sí
Sí Sí No 210 No
Sí Sí No 100 Sí
No Sí Sí 120 No
Sí No No 95 Sí
K-Fold Cross-Validation
Dividir en 3 folds

---

## Pagina 49

K-Fold Cross-Validation
No No No 125 No
Sí Sí Sí 180 Sí
Sí Sí No 210 No
Sí Sí No 100 Sí
No Sí Sí 120 No
Sí No No 95 Sí
No No No 125 No
Sí Sí Sí 180 Sí
Sí Sí No 210 No
Sí Sí No 100 Sí
No Sí Sí 120 No
Sí No No 95 Sí
No No No 125 No
Sí Sí Sí 180 Sí
Sí Sí No 210 No
Sí Sí No 100 Sí
No Sí Sí 120 No
Sí No No 95 Sí
Accuracy:
93.41%
Accuracy:
94.12%
Accuracy:
92.89%
Accuracy General  = 
93.14% + 94.12% + 92.89%
3
=  93.47%

---

## Pagina 50

Hyperparameter 
Tuning

---

## Pagina 51

Ajuste de hiperparámetros
El ajuste de hiperparámetros es el proceso de prueba y error que permite encontrar el conjunto de 
hiperparámetros más adecuado para el modelo y los datos utilizados

---

## Pagina 52

Hiperparámetros de KNN
El K-Vecinos más cercanos puede configurarse con los siguientes hiperparámetros:
● k_neighbors: número de vecinos cercanos a considerar para realizar la predicción
● distance: métrica de distancia utilizada (euclideana, manhattan, …)

---

## Pagina 53

Hiperparámetros de Random Forest
El Random Forest puede configurarse con los siguientes hiperparámetros:
● n_estimators: Cuántos árboles individuales se crearán en el ensamble
● max_depth: El límite de niveles o ramas que puede crecer cada árbol.
● max_features: Limita cuantas columnas puede evaluar el árbol en cada nodo.
○ sqrt: el número de variables a considerar es la raíz cuadrada del total de variables
○ log2: el número de variables a considerar es el logaritmo en base 2 del total de variables
● criterion: La fórmula matemática que evalúa qué tan buena es una división en cada nodo. 
○ En regresión mide el error (como squared_error), 
○ En clasificación mide la pureza de las clases (gini o entropy).

---

## Pagina 54

Grid Search
Grid Search es un método de optimización de hiperparámetros que evalúa de forma exhaustiva todas las 
combinaciones posibles dentro de un conjunto predefinido de valores para encontrar la configuración óptima 
de un modelo

---

## Pagina 55

Grid Search
Hiperparámetro Valores
n_estimators [10, 20, 50]
max_features [“sqrt”, “log2”]
criterion [“squared_error”]
Hiperparámetro Mejor valor
n_estimators 50
max_features sqrt
criterion squared_error

---

## Pagina 56

Grid Search + Cross Validation
Hiperparámetro Valores
n_estimators [10, 20, 50]
max_features [“sqrt”, “log2”]
criterion [“squared_error”]
K = 5
6 combinaciones de hiperparámetros x 5 folds = 30 modelos distintos

---

## Pagina 57

Random Search
Random Search es un método de optimización de hiperparámetros que selecciona y evalúa combinaciones al 
azar a partir de un espacio de búsqueda definido, durante un número fijo de iteraciones.

---

## Pagina 58

Resumen
Clase 5

---

## Pagina 59

Agenda de hoy
Métricas de 
regresión
- MSE
- RMSE
- MAE
- R2
Métricas de 
clasificación
- Accuracy
- Matriz de confusión
- Precision
- Recall
- FScore
Cross 
Validation
- K-Fold Validation
Hyperparameter 
Tuning
- Grid Search
- Random Search

---

## Pagina 60

¡Gracias!
