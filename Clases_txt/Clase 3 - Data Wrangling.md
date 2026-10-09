# Clase 3 - Data Wrangling

## Pagina 1

Machine Learning

---

## Pagina 2

CLASE 2
Análisis exploratorio
Repaso

---

## Pagina 3

El almacenamiento es la base de todo proceso de machine learning. Sin un lugar donde guardar los 
datos de entrenamiento, los modelos no funcionarán
Almacenamiento

---

## Pagina 4

Propiedades Esenciales de los Datos
as 
Volumen
El tamaño absoluto y la escala 
de la información que la 
organización recopila, almacena 
y procesa activamente.

Velocidad
La tasa en tiempo real a la que la 
data es generada, recolectada, 
procesada y puesta a 
disposición para decisiones.

Variedad
Diferentes formatos, 
estructuras y orígenes de la 
información, desde tablas 
rígidas hasta archivos 
multimedia sin estructura.

---

## Pagina 5

Tipos de Datos en la Era Moderna

Estructurados
Información altamente 
organizada que sigue un 
esquema rígido y predefinido.
EJEMPLOS:
Tablas de bases de datos 
relacionales, archivos CSV, hojas 
de cálculo Excel.

No Estructurados
Datos sin una estructura o 
modelo predefinido. Es el 
formato más abundante y 
complejo de procesar.
EJEMPLOS:
Archivos de texto libre, videos, 
archivos de audio, imágenes.

Semi-estructurados
No se ajustan a un esquema, 
pero contienen etiquetas o 
marcadores que separan 
elementos en jerarquías.
EJEMPLOS:
Documentos JSON, archivos 
XML, formatos NoSQL.

---

## Pagina 6

s torageS3
Un lugar gigante para guardar 
archivos sueltos (fotos, videos, 
datasets), pensado para volúmenes 
enormes de información. 
Servicios de AWS para almacenamiento
s torageEBS
Un disco rígido virtual, para una 
sola computadora a la vez.
s torageFSx
Como EFS, pero optimizados por 
ejemplo para entregar datos para 
el entrenamiento de modelos
s torageEFS
Una carpeta compartida en red, a 
la que varias computadoras 
acceden al mismo tiempo.
s torageRDS
Una base de datos tradicional, con 
tablas prolijas y ordenadas
s torageDynamoDB
Una base de datos súper rápida y 
flexible, sin esa estructura fija de 
tablas.

---

## Pagina 7

La ingesta es el proceso que trae los datos de un origen hacia un destino, donde se llevará a cabo el 
proceso de Machine Learning. 
Ingesta
Amazon RDS
Smartwatch

---

## Pagina 8

Tipos de ingesta
Batch
Procesa datos por lotes
Ejemplos
● Un banco que cada noche calcula el resumen 
de todas las transacciones del día.
● Una tienda online que actualiza su catálogo 
de productos una vez por semana.
Streaming
Procesa datos en tiempo real
Ejemplos
● Una app de delivery que actualiza la ubicación 
del repartidor en el mapa a medida que se 
mueve. 
● Una red social con sus likes, comentarios o 
vistas

---

## Pagina 9

s torageKinesis Data 
Streams
Recibe los datos que llegan, los 
guarda, y aguarda que sean 
consumidos
Servicios de AWS para ingesta
s torageKinesis Data
Firehose
Recibe los datos que llegan y los 
entrega a un destino
s torageDatabase 
Migration Service
Copia datos de una base de datos 
a otra
s torageManaged Stream.
Apache Kafka
Una alternativa de Kinesis
s torageTransfer 
Family
Permite que agentes externos 
suban archivos 
s torageSnow
Family
Dispositivos físicos que permiten 
transferir datos desde o hacia AWS

---

## Pagina 10

El análisis exploratorio de datos (EDA) es el proceso de examinar un dataset para entender su estructura, 
calidad y patrones principales, antes de limpiarlo, transformarlo o usarlo para entrenar un modelo
Análisis Exploratorio
TITANIC DATASET

---

## Pagina 11

Fases del análisis Exploratorio
Pregunta a responder1
Generalidades del dataset2
Tipos de datos3
Estadística descriptiva4
Visualización5
Interacciones6
Resumen7

---

## Pagina 12

Fases del análisis Exploratorio
¿Qué pregunta queremos responder?:  en este caso queremos saber qué tipo de personas tenían la 
probabilidad más alta de sobrevivir al hundimiento del Titanic  
1
2
Dar una primera mirada al dataset:  mirar su tamaño, determinar cuáles son las características (features) y 
dar un primer barrido a sus registros (observaciones)

---

## Pagina 13

Fases del análisis Exploratorio
Definir los tipos de datos                         3
Numéricas
Discretos Continuos

---

## Pagina 14

Fases del análisis Exploratorio
Definir los tipos de datos                         3
Categóricas
Nominales Binarios Ordinales

---

## Pagina 15

Fases del análisis Exploratorio
Descripción estadística de los datos
4
Tendencia Central
Variabilidad
Media
Mediana
Desviación 
Estándar
Rangos 
Intercuartiles

---

## Pagina 16

Fases del análisis Exploratorio 
5 Visualizar los datos
Gráficos: CodificandoBits
Histograma
Edad
Densidad
Tarifa
Densidad
0                   20                    40                  60             80 0              100            200            300             400

---

## Pagina 17

Fases del análisis Exploratorio 
5 Visualizar los datos
Gráficos: CodificandoBits
Boxplots
80
70
60
50
40
30
20
10
0
Edad
500
400
300
200
100
0
Tarifa

---

## Pagina 18

Fases del análisis Exploratorio 
5 Visualizar los datos
Gráficos: CodificandoBits
Gráfico de barras
0 = No sobrevivió
1 = Sobrevivió

---

## Pagina 19

Fases del análisis Exploratorio 
6 Análisis bivariado
Gráficos: CodificandoBits
Correlación lineal positiva
 Correlación lineal inversa
 No hay correlación lineal

---

## Pagina 20

Fases del análisis Exploratorio 
6 Análisis bivariado
Gráficos: CodificandoBits

---

## Pagina 21

Fases del análisis Exploratorio 
6 Análisis bivariado
Gráficos: CodificandoBits

---

## Pagina 22

CLASE 3
Data Wrangling

---

## Pagina 23

Agenda de hoy
01
Datos faltantes
02
Duplicados
03
Outliers
04
Feature 
Engineering

---

## Pagina 24

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

## Pagina 25

Procesamiento de
datos

---

## Pagina 26

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

## Pagina 27

Procesamiento de
datos
Análisis de datos faltantes

---

## Pagina 28

Un dato faltante es la ausencia de un valor en una observación donde se esperaría que hubiera uno, ya sea porque no 
fue recolectado, no se registró, o no aplica.
● Se representan comúnmente como NULL, NaN o vacío
● Los nulos también pueden influenciar los resultados de los modelos de machine learning
Datos faltantes
Nombre Apellido Edad Altura (cm) Género
Luis NULL 24 NULL Masculino
NULL Brunetti 55 160 NULL

---

## Pagina 29

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

## Pagina 30

Estrategias para trabajar con datos faltantes
Eliminación de registros
Sustitución de datos
Sustitución por media o mediana
Imputación Cold Deck
Imputación Hot Deck
Imputación por regresión
MICE

---

## Pagina 31

Eliminación de datos: Consiste en excluir del análisis las filas o columnas que presentan valores vacíos.
● No se recomienda aplicar esta estrategia en situaciones que no sean MCAR (Missing Completely 
At Random), ya que introduce sesgos graves en la distribución.
Estrategias para trabajar con datos faltantes
Id Nombre Apellido Email Género Cumpleaños
12345 NULL NULL NULL NULL NULL
12345 Ricardo Lopez mp@gmail.com F 1997-02-24

---

## Pagina 32

Sustitución por expertos: Reemplazo por valores no observados guiado por un especialista del dominio 
o fuente confiable.
Estrategias para trabajar con datos faltantes
País Capital
Argentina Buenos Aires
Brasil NULL
Chile Santiago de Chile
País Capital
Argentina Buenos Aires
Brasil Brasilia
Chile Santiago de Chile

---

## Pagina 33

Media o Mediana: Reemplazo utilizando la media calculada de los valores presentes. Desventaja: Reduce 
artificialmente la varianza, distorsiona la distribución y deprime las correlaciones.
Cold Deck: Deducción usando fuentes externas o relaciones lógicas (ej. coordenadas para determinar barrio).
Hot Deck: Copia datos de registros similares vecinos (ej. estimar baños según habitaciones conocidas).
Estrategias para trabajar con datos faltantes

---

## Pagina 34

Imputación Avanzada
Imputación por Regresión: Se entrena un modelo predictivo para estimar el dato faltante como variable objetivo.
MICE (Chained Equations): Asume un origen MAR (Missing At Random).
● Proceso iterativo (aprox. 10 ciclos) donde cada variable se predice en función de las demás. Comienza con una 
imputación simple y refina las estimaciones interconectadas hasta lograr la convergencia.

---

## Pagina 35

Procesamiento de
datos
Deduplicación

---

## Pagina 36

Duplicados
Un registro duplicado es una fila que representa la misma entidad u observación más de una vez en el dataset, ya sea 
de forma idéntica o con variaciones menores.
● Se originan por errores de carga, reintentos de sistemas, joins mal hechos, o ausencia de una clave única 
● Los duplicados pueden inflar artificialmente conteos, sumas y promedios, sesgando el análisis y el 
entrenamiento de modelos 
Id Nombre Apellido Email Fecha de alta
12345 Carlos M cm@gmail.com 2022-01-01
12345 Carlos Martinez cm@gmail.com 2002-01-03

---

## Pagina 37

Tipos de duplicados
Los tipos de duplicados son:
● Exactos: todas las columnas son idénticas 
● Por clave: mismo identificador (ej. mismo user_id), pero con diferencias en otras columnas 
● Casi-duplicados (fuzzy): no son idénticos, pero refieren a la misma entidad. Ejemplo: "Juan Pérez" y 
"juan perez" con el mismo email

---

## Pagina 38

Tipos de duplicados
Id Nombre Apellido Email Fecha de alta
12345 Noelia Ponce np@gmail.com 2024-10-02
12345 Noelia Ponce np@gmail.com 2024-10-02
Id Nombre Apellido Email Fecha de alta
12345 Noelia Ponce np@gmail.com 2024-10-02
12345 Marcos Sosa ms@gmail.com 2024-10-02
Id Nombre Apellido Email Fecha de alta
12345 Noelia ponce np@gmail.com 2024-10-02
12345 Noelia Ponce np@gmail.com 2024-10-02
Exactos
Por clave
Casi 
duplicados

---

## Pagina 39

¿Cómo tratar los duplicados?
Las técnicas para tratar duplicados son:
● Eliminar duplicados exactos: conservar una sola copia
● Deduplicar por clave, quedándose con el registro más reciente o más completo
● Fuzzy matching: usar similitud de texto o reglas de negocio para unificar registros que refieren a la misma 
entidad pero no calzan exacto

---

## Pagina 40

Procesamiento de
datos
Análisis de valores atípicos

---

## Pagina 41

Un outlier es una observación que se desvía tanto de las otras observaciones como para despertar sospechas que fue 
generado por un mecanismo diferente
● Es un concepto subjetivo al problema
● Son observaciones distantes del resto de los datos
● Los outliers pueden influenciar los resultados de los modelos de machine learning
Outliers
Nombre Apellido Edad Altura (cm) Género
Pablo Perez 4 180 Masculino
Gerardo Brunetti 130 160 Masculino

---

## Pagina 42

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

## Pagina 43

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

## Pagina 44

Formas de tratar un outlier
● Eliminarlo: cuando se introdujo por algún error (no representa un valor real del fenómeno estudiado)
● Transformarlo: es un valor legítimo pero su magnitud distorsiona el análisis
● Imputarlo: se reemplaza el valor por otro valor "razonable", similar al tratamiento de datos faltantes
¿Cómo tratar los outliers?

---

## Pagina 45

Procesamiento de
datos
Feature Engineering

---

## Pagina 46

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

## Pagina 47

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

## Pagina 48

La Discretización tiene como objetivo convertir una variable continua en categorías/intervalos
Binning: divide a la variable en un número específico de bins
● Igual Ancho: Por ejemplo la edad de 0 a 100 años se divide en bins de 20 años. Problema: si los datos no están 
distribuidos uniformemente, algunos bins quedan vacíos y otros sobrecargados
● Igual Frecuencia: cada bin tiene la misma cantidad de observaciones
Feature Engineering | Discretización

---

## Pagina 49

A partir de las columnas existentes, se crean atributos nuevos que capturan información útil que no estaba explícita. 
Ejemplos típicos:
● De una fecha de nacimiento → calcular la edad.
● De precio total y cantidad → calcular precio unitario.
● De una fecha → extraer día de la semana, mes, si es fin de semana.
Feature Engineering | Generación de variables

---

## Pagina 50

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

## Pagina 51

Label Encoding: asigna un número arbitrario a cada categoría nominal (0, 1, 2...). 
Feature Engineering | Label Encoding
Id Nivel educativo Nivel Educativo
1 Primario 0
2 Secundario 1
3 Universitario 2

---

## Pagina 52

Procesamiento y
Transformación
Reducción de la dimensionalidad

---

## Pagina 53

La reducción de la dimensionalidad es una técnica que consiste en disminuir la cantidad de variables (features) de un 
dataset, transformándolas en un nuevo conjunto más chico de variables (o eliminando directamente las menos 
relevantes), tratando de conservar la mayor cantidad de información posible de los datos originales.
Usos
● Aceleración de tiempos de entrenamiento de un modelo
● Visualización de datos para entender su distribución
● Reducción de ruido
Reducción de la dimensionalidad

---

## Pagina 54

Selección de variables: es una técnica de reducción de dimensionalidad que elimina directamente las variables menos 
útiles
● Varianza casi nula: una columna que casi no cambia entre registros aporta poca información para diferenciar 
observaciones. Ejemplo: la columna "país" cuando el 99% del dataset es de Argentina
● Alta correlación entre variables: si dos columnas están muy correlacionadas, conservar ambas puede ser 
redundante. Ejemplo: en un dataset de propiedades, "M2 totales" y "M2 cubiertos" están altamente 
correlacionadas — se puede eliminar una sin perder mucha información
Selección de variables

---

## Pagina 55

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

## Pagina 56

Procesamiento y
Transformación
Servicios de AWS

---

## Pagina 57

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

## Pagina 58

Resumen
Clase 3

---

## Pagina 59

Resumen de hoy
Datos faltantes
- MCAR, MAT y MNAR
- Eliminación
- Sustitución por expertos
- Imputación por media
- Hot y cold deck
- Imputación por regresión
- MICE
Duplicados
- Tipos de duplicados
- Eliminación
- Deduplicación por clave
- Fuzzy matching
Outliers
- Tipos de outliers
- Eliminación
- Transformación
- Imputación
Feature 
Engineering
- Min-Max Scaling
- Z-Score
- X-Decimal
- Binning
- Generación de variables
- Encoding
- Reducción de 
dimensionalidad

---

## Pagina 60

¡Gracias!
