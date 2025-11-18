# 🚲 Bike Demand Predictor: End-to-End Data Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 📋 Projektübersicht
Dieses Projekt ist eine **End-to-End Data Science Case Study**.
Ziel ist es, für einen Fahrradverleih in Seoul vorherzusagen, wie viele Fahrräder zu einer bestimmten Uhrzeit benötigt werden, um Engpässe zu vermeiden.

Das Projekt deckt den gesamten Daten-Lebenszyklus ab:
1.  **Data Engineering:** ETL-Pipeline von CSV in eine normalisierte MySQL-Datenbank.
2.  **Analysis:** Explorative Datenanalyse (EDA) zur Identifikation von Einflussfaktoren.
3.  **Machine Learning:** Training eines Random Forest Regressors (R² = 0.85).
4.  **Deployment:** CLI-Tool für Echtzeit-Vorhersagen.

---

## 🛠️ Tech Stack & Skills

* **Languages:** Python
* **Data Manipulation:** Pandas, NumPy
* **Database:** MySQL, SQLAlchemy (Schema Design, Normalization)
* **Visualization:** Seaborn, Matplotlib
* **Machine Learning:** Scikit-Learn (Regression, Feature Importance)

---

## 📊 Key Insights (Ergebnisse)

### 1. Wann fahren die Leute? (Rush Hour)
Die Analyse zeigt zwei massive Spitzen im Berufsverkehr (8 Uhr und 18 Uhr).
![Hourly Trend](images/hourly_trend.png)

### 2. Was beeinflusst die Entscheidung?
Die Temperatur ist der stärkste Indikator für die Nachfrage.
![Feature Importance](images/feature_importance.png)

### 3. Korrelationen
![Correlation Heatmap](images/correlation_heatmap.png)

---

## 🧠 Model Performance

Ich habe ein **Random Forest Modell** trainiert.
* **R² Score:** 0.85 (Erklärt 85% der Varianz)
* **MAE (Mean Absolute Error):** ~150 Räder Abweichung im Schnitt.

---

## 🚀 How to Run

### 1. Clone Repository
```bash
git clone [https://github.com/WaldemarEck/bike-demand-predictor.git](https://github.com/WaldemarEck/bike-demand-predictor.git)
cd bike-demand-predictor