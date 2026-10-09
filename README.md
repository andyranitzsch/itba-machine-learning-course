# 🏠 Predicting Property Prices in Buenos Aires

> **Machine Learning Engineering — ITBA**
> End-to-end machine learning (ML) pipeline: from raw real-estate listings to a tuned Random Forest that predicts property prices in **Capital Federal**.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-data-150458?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![seaborn](https://img.shields.io/badge/seaborn-visuals-4C72B0?style=flat-square)

---

## 📖 About this repo

This repository holds the solution to the final assignment of the Machine Learning Engineering course: **predict the sale price of properties in Buenos Aires (Capital Federal)** using the full lifecycle of a real ML project.

📄 **Assignment brief (original, in Spanish):** [`ENUNCIADO.md`](ENUNCIADO.md)

Working on it means touching every stage a machine learning engineer faces in the wild:

| Stage | What you build | What you learn |
|-------|----------------|----------------|
| 🔍 **EDA** (Exploratory Data Analysis) | 6 justified visualizations | Read a 1M-row dataset before modeling it |
| 🛠️ **Feature engineering** | Missing-data policy, outlier detection (IQR — Interquartile Range — / Z-score), one-hot encoding | Every cleaning decision needs a reason, not a habit |
| 📐 **Metrics** | Choose and justify MAE (Mean Absolute Error) | Why error metrics break on skewed targets |
| 🤖 **Modeling** | Linear Regression vs Random Forest | When a linear model is not enough |
| 🎛️ **Tuning** | `GridSearchCV` | What hyperparameters actually do to performance |
| 📝 **Conclusions** | Model recommendation | Trade-offs & interpretability over raw scores |

> *“There is no single correct way to solve this assignment. The reasoning behind each decision matters more than the final score of the model.”* — course brief

## 🗂️ Repository structure

```
.
├── TP_MLE.ipynb        # 📓 The assignment — full pipeline, run end-to-end
├── nbpatch.py          # 🔧 Helper to patch notebook cells in place (no full regeneration)
├── extract_clases.py   # 🔧 Extracts the class PDFs in Clases/ to Markdown in Clases_txt/
├── requirements.txt    # 📦 Python dependencies
├── ENUNCIADO.md        # 📄 Assignment brief (original, Spanish)
├── properati.csv       # ⬇️  Dataset — download it yourself (see below)
└── README.md
```

## 📊 Dataset

`properati.csv` contains **~992,000 real-estate listings** from Argentina with location, surface area, rooms and price, among other variables.

It is **not included in this repo** (862 MB — GitHub blocks files over 100 MB). Download it from **[Properati Open Data](https://www.properati.com.ar/open-data)** (the `properati.csv` file) and drop it in the project root:

```
properati.csv   ← same folder as TP_MLE.ipynb
```

**What the notebook does with it:** filter to *Capital Federal · Venta · USD (US dollars)* (~169k rows), then explore, clean, transform, model and evaluate.

## 🚀 Getting started

**1. Clone the repo**

```bash
git clone https://github.com/andyranitzsch/itba-machine-learning-course.git
cd itba-machine-learning-course
```

**2. Create a virtual environment** *(recommended)*

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add the dataset** — download `properati.csv` (link above) into the project root.

**5. Run it**

```bash
jupyter notebook TP_MLE.ipynb
```

Run all cells top to bottom — the notebook executes end-to-end, figures and all.

## 🧠 What you take away from this repo

- **Exploration drives modeling.** Correlation matrices, boxplots and maps are not decoration: they decide which features survive.
- **Data is dirty.** Swapped `lat`/`lon` columns, prices of 11 USD, 60,000 m² surfaces — real datasets fight back.
- **Baselines matter.** Linear Regression sets the bar; Random Forest has to beat it honestly, and `GridSearchCV` has to prove the tuning was worth it.

## 🛠️ Tech stack

| Layer | Tools |
|-------|-------|
| Data | `pandas`, `numpy` |
| Visualization | `matplotlib`, `seaborn` |
| Modeling | `scikit-learn` (`LinearRegression`, `RandomForestRegressor`, `GridSearchCV`) |
| Environment | Jupyter Notebook, Python 3.13 |

---

<p align="center"><sub>Built for the ITBA Machine Learning Engineering course · 2026</sub></p>
