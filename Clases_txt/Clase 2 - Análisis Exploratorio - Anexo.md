# Clase 2 - Análisis Exploratorio - Anexo

## Pagina 1

Machine Learning

---

## Pagina 2

CLASE 2
Análisis Exploratorio
Anexo

---

## Pagina 3

Amazon 
S3

---

## Pagina 4

Amazon S3
Amazon S3 es un servicio de AWS que permite almacenar objetos dentro de contenedores llamados buckets
● El nombre del bucket debe ser único en todo el mundo, aplicándose de forma global a través de todas 
las regiones de AWS y cuentas de usuario.

---

## Pagina 5

Amazon S3 | Objetos
Los objetos de S3 son archivos identificados por una Key que representa su ruta completa:
s3://my-bucket/my-folder/another-folder/my-file.txt
prefijo object name

---

## Pagina 6

Amazon S3 | Seguridad
La seguridad en Amazon S3 se gestiona principalmente a través de tres mecanismos complementarios de 
control de acceso y protección de datos.
● User-Based Policies: Se adjuntan directamente a los usuarios, grupos o roles de IAM. Especifican qué 
buckets, objetos y acciones tiene permitido realizar cada usuario.
● Resource-Based Policies: Se configuran en el propio recurso, conocidas como Bucket Policies. Definen 
qué cuentas o usuarios tienen autorización para acceder al bucket.
● Encriptación: Protege los datos en reposo y tránsito mediante claves de S3, KMS o del cliente. 
Garantiza que la información confidencial permanezca segura y privada.

---

## Pagina 7

Amazon S3 | Seguridad
Las políticas de S3 se definen en formato JSON y contienen los siguientes elementos fundamentales:
● Principal: Define a qué usuario, cuenta o entidad se le aplica la política (ej. "*" para todos).
● Effect: Especifica si la política va a permitir (Allow) o denegar (Deny) de forma explícita.
● Actions: Conjunto de operaciones de la API de S3 sobre las que se aplicará la regla (ej. s3:GetObject).
● Resources: Identifica los buckets y objetos específicos de S3 mediante su ARN único.

---

## Pagina 8

Amazon S3 | Seguridad
{ 
     "Version": "2012-10-17", 
     "Statement": [ 
          { 
               "Sid": "PublicRead", 
               "Effect": "Allow", 
               "Principal": "*", 
               "Action": [ "s3:GetObject" ], 
               "Resource": [ "s3://examplebucket/*" ] 
          } 
     ] 
}

---

## Pagina 9

S3 Versioning
El versionado en Amazon S3 permite mantener múltiples variantes de un objeto en el mismo bucket, ofreciendo 
una capa esencial de protección y recuperación de datos.

---

## Pagina 10

S3 Replication
La replicación en S3 es asincrónica y requiere obligatoriamente tener el versionado habilitado tanto en el 
bucket de origen como en el de destino, respaldado por los permisos IAM adecuados.
Tipos de replicación
● CRR (Cross-Region): Replicación entre regiones para lograr baja latencia y compliance.
● SRR (Same-Region): Replicación en la misma región, ideal entre producción y test

---

## Pagina 11

Storage Classes disponibles
● Standard - General Purpose
● Standard - Infrequent Access (IA)
● One Zone - Infrequent Access
● Glacier Instant Retrieval
● Glacier Flexible Retrieval
● Glacier Deep Archive
● Intelligent - Tiering
99.999999999%
Durabilidad (11 nueves). Al guardar 10M de objetos, 
se esperaría perder solo 1 cada 10.000 años.
99.99%
Disponibilidad en S3 Standard. Equivale a un máximo 
de 53 minutos de inactividad por año.
S3 Storage Classes

---

## Pagina 12

Es un data center aislado dentro de una 
región.
Availability Zone (AZ)

---

## Pagina 13

Región: sa-east-1
Zonas de disponibilidad (AZ): sa-east-1a, sa-east-1b, sa-east-1c
Availability Zone (AZ)

---

## Pagina 14

99.99% de disponibilidad. Se replica en 3 AZ
Se usa para data accedida frecuentemente
Casos de uso: Big Data Analytics, Gaming Apps, Distribución de contenido
S3 Standard - General Purpose

---

## Pagina 15

99.9% de disponibilidad. Se replica en 3 AZ
Para data menos frecuente, pero que requiere rápido acceso cuando se necesite
Casos de uso: Disaster Recovery, Backups
S3 Standard - Infrequent Access

---

## Pagina 16

Glacier Instant Retrieval: data raramente accedida, recuperación instantánea
Glacier Flexible Retrieval: data accedida 1-2 veces/año, recuperación en minutos
Glacier Deep Archive: data casi nunca accedida, retención regulatoria
S3 Glacier

---

## Pagina 17

99.5% de disponibilidad. Solo vive en una AZ
La data se pierde si la AZ se destruye
Casos de uso: Backups secundarios, data que se puede recrear
S3 One Zone - Infrequent Access

---

## Pagina 18

Mueve objetos automáticamente entre Storage Classes basado en el uso
S3 Intelligent Tiering

---

## Pagina 19

Uno define la transición entre Storage Classes basado en un período de tiempo
S3 Lifecycle Rules

---

## Pagina 20

S3 Event Notifications
S3 Event Notification: es una función de Amazon S3 que permite generar y enviar automáticamente notificaciones 
cuando ocurren determinados eventos en un bucket, como la creación, eliminación o modificación de objetos.
● Eventos Soportados: Soportado para mutaciones de objetos como s3:ObjectCreated, s3:ObjectRemoved, y 
s3:Replication.
● Performance & Filtros: Las notificaciones típicamente se lanzan en segundos, aunque a veces pueden tardar 
más. Se pueden limitar usando filtros por prefijos.
● Seguridad & IAM: Requiere configurar la política de recursos destino con permisos para que S3 invoque la 
acción de envío (ej. SendMessage).

---

## Pagina 21

Amazon
S3
SNS Topic
 Email, SMS, HTTP 
Endpoints
SQS Queue
 Cola leída por 
servidores / EC2
AWS Lambda
 Ejecución directa de 
scripts / código
EventBridge
 Enrutamiento masivo 
por reglas de AWS
Arquitectura de Notificaciones

---

## Pagina 22

S3 Optimization Performance
S3 escala de forma transparente el rendimiento de solicitudes sin necesidad de intervención manual o 
aprovisionamiento.
3,500 
POST / PUT / DELETE
por segundo
5,500 
GET / HEAD
por segundo

---

## Pagina 23

S3 Optimization Performance
Multipart Uploads: permite que la información se divida y se suba en paralelo
● Es obligatorio para archivos > 5 GB y altamente recomendado para archivos mayores a 100 MB. Permite la 
paralelización y mejora la tolerancia a fallos de red.
● Si una falla, solo se reintenta esa parte. Al completarse, S3 las une de forma transparente.
Archivo 
Grande
Parte 1
Parte 2
Parte 3
S3 Bucket

---

## Pagina 24

S3 Encryption
S3 Encryption: es el conjunto de mecanismos de Amazon S3 para cifrar los datos
Datos
(Sin Cifrar)
Llave KMS/S3
S3 Bucket
(Guardado Cifrado)

---

## Pagina 25

S3 Encryption | Server Side
SSE-S3: Con llaves manejadas por Amazon S3: Default para nuevos buckets. La encriptación y desencriptación 
ocurre de manera transparente utilizando llaves de encriptación que son administradas y protegidas al 100% por 
AWS.
SSE-KMS: Con llaves guardadas en AWS KMS: Usa llaves administradas mediante el AWS Key Management 
Service. Permite políticas de uso de llaves, rotación y un trail de auditoría completo de quién y cuándo usó la llave.
SSE-C: Con llaves provistas por el Cliente: El usuario administra y provee sus propias llaves criptográficas fuera de 
AWS. El cliente envía la llave en cada request; S3 encripta/desencripta en memoria y no guarda la llave.

---

## Pagina 26

S3 Encryption | Client Side
Los clientes deben encriptar la data localmente antes de realizar la subida a S3, y desencriptarla ellos mismos luego 
de descargarla.
● AWS no tiene visibilidad ni acceso a las llaves o a la data sin encriptar.

---

## Pagina 27

S3 Storage Lens
S3 Storage Lens: es un servicio diseñado para entender, analizar y optimizar el almacenamiento en toda la 
organización de AWS.
● Visibilidad Global: Agrega datos para toda la organización, cuentas específicas, regiones y buckets.
● Insights Accionables: Descubre anomalías, identifica eficiencias de costo y aplica protección de datos.
● Exportación Diaria: Configurable para exportar métricas diariamente a un bucket de S3 para análisis 
personalizado.

---

## Pagina 28

S3 Storage Lens
Categorías Clave
● Summary & Activity: Bytes de almacenamiento, cantidad de objetos y cómo se solicita la data (Get/Put).
● Cost Optimization: Identifica buckets con multipart uploads incompletos y sugiere clases de menor costo.
● Data Protection & Security: Estado de Versioning, encriptación SSE-KMS

---

## Pagina 29

Amazon
Elastic Compute Cloud

---

## Pagina 30

Amazon EC2: es un servicio que provee servidores virtuales que pueden usarse para correr aplicaciones sin manejar 
hardware físico. Tienen su propio almacenamiento efímero llamado Instance Store.
Familias de instancias: 
● General Purpose (T, M)
● Compute Optimized (C)
● Memory Optimized (R, X)
Ciclo de vida de una instancia EC2
Amazon EC2
Pending Running Stopping Stopped Terminated

---

## Pagina 31

Amazon
Elastic Block Store

---

## Pagina 32

Amazon EBS:  es un servicio de almacenamiento que se conecta a una instancia EC2.  Permite que las instancias 
persistan datos, incluso después de su terminación
● Sólo puede montarse en una instancia EC2 a la vez
● Se puede desacoplar de una instancia EC2 y adjuntar a otra
● Los volúmenes de EBS tienen una capacidad provisionada
EBS
10GB
EBS
100GB
EBS
50GB
EBS
10GB
(Unattached)
Amazon EBS

---

## Pagina 33

Cuando se lanza una instancia EC2, por defecto tiene un volumen EBS llamado 
root volume
● Contiene el sistema operativo y es requerido para bootear la instancia
● Delete on termination: al terminar la instancia, el root volume se borra (se puede deshabilitar)
Amazon EBS

---

## Pagina 34

Amazon
Elastic File System

---

## Pagina 35

Amazon EFS: es un servicio de almacenamiento que se puede conectar a múltiples instancias EC2. Permite que 
múltiples instancias EC2 accedan y persistan datos compartidos al mismo tiempo
● Es análogo a una carpeta compartida en red
● La capacidad de EFS escala automáticamente, no se provisiona de antemano
EFS
10GB en uso
EFS
5GB en uso
Amazon EFS

---

## Pagina 36

Amazon EBS Amazon EFS Amazon S3
Tipo de storage Block storage File storage Object storage
Se monta en 1 instancia EC2 a la vez Múltiples instancias EC2 en simultáneo No se "monta"; se accede vía API/HTTP
Escalabilidad Capacidad provisionada manualmente Escala automáticamente según uso Prácticamente ilimitada
Persistencia Sobrevive a la instancia (salvo delete on 
termination)
Independiente del ciclo de vida de 
cualquier instancia Independiente, con versionado opcional
EBS vs. EFS vs. S3

---

## Pagina 37

Amazon
FSx

---

## Pagina 38

Amazon FSx
Amazon FSx es un servicio de sistema de archivos que acelera los trabajos de entrenamiento brindando sus datos de 
S3 a Amazon SageMaker a altas velocidades
● La primera vez que se ejecute un trabajo de entrenamiento, FSx copiará automáticamente los datos de S3 y los 
pondrá a disposición de SageMaker
● Evita descargas repetidas de objetos S3

---

## Pagina 39

Bases de 
Datos

---

## Pagina 40

La información se organiza en tablas estructuradas con filas y columnas.
Componentes:
● Tablas (Entidades): Clientes, Órdenes, Productos.
● Filas (Registros): Cada registro es una instancia única.
● Columnas (Atributos): Campos con tipos de datos definidos.
Ejemplos en AWS
RDS Aurora
¿Qué es una base de datos relacional?

---

## Pagina 41

La información se almacena sin una estructura rígida, permitiendo esquemas dinámicos.
Tipos
● Documentales: Documentos autodescriptivos como JSON (MongoDB).
● Clave-Valor: Diccionarios simples de altísima velocidad (Redis).
● Grafos: Nodos y relaciones para redes complejas (Neo4j).
Ejemplos en AWS
DynamoDB DocumentDB
 Neptune
 Keyspaces
 ElastiCache
 MemoryDB
 Timestream
¿Qué es una base de datos no relacional?

---

## Pagina 42

Elastic Load
Balancer
EC2 
Instance
EC2 
Instance
Amazon 
RDS
Auto Scaling Group
Application Layer Database Layer
Clients
Arquitectura tradicional

---

## Pagina 43

Elastic Load
Balancer
EC2 
Instance
EC2 
Instance
Amazon 
RDS
Auto Scaling Group
Application Layer Database Layer
Clients
Se basa en bases de datos relacionales
● El Load Balancer distribuye el tráfico entre diferentes servidores
● Los grupos de Auto Scaling ajustan el número de instancias EC2 basado en la demanda
○ Escalamiento vertical: obtener más poder de CPU/RAM
○ Escalamiento horizontal: agregar más instancias
Arquitectura tradicional

---

## Pagina 44

Bases de 
Datos
DynamoDB

---

## Pagina 45

Amazon DynamoDB: es una base de datos NO-SQL administrada por AWS
● Cuenta con alta disponibilidad y replicación entre múltiples AZ
● Soporta millones de requests por segundo, trillones de registros y 100s TB de almacenamiento
● Integrado con IAM para seguridad, autorización y administración
Casos de uso: Apps Móviles, Gaming, Ecommerce, Ads
Anti Patrón: bases de datos relacionales tradicionales, JOINs o transacciones complejas
Amazon DynamoDB

---

## Pagina 46

Server 1
Replicación
Aplicación
Server 3
Server 2
Write
Read
Replicación

---

## Pagina 47

Aplicación
Write
FUNCIÓN HASH
PARTICIÓN 1 PARTICIÓN 2
Colección
Id13
id45
Id13 Id45
Particionamiento

---

## Pagina 48

DynamoDB Stream: un log de cada modificación a nivel ítem que ocurre en una tabla (create, update, delete)
● Es un "changelog" en tiempo real de la tabla
● Retención: los registros quedan disponibles por 24 horas (después se pierden si nadie los consumió)
Tipos de vista configurable
● KEYS_ONLY: solo las keys del ítem modificado
● NEW_IMAGE: el ítem completo, como quedó después del cambio
● OLD_IMAGE: el ítem completo, como estaba antes del cambio
● NEW_AND_OLD_IMAGES: ambas versiones, útil para comparar qué cambió
DynamoDB Stream

---

## Pagina 49

Write
Application
 Table
 DynamoDB
Streams
Kinesis Data
Streams
Kinesis Data 
Firehose
Redshift
S3
OpenSearch
Processing Layer
SNS
DynamoDB
Table
DynamoDB Stream

---

## Pagina 50

Time To Live (TTL): automáticamente elimina ítems luego de un timestamp de expiración
● No consume ningún WCU
● Los ítems expirados son eliminados un par de días después de que expiran
Time To Live (TTL)

---

## Pagina 51

1234.png
Application
upload
S3
 Application
1234.png
download
Store
Metadata
product_id product_name image_url
Get
Metadata
Products Table
Patrones con S3

---

## Pagina 52

Bases de 
Datos
RDS

---

## Pagina 53

Amazon RDS: es un servicio administrado de AWS para desplegar, operar y escalar bases de datos relacionales
● Puede ser MySQL, PostgreSQL, MariaDB, SQL Server…
● Ofrece ACID
Propiedades ACID
● Atomicidad: la transacción es todo o nada, si falla una parte fallan todas.
● Consistencia: la base de datos pasa de un estado válido a otro estado válido
● Isolation: las transacciones concurrentes no se interfieren entre sí
● Durability: una vez confirmada la transacción, los datos no se pierden aunque el sistema falle
Amazon RDS

---

## Pagina 54

RDS Performance Insights: es un dashboard dentro de la consola de RDS que muestra en tiempo real qué está 
consumiendo recursos en tu base de datos. 
● La métrica principal es DB Load: cuántas queries están activas en cada moment
RDS Performance Insights

---

## Pagina 55

Aurora: es la base de datos relacional propia de AWS 
 Neptune: es una base de datos no relacional basada en grafos
Timestream: es una base de datos no relacional de series temporales 
DocumentDB: es una base de datos no relacional basada en MongoDB
Keyspaces: es una base de datos no relacional basada en Apache Cassandra
Otras bases de datos

---

## Pagina 56

OLTP
Online Transaction Processing
Optimizado para muchas transacciones pequeñas y rápidas en 
tiempo real (ej. registrar un pago, crear un usuario).
Características claves
● Muchas escrituras y lecturas rápidas
● Latencia extremadamente baja (milisegundos)
● Datos actualizados rigurosamente en tiempo real
● Soporte para gran volumen de usuarios concurrentes
Servicios en AWS
RDS Aurora DynamoDB
OLAP
Online Analytical Processing
Optimizado para pocas consultas complejas sobre grandes 
volúmenes de datos históricos (ej. análisis de ventas anuales).
Características claves
● Pocas escrituras masivas, predominio de lecturas
● Queries complejas que escanean millones de filas
● Enfoque en datos históricos agregados
● Diseñado para analistas y pocos usuarios concurrentes
Servicios en AWS
Redshift Athena
OLAP vs. OLTP

---

## Pagina 57

Amazon
Kinesis

---

## Pagina 58

INGESTA
Kinesis Data
 Streams
Captura de eventos en tiempo 
real con múltiples aplicaciones 
consumidoras en paralelo.
ENTREGA
Kinesis Data 
Firehose
Entrega streaming totalmente 
administrada hacia S3, Redshift, 
OpenSearch, sin escribir código.
ANÁLISIS
Amazon 
Managed 
Service for 
Apache Flink
Procesa y analiza streams con 
SQL o Apache Flink: 
agregaciones, ventanas de 
tiempo, detección de anomalías.
La familia Kinesis

---

## Pagina 59

Amazon
Kinesis
Kinesis Data Streams

---

## Pagina 60

Kinesis Data Streams: es un servicio totalmente administrado de AWS para capturar, procesar y 
almacenar grandes flujos de datos en tiempo real de forma continua, permitiendo que múltiples 
consumidores los lean y procesen casi instantáneamente.
Los datos se organizan en shards
● La data es partida entre los shards en base a una clave primaria
● Los shards definen la capacidad del stream en términos de ingesta y consumo
● Productores: envían datos 
● Consumidores: reciben los datos
Kinesis Data Streams
Shard 1
Shard 2
Shard 3
Productores Consumidores

---

## Pagina 61

Propiedades
● Cada shard soporta 1 MB/s de escritura y 2 MB/s de lectura
● La retención puede ser entre 1 y 365 días
● Una vez que la data es insertada en Kinesis, no puede ser borrada (inmutabilidad)
Modos de capacidad
● Provisioned: se elige la cantidad de shards de antemano 
● On-demand: escala automáticamente la cantidad de shard basado en lo observado
Kinesis Data Streams

---

## Pagina 62

On-Demand Provisioned
Escalado Automático según uso Manual: uno elige la cantidad de shards
Costo Se paga por volumen de datos Se paga por hora, por shard aprovisionado
Ideal para Cargas impredecibles o nuevas Cargas estables y predecibles
Kinesis Data Streams: Modos de capacidad

---

## Pagina 63

Kinesis Producer Library: Es una librería que corre del lado del cliente. Provee las APIs PutRecord y 
PutRecords
Kinesis Producer Library (KPL)
2 KB 40 KB 500 KB
Agregar en un registro < 1 MB
PutRecords

---

## Pagina 64

Kinesis Consumer Library: es una librería que abstrae la complejidad de leer datos de un Kinesis Data 
Stream. Se usan las APIs GetRecords
● Se puede tener 2 MB/s en lectura en total del mismo shard entre todos los consumidores
● Kinesis Enhanced Fanout: se utiliza para que cada consumidor obtenga 2 MB/s propios del 
mismo shard
Kinesis Consumer Library (KCL)

---

## Pagina 65

Los reintentos de los productores pueden crear duplicados debido a timeouts de conexión
● Fix: embeber un ID único a cada registro para deduplicar del lado del consumidor
Manejo de duplicados para productores
1. PutRecord [DATA]
Seq #123
[DATA]
2. Nunca llega el ACK
3. Retry PutRecord [DATA]
4. ACK
Seq #124
[DATA]
KDSPRODUCER

---

## Pagina 66

Amazon
Kinesis
Kinesis Data Firehose

---

## Pagina 67

Kinesis Data Firehose: es un servicio near real-time administrado que permite:
● Redirigir la data a Redshift, Amazon S3, entre otros
● Convertir data de JSON a Parquet
● Transformar datos en tránsito usando una Lambda Function
● Acumular los datos en un buffer, el cual es limpiado basado en un tiempo o reglas de tamaño
Kinesis Data Firehose
Aplicación

---

## Pagina 68

Data Streams Data Firehose
Gestión Uno gestiona shards y consumidores Totalmente administrado
Latencia Tiempo real (~200ms) Near real-time (segundos)
Consumidores Múltiples, en paralelo Un único destino por stream
Almacena datos Sí, hasta 365 días No, solo entrega
ITBA
Kinesis Data Streams vs. Data Firehose

---

## Pagina 69

Amazon
Kinesis
Amazon Managed Service for Apache Flink

---

## Pagina 70

Amazon Managed Service for Apache Flink: (antes llamado Kinesis Data Analytics) es un servicio administrado 
de AWS para ejecutar aplicaciones de Apache Flink sin tener que aprovisionar ni gestionar la infraestructura 
subyacentes
● Permite hacer agregaciones sobre ventanas de tiempo (ej: promedio de los últimos 30 minutos)
● Mantiene estado entre eventos (recuerda datos anteriores para calcular sobre ellos) 
● Detecta anomalías en tiempo real (caídas, spikes, patrones inusuales) con latencia de milisegundos 
Amazon Managed Service for Apache Flink

---

## Pagina 71

Amazon
Managed Streaming for Apache Kafka

---

## Pagina 72

Managed Streaming for Apache Kafka:  es un servicio totalmente administrado de AWS que facilita la creación, 
operación y escalado de clústeres Apache Kafka para procesar flujos de datos en tiempo real 
● Los productores escriben en tópicos y los consumidores leen de él
● Es la alternativa a Kinesis Data Streams
Managed Streaming for Apache Kafka
Broker 1
Broker 2 Broker 3
Replicación
MSK Cluster
Productor Consumidor
Escribe al topic Lee del topic

---

## Pagina 73

Kinesis Data Streams Amazon MSK
Modelo Servicio propietario de AWS Apache Kafka open-source administrado
Unidad de escalado Shards Partitions / Brokers
Portabilidad Específico de AWS Migrable a cualquier Kafka
Ideal para Empezar rápido, nativo de AWS Ya se tiene Kafka o se necesita su ecosistema
Kinesis Data Streams vs. MSK

---

## Pagina 74

Amazon
Database Migration Service

---

## Pagina 75

Database Migration Service: es un servicio administrado de AWS que permite migrar o replicar bases de datos hacia 
AWS de forma continua
● Soporta migraciones homogéneas (ej: MySQL → MySQL)
● Soporta migraciones heterogéneas (ej: Oracle → Aurora), usando AWS Schema Convertion Tool (SCT)
● Puede hacer una carga completa (Full Load) de los datos existentes
● Puede hacer Change Data Capture (CDC): replica en tiempo casi real los cambios que van ocurriendo en el 
origen después de la carga inicial
Amazon DMS
AWS DMS
Base de 
datos DestinoReplication Instance
(On-premise / cloud)
MySQL, PostgreSQL, etc
RDS, Aurora, Redshift, S3

---

## Pagina 76

Amazon
Transfer Family

---

## Pagina 77

Database Migration Service: es un servicio totalmente administrado de AWS que permite transferir archivos hacia y 
desde AWS usando protocolos estándar de la industria, sin tener que mantener servidores propios. 
● Soporta los protocolos SFTP, FTPS y FTP
● Los archivos se depositan directamente en Amazon S3 o Amazon EFS, sin pasos intermedios
● Se usa cuando se tiene un partner o cliente externo que necesita subir/bajar archivos
Amazon Transfer Family
AWS Transfer Family
Cliente 
externo
Amazon S3 
(o EFS)SFTP/FTPS/FTP

---

## Pagina 78

Amazon
DataSync

---

## Pagina 79

Database Migration Service: es un servicio totalmente administrado de AWS que automatiza y acelera la transferencia 
de grandes volúmenes de datos entre distintos sistemas de almacenamiento, tanto on-premise como dentro de AWS.
● Mueve datos entre on-premise ↔ AWS o entre servicios de AWS entre sí 
● Usa un agente que se encarga de leer los datos y transferirlos de forma optimizada
AWS DataSync
AWS DataSync
Almacenamiento 
on-premise
Destino 
AWSAgente
NFS, SMB, HDFS S3, EFS, FSx

---

## Pagina 80

Amazon DMS Amazon Transfer Family AWS DataSync
Qué mueve Datos de bases de datos Archivos, vía protocolo estándar Archivos/objetos, a gran escala
Protocolo Replication instance (motor EC2) SFTP, FTPS, FTP, AS2 Agente instalado en el origen
Origen típico Base de datos relacional (on-premise o 
cloud)
Socio externo / cliente que sube un 
archivo
NAS/NFS/SMB on-premise, u otro 
storage de AWS
Destino típico RDS, Aurora, Redshift o S3 S3 o EFS S3, EFS o FSx
Patrón de uso Full load + CDC (cambios continuos) Puntual, por archivo, caso a caso Recurrente/programado, grandes 
volúmenes
DMS vs. Transfer Family vs. DataSync

---

## Pagina 81

AWS Snow Family: es un conjunto de dispositivos físicos administrados por AWS que permiten transferir grandes 
volúmenes de datos hacia (o desde) AWS cuando la transferencia por red no es práctica
● AWS envía el dispositivo, uno carga los datos localmente, y se devuelve para que los datos se carguen en S3
AWS Snow Family

---

## Pagina 82

Amazon
Athena

---

## Pagina 83

Amazon Athena: es un servicio serverless de AWS que permite consultar datos directamente en Amazon S3 usando 
SQL estándar, sin necesidad de cargarlos en una base de datos ni de gestionar infraestructura.
● Es la herramienta natural para la primera fase del análisis exploratorio
● Soporta múltiples formatos: CSV, JSON, Parquet, Avro, ORC
● El costo se calcula por cantidad de datos escaneados en cada consulta, no por tiempo de cómputo reservado
● Usar formato Parquet (columnar) en vez de CSV reduce drásticamente los datos escaneados por consulta, 
porque Athena puede leer solo las columnas que necesita
Amazon Athena

---

## Pagina 84

Amazon Athena

---

## Pagina 85

Amazon
QuickSight

---

## Pagina 86

Amazon QuickSight: es un servicio de Business Intelligence (BI) serverless de AWS que permite crear dashboards y 
visualizaciones interactivas para explorar y compartir datos, sin gestionar infraestructura.
● Se conecta directamente a fuentes como Athena, Redshift, RDS, S3, y también a archivos subidos manualmente 
(Excel, CSV)
● Está pensado para que el resultado del análisis se comparta con stakeholders no técnicos en un dashboard 
interactivo
Modos de conexión
● Direct Query mode: Cada vez que un usuario abre el dashboard, QuickSight ejecutar una query en vivo contra la 
fuente de datos. El problema es que Athena cobra por datos escaneados.
● SPICE: Los datos se importan a la memoria de QuickSight una vez. Todos los usuarios consultan esa copia en 
memoria, no la fuente original. El trade-off es que los datos no son en tiempo real.
Amazon QuickSight

---

## Pagina 87

Amazon QuickSight

---

## Pagina 88

AWS
Glue

---

## Pagina 89

AWS Glue es el servicio servicio de integración de datos serverless de AWS
● Permite descubrir, preparar, mover y combinar datos de múltiples fuentes de forma automática
● Es serverless: no hay que aprovisionar ni administrar infraestructura (AWS gestiona los recursos de cómputo)
● Basado en Apache Spark por debajo (para los jobs de ETL)
● Se paga por uso (por tiempo de cómputo consumido, no por servidores encendidos)
AWS Glue

---

## Pagina 90

¡Gracias!
