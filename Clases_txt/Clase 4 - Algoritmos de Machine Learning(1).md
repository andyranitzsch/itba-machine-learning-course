# Clase 4 - Algoritmos de Machine Learning(1)

## Pagina 1

Machine Learning

---

## Pagina 2

CLASE 3
Data Wrangling
Repaso

---

## Pagina 3

El data wrangling es el proceso de procesamiento y transformación de los datos crudos para que sean consumibles y 
útiles para el análisis y los modelos de machine learning.
● Generalmente es la etapa que consume más tiempo en todo el flujo de machine learning.
● Incluye manejo de datos faltantes, corrección de errores e inconsistencias, detección y tratamiento de valores 
atípicos, transformación e enriquecimiento de la información
Data Wrangling

---

## Pagina 4

El data cleaning es el conjunto de técnicas que corrigen, completan o eliminan datos inválidos, faltantes o 
inconsistentes, para asegurar que el dataset sea confiable antes de entrenar un modelo.
● Es un prerrequisito: un modelo entrenado sobre datos sucios va a aprender patrones incorrectos, sin importar 
cuánto feature engineering se aplique después
Data Cleaning
Problemas que resuelve:
● Datos faltantes
● Registros duplicados
● Valores atípicos (outliers)
● Inconsistencias de formato

---

## Pagina 5

Tipos de datos faltantes
MCAR
Missing Completely At 
Random
La razón de la falta de datos es 
completamente ajena a los datos 
mismos.
Ejemplo: Justo en el milisegundo 
en el que se enviaba un registro, 
hubo un microcorte en la red wifi
MAR
Missing At Random
La causa no depende de estos 
mismos datos pero puede estar 
relacionada con otras variables 
del dataset.
Ejemplo: encuestas mal 
diseñadas. Si se pregunta "¿Tiene 
hijos?" y luego "¿Qué edad tienen 
sus hijos?", la segunda tendrá 
faltantes condicionados.
MNAR
Missing Not At Random
La falta de datos depende 
precisamente de los mismos 
valores no observados.
Ejemplo: Una balanza solo 
aguanta hasta 150 kilos. Si una 
persona pesa 180 kilos y se sube, 
la pantalla marca "ERROR" y no da 
ningún número.

---

## Pagina 6

Estrategias para trabajar con datos faltantes
Eliminación de registros
Sustitución de datos
Sustitución por media o mediana
Imputación Cold Deck
Imputación Hot Deck
Imputación por regresión
MICE

---

## Pagina 7

Tipos de duplicados
Los tipos de duplicados son:
● Exactos: todas las columnas son idénticas 
● Por clave: mismo identificador (ej. mismo user_id), pero con diferencias en otras columnas 
● Casi-duplicados (fuzzy): no son idénticos, pero refieren a la misma entidad. Ejemplo: "Juan Pérez" y "juan perez" 
con el mismo email

---

## Pagina 8

¿Cómo tratar los duplicados?
Las técnicas para tratar duplicados son:
● Eliminar duplicados exactos: conservar una sola copia
● Deduplicar por clave, quedándose con el registro más reciente (o más completo): la estrategia que ya usaste en 
el Ejemplo 2 (int_users) del Modelo Medallion
● Fuzzy matching: usar similitud de texto o reglas de negocio para unificar registros que refieren a la misma 
entidad pero no calzan exacto

---

## Pagina 9

Por naturaleza
● Global Outlier: hay un grupo de observaciones y otro subgrupo alejado. Ejemplo: hay un dataset de sueldos 
donde la mayoría gana entre $500.000 y $2.000.000, y aparece una persona que gana $80.000.000
● Contextual Outlier: El valor no es raro en sí mismo, pero sí lo es dado el contexto en el que aparece (tiempo, 
ubicación, categoría, etc.). El mismo valor puede ser perfectamente normal en otro contexto. Ejemplo: hay un 
dataset de clima que dice que en Julio hubo 40º (el outlier depende del mes)
● Collective Outlier: hay un subgrupo de observaciones que, tomadas en conjunto, se comportan de forma 
anómala. Ejemplo: hay un dataset de latidos, donde un latido irregular no dice mucho, pero una secuencia sí.
Tipos de Outliers

---

## Pagina 10

Por cantidad de variables
● Univariados: Son outliers que se detectan mirando una sola variable de forma aislada, sin considerar su relación 
con otras. Ejemplo: en la columna edad, un valor de 150 años es un outlier univariado — basta con mirar esa 
columna sola para detectarlo (con un boxplot, por ejemplo).
● Multivariados: Son outliers que no se detectan mirando cada variable por separado, sino que aparecen al 
considerar la combinación/relación entre dos o más variables en un espacio n-dimensional. Ejemplo: una 
persona de 20 años no es rara, y tener 15 años de experiencia laboral tampoco sería raro para alguien de 40 
años. Pero una persona de 20 años con 15 años de experiencia laboral sí es un combo imposible/raro.
Tipos de Outliers

---

## Pagina 11

Formas de tratar un outlier
● Eliminarlo: cuando se introdujo por algún error (no representa un valor real del fenómeno estudiado)
● Transformarlo: es un valor legítimo pero su magnitud distorsiona el análisis
● Imputarlo: se reemplaza el valor por otro valor "razonable", similar al tratamiento de datos faltantes
¿Cómo tratar los outliers?

---

## Pagina 12

El feature engineering es la etapa que incluye cualquier proceso de modificación de la forma de los datos con el 
objetivo de mejorar el rendimiento de los modelos creados
Feature Engineering
Técnicas de Feature Engineering
● Normalización
● Discretización
● Generación de nuevas variables
● Encoding
● Reducción de dimensionalidad

---

## Pagina 13

La Normalización tiene como objetivo llevar a todas las variables numéricas a una escala comparable
Min-Max Scaling: Lleva todo al rango [0,1]. Ejemplo: se tiene precio de propiedades entre $50.000 y $500.000. 
Luego de aplicar Min-Max, el más barato queda en 0 y el más caro en 1, y los demás se ubican proporcionalmente 
entre medio.
Z-Score: Centra los datos en media 0 y desvío estándar 1. Ejemplo: se tiene la altura de un grupo de personas 
(170cm, 190cm, etc). Luego de estandarizar, alguien con altura promedio queda en 0, alguien bastante más alto 
que el promedio queda en +2, y alguien más bajo -2
X-Decimal: Hace un corrimiento de coma en base a un número de dígitos. Ejemplo: se tienen montos de 
transacciones y se divide todo por 10.000. Entonces $9.800 pasa a ser 0.98
Feature Engineering | Normalización

---

## Pagina 14

La Discretización tiene como objetivo convertir una variable continua en categorías/intervalos
Binning: divide a la variable en un número específico de bins
● Igual Ancho: Por ejemplo la edad de 0 a 100 años se divide en bins de 20 años. Problema: si los datos no están 
distribuidos uniformemente, algunos bins quedan vacíos y otros sobrecargados
● Igual Frecuencia: cada bin tiene la misma cantidad de observaciones
Feature Engineering | Discretización

---

## Pagina 15

A partir de las columnas existentes, se crean atributos nuevos que capturan información útil que no estaba explícita. 
Ejemplos típicos:
● De una fecha de nacimiento → calcular la edad.
● De precio total y cantidad → calcular precio unitario.
● De una fecha → extraer día de la semana, mes, si es fin de semana.
Feature Engineering | Generación de variables

---

## Pagina 16

One-Hot Encoding: convierte variables categóricas en numéricas, ya que la mayoría de los algoritmos no pueden 
operar directamente sobre textos.
● Ejemplo: Se tiene un dataset de propiedades con una columna "tipo_propiedad" con valores Departamento, 
Casa y PH. Se reemplaza por 3 columnas nuevas → es_dpto, es_casa, es_ph
Feature Engineering | One-Hot Encoding
Id Tipo de propiedad Es Depto Es Casa Es PH
1 Depto 1 0 0
2 Casa 0 1 0
3 PH 0 0 1
4 Depto 1 0 0

---

## Pagina 17

Label Encoding: asigna un número arbitrario a cada categoría nominal (0, 1, 2...). 
Feature Engineering | Label Encoding
Id Nivel educativo Nivel Educativo
1 Primario 0
2 Secundario 1
3 Universitario 2

---

## Pagina 18

La reducción de la dimensionalidad es una técnica que consiste en disminuir la cantidad de variables (features) de un 
dataset, transformándolas en un nuevo conjunto más chico de variables (o eliminando directamente las menos 
relevantes), tratando de conservar la mayor cantidad de información posible de los datos originales.
Usos
● Aceleración de tiempos de entrenamiento de un modelo
● Visualización de datos para entender su distribución
● Reducción de ruido
Reducción de la dimensionalidad

---

## Pagina 19

Selección de variables: es una técnica de reducción de dimensionalidad que elimina directamente las variables menos 
útiles
● Varianza casi nula: una columna que casi no cambia entre registros aporta poca información para diferenciar 
observaciones. Ejemplo: la columna "país" cuando el 99% del dataset es de Argentina
● Alta correlación entre variables: si dos columnas están muy correlacionadas, conservar ambas puede ser 
redundante. Ejemplo: en un dataset de propiedades, "M2 totales" y "M2 cubiertos" están altamente 
correlacionadas — se puede eliminar una sin perder mucha información
Selección de variables

---

## Pagina 20

El Análisis de Componentes Principales (PCA) es una técnica de reducción de dimensionalidad que transforma un 
conjunto de variables (posiblemente correlacionadas entre sí) en un nuevo conjunto de variables llamadas 
componentes principales, que son combinaciones lineales de las variables originales.
● Ejemplo: en un dataset de propiedades las variables pueden estar muy correlacionadas entre sí: una propiedad 
más grande casi siempre tiene más ambientes. 
Análisis de Componentes Principales
Propiedad M2 totales M2 cubiertos Ambientes M2 por ambiente
1 80 75 3 25
2 120 110 4 27.5
3 45 42 1 42
Propiedad PC1 PC2
1 -0.50 -1.27
2 0.60 -0.71
3 -2.43 1.01

---

## Pagina 21

s torageGlue
Extrae, transforma y carga datos 
entre fuentes, con catálogo de 
metadatos centralizado
Servicios de AWS para procesamiento de datos
s torageEMR
Clusters administrados de 
Spark/Hadoop/Hive para procesar 
y transformar grandes volúmenes 
de datos
s torageLambda
Transformaciones livianas basadas 
en eventos
s torageAthena
Transformaciones sobre datos en 
S3
s torageRedshift
Transformaciones sobre datos en 
el warehouse

---

## Pagina 22

CLASE 4
Algoritmos de Machine Learning

---

## Pagina 23

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

## Pagina 24

Agenda de hoy
01
Algoritmos de 
regresión
02
Algoritmos de 
clasificación
03
Algoritmos de 
clusterización
04
Algoritmos de 
ensamble

---

## Pagina 25

¿Qué significa resolver un problema de ML?
En un problema de machine learning buscamos crear un modelo que sea capaz de tomar unos datos de 
entrada, encontrar ciertos patrones en esos datos, y en base a ello que logre realizar una predicción a partir de 
dichas propiedades 
● Para que el modelo aprenda patrones, usamos un set de entrenamiento
Datos Modelo Predicción
Modelo "perro"

---

## Pagina 26

Algoritmos de 
Machine Learning

---

## Pagina 27

Tipos de problemas: repaso
Antes de elegir un algoritmo, hay que saber qué queremos que el modelo responda
● Clasificación: la respuesta es una categoría (¿sobrevivió al Titanic o no?)
● Regresión: la respuesta es un número (¿cuánto va a costar una casa?)
● Clustering: no hay respuesta correcta, se buscan grupos parecidos (¿qué clientes se comportan similar?)

---

## Pagina 28

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

## Pagina 29

Regresión Lineal

---

## Pagina 30

Regresión Lineal
Ventajas
● Simplicidad: es fácil de entender e interpretar
● Rapidez: es computacionalmente eficiente
Desventajas
● Supuestos: Asume que la relación entre las variables es lineal
● Sensibilidad a valores atípicos: los outliers pueden torcer la recta entera
● Complejidad: no puede modelar relaciones no lineales entre variables sin transformaciones adicionales

---

## Pagina 31

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

## Pagina 32

Regresión Logística

---

## Pagina 33

Regresión Logística
Ventajas
● Simplicidad: es fácil de entender e interpretar
● Salida de probabilidades: no solo clasifica, sino que entrega una probabilidad exacta entre 0 y 1
Desventajas
● Clasificación binaria: está diseñado principalmente para clasificación binaria
● Vulnerable al desbalance: si una clase es muy dominante frente a la otra, el modelo puede sesgar sus 
predicciones

---

## Pagina 34

KNN
K-Vecinos más cercanos (KNN): es un algoritmo de aprendizaje supervisado que predice basándose en los K 
casos más parecidos que ya conoce, sin construir ninguna fórmula ni árbol de antemano.
k = 5
x
y

---

## Pagina 35

KNN
Ventajas
● Simplicidad: es fácil de entender e interpretar
● Adaptación: no asume nada sobre la forma de los datos. A diferencia de regresión lineal o logística, KNN 
se adapta a cualquier forma entre clases
Desventajas
● Costo: para clasificar un caso nuevo, hay que calcular la distancia contra todos los casos históricos, es 
caro computacionalmente
● Escala: puede disminuir su performance si los datos no vienen normalizados

---

## Pagina 36

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

## Pagina 37

K-Means
x
y

---

## Pagina 38

K-Means
x
y

---

## Pagina 39

K-Means
x
y

---

## Pagina 40

K-Means
Ventajas
● Velocidad: es simple y rápido
● Sin etiquetas: no requiere datos etiquetados para funcionar
● Interpretabilidad: fácil de interpretar el resultado
Desventajas
● Elección de K: hay que elegir el K de antemano
● Inicialización aleatoria: sensible a dónde caen los centros iniciales al azar — puede converger en 
resultados distintos según la corrida.
● Sensibilidad a escala: igual que KNN, hay que normalizar antes

---

## Pagina 41

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

## Pagina 42

Árboles de decisión
¿Es hora pico?
¿Distancia > 10km? ¿Distancia > 10km?
Sí No Sí No
$8000 $4500 $5500 $2000
Sí No

---

## Pagina 43

Árboles de decisión
Ventajas
● Interpretabilidad: Muy fácil de interpretar y visualizar 
● Sin normalización: No necesita que los datos estén normalizados.
● Flexibilidad de datos: Maneja bien variables numéricas y categóricas al mismo tiempo.
Desventajas
● Overfitting: Muy propenso a sobreajustar si no se le pone un límite de profundidad 
● Inestabilidad: Un cambio chico en los datos puede generar un árbol completamente distinto.
● Precisión limitada: Por sí solo, generalmente menos preciso que Random Forest o XGBoost.

---

## Pagina 44

Random Forest
Random Forest: es un algoritmo de ensemble que entrena muchos árboles de decisión distintos entre sí, y 
combina sus resultados — para clasificación, vota la mayoría; para regresión, promedia.
1. Se eligen N árboles se quieren entrenar
2. Para cada árbol se toma una muestra al azar
3. Se entrena el árbol completo con esas reglas
4. Se repite el proceso N veces, generando N árboles distintos
5. Para un caso nuevo, se le pregunta a los 100 árboles y votan (clasificación) o promedian (regresión)

---

## Pagina 45

Random Forest
Médico Pacientes que atendió Síntomas que le preguntó Diagnóstico
1 A, C, D, F Fiebre, tos Gripe
2 B, D, E, F Estornudos, picazón de ojos Alergia
3 A, C, E, F Fiebre, dolor de garganta Gripe
4 B, C, D, E Tos, picazón de ojos Alergia
5 A, B, C, E, F Fiebre, estornudos Gripe

---

## Pagina 46

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

## Pagina 47

XGBoost
XGBoost: es un algoritmo de ensemble que entrena árboles en secuencia, donde cada árbol nuevo se enfoca 
específicamente en corregir los errores que cometió el conjunto de árboles anterior.
1. El primer árbol hace una predicción básica
2. El segundo árbol se centra en los casos donde el primer árbol se equivocó
3. Así sucesivamente

---

## Pagina 48

Selección del
algoritmo

---

## Pagina 49

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

## Pagina 50

Ejercicio
1. Se quiere predecir el precio de un departamento a partir de sus metros cuadrados, ubicación y antigüedad.
● Regresión Lineal
2. Se quiere predecir si un cliente va a dejar de pagar un préstamo (sí/no), a partir de sus ingresos y su historial.
● Regresión Logística
3. Se quiere descubrir si existen grupos naturales de comportamiento en datos de clientes, sin ninguna etiqueta
● K-Means

---

## Pagina 51

Resumen
4. Se quiere estimar el precio de una casa mirando los precios de las casas más parecidas que se vendieron 
recientemente en el mismo barrio
● KNN
5. Un banco necesita explicarle a un cliente, paso a paso, por qué le rechazaron un crédito
● Árboles de decisión

---

## Pagina 52

Resumen
6. Una app de delivery quiere estimar rápido si una reseña de un restaurante es falsa o rea
● Random Forest
7. Se está compitiendo en una competencia donde el ranking se define por centésimas de precisión y no hay 
restricción de tiempo
● XGBoost

---

## Pagina 53

Resumen
Clase 4

---

## Pagina 54

Resumen de hoy
Algoritmos de 
regresión
- Regresión lineal
- Árboles de decisión
Algoritmos de 
clasificación
- Regresión logística
- KNN
- Árboles de decisión
Algoritmos de 
clusterización
- K-Means
Algoritmos de 
ensamble
- Random Forest
- XGBoost

---

## Pagina 55

¡Gracias!
