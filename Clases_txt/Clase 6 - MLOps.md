# Clase 6 - MLOps

## Pagina 1

Machine Learning

---

## Pagina 2

CLASE 5
Evaluación y ajuste de modelos
Repaso

---

## Pagina 3

MSE
La error cuadrático medio (MSE)  es una métrica de regresión que indica el promedio de las diferencias entre el 
valor real y el predicho, elevadas al cuadrado
N: número de datos
yi: dato conocido
ŷi: dato predicho

---

## Pagina 4

RMSE
La raíz cuadrada del error cuadrático medio (RMSE)  es una métrica de regresión que calcula el promedio de las 
diferencias entre el valor real y el predicho elevadas al cuadrado, y luego le aplica la raíz cuadrada para volver a 
las unidades originales
N: número de datos
yi: dato conocido
ŷi: dato predicho

---

## Pagina 5

MAE
La error absoluto medio (MAE)  es una métrica de regresión que indica el promedio de las diferencias absolutas 
entre el valor real y el predicho
N: número de datos
yi: dato conocido
ŷi: dato predicho

---

## Pagina 6

R2
La coeficiente de determinación (R2)  es una métrica de regresión que mide la variabilidad explicada del 
modelo
● Indica que tan "bueno" es el modelo prediciendo datos reales
● Va de 0 a 1

---

## Pagina 7

Accuracy
El accuracy  es una métrica de clasificación que mide la proporción de predicciones correctas sobre el total de 
predicciones hechas
accuracy   =
número de aciertos
cantidad total de datos

---

## Pagina 8

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

## Pagina 9

Matriz de confusión
89 1
9 1
reales
predichos

---

## Pagina 10

Precision
El precision es una métrica de clasificación que mide la proporción de predicciones positivas correctas sobre el 
total de predicciones positivas realizadas por el modelo
● De todo lo clasificado como positivo, ¿qué es realmente positivo?
Precision  =
TP
TP + FP

---

## Pagina 11

Recall
El recall es una métrica de clasificación que mide la proporción de casos positivos reales que el modelo logró 
identificar correctamente sobre el total de casos positivos reales que existían
● De todo lo que es realmente positivo, ¿qué proporción fue clasificada como positivo?
Recall     =
TP
TP + FN

---

## Pagina 12

F-Score
El F-Score es una métrica de clasificación que combina la Precisión y el Recall en un solo número
De todo lo que es realmente positivo, ¿qué proporción fue clasificada como positivo?
β = 0:     nos quedamos con el precision
β = 0.5:  se da más importancia al recall
β = 1:      F1-Score, precision y recall tienen igual importancia

---

## Pagina 13

Cross-Validation
La validación cruzada es una técnica de evaluación de modelos que consiste en dividir los datos de 
entrenamiento en múltiples partes para entrenar y probar el modelo varias veces, asegurando que los 
resultados sean estables y no dependan de una sola división de datos.

---

## Pagina 14

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

## Pagina 15

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

## Pagina 16

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

## Pagina 17

Ajuste de hiperparámetros
El ajuste de hiperparámetros es el proceso de prueba y error que permite encontrar el conjunto de 
hiperparámetros más adecuado para el modelo y los datos utilizados

---

## Pagina 18

Hiperparámetros de KNN
El K-Vecinos más cercanos puede configurarse con los siguientes hiperparámetros:
● k_neighbors: número de vecinos cercanos a considerar para realizar la predicción
● distance: métrica de distancia utilizada (euclideana, manhattan, …)

---

## Pagina 19

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

## Pagina 20

Grid Search
Grid Search es un método de optimización de hiperparámetros que evalúa de forma exhaustiva todas las 
combinaciones posibles dentro de un conjunto predefinido de valores para encontrar la configuración óptima 
de un modelo

---

## Pagina 21

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

## Pagina 22

Grid Search + Cross Validation
Hiperparámetro Valores
n_estimators [10, 20, 50]
max_features [“sqrt”, “log2”]
criterion [“squared_error”]
K = 5
6 combinaciones de hiperparámetros x 5 folds = 30 modelos distintos

---

## Pagina 23

Random Search
Random Search es un método de optimización de hiperparámetros que selecciona y evalúa combinaciones al 
azar a partir de un espacio de búsqueda definido, durante un número fijo de iteraciones.

---

## Pagina 24

CLASE 6
MLOps

---

## Pagina 25

Ciclo de vida
de los modelos

---

## Pagina 26

Datos crudos
Flujo del aprendizaje automático
Data Wrangling
Conjunto de 
entrenamiento
Conjunto de 
test
Algoritmo de 
machine learning
Modelo
Entrenamiento
Inferencia
Datos nuevos Data Wrangling Inferencia Resultado
Despliegue del modelo

---

## Pagina 27

Deuda técnica oculta
Los sistemas basados en machine learning poseen la denominada deuda técnica oculta debido a la gran 
cantidad de componentes relacionados con el proceso de aprendizaje
ML Code
Testing and 
debugging
Data Collection
Automation
Configuration
Feature Engineering
Data
 Verification
Resource 
management
Metadata management
Model analysis
Serving 
infrastructure
Process 
management
Monitoring
Paper: Hidden Technical Debt in Machine Learning Systems

---

## Pagina 28

Ciclo de vida de los modelos
La canalización para la construcción de un modelo de machine learning está formada por las siguientes 
operaciones
Data 
Ingestion
Data 
Analysis
Data 
Transformation
Data 
Validation
Data 
Splitting
Training Model 
Building
Model 
Validation Rollout
Serving Monitoring Logging

---

## Pagina 29

MLOps
MLOps es un conjunto de prácticas que automatizan y simplifican los flujos de trabajo y los despliegues de 
machine learning. 
● Este concepto de MLOps deriva del concepto de DevOps, que son las diferentes acciones que se realizan 
durante el ciclo de vida del software desde su fase inicial hasta su fase final
DEV OPSML

---

## Pagina 30

MLOps
El proceso de entrenamiento e inferencia de un modelo está formado por cinco operaciones básicas
Entrenamiento Empaquetado Evaluación Despliegue Monitorización
Re-entrenamiento

---

## Pagina 31

Despliegue
El despliegue de un modelo de machine learning consiste en llevar de la etapa de desarrollo a la etapa de 
producción para que esté a disposición del usuario final
Requerimientos de diseño
● Predicción: ¿es en tiempo real o por lotes?
● Latencia: es el tiempo de respuesta requerido desde que se envía la solicitud al modelo hasta que se 
recibe la predicción
● Rendimiento: número de solicitudes por segundo que puede soportar el sistema donde está alojado el 
modelo

---

## Pagina 32

Tipos de despliegue
En la nube: el cómputo requerido para las predicciones se realiza en servidores alojados en la nube
● Los datos y las predicciones se transfieren por internet
● Se usa cuando la latencia no es un problema
On the edge: el cómputo se realiza en el dispositivo local
● Se usa cuando no se requiere muchos recursos computacionales
● Se usa cuando se requiere baja latencia

---

## Pagina 33

Monitoreo
El monitoreo de un modelo de machine learning permite observar continuamente el desempeño del modelo y 
determinar si está funcionando correctamente
Gráficos: CodificandoBits

---

## Pagina 34

Monitoreo | Fallos del modelo
El data drift (deriva de datos) indica cambios ligeros o significativos en las características o distribución de 
datos de entrada con respecto a los usados con el entrenamiento
● Ejemplo: modelo de detección de fraude durante el Black Friday
El concept drift (deriva de conceptos) indica que la distribución de los datos de entrada permanece sin 
variación, pero a pesar de ello las predicciones hechas por el modelo comienza a cambiar
● Ejemplo: predicción de precios de viviendas tras inflación

---

## Pagina 35

Mantenimiento
El mantenimiento de un modelo de machine learning es el proceso mediante el cual se actualiza el modelo 
desplegado para mantener su desempeño
Gráficos: CodificandoBits
Rapidez de respuesta
 Periodicidad de desempeño Periodicidad de los datos

---

## Pagina 36

Mantenimiento
Las actualizaciones no se hacen directamente sobre el modelo desplegado, sino que se genera una réplica del 
modelo y actualizar sobre esas réplicas
Estrategias de mantenimiento
● Afinación del modelo existente: se toma como punto de partida el modelo ya desplegado, se replica y se 
continua su entrenamiento con nuevos datos
● Entrenamiento desde cero: se genera una réplica de la arquitectura original del modelo, se recolecta un 
nuevo set de datos y se ejecuta un entrenamiento desde cero

---

## Pagina 37

Niveles de
automatización

---

## Pagina 38

Niveles de automatización
Los niveles de automatización indican el grado de automatización de las operaciones del proceso MLOps
Nivel 0
Nivel 1
Nivel 2
Automatización

---

## Pagina 39

Niveles de automatización
Tipos de operaciones
● Integración Continua (IC): Valida que el código, los datos y el modelo funcionen bien juntos
● Entrega Continua (EC): Despliega automáticamente los pipelines y servicios a producción.
● Entrenamiento Ininterrumpido (EI): Reentrena el modelo automáticamente y lo sustituye si supera al 
anterior.

---

## Pagina 40

Nivel de automatización 0
Nivel de automatización 0: proceso manual de la generación de modelos
● Transición manual entre las etapas de entrenamiento y despliegue
● Versionado manual de modelos
● No existe Integración Continua (IC)
● No existe Entrega Continua (EC)
● Generación manual del modelo
● No existe monitorización

---

## Pagina 41

Nivel de automatización 1
Nivel de automatización 1: proceso automático de la generación de modelos
● Versionado automático de modelos
● No existe Integración Continua (IC)
● Existe Entrega Continua (EC)
● Generación manual del modelo
● Existe monitorización

---

## Pagina 42

Nivel de automatización 2
Nivel de automatización 2: proceso completamente automatizado para la generación y despliegue de modelos
● Versionado automático de modelos
● Existe Integración Continua (IC)
● Existe Entrega Continua (EC)
● Generación manual del modelo
● Existe monitorización

---

## Pagina 43

Tecnologías de
AWS

---

## Pagina 44

MLOps basado en Amazon SageMaker
Amazon RDS Amazon S3
AWS Lambda Amazon 
EventBridge
AWS Step 
Functions
AWS Glue AWS Fargate Amazon 
SageMaker
AWS Step 
Functions
Amazon S3
Amazon 
SageMaker
Amazon 
DynamoDB
Amazon S3
Amazon CloudWatch
Feature Store
Repositorio para data curada
Trigger
Reentrena modelos (con schedule o 
basado en degradación)
Model Pipeline
Orquestación de la transformación de 
datos, entrenamiento y despliegue
Extracción y 
transformación
Entrenamiento y 
Evaluación del modelo
Validación del 
modelo
Repositorio fuente
Código fuente para las transformaciones
Inferencia del 
modelo
Monitoreo
Metadata
Información de la ejecución del pipeline
Amazon S3
Output Store

---

## Pagina 45

¡Gracias!
