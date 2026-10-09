import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

def md(src):
    cells.append(nbf.v4.new_markdown_cell(src))

def code(src):
    cells.append(nbf.v4.new_code_cell(src))

md("""# Trabajo Práctico — Machine Learning Engineering
## Predicción del precio de venta de propiedades en Capital Federal

**Dataset:** `properati.csv` — publicaciones de propiedades en Argentina.

**Objetivo:** aplicar el ciclo completo de un proyecto de Machine Learning: exploración, preprocesamiento, transformación, modelado y evaluación, para predecir el precio de venta de propiedades en Capital Federal.

> Las decisiones tomadas a lo largo del trabajo están justificadas en celdas de Markdown.

---

## 0. Setup""")

code("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook")
pd.set_option("display.max_columns", 60)

RANDOM_STATE = 42
df_raw = pd.read_csv("properati.csv")
df_raw.shape""")

code("""df_raw.head()""")

code("""resumen = pd.DataFrame({
    "dtype": df_raw.dtypes,
    "nulos": df_raw.isna().sum(),
})
resumen["% nulos"] = (resumen["nulos"] / len(df_raw) * 100).round(2)
resumen.sort_values("% nulos", ascending=False)""")

code("""# Regiones (l2) presentes en el dataset: cuántas filas hay de cada una
df_raw["l2"].value_counts(dropna=False).rename_axis("l2").rename("publicaciones").to_frame()""")

code("""# ¿Contenido de l4, l5 y l6? Se mira cobertura total Y cobertura dentro de CABA
caba = df_raw[df_raw["l2"] == "Capital Federal"]

resumen_geo = pd.DataFrame({
    "valores únicos": [df_raw[c].nunique(dropna=True) for c in ["l4", "l5", "l6"]],
    "filas con dato": [int(df_raw[c].notna().sum()) for c in ["l4", "l5", "l6"]],
    "% nulo": [(df_raw[c].isna().mean() * 100).round(1) for c in ["l4", "l5", "l6"]],
    "filas con dato en CABA": [int(caba[c].notna().sum()) for c in ["l4", "l5", "l6"]],
}, index=["l4", "l5", "l6"])
print(resumen_geo)
print()
print("Top de valores de l4 (todo el dataset):")
print(df_raw["l4"].value_counts().head(6))
print()
print("l4 dentro de CABA (sub-barrios, solo 10.091 filas):")
print(caba["l4"].value_counts().head(6))
print()
print("l5 — 21 valores en total, ninguno cae en CABA:")
print(df_raw["l5"].value_counts().head(6))""")

code("""# ¿Qué hay en title/description? Evidencia de encoding dañado y HTML embebido
def con_bytes_rotos(s):
    return isinstance(s, str) and "\\ufffd" in s

titulos = df_raw["title"].dropna()
descs = df_raw["description"].dropna()
rotos_t = titulos[titulos.map(con_bytes_rotos)]
rotos_d = descs[descs.map(con_bytes_rotos)]

print(f"Titles con bytes rotos: {len(rotos_t):,} / {len(titulos):,}")
print(f"Descriptions con bytes rotos: {len(rotos_d):,} / {len(descs):,}")
print()
print("Ejemplo de title (repr escapado):")
print(ascii(rotos_t.iloc[0]))
print()
print("Ejemplo de description: contexto alrededor del primer byte perdido:")
ejemplo = rotos_d.iloc[0]
pos = ejemplo.find("\\ufffd")
print(ascii(ejemplo[max(0, pos - 90):pos + 60]))""")

md("""### Decisiones de alcance previas a explorar

1. **Filtrar por `l2 == "Capital Federal"`**: el objetivo del TP (Trabajo Práctico) es predecir precios *en Capital Federal* (CABA: Ciudad Autónoma de Buenos Aires). Mezclar otras provincias introduce variación de precio por mercado (distinta demanda, distinta moneda de referencia) que no queremos modelar. En la celda de regiones (`l2`) se ven las disponibles: Capital Federal concentra 249.738 de 992.192 publicaciones.
2. **Filtrar por `operation_type == "Venta"`**: hay publicaciones de alquiler y alquiler temporal. La variable objetivo es precio de *venta*; alquilar y vender son problemas distintos y las columnas no son comparables entre sí.
3. **Filtrar por `currency == "USD"`**: en el dataset conviven USD (dólares estadounidenses), ARS (pesos argentinos) y nulls. En CABA/Venta: 169.054 USD, 1.742 ARS y 6.315 sin moneda. Convertir ARS a USD exigiría un tipo de cambio histórico por fecha de publicación (no disponible y sujeto a brecha cambiaria). Descartar esos ~8k registros (menos del 5%) es más limpio que una conversión aproximada. Procedemos a descartar los **8.057** registros.
4. **Se descartan `l4`, `l5`, `l6`** (coberturas y valores en la celda anterior):
   - `l6`: **100% nulo, 0 valores únicos**. Columna completamente vacía.
   - `l5`: 99,5% nulo; 21 valores en total ("Barrio Los Alisos", "Barrio El Golf"... son barrios privados del GBA (Gran Buenos Aires)) y **0 filas con dato dentro de CABA**. No aplica al universo del TP.
   - `l4`: 77% nulo. En CABA solo **10.091 filas (4,0%)** tienen dato, y **todas son de Palermo** (Palermo Hollywood/Soho/Chico/Viejo). El contenido es más fino que `l3`, pero con 4% de cobertura concentrada en un solo barrio no se puede usar sin inventar datos para el resto. Se descarta por **cobertura sesgada**, no por contenido.
5. **Se descartan `title` y `description`**: son texto libre; no aplicaremos NLP (*Natural Language Processing*, Procesamiento de Lenguaje Natural) en este TP y no aportan a un modelo tabular básico (la celda anterior muestra qué contienen).""")

code("""print("Dataset completo:", df_raw.shape)

caba_venta = df_raw[
    (df_raw["l2"] == "Capital Federal")
    & (df_raw["operation_type"] == "Venta")
].copy()
print("CABA + Venta:", caba_venta.shape)

df = caba_venta[caba_venta["currency"] == "USD"].copy()
descartados = len(caba_venta) - len(df)
print(f"Descartados por currency != USD: {descartados:,}")
print("Final (CABA + Venta + USD):", df.shape)
print()
print("Precio (USD):")
print(df["price"].describe())""")

md("""---

## Parte 1 a) — Visualización de los datos

Seis gráficos, cada uno con una pregunta distinta:

| # | Gráfico | Pregunta que responde |
|---|---------|----------------------|
| 1 | Histograma de precio (log) | ¿Cómo es la distribución? ¿Hay sesgo/colas largas? |
| 2 | Conteo por tipo de propiedad | ¿Está balanceado el dataset por tipo? |
| 3 | Boxplot de precio por tipo | ¿Cambia el rango de precios entre tipos? |
| 4 | Scatter superficie vs precio | ¿Hay relación (semi)lineal? ¿Homocedasticidad? |
| 5 | Matriz de correlación | ¿Qué numéricas están linealmente relacionadas? |
| 6 | Mapa geográfico (lat/lon) | ¿El espacio explica precio? |
| 7 | Mediana de precio por barrio (`l3`) | ¿Cuánto explica el barrio, si no entra en la correlación? |""")

md("""### Gráfico 1 — Distribución de precios (histograma, escala logarítmica)

**Por qué:** el precio es la variable objetivo. Conocer su distribución define casi todo lo demás: qué métrica conviene (si hay cola larga, el RMSE — *Root Mean Squared Error*, raíz del error cuadrático medio — la penaliza de más), si conviene escalar o transformar, y si hay valores absurdos.

**Qué espero descubrir:** precios inmobiliarios suelen tener distribución sesgada a la derecha (pocas propiedades muy caras). La escala logarítmica permite ver la forma real de la cola.""")

code("""fig, ax = plt.subplots(figsize=(10, 5))
precios = df.loc[df["price"] > 0, "price"]

sns.histplot(precios, bins=100, log_scale=True, ax=ax, color="steelblue")
ax.axvline(precios.median(), color="red", ls="--", label=f"Mediana: {precios.median():,.0f} USD")
ax.axvline(precios.mean(), color="orange", ls="--", label=f"Media: {precios.mean():,.0f} USD")

ax.set_title("Distribución de precios de venta (USD, escala log)")
ax.set_xlabel("Precio (USD)")
ax.legend()
plt.tight_layout()
plt.show()""")

md("""**Observaciones:**
- Distribución **sesgada a la derecha**: mediana 160.000 USD vs media 285.000 USD. La media es afectada por las pocas propiedades muy caras.
- Este sesgo es lo esperado en un mercado inmobiliario: pocos inmuebles premium estiran la cola y la masa se concentra en un rango medio.
- Cola derecha que llega hasta ~30 millones de USD.
- Pico secundario alrededor de 10.000–40.000 USD: probablemente cocheras y locales chicos mezclados en la misma distribución.
- **Implicancia para el TP:** la distribución no es simétrica. Eso favorece una métrica robusta como el MAE — *Mean Absolute Error*, error absoluto medio (no la media de errores al cuadrado, muy sensible a la cola).""")

md("""### Gráfico 2 — Cantidad de publicaciones por tipo de propiedad

**Por qué:** `property_type` es una variable categórica con alta probabilidad de ser feature. Antes de usarla, hay que saber si todos los tipos tienen suficientes muestras.

**Qué espero descubrir:** si el dataset está dominado por departamentos, y si hay tipos con tan pocos registros que convenga agruparlos o descartarlos.""")

code("""orden = df["property_type"].value_counts().index

fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=df, y="property_type", order=orden, hue="property_type",
              palette="viridis", legend=False, ax=ax)
ax.set_title("Publicaciones por tipo de propiedad")
ax.set_xlabel("Cantidad")
ax.set_ylabel("")
for i, v in enumerate(df["property_type"].value_counts()):
    ax.text(v + 500, i, f"{v:,}", va="center", fontsize=9)
plt.tight_layout()
plt.show()""")

md("""**Observaciones:**
- **Departamento domina**: 100.232 de 169.054 publicaciones (~59%). El dataset está desbalanceado por tipo.
- `Otro` es la segunda categoría (26.341) pero es una **categoría-vertedero**: no define un tipo de propiedad. Candidata a descarte o a reasignación.
- `Casa de campo` tiene **5 registros**: no alcanza para aprender nada. Se descarta.
- El resto tiene muestra suficiente (≥ 862), aunque `Depósito` y `Cochera` quedan como tipos minoritarios.""")

md("""### Gráfico 3 — Distribución de precios por tipo de propiedad (boxplot)

**Por qué:** compara la variable objetivo entre categorías. Si los rangos no se solapan, el tipo de propiedad es predictiva fuerte.

**Qué espero descubrir:** si un "Casa" y un "Cochera" viven en universos de precio distintos; si hay outliers dentro de cada tipo.""")

code("""tipos = df["property_type"].value_counts().index.tolist()

fig, ax = plt.subplots(figsize=(11, 6))
sns.boxplot(data=df, x="property_type", y="price", order=tipos,
            hue="property_type", palette="Set2", legend=False, ax=ax)
ax.set_yscale("log")
ax.set_title("Precio (USD, escala log) por tipo de propiedad")
ax.set_xlabel("")
ax.set_ylabel("Precio (USD)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()""")

md("""**Observaciones:**
- **Medianas muy distintas por tipo**: cochera ~25.000 USD, departamento ~160.000 USD, depósito/lote ~500.000 USD. `property_type` es una feature de primer nivel.
- **Outliers en todos los tipos**: casi todos superan 1.000.000 USD arriba de su caja. Son en parte reales (penthouses, casas premium) y en parte errores de carga.
- `Otro` llega a **11 USD**: imposible. O error de carga, o "precio a convenir" cargado como número. Se revisa en el punto 1b.1 (datos mal ingresados).
- Los rangos de `Cochera` y `Depósito` casi no se solapan con los de `Departamento`: ignorar `property_type` sería un error grave.""")

md("""### Gráfico 4 — Relación superficie cubierta vs precio (muestra)

**Por qué:** superficie y precio son las dos variables numéricas centrales del problema. Un scatter muestra la forma de la relación: si es lineal, si la varianza crece con el precio (heterocedasticidad), y si hay puntos imposibles (supertotal vs precio).

**Qué espero descubrir:** se espera correlación positiva, con nubes de puntos alejados (ph/locales) y valores de superficie absurdos.

> Se grafica una **muestra aleatoria de 5.000 puntos**: con 160k+ puntos el scatter queda como mancha sólida y no se ve nada (overplotting). La semilla fija hace el gráfico reproducible.""")

code("""muestra = df.dropna(subset=["surface_covered", "price"]).sample(
    n=5000, random_state=RANDOM_STATE
)

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=muestra, x="surface_covered", y="price",
                hue="property_type", alpha=0.5, s=25, ax=ax)
ax.set_title("Precio vs superficie cubierta (muestra de 5.000 publicaciones)")
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio (USD)")
ax.set_yscale("log")

# Los outliers de superficie (hay superficies de >60.000 m2) aplastan el eje X.
# Se recorta la vista al percentil 99 para poder ver la forma de la nube de puntos.
p99 = muestra["surface_covered"].quantile(0.99)
ax.set_xlim(0, p99 * 1.05)
ax.axvline(p99, color="gray", ls=":", lw=1, label=f"P99 = {p99:.0f} m2")
ax.legend()
plt.tight_layout()
plt.show()""")

md("""**Observaciones:**
- Relación **positiva pero ruidosa**: a más superficie, más precio, con mucha dispersión.
- **Heterocedasticidad**: la dispersión del precio crece con la superficie (y con el precio mismo). Esto castiga a la Regresión Lineal en los valores altos.
- El primer intento de este gráfico fue **ilegible**: un outlier de 63.000 m2 comprimía todo el eje X. Recortar la vista al P99 (percentil 99, línea punteada) hizo visible la forma real. Los outliers siguen existiendo en el dataset: esto es solo una decisión de visualización, no de limpieza.
- Hay puntos con superficie casi 0: otro indicio de datos mal cargados para la parte 1b.""")

md("""### Gráfico 5 — Matriz de correlación de las numéricas

**Por qué:** detecta colinealidad. Si dos features se corrrelacionan fuerte entre sí, la Regresión Lineal se vuelve inestable (coeficientes inflados); con Random Forest no es problema, pero sirve para decidir qué variables descartar.

**Qué espero descubrir:** `rooms`/`bedrooms`/`bathrooms` seguramente correlacionen entre sí; `surface_total` y `surface_covered` también. Ahí hay candidatas a descarte o a feature engineering.""")

code("""numericas = ["lat", "lon", "rooms", "bedrooms", "bathrooms",
             "surface_total", "surface_covered", "price"]

corr = df[numericas].corr()

fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, vmin=-1, vmax=1, ax=ax)
ax.set_title("Matriz de correlación (Pearson)")
plt.tight_layout()
plt.show()""")

md("""**Observaciones:**
- `rooms` vs `bedrooms`: **0,91**. Casi la misma información. Para la Regresión Lineal eso es multicolinealidad (coeficientes inestables); conviene quedarse con una o combinarlas. Para Random Forest no molesta tanto.
- `bathrooms` es la numérica que **más correlaciona con precio (0,53)** — más que superficie.
- `surface_total`/`surface_covered` correlacionan flojo con precio (0,17 / 0,12): Pearson en crudo los hunde por los outliers extremos y por tener ~55% de nulos. No significa que no sirvan; significa que la relación no es lineal pura.
- `lat`/`lon` dan ~0 con precio. **No significa que la ubicación no importe**: significa que la relación entre ubicación y precio no es lineal (es espacial). El gráfico 6 lo muestra. (Además, como se descubrió después, esas columnas están invertidas — ver gráfico 6.)
- `l3` (barrio) **no aparece en esta matriz por ser categórica**: el coeficiente de correlación de Pearson solo se calcula entre variables numéricas. Su poder predictivo se mide aparte, en el gráfico 7.""")

md("""### Gráfico 6 — Mapa geográfico de precios (lat/lon)

**Por qué:** la ubicación es el factor clásico del valor inmobiliario. Un scatter espacial permite ver si el precio tiene estructura geográfica, algo que las numéricas solas no muestran.

**Qué espero descubrir:** focos caros (Palermo, Recoleta, Puerto Madero), zona sur más barata, y posibles coordenadas mal cargadas (fueras de CABA).""")

code("""# Hallazgo de calidad de datos: las columnas están INVERTIDAS en el dataset.
# lat contiene -58.x (longitud real) y lon contiene -34.x (latitud real).
# Verificado en las primeras filas: lat=-58.4424, lon=-34.5736 = Colegiales, CABA.
print("lat (crudo) rango:", df["lat"].min(), "a", df["lat"].max())
print("lon (crudo) rango:", df["lon"].min(), "a", df["lon"].max())

df["lon_real"] = df["lat"]   # longitud correcta
df["lat_real"] = df["lon"]   # latitud correcta

# Límites geográficos plausibles de CABA
LAT_MIN, LAT_MAX = -34.71, -34.52
LON_MIN, LON_MAX = -58.54, -58.33

geo = df.dropna(subset=["lat_real", "lon_real", "price"]).copy()
fuera = ~geo["lat_real"].between(LAT_MIN, LAT_MAX) | ~geo["lon_real"].between(LON_MIN, LON_MAX)
print(f"Publicaciones con coordenadas fuera de CABA: {fuera.sum():,} de {len(geo):,} ({fuera.mean():.1%})")

muestra_geo = geo[~fuera].sample(n=6000, random_state=RANDOM_STATE)

fig, ax = plt.subplots(figsize=(9, 8))
sns.scatterplot(data=muestra_geo, x="lon_real", y="lat_real", hue="price",
                hue_norm=(0, muestra_geo["price"].quantile(0.95)),
                palette="magma", alpha=0.6, s=15, ax=ax, legend=False)
ax.set_title("Precio (USD) por ubicación — muestra de 6.000 publicaciones en CABA")
ax.set_xlabel("Longitud")
ax.set_ylabel("Latitud")
ax.set_aspect("equal")
plt.tight_layout()
plt.show()""")

md("""**Observaciones:**
- **`lat` y `lon` están invertidas en el dataset**: `lat` guarda la longitud (-58.x) y `lon` la latitud (-34.x). Es un error de carga del dataset, no de las publicaciones. Se corrigió renombrando los valores (`lon_real`/`lat_real`). Sin esta corrección, cualquier modelo con coordenadas usaría los ejes al revés.
- **Hay coordenadas fuera de CABA** incluso tras corregir el swap: se imprimió el % arriba. Sirve como insumo para la limpieza de la parte 1b.
- Tras corregir, se ve la silueta de CABA. El color no muestra un gradiente fuerte: el precio no depende de lat/lon solamente, sino de **barrio** (`l3`), que es categórica. Eso sugiere usar `l3` (o los centroides por barrio) como feature en vez de confiar en una relación lineal con las coordenadas.""")

md("""### Gráfico 7 — Mediana de precio por barrio (`l3`)

**Por qué:** `l3` es categórica, así que no entra en la matriz de correlación; aun así, el barrio es el predictor territorial clásico. Se compara la mediana de precio por barrio y se cuantifica su poder con el *correlation ratio* (η², η cuadrado): el equivalente de la correlación para una variable categórica contra una numérica, con valores entre 0 y 1.

**Qué espero descubrir:** si las medianas difieren mucho entre barrios, `l3` será una feature fuerte para la Parte 2.""")

code("""# Mediana de precio por barrio. Se filtra por cantidad para evitar barrios con 1-2 publicaciones.
precio_por_barrio = df.groupby("l3")["price"].agg(["median", "count"])
top_barrios = precio_por_barrio[precio_por_barrio["count"] >= 50].sort_values("median", ascending=False)

fig, ax = plt.subplots(figsize=(10, 8))
top_barrios.head(15)["median"].sort_values().plot.barh(ax=ax, color="steelblue")
ax.set_title("Mediana de precio (USD) por barrio — 15 más caros con al menos 50 publicaciones")
ax.set_xlabel("Mediana del precio (USD)")
ax.set_ylabel("")
for i, v in enumerate(top_barrios.head(15)["median"].sort_values()):
    ax.text(v * 1.02, i, f"{v:,.0f}", va="center", fontsize=8)
plt.tight_layout()
plt.show()

# Correlation ratio (eta^2): cuánto de la varianza del precio explica el barrio
media_global = df["price"].mean()
grupos = df.groupby("l3")["price"]
ss_between = sum(len(g) * (g.mean() - media_global) ** 2 for _, g in grupos)
ss_total = ((df["price"] - media_global) ** 2).sum()
print(f"Correlation ratio eta^2 (l3 -> price): {ss_between / ss_total:.3f}")

# El eta^2 crudo lo distorsionan los outliers; se repite en escala logarítmica
log_price = np.log10(df["price"])
media_log = log_price.mean()
ss_between_log = sum(
    len(pr) * (np.log10(pr).mean() - media_log) ** 2
    for _, pr in df.groupby("l3")["price"]
)
ss_total_log = ((log_price - media_log) ** 2).sum()
print(f"Correlation ratio eta^2 (l3 -> log10(price)): {ss_between_log / ss_total_log:.3f}")
print(f"Barrios evaluados (>= 50 publicaciones): {len(top_barrios)}")
print(f"Razón mediana max/min: {top_barrios['median'].iloc[0] / top_barrios['median'].iloc[-1]:.1f}x")
print()
print("3 barrios más caros y 3 más baratos (mediana, cantidad):")
print(top_barrios[["median", "count"]].head(3))
print(top_barrios[["median", "count"]].tail(3))
""")

md("""**Observaciones:**
- Las medianas difieren mucho entre barrios: **7,4x** entre el más caro (Puerto Madero, 700.000 USD) y el más barato (Villa Lugano, 95.000 USD). El barrio pesa.
- El *correlation ratio* en escala cruda da solo **0,047**: la varianza del precio está dominada por los outliers (media sensible). Calculado sobre `log10(price)` sube a **0,096**: el barrio explica ~10% de la varianza transformada, más información que cualquier numérica suelta del heatmap.
- Parque Patricios aparece con mediana alta (215.000 USD, por encima de lo esperable para la zona): mezcla desarrollos nuevos y lotes. Revisar junto a `surface_*` en la Parte 1b.
- En una misma ciudad conviven mercados con precios 7x distintos: `l3` es candidata de primera línea para One-Hot Encoding en la Parte 1b.""")

md("""---

## Parte 1 b) — Ingeniería de características

### b.1) Datos faltantes o mal ingresados""")

md("""**Diagnóstico:** la tabla siguiente muestra los nulos que quedan tras el filtro de alcance. Como se ve, el 33% de las filas no tiene *ninguna* de las dos superficies, `bedrooms` supera el 50% de nulos y `l3` tiene ~11,5%. El target (`price`) no tiene nulos.""")

code("""columnas = ["price", "lat", "lon", "l3", "rooms", "bedrooms", "bathrooms",
            "surface_total", "surface_covered", "property_type"]

faltantes = pd.DataFrame({
    "nulos": df[columnas].isna().sum(),
    "% nulos": (df[columnas].isna().mean() * 100).round(1),
}).sort_values("% nulos", ascending=False)
faltantes""")

code("""# Mal ingresados: situaciones imposibles o incoherentes, no meros faltantes
print("Precios por debajo de 5.000 USD:", (df["price"] < 5000).sum())
print("Superficie total <= 0:", (df["surface_total"] <= 0).sum())
print("Superficie total < 15 m2:", ((df["surface_total"] > 0) & (df["surface_total"] < 15)).sum())
print("Superficie cubierta > superficie total:", (df["surface_covered"] > df["surface_total"]).sum())
print("Coordenadas nulas:", (df["lat"].isna() | df["lon"].isna()).sum())
print("end_date con centinela 9999-12-31:", (df["end_date"] == "9999-12-31").sum())
print("Publicaciones sin filas duplicadas:", df.duplicated().sum() == 0, "| ids repetidos:", df["id"].duplicated().sum())
print("Columnas constantes: ad_type, l1, l2, operation_type, currency (un solo valor cada una)")

# z-score vs IQR: con datos tan sesgados, el z-score paga doble
s = df["surface_total"].dropna()
z = (s - s.mean()) / s.std()
print("Superficies con |z| > 3:", (z.abs() > 3).sum(), "— el z-score usa media y desvío, que los propios outliers inflan")
""")

md("""**Decisiones** (cada una con su justificación):

1. **`bedrooms` (83.888 nulos, 50%)**: se descarta la columna. `rooms` y `bedrooms` correlacionan 0,91 (gráfico 5), `rooms` tiene la mitad de nulos y correlaciona más con el precio (0,38 vs 0,19). Con una de las dos alcanza y se evita duplicar información (multicolinealidad en la Regresión Lineal).
2. **`rooms` (55.585 nulos) y `bathrooms` (26.632)**: **sustitución por mediana por tipo de propiedad** (estrategia de la Clase 3), más columnas indicadoras (`*_missing`). La mediana, no la media, porque son variables discretas de escala corta (1, 2, 3 ambientes): la media inventaría valores como 2,4 ambientes. La segmentación por tipo importa: la mediana global de `rooms` es 3, pero la de una cochera es 1 — sin segmentar, toda cochera sin dato quedaría con 3 ambientes. La clase advierte que este método reduce la varianza y deprime las correlaciones: las columnas indicadoras y conservar el resto de las features lo mitigan en parte. El indicador preserva la información *"este dato no estaba"*, que puede correlacionar con el precio.
3. **`surface_total` / `surface_covered` (60.638 / 64.514 nulos; 55.755 filas sin ninguna de las dos)**: **sustitución por mediana por tipo de propiedad**, no se descartan filas (la clase desaconseja eliminar salvo faltantes MCAR): perder el 33% de los datos es peor que estimar el valor ausente. Antes de imputar se corrigen dos inconsistencias de carga: (a) si `surface_covered` > `surface_total` (1.141 filas) es imposible, y se toma el cubierto como nuevo total; (b) si falta el total pero existe el cubierto, se copia el cubierto al total (el cubierto siempre es piso del total, así que el dato queda subestimado a lo sumo). Los casos restantes se imputan con la mediana por tipo y se marca `surface_missing`.
4. **Mal ingresados eliminatorios**: precio < 5.000 USD (1 fila, imposible para CABA) y superficies de 0 m2 o menores a 15 m2 (1.156 filas) se tratan como carga errónea: pasan a NaN y luego se imputan con el resto.
5. **Coordenadas**: **Cold Deck** (deducción por relación lógica, el ejemplo canónico de la Clase 3). Se corrige la inversión `lat`/`lon` detectada en 1a, se eliminan las publicaciones fuera del rectángulo de CABA (~0,1%) y los 24.224 nulos se rellenan con la mediana de su barrio, no con la mediana global (así la coordenada imputada apunta al barrio correcto).
6. **`l3` (19.528 nulos)**: se imputa con la categoría `"Desconocido"`. En lugar de perder 11,5% de las filas o inventar un barrio, se deja una categoría propia que el One-Hot Encoding trata después como una más.
7. **Columnas constantes** (`ad_type`, `l1`, `l2`, `operation_type`, `currency`): un solo valor en todo el dataset → se descartan, aportan varianza cero.
8. **Fechas**: `start_date`, `created_on` y `end_date` se descartan. El dataset cubre 13 meses (jul-2019 a jul-2020) y `end_date` tiene el centinela `9999-12-31` en 28.988 filas (aviso todavía activo): no permiten construir una feature temporal confiable.
9. **Duplicados**: no hay (ids únicos, 0 filas duplicadas) → nada que hacer.
10. **Alternativas de la clase que no se usaron** (*Hot Deck*: copiar de registros similares, imputación por regresión, MICE): quedan para un trabajo más avanzado — con 33% de faltantes el imputador se apoyaría en demasiados datos incompletos y el costo/beneficio no justifica la complejidad en este TP.""")

code("""df_ml = df[[
    "price", "property_type", "l3", "rooms", "bathrooms",
    "surface_total", "surface_covered", "lat", "lon"
]].copy()

# 1) Corrección de lat/lon invertidas (detectado en 1a)
df_ml["lat"], df_ml["lon"] = df_ml["lon"], df_ml["lat"]

# 2) Cobertura por errores de carga imposibles
mask_error_surface = (df_ml["surface_total"] <= 0) | (df_ml["surface_total"] < 15)
df_ml.loc[mask_error_surface, "surface_total"] = np.nan
df_ml.loc[df_ml["surface_covered"] <= 0, "surface_covered"] = np.nan

# 3) Coordenadas: fuera de CABA se eliminan (solo las no nulas), nulas se imputan por barrio
tiene_coords = df_ml["lat"].notna() & df_ml["lon"].notna()
fuera = tiene_coords & (~df_ml["lat"].between(-34.71, -34.52) | ~df_ml["lon"].between(-58.54, -58.33))
print("Filas eliminadas por coordenadas fuera de CABA:", int(fuera.sum()))
df_ml = df_ml[~fuera]

df_ml["l3"] = df_ml["l3"].fillna("Desconocido")
df_ml["lat"] = df_ml["lat"].fillna(df_ml.groupby("l3")["lat"].transform("median"))
df_ml["lon"] = df_ml["lon"].fillna(df_ml.groupby("l3")["lon"].transform("median"))

# 4) Superficies: inconsistencias primero, imputación después
df_ml.loc[df_ml["surface_covered"] > df_ml["surface_total"], "surface_total"] = df_ml["surface_covered"]
df_ml.loc[df_ml["surface_total"].isna() & df_ml["surface_covered"].notna(), "surface_total"] = df_ml["surface_covered"]

df_ml["surface_missing"] = df_ml["surface_total"].isna().astype(int)
df_ml["rooms_missing"] = df_ml["rooms"].isna().astype(int)
df_ml["bathrooms_missing"] = df_ml["bathrooms"].isna().astype(int)

mediana_tipo = df_ml.groupby("property_type")[["surface_total", "surface_covered", "rooms", "bathrooms"]].transform("median")
cols_num = ["surface_total", "surface_covered", "rooms", "bathrooms"]
df_ml[cols_num] = df_ml[cols_num].fillna(mediana_tipo)
# Queda un residuo si algún tipo de propiedad tiene todas sus superficies ausentes: mediana global
df_ml[cols_num] = df_ml[cols_num].fillna(df_ml[cols_num].median())

# 5) El target no admite faltantes ni precios imposibles
df_ml = df_ml[df_ml["price"].notna() & (df_ml["price"] >= 5000)]

print("Filas tras la limpieza:", f"{len(df_ml):,}")
print("Nulos restantes:", int(df_ml.isna().sum().sum()))
""")

md("""### b.2) Columnas a descartar o crear

**Se descartan** (además de las de 1a): `bedrooms`, `id`, `ad_type`, `l1`, `l2`, `operation_type`, `currency`, `price_period`, `start_date`, `end_date`, `created_on`.

**Se crean:**
- `surface_ratio` = `surface_covered` / `surface_total`: proporción construida sobre el terreno. Un valor bajo indica mucho patio/terraza; suele separar casas y PH de departamentos.
- Las tres columnas indicadoras (`surface_missing`, `rooms_missing`, `bathrooms_missing`).

**No se crean** features derivadas del target. `precio_por_m2 = price / surface_total` parece útil, pero **no es una feature: es el target disfrazado**. Un modelo que la use como predictor memorizaría el precio en lugar de aprender a estimarlo (*data leakage*, fuga de información).""")

code("""df_ml["surface_ratio"] = df_ml["surface_covered"] / df_ml["surface_total"]

df_ml = df_ml[[
    "price", "property_type", "l3", "rooms", "bathrooms",
    "surface_total", "surface_covered", "surface_ratio", "lat", "lon",
    "surface_missing", "rooms_missing", "bathrooms_missing",
]]
df_ml.head()""")

md("""### b.3) Outliers

**Método:** rango intercuartílico (IQR, *Interquartile Range*) como criterio principal. El z-score se calcula también, pero con esta distribución sesgada su propio resultado queda contaminado: la media y el desvío estándar los inflan los mismos valores que se quiere detectar (por eso `|z| > 3` marca solo 217 superficies y 2.772 precios, siempre menos de lo que el IQR detecta, porque los extremos agrandan la escala). El IQR usa percentiles y no se desplaza con los extremos.

**Decisiones sobre los que quedan:**
- **Precio**: los valores fuera del IQR (16.566 filas, 9,9%, con límite superior de 562.500 USD) **se mantienen**. Son propiedades reales (penthouses, casas premium): eliminarlos sesgaría el modelo a la baja y le quitaría precisión justo donde más duele. Sí se eliminaron los precios imposibles (< 5.000 USD) en b.1.
- **Superficie**: los valores extremos altos (> 2000 m2, 552 filas, 0,3%) **se eliminan**. En CABA no existe una propiedad individual de esas dimensiones salvo casos puntuales; el grueso corresponde a lotes o desarrollos cargados con datos inconsistentes.
- **Ambientes y baños** (`rooms > 6`, `bathrooms > 4`): se mantienen. Son consistentes con casas grandes, hoteles boutique y PH reciclados, no con errores.""")

code("""def iqr_bounds(s):
    q1, q3 = s.quantile(.25), s.quantile(.75)
    return q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)

for col in ["price", "surface_total", "rooms", "bathrooms"]:
    li, ls = iqr_bounds(df_ml[col])
    n = int(((df_ml[col] < li) | (df_ml[col] > ls)).sum())
    print(f"{col:<15} IQR: [{li:,.0f}, {ls:,.0f}]  -> fuera: {n:,} ({n/len(df_ml):.1%})")

antes = len(df_ml)
df_ml = df_ml[df_ml["surface_total"] <= 2000]
print(f"Filas eliminadas por superficie > 2000 m2: {antes - len(df_ml):,}")""")

code("""fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, col in zip(axes, ["price", "surface_total", "rooms"]):
    sns.boxplot(x=df_ml[col], ax=ax)
    ax.set_title(f"{col} tras la limpieza")
    ax.set_xlabel(col)
plt.tight_layout()
plt.show()""")

md("""**Observaciones:**
- El boxplot de precio conserva su cola: es la decisión buscada. Los valores altos son señal, no ruido.
- `surface_total` quedó acotado a 2000 m2; la caja ahora es legible.
- `rooms` y `bathrooms` muestran colas cortas y coherentes con el parque inmobiliario.""")

md("""### b.4) Encoding

One-Hot Encoding para las dos categóricas del modelo: `property_type` (10 valores) y `l3` (58 barrios + `Desconocido`). Cada categoría pasa a ser una columna 0/1: así los modelos lineales pueden usarlas sin inventar un orden entre categorías (el error que comete el Label Encoding).

Para la Regresión Lineal conviene eliminar una categoría por variable (`drop_first=True`) para no caer en multicolinealidad perfecta; Random Forest no lo necesita. Acá se usa `drop_first=False` para que los dos modelos reciban la misma matriz y en 1c se evalúa el impacto.""")

code("""df_ml = pd.get_dummies(
    df_ml,
    columns=["property_type", "l3"],
    prefix=["tipo", "barrio"],
    dtype=int,
)
print("Matriz final:", df_ml.shape)
print("Dummies creadas:", df_ml.shape[1] - 12)
print("Nulos en la matriz final:", int(df_ml.isna().sum().sum()))
df_ml.head()""")

md("""### b.5) Otras tareas de limpieza

- **Coordenadas corregidas**: `lat`/`lon` estaban invertidas en el dataset original (1a). Corregido en b.1.
- **Superficie cubierta mayor que total**: 1.141 filas corregidas (se toma `surface_covered` como piso de `surface_total`).
- **Centinela `9999-12-31`** en `end_date`: resuelto descartando la columna.
- **Columnas constantes**: descartadas (`ad_type`, `l1`, `l2`, `operation_type`, `currency`).
- **Duplicados**: verificados, no hay.
- **Moneda**: resuelto en 1a filtrando solo USD, que evita mezclar precios en distintas divisas.""")

code("""print("Filas del dataset final:", f"{len(df_ml):,}")
print("Columnas del dataset final:", df_ml.shape[1])
print("Nulos:", int(df_ml.isna().sum().sum()))
df_ml[["price", "rooms", "bathrooms", "surface_total", "surface_covered", "surface_ratio"]].describe().round(2)""")

md("""---

## Parte 1 c) — Descripción de los datos

### Qué descubrí del dataset

- **Alcance**: de 992.192 publicaciones originales se trabajan las **166.652** de Capital Federal, operación Venta y moneda USD, con **80 features**: 6 numéricas de entrada, coordenadas, 3 indicadoras de imputación, 68 columnas One-Hot (tipo de propiedad y barrio). Cero nulos en la matriz final.
- **El mercado segmentado manda**: el target tiene mediana de 160.000 USD y media de 285.000 USD (sesgo esperado en un mercado inmobiliario: ~10% de las propiedades supera el límite superior del IQR, 562.500 USD). El tipo de propiedad separa rangos que casi no se solapan, y el barrio es la señal territorial más fuerte: 7,4x entre la mediana de Puerto Madero y la de Villa Lugano.
- **Las features físicas importan, con ruido**: superficie, ambientes y baños correlacionan positivamente con el precio, pero con heterocedasticidad (la dispersión crece con el valor). La lat/lon lineal pesa poco; el barrio como categoría pesa más.
- **La calidad de los datos era baja y dirigió las decisiones**: `lat`/`lon` invertidas, monedas mezcladas (8.057 registros descartados), textos con *encoding* dañado, centinela `9999-12-31` en `end_date`, columnas constantes y sub-barrio (`l4`) con cobertura sesgada.
- **Faltanza masiva**: el 33% de las filas no tenía ninguna superficie. La mediana por tipo de propiedad preservó esas filas, con el costo conocido (reduce varianza); las columnas `*_missing` conservan el patrón de ausencia.

### Métrica para evaluar los modelos

**Métrica principal: MAE — *Mean Absolute Error*, error absoluto medio.** Como se ve en la Clase 5, es el promedio de las diferencias absolutas entre predicción y valor real, y queda expresado **en las unidades del target** (USD). Tres razones para elegirla:

1. **El target es sesgado con cola larga**. MSE y RMSE elevan los errores al cuadrado: una propiedad de 30M mal predicha pesa como cientos de departamentos estándar. MAE mide en USD reales y no premia castigar a los inmuebles premium.
2. **Interpretabilidad de negocio**. Un MAE de 40.000 USD responde *"en promedio, el modelo se equivoca por 40.000 dólares"* — lo que un vendedor o tasador entiende directo.
3. **Coherencia con el resto**: la clase define MAE, RMSE y R²; usar la principal que mejor respeta la distribución y luego las otras como referencia mantiene la comparación entre modelos consistente.

**Secundarias**: **RMSE** (penaliza los errores grandes; útil para ver si el modelo falla justo en las propiedades caras, que conservamos en 1b) y **R²** — *coeficiente de determinación*, variabilidad explicada — para comparar el modelo contra la línea de base sin información calculada arriba (predecir siempre la mediana, R² = 0 por definición).

**Nota de evaluación**: la misma métrica se usa en validación (dentro de `GridSearchCV`) y en test, y si en la Parte 2 se prueba `log(price)`, el MAE se reporta **des-transformado a USD** para que los modelos sean comparables.""")

code("""# Magnitud de referencia: cuánto se equivoca un modelo sin información,
# que siempre predice la mediana y otro que siempre predice la media.
from sklearn.metrics import mean_absolute_error, mean_squared_error

y = df_ml["price"]
pred_mediana = pd.Series(y.median(), index=y.index)
pred_media = pd.Series(y.mean(), index=y.index)

print(f"MAE predecir siempre la mediana: {mean_absolute_error(y, pred_mediana):,.0f} USD")
print(f"MAE predecir siempre la media:  {mean_absolute_error(y, pred_media):,.0f} USD")
print(f"MSE del predictor de mediana:    {mean_squared_error(y, pred_mediana):,.0f}")
print("-> Cualquier modelo debe bajar de estos valores de referencia.")
""")

nb["cells"] = cells
nb.metadata = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.13"},
}

with open("TP_MLE.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)
print("ok")
