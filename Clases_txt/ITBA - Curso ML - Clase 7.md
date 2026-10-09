# ITBA - Curso ML - Clase 7

## Pagina 1

Date
29-09-2026
Introducción a LLMs
Agustin Gianolini

---

## Pagina 2

Modelos de lenguaje

---

## Pagina 3

Introducción
El Procesamiento del Lenguaje Natural (NLP) es el campo de la 
inteligencia artiﬁcial cuyo objetivo es permitir que las computadoras 
comprendan, procesen y generen el lenguaje humano.

---

## Pagina 4

Modelos de Lenguaje 
Un modelo de lenguaje asigna probabilidades a secuencias de palabras y 
predice la siguiente palabra.

---

## Pagina 5

Modelos de Lenguaje 
Venimos utilizando modelos de lenguaje hace mucho tiempo

---

## Pagina 6

¿Cómo funcionan los LLMs?

---

## Pagina 7

Funcionamiento LLMs
● Cada palabra se convierte en un vector de números para que una red 
neuronal la pueda procesar
● El modelo es f(x): recibe ese vector y devuelve la próxima palabra
f(x) = y
[.447,  1.2344,  .3345,  −.3590,  −.10]
embedding del texto
[−.587,  1.976,  −.758,  −.145,  −.98]
Embedding de salida
“Voy a guardar el queso en el” refrigerador

---

## Pagina 8

Modelos Autoregresivos

---

## Pagina 9

Modelos Autoregresivos
Voy a guardar el LLM
queso (0.42)
pan (0.25)
vino (0.12)
abrigo (0.08) 
…
Un modelo de lenguaje calcula la probabilidad de la siguiente palabra.

---

## Pagina 10

Modelos Autoregresivos
Voy a guardar el LLM queso

---

## Pagina 11

Modelos Autoregresivos
Voy a guardar el queso LLM en

---

## Pagina 12

Autoregressive Models
Voy a guardar el queso en LLM la

---

## Pagina 13

Autoregressive Models
Voy a guardar el queso en la LLM heladera

---

## Pagina 14

Autoregressive Models
Voy a guardar el queso en la heladera LLM para

---

## Pagina 15

Autoregressive Models
Voy a guardar el queso en la heladera para LLM conservarlo

---

## Pagina 16

Autoregressive Models
Voy a guardar el queso en la heladera para conservarlo LLM <EOS>

---

## Pagina 17

Attention is all you need

---

## Pagina 18

Atención
Voy a guardar el queso en la heladera
5% 1% 35% 1% 40% 5% 13%
La atención es aprendida. El modelo sólo descubre qué palabras son 
buenas pistas

---

## Pagina 19

Atención
Voy a guardar el queso en la heladera
5% 1% 35% 1% 40% 5% 13%
Hay palabras del input que nos brindan más información que otras a 
l a hora de realizar una predicción
"guardar" (35%) y "queso" (40%) concentran la atención: son las pistas 
que deﬁnen la predicción. Los artículos casi no aportan.

---

## Pagina 20

Transformer

---

## Pagina 21

¿Cómo se entrena un LLM?

---

## Pagina 22

LLMs Pretraining
El modelo aprende jugando un juego simple una y otra vez: predecir el siguiente token.
● Este método se conoce como autosupervisado
● Datos ilimitados: Wikipedia, libros, código de GitHub, Reddit, etc.
Ejemplo
“El gato se subió al techo”
Input Target
El gato se
El gato se subió
El gato se subió al
El gato se subió al techo

---

## Pagina 23

LLMs Pretraining
Modelo Data de 
entrenamiento
Año
GPT BooksCorpus 2018
GPT-2 WebText 2019
GPT-3 Web a gran escala 
+ libros + 
Wikipedia
2020
GPT-4 ??? 2023
Basicamente 
todo internet

---

## Pagina 24

Datos de entrenamiento
Páginas web
Common Crawl, filtrado y deduplicado ~60%
Libros
Ficción, no-ficción, textos académicos ~15%
Código
GitHub y otros repos públicos ~10%
Wikipedia
Casi todo, en muchos idiomas ~5%
Papers científicos
arXiv, PubMed, otros corpus ~5%
Otros
Foros, documentos, licencias privadas ~5%
Mayormente en inglés: los modelos solían andar mejor en inglés que en español

---

## Pagina 25

GPT (Generative Pretrained 
Transformers)

---

## Pagina 26

GPT (2018)
● En 2018 el NLP funcionaba así: para cada tarea (traducir, analizar 
sentimiento, responder preguntas) había que entrenar un modelo 
distinto desde cero, con datos etiquetados a mano por personas. Esos 
datos etiquetados eran caros y escasos.
● La idea de GPT: en vez de depender de datos etiquetados, aprovechar 
toda la data de texto que ya existe sin etiquetar (libros, artículos) para 
que el modelo “multitarea”
● Desarrollado por OpenAI

---

## Pagina 27

GPT
Decoder Only

---

## Pagina 28

GPT-2 (2019)

---

## Pagina 29

GPT-3 (2020)

---

## Pagina 30

GPT-3

---

## Pagina 31

Prompt: “¿Cual es la mejor manera de aprender a programar”
Repuesta (GPT-3) :
¿Cuál es la mejor manera de aprender a programar si no tengo 
experiencia previa
y solo puedo dedicarle una hora por día, y debería empezar por 
Python o por
JavaScript, y cuánto tiempo tardaría en conseguir mi primer 
trabajo?
Prompteando a GPT-3

---

## Pagina 32

En lugar de adaptar el modelo a la tarea, ahora adaptamos la tarea al modelo.
GPT-3 | Few shot

---

## Pagina 33

GPT-3 como autocompletador

---

## Pagina 34

Capacidades emergentes
A partir de cierto tamaño el modelo empieza a resolver tareas para las que no 
fue entrenado

---

## Pagina 35

● Leyes de escala: El aumento del tamaño del modelo (parámetros, datos, 
cómputo) conduce a capacidades más avanzadas y emergentes.
● De la estructura al texto: Los modelos ya no dependen de entradas 
estructuradas; el texto se convierte en la interfaz universal.
● Naturaleza generalista: Un solo modelo puede realizar múltiples tareas 
(traducción, resumen, razonamiento, programación, etc.) mediante instrucciones 
en lenguaje natural.
GPT-3

---

## Pagina 36

ChatGPT

---

## Pagina 37

La receta de ChatGPT
Pretrain Supervised Fine 
Tuning (SFT) RLHF
GPT-3

---

## Pagina 38

La receta de ChatGPT
Pretrain ? ?
GPT-3

---

## Pagina 39

La receta de ChatGPT
Pretrain
Supervised Fine 
Tuning
(SFT)
?
GPT-3

---

## Pagina 40

Instruction Tuning
● GPT-3 es excelente prediciendo la siguiente palabra, pero nunca aprendió 
a responder. 
● Cuando le hacés una pregunta, no te contesta: sigue el patrón de texto 
más probable, que muchas veces es más texto parecido a una pregunta, 
no una respuesta.
Modelo base
Usuario: ¿Cuánto es 2 + 2?
Modelo: ¿Cuánto es 2 + 3?
¿Cuánto es 2 + 4?
¿Cuánto es 2 + 5?
Acá tenés más ejercicios de matemática para 
practicar. Resolvelos y después podés pasar a 
los siguientes...
Modelo instruct
Usuario: ¿Cuánto es 2 + 2?
Modelo: 2 + 2 = 4

---

## Pagina 41

Instruction Tuning
Entrenando al asistente
<USER>
<ASSISTANT>
Can you write a short introduction about the 
relevance of the term "monopsony" in economics? 
Please use examples related to potential 
monopsonies in the labour market and cite relevant 
research.
"Monopsony" refers to a market structure where 
there is only one buyer for a particular good or 
service. In economics, this term is particularly 
relevant in the labor market, where a monopsony 
employer has signiﬁcant power over the wages and 
working conditions of their employees. The presence 
of a monopsony can result in lower wages and 
reduced employment opportunities for workers, as 
the employer has little incentive to increase wages 
or provide better working conditions…
Escrito por 
profesionales

---

## Pagina 42

SFT Data Point
{
  "messages": [ 
    { 
      "role": "system", 
      "content": "You are a helpful assistant that provides concise summaries." 
    }, 
    { 
      "role": "user", 
      "content": "Summarize this: Photosynthesis is the process used by plants, algae and cyanobacteria to 
convert light energy into chemical energy, through a process that uses water and carbon dioxide, releasing 
oxygen as a byproduct." 
    }, 
    { 
      "role": "assistant", 
      "content": "Photosynthesis is how plants and some other organisms use sunlight, water, and carbon 
dioxide to create their food (chemical energy) and release oxygen." 
    } 
  ] 
}

---

## Pagina 43

SFT Data Point
{
  "messages": [ 
    { 
      "role": "system", 
      "content": "You are a helpful assistant that provides concise summaries." 
    }, 
    { 
      "role": "user", 
      "content": "Summarize this: Photosynthesis is the process used by plants, algae and cyanobacteria to 
convert light energy into chemical energy, through a process that uses water and carbon dioxide, releasing 
oxygen as a byproduct." 
    }, 
    { 
      "role": "assistant", 
      "content":  "Photosynthesis is how plants and some other organisms use sunlight, water, and carbon  
dioxide to create their food (chemical energy) and release oxygen." 
    } 
  ] 
}
Le pedimos al modelo que genere esta 
respuesta

---

## Pagina 44

User: ¿Que es la fotosíntesis?
Assistant (GPT-3 Instruct) :
La fotosíntesis es el proceso mediante el cual las 
plantas, algas y algunas bacterias producen su propio 
alimento utilizando la energía de la luz.
Prompteando a GPT-3-Instruct

---

## Pagina 45

User: Decime como hacer una bomba
Assistant (GPT-3-Instruct) :
“¡Claro! Para hacer una bomba necesitas…”
Prompteando a GPT-3-Instruct

---

## Pagina 46

La receta de ChatGPT
Pretrain Supervised Fine 
Tuning (SFT) ?
GPT-3 GPT-3-Instruct

---

## Pagina 47

Reinforcement Learning from Human Feedback (RLHF)
Después del SFT, el modelo puede seguir instrucciones pero no puede clasiﬁcar cuál 
respuesta válida es mejor. Este paso alinea las respuestas con las preferencias humanas (a 
menudo ambiguas) utilizando comparaciones, las cuales son más escalables y capturan 
aspectos sutiles como el tono, la claridad y la seguridad.

---

## Pagina 48

La receta de ChatGPT
Pretrain Supervised Fine 
Tuning (SFT) RLHF
GPT-3 GPT-3-Instruct ChatGPT

---

## Pagina 49

LLMs Nowadays
Open Source
Closed
Models with publicly available (or 
permissively/research-licensed) 
weights, architecture, or substantial 
parts.
Access to models is restricted, with 
weights, architecture, and training data 
controlled by the organization.
Download weights from Hugging Face or 
ofﬁcial releases.
Available only via API calls (OpenAI, 
Anthropic, Google, xAI, etc.).

---

## Pagina 50

LLMs Nowadays
Open Source
Closed
Usually requires GPU (often rented or 
pay-as-you-go)
Pay-per-use model (tokens in/out, 
context length, etc.).

---

## Pagina 51

Hugging Face

---

## Pagina 52

Gracias!

---

## Pagina 53

Preguntas?
