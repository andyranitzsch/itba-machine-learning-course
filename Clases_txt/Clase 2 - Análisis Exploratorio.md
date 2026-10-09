# Clase 2 - Análisis Exploratorio

## Pagina 1

Machine Learning

---

## Pagina 2

YA DICTADO
1. Foundations y Cloud 
Architecture
CURSO ACTUAL
2. Machine Learning 
Engineering
OCTUBRE
3. Data Engineering 
Applications
Certificación Cloud Data Engineering

---

## Pagina 3

Requisitos de aprobación
Trabajo
Práctico
    70% Asistencia

---

## Pagina 4

CLASE 1
Fundamentos de Machine Learning
Repaso

---

## Pagina 5

El machine learning (aprendizaje automático) es un subconjunto de la inteligencia artificial (IA)
● El aprendizaje profundo es un subdominio del aprendizaje automático
Machine Learning != Inteligencia Artificial
Inteligencia Artificial (IA)
Aprendizaje Automático (ML)
Aprendizaje Profundo (DL)

---

## Pagina 6

Tipos de aprendizaje automático
Aprendizaje Supervisado
El modelo se entrena con datos 
etiquetados. 
El objetivo es que el modelo 
aprenda la relación entre ambas 
para poder predecir la salida ante 
nuevas entradas. 
Aprendizaje No 
Supervisado
El modelo trabaja con datos sin 
etiquetar
Su objetivo es descubrir por sí 
mismo patrones, agrupamientos o 
relaciones ocultas dentro de los 
datos.
Aprendizaje por Refuerzo
El modelo aprende a través de 
prueba y error, interactuando con 
un entorno
En cada paso recibe una 
recompensa o penalización según 
sus acciones, y ajusta su 
comportamiento con el objetivo 
de maximizar la recompensa 
acumulada a lo largo del tiempo

---

## Pagina 7

Entendimiento del dominio
Flujo del aprendizaje automático
1
Recopilación de datos2
Análisis Exploratorio3
Procesamiento de datos4
Entrenamiento del modelo5
Evaluación del modelo6
Ajuste del modelo7
¿Cumple con el objetivo?
Aumento de característicasAumento de datos No

---

## Pagina 8

Entrenamiento de modelos
Dataset de entrenamiento
Dataset de prueba
Algoritmo 
Seleccionado
Modelo 
Entrenado
Modelo 
Alojado
Predicción
Hiperparámetros
Métricas
Reajuste

---

## Pagina 9

Overfitting y Underfitting
Overfitting Underfitting Equilibrio

---

## Pagina 10

Desafíos del ML
Datos
● Mala calidad
● No representativo
● Insuficiente
● Overfitting
● Underfitting
Negocio
● Falta de definiciones
● Falta de conexión 
entre los equipos
● Falta de 
documentación
Tecnología
● Problemas de 
privacidad
● Selección de 
herramientas 
costosas
● Integración con 
otros sistemas

---

## Pagina 11

Observaciones
ID Cliente Fecha Tipo Monto Es Fraude
124345346 2026/09/03 VISA $50.000 No
23423522 2026/07/13 MASTERCARD $13.000 No
123456 2026/04/11 VISA $99.997 Sí
Los problemas de aprendizaje automático necesitan una gran cantidad de datos, también llamados observaciones
● Los datos que ya tienen una respuesta se llaman datos etiquetados
● Cada observación se compone de dos elementos
○ Target: es la respuesta que se quiere predecir
○ Feature: es un atributo del dato que se puede utilizar para identificar patrones y predecir 
Features Target

---

## Pagina 12


1. Entrada
(Garbage In)
Datos erróneos, 
incompletos, duplicados o 
mal estructurados ingresan 
al sistema.


2. Proceso
(Algoritmo / ML)
El modelo procesa los 
datos sin "saber" que son 
incorrectos


3. Salida
(Garbage Out)
Resultados deficientes, 
predicciones erróneas y 
decisiones de negocio 
equivocadas.
Garbage In, Garbage Out (GIGO)

---

## Pagina 13

CLASE 2
Análisis Exploratorio

---

## Pagina 14

Agenda de hoy
01
Almacenamiento
02
Ingesta
03
Análisis 
exploratorio

---

## Pagina 15

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

## Pagina 16

Almacenamiento

---

## Pagina 17

El almacenamiento es la base de todo proceso de machine learning. Sin un lugar donde guardar los 
datos de entrenamiento, los modelos no funcionarán
Almacenamiento

---

## Pagina 18

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

## Pagina 19

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

## Pagina 20

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

## Pagina 21

Ingesta

---

## Pagina 22

La ingesta es el proceso que trae los datos de un origen hacia un destino, donde se llevará a cabo el 
proceso de Machine Learning. 
Ingesta
Amazon RDS
Smartwatch

---

## Pagina 23

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

## Pagina 24

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

## Pagina 25

Analisis
Exploratorio

---

## Pagina 26

El análisis exploratorio de datos (EDA) es el proceso de examinar un dataset para entender su estructura, 
calidad y patrones principales, antes de limpiarlo, transformarlo o usarlo para entrenar un modelo
Análisis Exploratorio
TITANIC DATASET

---

## Pagina 27

Fases del análisis Exploratorio
Pregunta a responder1
Generalidades del dataset2
Tipos de datos3
Estadística descriptiva4
Visualización5
Interacciones6
Resumen7

---

## Pagina 28

Fases del análisis Exploratorio
Pregunta a responder1
Generalidades del dataset2
Tipos de datos3
Estadística descriptiva4
Visualización5
Interacciones6
Resumen7

---

## Pagina 29

Fases del análisis Exploratorio
¿Qué pregunta queremos responder?:  en este caso queremos saber qué tipo de personas tenían la 
probabilidad más alta de sobrevivir al hundimiento del Titanic  
1
2
Dar una primera mirada al dataset:  mirar su tamaño, determinar cuáles son las características (features) y 
dar un primer barrido a sus registros (observaciones)

---

## Pagina 30

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

## Pagina 31

Un dato faltante es la ausencia de un valor en una observación donde se esperaría que hubiera uno, ya sea porque no 
fue recolectado, no se registró, o no aplica.
● Se representan comúnmente como NULL, NaN o vacío
● Los nulos también pueden influenciar los resultados de los modelos de machine learning
Datos faltantes
Nombre Apellido Edad Altura (cm) Género
Luis NULL 24 NULL Masculino
NULL Brunetti 55 160 NULL

---

## Pagina 32

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

## Pagina 33

Fases del análisis Exploratorio
Pregunta a responder1
Generalidades del dataset2
Tipos de datos3
Estadística descriptiva4
Visualización5
Interacciones6
Resumen7

---

## Pagina 34

Fases del análisis Exploratorio
Definir los tipos de datos                         3
Numéricas
Discretos Continuos

---

## Pagina 35

Fases del análisis Exploratorio
Definir los tipos de datos                         3
Categóricas
Nominales Binarios Ordinales

---

## Pagina 36

Fases del análisis Exploratorio
Pregunta a responder1
Generalidades del dataset2
Tipos de datos3
Estadística descriptiva4
Visualización5
Interacciones6
Resumen7

---

## Pagina 37

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

## Pagina 38

Fases del análisis Exploratorio 
4
Media = 29.88 Media = 33.29
Descripción estadística de los datos
● Tendencia Central
Media

---

## Pagina 39

Fases del análisis Exploratorio
4
Mediana = 3 Mediana = 28
Descripción estadística de los datos
● Tendencia Central
1  3  3  6  7  8  9 
1  2  3  4 5  7  8  9 
M = 6
M = (4+5)/2 = 3.5
Mediana

---

## Pagina 40

Fases del análisis Exploratorio 
4 Descripción estadística de los datos
● Variabilidad
Menor desviación 
Menor dispersión
Desviación Estándar

---

## Pagina 41

Fases del análisis Exploratorio 
4 Descripción estadística de los datos
● Variabilidad
25% 25% 25% 25%
Percentil 25 Percentil 75
Mediana
Rango intercuartiles
Rango Intercuartiles

---

## Pagina 42

Fases del análisis Exploratorio 
4 Descripción estadística de los datos
● Variabilidad
Percentil 25 Percentil 75
Mediana
edad
(años)
0 8021 28 39
Rango intercuartiles
39 - 21 = 18 años
Rango Intercuartiles

---

## Pagina 43

Fases del análisis Exploratorio
Pregunta a responder1
Generalidades del dataset2
Tipos de datos3
Estadística descriptiva4
Visualización5
Interacciones6
Resumen7

---

## Pagina 44

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

## Pagina 45

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

## Pagina 46

Fases del análisis Exploratorio 
5 Visualizar los datos
Gráficos: CodificandoBits
Gráfico de barras
0 = No sobrevivió
1 = Sobrevivió

---

## Pagina 47

Fases del análisis Exploratorio
Pregunta a responder1
Generalidades del dataset2
Tipos de datos3
Estadística descriptiva4
Visualización5
Interacciones6
Resumen7

---

## Pagina 48

Fases del análisis Exploratorio 
6 Análisis bivariado
Gráficos: CodificandoBits

---

## Pagina 49

Fases del análisis Exploratorio 
6 Análisis bivariado
Gráficos: CodificandoBits
Correlación lineal positiva
 Correlación lineal inversa
 No hay correlación lineal

---

## Pagina 50

Fases del análisis Exploratorio 
6 Análisis bivariado
Gráficos: CodificandoBits

---

## Pagina 51

Fases del análisis Exploratorio 
6 Análisis bivariado
Gráficos: CodificandoBits

---

## Pagina 52

Fases del análisis Exploratorio
Pregunta a responder1
Generalidades del dataset2
Tipos de datos3
Estadística descriptiva4
Visualización5
Interacciones6
Resumen7

---

## Pagina 53

s torageAthena
Permite hacer consultas sobre los 
datos
Servicios de AWS para análisis exploratorio
s torageQuickSight
Permite hacer gráficos y tableros 
visuales 
s torageSageMaker AI
Espacio para explorar datos
s torageGlue
Cataloga, observa los datos, y 
expone nulos, outliers, entre otros

---

## Pagina 54

Resumen
Clase 2

---

## Pagina 55

Resumen de hoy
Almacenamiento
- Propiedades de los datos
- Servicios de AWS
Ingesta
- Tipos de ingesta
- Servicios de AWS
Análisis 
Exploratorio
- Fases del análisis 
exploratorio
- Outliers, datos faltantes y 
duplicados
- Tipos de datos
- Estadística descriptiva
- Visualización
- Interacciones

---

## Pagina 56

¡Gracias!
