# HANDOFF — Revisión independiente del TP

Documento para que otro agente (o persona) pueda revisar este trabajo sin contexto previo de la conversación que lo produjo.

## 1. Qué es esto

Trabajo práctico de *Machine Learning Engineering* (ITBA). Entregable: **`TP_MLE.ipynb`**, un notebook que predice el precio de venta de propiedades en Capital Federal sobre el dataset `properati.csv`.

- Enunciado original: [`ENUNCIADO.md`](ENUNCIADO.md)
- Repo: https://github.com/andyranitzsch/itba-machine-learning-course (público, rama `master`)

## 2. Cómo reproducirlo

```bash
git clone https://github.com/andyranitzsch/itba-machine-learning-course.git
cd itba-machine-learning-course
python -m pip install -r requirements.txt
# bajar properati.csv (~862 MB) de Properati Open Data y ponerlo en la raíz del repo:
# https://www.properati.com.ar/open-data

jupyter nbconvert --to notebook --execute --inplace TP_MLE.ipynb
```

Notas de ejecución:

- El notebook corre entero sin errores. La ejecución completa tarda **~30 minutos**: el 90% es el `GridSearchCV` de 2b (40 modelos).
- Python 3.13, pandas 3.x, scikit-learn 1.9.
- **No regenerar el notebook desde un script**: `build_nb.py` fue eliminado a propósito (regeneraba el archivo completo y pisaba ediciones manuales). Los cambios se aplican con parches sobre el `.ipynb` (ver `nbpatch.py`).
- `Clases_txt/` contiene el texto de los PDFs de clase extraído con `extract_clases.py` (material de referencia, no parte del TP).

## 3. Estructura del notebook (65 celdas)

| Sección | Contenido |
|---|---|
| Setup | imports, `RANDOM_STATE = 42`, carga y perfilado del dataset |
| Decisiones de alcance | filtros: CABA + Venta + USD (8.057 registros descartados por moneda); descarte de `l4/l5/l6` y `title/description`, cada uno con celda de evidencia (regiones, coberturas, ejemplos de encoding roto) |
| 1a) 7 gráficos | histograma de precio (log), conteo por tipo, boxplot por tipo, scatter superficie-precio, heatmap de correlación, mapa lat/lon, mediana por barrio con η². Cada uno con celdas "Por qué / Observaciones" |
| 1b) Ingeniería de características | nulos (mediana por tipo + flags; cubierta = total × proporción mediana del tipo), lat/lon invertidas (Cold Deck) y nulos de coordenadas (mediana del barrio), superficies imposibles con umbral por tipo (15 m² vivienda / 5 m² resto, para no tratar cocheras como error), descarte de `Casa de campo`, creación de `surface_ratio`, decisión de NO crear `precio_por_m2` (leakage), outliers por IQR y z-score, One-Hot de `property_type` y `l3` |
| 1c) Métrica | MAE principal (+RMSE y R²), baseline de referencia (MAE 180.630 USD predecir siempre la mediana) |
| 2a) Modelos | split 80/20 (con la limitación de imputar antes del split declarada), Regresión Lineal (+ comparación con/sin `drop_first`), Random Forest con hiperparámetros justificados |
| 2b) GridSearchCV | grilla `n_estimators [50,100] × max_features ["sqrt","log2"] × max_depth [10,20]`, cv=5, scoring MAE |
| 2c) Conclusiones | recomendación fundamentada con tabla comparativa |

## 4. Resultados clave (test)

| Modelo | MAE (USD) | RMSE (USD) | R² |
|---|---|---|---|
| Baseline (mediana) | 180.348 | 446.449 | −0,077 |
| Regresión Lineal | 126.072 | 309.420 | 0,483 |
| Random Forest (2a) | 82.270 | 242.907 | 0,681 |
| Random Forest (grid) | 82.270 | 242.907 | 0,681 |

GridSearchCV cayó en la misma configuración elegida a mano en 2a (100 árboles, `sqrt`, profundidad 20): diferencia 0 en test. Conclusión documentada en el notebook: el tuning valida la elección, no la supera; el cuello de botella son las features, no los hiperparámetros.

Pipeline de datos: 992.192 filas → 169.054 (filtro CABA/Venta/USD) → 166.651 filas × 78 features (68 One-Hot: 9 tipos + 59 barrios; 7 numéricas; 3 flags), sin nulos.

## 5. Decisiones controvertidas (revisar con ojo crítico)

1. **Filtrar USD y descartar ARS**: 1.742 ARS + 6.315 nulls descartados (8.057 en CABA/Venta) en vez de convertir con tipo de cambio histórico.
2. **Conservar outliers de precio**: los 16.566 valores fuera del IQR (9,9%) se mantienen por ser propiedades reales; solo se eliminaron superficies > 2000 m² (550 filas) y precios < 5.000 USD.
3. **Imputación por mediana por `property_type`** en superficie total/ambientes/baños con columnas indicadoras; la cubierta se imputa como total × proporción mediana del tipo (garantiza cubierta ≤ total). Reduce varianza — está documentado, con alternativas descartadas (Hot Deck, regresión, MICE).
4. **`lat`/`lon` venían invertidas** en el dataset original; corrección en 1b (no en la fuente).
5. **`precio_por_m2` deliberadamente NO creado** (leakage del target). Verificar que ninguna feature derive de `price`.
6. **Outliers de superficie**: 550 filas > 2000 m² eliminadas; el notebook explica por qué no se usa el límite del IQR (545 m²): eliminaría casas, lotes y depósitos reales.
7. **Umbral mínimo de superficie por tipo**: 15 m² para vivienda, 5 m² para el resto. Un umbral único de 15 m² trataba como error a 1.012 cocheras reales (mediana de cocheras: 13 m²).
8. **Imputación antes del split**: las medianas se calculan con todo el dataset; declarado como limitación en 2a (efecto despreciable con 166k filas).

## 6. Checklist de revisión sugerida

- [ ] El texto de los markdowns suena a escrito por un alumno (tono formal-académico, sin conversacional ni meta-comentarios tipo "como vimos en clase").
- [ ] Las siglas van glosadas la primera vez (MAE, RMSE, IQR, R², NLP, CABA, GBA, Cold Deck...).
- [ ] Los números citados en los markdowns coinciden con los outputs de las celdas (especialmente 1b y 2b).
- [ ] Ninguna feature deriva del target (leakage).
- [ ] El test se usa una sola vez por modelo, nunca para elegir hiperparámetros.
- [ ] Las decisiones de 1b siguen la taxonomía de faltantes de la Clase 3 (eliminación/sustitución/Cold Deck/Hot Deck/MICE).
- [ ] Gráficos legibles y justificados (1a pide justificar cada uno).
- [ ] Conclusión (2c) responde al enunciado con argumentos y números, no con adjetivos.

## 7. Estado

- Rama `master`. Revisión independiente aplicada (umbral de superficie por tipo, imputación coherente de la cubierta, `Casa de campo`, textos y cifras) y notebook re-ejecutado de cero.
- `properati.csv` y `Clases/` (PDFs) fuera del repo (tamaño / copyright). `Clases_txt/` (texto extraído) sí está versionado como material de referencia.
- Un force-push histórico (`c37e8f2` → `fd34f1e`) por un mensaje de commit mal escrito.
