# Clase 3 - Procesamiento de datos - Anexo

## Pagina 1

Machine Learning

---

## Pagina 2

CLASE 3
Procesamiento de datos
Anexo

---

## Pagina 3

Proceso
ETL

---

## Pagina 4

¿Qué es un proceso ETL?
PASO 1
Extract →
PASO 2
Transform →
PASO 3
Load

---

## Pagina 5

¿Qué es un proceso ETL? | Ejemplo
PASO 1
Conectar MongoDB e 
ingestar documentos →
PASO 2
Limpiar campos y filtrar 
registros →
PASO 3
Insertar en PostgreSQL y 
confirmar escrituras

---

## Pagina 6

Las desventajas del proceso ETL son:
● El dato crudo se pierde
● Las transformaciones quedan desperdigadas
● En caso de reprocesamiento, se sobrecarga la fuente
Problemas del ETL
PASO 1
Extract →
PASO 2
Transform →
PASO 3
Load

---

## Pagina 7

PASO 1
Extract →
PASO 2
Load →
PASO 3
Transform
¿Qué es un proceso ELT?
Los datos se transforman en el destino

---

## Pagina 8

Las características del proceso ELT son:
● El dato crudo siempre está disponible
● Tiene un mayor costo de almacenamiento
● Centraliza las transformaciones
Características del ELT
PASO 1
Extract →
PASO 2
Load →
PASO 3
Transform

---

## Pagina 9

Modelo 
Medallion

---

## Pagina 10

Se solicita un reporte de las
transacciones mensuales de los usuarios
¿Cómo aplicaríamos el modelo Medallion?
Ejemplo

---

## Pagina 11

raw_users 
raw_transactions 
id name name_2 email created_at
1 Juan Perez juan.p@gmail.com 2026-03-20
2 María Lopez maria.l@gmail.com 2024-12-11
3 Carlos M carlos.m@gmail.com 2022-01-01
3 Carlos Martinez carlos.m@gmail.com 2022-01-03
id user_id amount status created_at
1 1 10 APPROVED 2026-03-20
2 1 50 APPROVED 2026-03-21
3 2 100 APPROVED 2025-01-01
4 2 200 APPROVED 2025-02-01
5 3 5000 REJECTED 2022-10-31
Datos Crudos

---

## Pagina 12

id name name_2 email created_at
1 Juan Perez juan.p@gmail.com 2026-03-20
2 María Lopez maria.l@gmail.com 2024-12-11
3 Carlos M carlos.m@gmail.com 2022-01-01
3 Carlos Martinez carlos.m@gmail.com 2022-01-03
user_id ﬁrst_name last_name email user_created_at
1 Juan Perez juan.p@gmail.com 2026-03-20
2 María Lopez maria.l@gmail.com 2024-12-11
3 Carlos M carlos.m@gmail.com 2022-01-01
3 Carlos Martinez carlos.m@gmail.com 2022-01-03
raw_users stg_users 
Renombramiento de columnas
Ejemplo 1: stg_users

---

## Pagina 13

int_users 
user_id ﬁrst_name last_name email user_created_at
1 Juan Perez juan.p@gmail.com 2026-03-20
2 María Lopez maria.l@gmail.com 2024-12-11
3 Carlos Martinez carlos.m@gmail.com 2022-01-03
user_id ﬁrst_name last_name email user_created_at
1 Juan Perez juan.p@gmail.com 2026-03-20
2 María Lopez maria.l@gmail.com 2024-12-11
3 Carlos M carlos.m@gmail.com 2022-01-01
3 Carlos Martinez carlos.m@gmail.com 2022-01-03
stg_users 
Deduplicación por clave primaria
Ejemplo 2: int_users

---

## Pagina 14

stg_transactions raw_transactions 
Renombramiento de columnas
id user_id amount status created_at
1 1 10 APPROVED 2026-03-20
2 1 50 APPROVED 2026-03-21
3 2 100 APPROVED 2025-01-01
4 2 200 APPROVED 2025-02-01
5 4 5000 REJECTED 2022-10-31
txn_id user_id amount status txn_created_at
1 1 10 APPROVED 2026-03-20
2 1 50 APPROVED 2026-03-21
3 2 100 APPROVED 2025-01-01
4 2 200 APPROVED 2025-02-01
5 4 5000 REJECTED 2022-10-31
Ejemplo 3: stg_transactions

---

## Pagina 15

stg_transactions 
txn_id user_id amount status txn_created_at
1 1 10 APPROVED 2026-03-20
2 1 50 APPROVED 2026-03-21
3 2 100 APPROVED 2025-01-01
4 2 200 APPROVED 2025-02-01
5 4 5000 REJECTED 2022-10-31
txn_id user_id amount status txn_created_at
1 1 10 APPROVED 2026-03-20
2 1 50 APPROVED 2026-03-21
3 2 100 APPROVED 2025-01-01
4 2 200 APPROVED 2025-02-01
Filtro por transacciones aprobadas
int_transactions 
Ejemplo 4: int_transactions

---

## Pagina 16

int_users 
user_id ﬁrst_name period total_amount total_txns
1 Juan 2026-03 60 2
2 María 2025-01 100 1
2 Carlos 2025-02 200 1
user_id ﬁrst_name last_name email user_created_at
1 Juan Perez juan.p@gmail.com 2026-03-20
2 María Lopez maria.l@gmail.com 2024-12-11
4 Carlos Martinez carlos.m@gmail.com 2022-01-01
txn_id user_id amount status txn_created_at
1 1 10 APPROVED 2026-03-20
2 1 50 APPROVED 2026-03-21
3 2 100 APPROVED 2025-01-01
4 2 200 APPROVED 2025-02-01
int_transactions 
fct_monthly_transactions 
Ejemplo 5: fct_monthly_transactions

---

## Pagina 17

users_raw
transactions_raw
stg_users
fact_monthly_transactions
stg_transactions
int_users
int_transactions
source staging intermediate marts
Linaje de datos con Modelo Medallion

---

## Pagina 18

AWS
Glue

---

## Pagina 19

AWS Glue es el servicio servicio de integración de datos serverless de AWS
● Permite descubrir, preparar, mover y combinar datos de múltiples fuentes de forma automática
● Es serverless: no hay que aprovisionar ni administrar infraestructura (AWS gestiona los recursos de cómputo)
● Basado en Apache Spark por debajo (para los jobs de ETL)
● Se paga por uso (por tiempo de cómputo consumido, no por servidores encendidos)
AWS Glue

---

## Pagina 20

Data Catalog: es el repositorio central de metadatos de AWS Glue. 
● Funciona como un "diccionario" que guarda la definición de las tablas (schema, tipos de datos, ubicación, 
formato) sin mover ni duplicar los datos reales — los datos siguen en S3, RDS, etc
● El Data Catalog solo sabe dónde están y cómo están estructurados. Otros servicios como Athena, Redshift 
Spectrum o EMR lo consultan para saber cómo leer esos datos.
● Este catálogo no es exclusivo de Glue. Lo usan también Athena (para saber qué consultar), Redshift Spectrum 
(para consultar datos en S3 desde Redshift), y EMR (como si fuera Hive Metastore). Es el diccionario 
compartido entre todos los servicios de analytics de AWS
AWS Glue | Glue Data Catalog

---

## Pagina 21

Glue Crawler: escanea fuentes (S3, RDS, Redshift) para inferir schema y actualizar el Data Catalog automáticamente. 
● En vez de que el crawler escanee todo el bucket cada vez (lento y caro) se puede configurar qué S3 mande un 
evento a una cola SQS cada vez que llega un archivo nuevo, y el crawler usa esa cola para saber exactamente 
que cambió, asi solo procesa incremental, no todo de cero.
AWS Glue | Glue Crawler
Nuevo archivo 
llega a S3
Notificación
Evento encolado 
en SQS
Glue Crawler se 
entera del cambio
Glue Data Catalog 
es actualizado

---

## Pagina 22

Glue ETL Jobs: es el tipo de job "clásico" de AWS Glue, que ejecuta un script de Extract, Transform, Load (ETL) sobre 
un motor administrado por AWS
● Se le da un script (Python con PySpark, o Scala) que:
○ Define cómo extraer datos de una fuente (S3, RDS, JDBC, etc.), 
○ Define cómo transformarlos (limpiar, unir, filtrar, cambiar formato) 
○ Define cómo cargarlos en un destino (otro bucket de S3, un data warehouse, etc.),
● AWS se encarga de levantar los recursos de Spark necesarios (workers), ejecutar el job, y apagarlos al terminar 
— todo bajo el modelo serverless, pagando solo por el tiempo de cómputo (DPUs) que consumió el job.
AWS Glue | Glue ETL Jobs

---

## Pagina 23

Glue Job Bookmarks: es una funcionalidad de AWS Glue que le permite a un job de ETL recordar qué datos ya procesó 
en ejecuciones anteriores, para que en la siguiente corrida solo procese los datos nuevos o modificados, en vez de 
reprocesar todo el dataset desde cero cada vez.
AWS Glue | Glue Job Bookmarks

---

## Pagina 24

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window
# --- Setup estándar de un Glue Job --- 
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
AWS Glue | Glue ETL Jobs

---

## Pagina 25

# --- PASO 1: EXTRACT ---
# Lee raw_users desde el Data Catalog (la tabla ya fue descubierta por un Glue Crawler)
raw_users = glueContext.create_dynamic_frame.from_catalog(
    database="mi_database",
    table_name="raw_users"
).toDF()
# --- PASO 2: TRANSFORM ---
# Renombrar columnas 
transformed = raw_users \
    .withColumnRenamed("id", "user_id") \
    .withColumnRenamed("name", "first_name") \
    .withColumnRenamed("name_2", "last_name") \
    .withColumnRenamed("created_at", "user_created_at")
AWS Glue | Glue ETL Jobs

---

## Pagina 26

# Deduplicación por clave primaria: se queda con el registro más reciente por user_id
window_spec = Window.partitionBy("user_id").orderBy(col("user_created_at").desc())
stg_users = transformed \
    .withColumn("row_num", row_number().over(window_spec)) \
    .filter(col("row_num") == 1) \
    .drop("row_num")
# --- PASO 3: LOAD ---
# Escribe el resultado en S3, en formato Parquet, particionado
glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(stg_users, glueContext, "stg_users"),
    connection_type="s3",
    connection_options={"path": "s3://mi-bucket/staging/stg_users/"},
    format="parquet"
job.commit()
AWS Glue | Glue ETL Jobs

---

## Pagina 27

Glue Triggers: es el mecanismo de AWS Glue para orquestar y disparar la ejecución de jobs y crawlers 
automáticamente, sin que alguien tenga que arrancarlos a mano.
● Define cuándo y en qué orden se ejecutan los jobs/crawlers dentro de un pipeline
AWS Glue | Glue Triggers

---

## Pagina 28

Glue Workflows: es un diagrama visual en la consola de AWS que muestra el grafo completo del pipeline (qué corre 
primero, qué depende de qué)
● Funciona como contenedor que permite agrupar y visualizar todo un pipeline de Crawlers + Jobs + Triggers 
como una sola unidad
● Estado de ejecución unificado: se puede ver si el pipeline completo corrió bien, o en qué paso específico falló
AWS Glue | Glue Workflows

---

## Pagina 29

Glue DataBrew: es una herramienta visual de preparación de datos que permite limpiar y transformar datos sin escribir 
código, a través de una interfaz de apuntar y hacer clic.
● Ofrece más de 250 transformaciones predefinidas (manejo de nulos, outliers, normalización, encoding, filtrado, 
etc.)
● Cada conjunto de transformaciones aplicadas se guarda como una recipe (receta), reutilizable sobre nuevos 
datasets 
AWS Glue | Glue DataBrew

---

## Pagina 30

Amazon
Elastic Map Reduce

---

## Pagina 31

Amazon Elastic Map Reduce: un servicio totalmente administrado de AWS que permite ejecutar y escalar frameworks 
de procesamiento de big data como Apache Spark, Hadoop, Hive y Presto sobre clústeres de infraestructura 
administrados
Amazon EMR

---

## Pagina 32

Un cluster de EMR es una colección de instancias EC2 que corren Hadoop.
● Cada instancia se llama nodo. 
● Cada nodo tiene un rol en el cluster, según el tipo:
○ Master node: maneja el cluster y coordina la distribución de la data
○ Core node:  corre tareas y guarda data  en el HDFS (Hadoop Distributed File System)
○ Task node: solo corre tareas, pero no guarda data en HDFS
Si un task node se cae, no hay riesgo de perder información. Con core nodes si.
Amazon EMR Cluster

---

## Pagina 33

AWS
Lambda

---

## Pagina 34

AWS Lambda: es un servicio que permite ejecutar transformaciones livianas orientadas a eventos (ej. un archivo que 
llega a S3 dispara una función que lo limpia o convierte)
● Ideal para transformaciones puntuales o de bajo volumen dentro de un pipeline
● Se paga por invocación y tiempo de ejecución
AWS Lambda

---

## Pagina 35

Amazon
Athena

---

## Pagina 36

Amazon Athena: es un servicio que permite consultar y transformar datos directamente en S3 usando SQL estándar, 
sin mover ni cargar los datos a otro lugar
● Es serverless: no hay que aprovisionar ni administrar infraestructura
● Se paga por dato escaneado
Amazon Athena

---

## Pagina 37

Amazon
Redshift

---

## Pagina 38

Amazon Redshift: es un data warehouse administrado que permite transformar datos con SQL directamente sobre 
grandes volúmenes (enfoque ELT: cargar primero, transformar adentro)
● Optimizado para queries analíticas complejas sobre datos estructurados a gran escala
Amazon Redshift

---

## Pagina 39

¡Gracias!
