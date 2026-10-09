# Clase 8 - Generative AI

## Pagina 1

Machine Learning

---

## Pagina 2

CLASE 7
Procesamiento de lenguaje natural
Repaso

---

## Pagina 3

Procesamiento de lenguaje natural
El Procesamiento del Lenguaje Natural (NLP) es el campo de la inteligencia artificial cuyo objetivo es 
permitir que las computadoras comprendan, procesen y generen el lenguaje humano.

---

## Pagina 4

Large Language Models
Un Large Language Model (LLM) es un tipo de Foundation Model especializado en procesar, comprender y 
generar texto en lenguaje natural.
● Se entrenan procesando texto masivo proveniente de libros, artículos, sitios web, repositorios
● Usan arquitecturas de redes neuronales profundas 
● Es un sistema de predicción probabilística de lenguaje: predice cuál es la palabra o token más probable 
que debe seguir a un texto determinado

---

## Pagina 5

f(x) = y
[.447,  1.2344,  .3345,  −.3590,  −.10]
embedding del texto
[−.587,  1.976,  −.758,  −.145,  −.98]
Embedding de salida
“Voy a guardar el queso en el” refrigerador
Funcionamiento de los LLMs
● Cada palabra se convierte en un vector de números para que una red neuronal la pueda procesar
● El modelo es f(x): recibe ese vector y devuelve la próxima palabra

---

## Pagina 6

La tokenización es el proceso de dividir un texto en unidades más pequeñas (tokens) que puedan ser 
procesadas por el modelo
La tokenización puede ser:
● Nivel palabra [Nice, day, my, friend]
● Nivel caracter [N, i, c, e, d, a, y, m, y, f, r, i, e, n, d]
● Nivel subpalabra [Nic, e, d, ay, my, fri, end]
Tokenización

---

## Pagina 7

El Supervised Fine-Tuning (SFT)  es el paso donde se le enseña a un modelo pre-entrenado, que solo sabe 
completar texto, a seguir instrucciones. 
● Se lo reentrena con pares de (instrucción, respuesta correcta) escritos por humanos
Sin SFT:
● Input: "¿Cuál es la capital de Francia?"
● Salida: "¿Cuál es la capital Francia? ¿Y la de España?"
Con SFT:
● Instrucción: "¿Cuál es la capital de Francia?"
● Respuesta deseada: "La capital de Francia es Paris.”
Supervised Fine Tuning

---

## Pagina 8

El Reinforcement Learning from Human Feedback (RLHF)  es el paso que alinea las respuestas con 
preferencias humanas utilizando comparaciones, las cuales son más escalables y capturan aspectos sutiles 
como el tono, la claridad y la seguridad
● Después del SFT, el modelo no puede seguir instrucciones pero no puede clasificar cuál respuesta válida 
es mejor.
Reinforcement Learning from Human Feedback

---

## Pagina 9

CLASE 8
Generative AI

---

## Pagina 10

El machine learning (aprendizaje automático) es un subconjunto de la inteligencia artificial (IA)
● El aprendizaje profundo es un subdominio del aprendizaje automático
Machine Learning != Inteligencia Artificial
Inteligencia Artificial (IA)
Aprendizaje Automático (ML)
Aprendizaje Profundo (DL)
Aprendizaje Automático (ML)
Aprendizaje Profundo (DL)
Inteligencia Artificial (IA)

---

## Pagina 11

Deep
Learning

---

## Pagina 12

Deep Learning
Deep Learning es una forma de aprendizaje automático donde una máquina intenta imitar al cerebro humano 
utilizando redes neuronales artificiales, que le permiten hacer predicciones con una gran precisión

---

## Pagina 13

Redes Neuronales
Una redes neuronal consta de 5 componentes principales
● Las entradas (x)
● Los pesos (w)
● Un sesgo (b)
● Una función de activación (f)
● Una salida (y)
Σ
x1
x2
y
w1 
w2 
x1w1 + x2w2 + b
f

---

## Pagina 14

Redes Neuronales | Ejemplo
Supongamos que queremos entrenar a una neurona para que decida si voy a un concierto (y).
● Las entradas (x)
○ x1: precio del ticket (del 1 al 10, donde 10 es muy caro). Supongamos x1 = 8
○ x2: qué tanto me gusta la banda (del 1 al 10). Supongamos x2 = 9
● Los pesos (w)
○ w1 = -1 (el precio influye de forma negativa, a mayor precio, menos ganas de ir)
○ w2 = 2 (que me guste la banda influye de forma positiva y con doble peso)
● Un sesgo (b)
○ b = -2 (un sesgo general negativo, me da pereza salir de casa)

---

## Pagina 15

Redes Neuronales | Ejemplo
Supongamos que queremos entrenar a una neurona para que decida si voy a un concierto (y).
Σ
8
8 
-1 
2 
8*-1 + 9*2 - 2 = 8
9
1
función de 
activación
¡Voy!

---

## Pagina 16

Redes Neuronales

---

## Pagina 17

Generative
AI

---

## Pagina 18

El Generative AI es un subset de Deep Learning
● Usa técnicas de como redes neuronales
Generative AI
Inteligencia Artificial (IA)
Aprendizaje Automático (ML)
Aprendizaje Profundo (DL)
Inteligencia Artificial Generativa

---

## Pagina 19

Generative AI
Generative AI es un tipo de inteligencia artificial que puede crear contenido
● Puede generar imágenes, videos, música, entre otros
● Lo hace con modelos preentrenados, llamados foundation models
● Los resultados pueden ser editados

---

## Pagina 20

Foundation Models
Un foundation model es un modelo de Inteligencia Artificial de gran escala (como GPT-4) que ha sido 
preentrenado con cantidades masivas de datos no etiquetados (texto, imágenes, audio, código) usando 
aprendizaje autosupervisado.
● Se le llama "fundacional" porque actúa como una base flexible y versátil: en lugar de resolver un solo 
problema específico, se puede adaptar a múltiples tareas (redactar correos, programar, analizar imágenes, 
resumir documentos, responder preguntas) simplemente a través de instrucciones
● Los Large Language Models (LLMs) son un tipo de foundation model

---

## Pagina 21

Modelos fundacionales vs. tradicionales

---

## Pagina 22

Prompt
Engineering

---

## Pagina 23

Prompt Engineering
El Prompt Engineering es el proceso de diseñar, estructurar y optimizar las instrucciones de texto (prompts) 
que se envían a los modelos de inteligencia artificial generativa para generar los resultados deseados
Estructura de un prompt
● Instrucción: Instrucciones: resumir la siguiente reseña de restaurant
● Contexto: Restaurant: Luigi’s; Ubicación: Nápoles, Italia; Especialidad: Pasta
● Input: Review: Pedimos los tagliatelle y la mozzarella caprese. Los tagliatelle eran una obra de arte: la 
pasta estaba justo en su punto y la salsa de tomate con albahaca fresca estaba perfecta. La caprese 
estaba bien, pero nada fuera de lo común. El servicio fue lento al principio, pero en general estuvo bien. 
Aparte de eso, ¡Luigi's fue una gran experiencia!
Salida: Luigi’s es un gran restaurant italiano con pasta deliciosa y buen servicio.

---

## Pagina 24

Técnicas de Prompt Engineering
● Zero-Shot
● Few-Shot
● Chain-of-thought

---

## Pagina 25

Técnicas de Prompt Engineering
Zero-Shot: se le pide al modelo que resuelva la tarea sin darle ningún ejemplo previo — confía pura y 
exclusivamente en lo que aprendió durante su entrenamiento.
Clasificá esta reseña como positiva o negativa: La comida estaba fria y el servicio era lento

---

## Pagina 26

Técnicas de Prompt Engineering
Few-Shot: se le da al modelo unos ejemplos de lo que queremos, entre 1 y 3, para ayudar a producir mejores 
resultados
Clasificá el sentimiento
Review: "Increíble servicio y comida" → Positivo
Review: "Las porciones eran muy chicas" → Negativo
Review: "La comida estaba fria y el servicio lento" →

---

## Pagina 27

Técnicas de Prompt Engineering
Chain-of-Though (CoT): queremos que el modelo razone paso a paso y que piense lógicamente antes de 
responder
Un local vende lapices a $2 cada uno. Si comprás 3 lápices y pagás con un billete de $10, 
¿cuánto vuelto debo darle?
Sin CoT: puede responder $4
Con CoT
3 lápices x $2 = $6
Pagó $10 → cambio = $4

---

## Pagina 28

Optimización de Prompts
La optimización de prompts es el proceso de iterativamente mejorar las prompts para obtener mejores 
resultados
● Usar instrucciones de rol claras: "Sos un asistente legal"
● Ser explícito: "Responder en formato JSON"
● Añadir límites: "Acortar a 100 palabras"

---

## Pagina 29

Agentes

---

## Pagina 30

Agentes
Un agente es un software que usa un LLM para aprovechar su inteligencia y ejecutar acciones
● Dentro del software hay indicaciones claras sobre cómo conectarse a herramientas, hacer las tareas, 
manejar el contexto, entre otros
● A diferencia de un ChatBot que es reactivo, el agente es autónomo
Ejemplos
● "Agendame un restaurant para mañana a las 3 de la tarde"
● "Entender el proyecto, generar código y subirlo a Github" (Claude Code)
● "Buscar propiedades una vez por día y mandarlas a mi Whatsapp"

---

## Pagina 31

Agentes | Ejemplo
Gráfico: Platzi

---

## Pagina 32

Agentes
Gráfico: EdTeam

---

## Pagina 33

Agentes
Agente Herramientas
LLM
Redactar correos Analizar datos Crear reportes
Skills

---

## Pagina 34

OpenClaw

---

## Pagina 35

Servicios
AWS

---

## Pagina 36

s torageAmazon BedRock
Acceso a Foundation Models de 
múltiples proveedores (Antropic, 
Meta, Amazon) sin gestionar 
infraestructura
Servicios de AWS
s torageAmazon Titan
La familia propia de Foundation 
Models de AWS
s torageAmazon BedRock 
Knowledge Bases
Se conecta a documentos (desde 
S3) para que un modelo responda 
con información específica
s torageAmazon BedRock 
Agents
Se definen las herramientas 
disponibles y AWS orquesta el 
razonamiento y la ejecución
s torageAmazon Q
Asistente que responde preguntas 
en lenguaje natural. Tiene su 
versión Business y Developer.
s torageAmazon 
SageMaker
JumpStart
Ofrece catálogos de Foundation 
Models propios y de terceros. Uno 
puede elegir la infraestructura

---

## Pagina 37

Repaso
Final

---

## Pagina 38

Clase 1: ¿Qué es machine learning?, proceso de machine learning, desafiíos del machine learning
Clase 2: Almacenamiento, ingesta y análisis exploratorio
Clase 3: Data Wrangling, tratamiento de datos faltantes, duplicados, outliers y feature engineering
Clase 4: Algoritmos de regresión, clasificación, clusterización y ensamble
Clase 5: Métricas de regresión, clasificación, cross-validation y tuneo de hiperparámetros
Clase 6: MLOps, deuda técnica oculta, ciclo de vida de los modelos, despliegue, monitoreo y mantenimiento, niveles de automatización
Clase 7: Procesamiento de lenguaje natural, LLMs, modelos autorregresivos, tokenización, atención, SFT, RLHF
Clase 8: Deep learning, generative AI, prompt engineering, agentes

---

## Pagina 39

¡Gracias!
