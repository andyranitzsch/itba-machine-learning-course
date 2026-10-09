# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

TP final de *Machine Learning Engineering* (ITBA): predecir el precio de venta de propiedades en Capital Federal con `properati.csv`. El entregable es **`TP_MLE.ipynb`** (único artefacto real; no hay paquete, tests ni CI). Enunciado en `ENUNCIADO.md`; `HANDOFF.md` documenta estructura del notebook, resultados, decisiones controvertidas y una checklist de revisión.

Idioma: el notebook, `HANDOFF.md` y `ENUNCIADO.md` están en español (tono de alumno, formal-académico, sin meta-comentarios); `README.md` está en inglés. Mantener el idioma de cada archivo.

## Comandos

```bash
python -m pip install -r requirements.txt
# properati.csv (~862 MB) NO está en el repo: bajarlo de https://www.properati.com.ar/open-data a la raíz
jupyter notebook TP_MLE.ipynb
jupyter nbconvert --to notebook --execute --inplace TP_MLE.ipynb   # corrida completa, ~30 min (90% es el GridSearchCV de 2b)
python extract_clases.py   # PDFs de Clases/ -> Clases_txt/*.md (usa pypdf)
```

Python 3.13, pandas 3.x, scikit-learn 1.9.

## Regla clave: editar el notebook solo con parches

**Nunca regenerar `TP_MLE.ipynb` desde un script** (`build_nb.py` se eliminó a propósito porque pisaba ediciones manuales). Usar `nbpatch.py`, que reemplaza/inserta solo las celdas tocadas:

- `find(nb, marker)` localiza celdas por un fragmento de texto; `replace_cell` / `replace_code` exigen que el marker matchee **exactamente 1** celda (si no, abortan).
- `append_cells(nb, cells, before_marker=...)` inserta antes de una celda; `md()` / `code()` crean celdas.
- Patrón: script efímero que hace `nb = load(); replace_cell(...); save(nb)`.

Los commits recientes siguen este flujo (ajustes de texto de celdas individuales).

## Arquitectura del notebook (65 celdas, pipeline lineal)

Setup (`RANDOM_STATE = 42`) → decisiones de alcance (CABA + Venta + USD; descarte de `l4/l5/l6`, `title/description`, cada uno con celda de evidencia) → 1a) 7 gráficos EDA → 1b) ingeniería de características → 1c) métrica (MAE principal + RMSE/R², baseline de la mediana) → 2a) split 80/20, Regresión Lineal, Random Forest → 2b) `GridSearchCV` (cv=5, scoring MAE) → 2c) conclusiones.

Cada decisión lleva una celda markdown de justificación ("Por qué / Observaciones"); el enunciado valora el razonamiento por encima del score.

Restricciones de diseño que hay que preservar al editar:

- **Sin leakage**: ninguna feature deriva de `price` (`precio_por_m2` se descartó deliberadamente).
- **Test set se usa una sola vez por modelo**; los hiperparámetros se eligen solo con CV sobre train.
- Los números citados en los markdowns deben coincidir con los outputs de las celdas (sobre todo 1b y 2b); si se re-ejecuta y cambian, actualizar los textos.
- Las decisiones de faltantes siguen la taxonomía de la Clase 3 (eliminación / sustitución / Cold Deck / Hot Deck / MICE).
- Siglas glosadas la primera vez que aparecen (MAE, RMSE, IQR, R², CABA, GBA…).

## Archivos fuera de git / notas

- `.gitignore` excluye `properati.csv`, `Clases/` (PDFs con copyright), `imgs/`, `.agents/`, `skills-lock.json`. `Clases_txt/` (texto extraído de las clases, material de referencia, no parte del TP) sí está versionado.
- Las cifras citadas en los markdowns (filas, features, métricas) dependen de la ejecución: si cambia la limpieza de 1b, re-ejecutar y actualizar los textos de 1b, 1c, 2b, 2c y `HANDOFF.md`.
- Rama principal: `master`.
