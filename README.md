# Real Estate Price Perception — Individual Analytics Project

High-quality, exam-ready repository using the **Real Estate Price Insights** dataset (Kaggle).  
Includes a config-driven ETL pipeline, structured EDA notebooks, saved figures, and an optional Dash mini-dashboard.

## Objectives
- Reproducible **ETL** (config-driven).
- **EDA & Visualisations** answering business questions.
- **Concise insights** and saved figures in `reports/figures/`.
- Optional **Dash** app for interactive exploration.

## Dataset
Place the Kaggle CSV at:
```
data/raw/real_estate_price_insights.csv
```
Update `config.yaml` if you use a different file name/path.

Typical columns: `City`, `Area`, `No. of Bedrooms`, `No. of Bathrooms`, `Area Size`, `Price`, `Price per Sqft`, `Status`, `Transaction Type`, `Property Type`.

## Business Questions
1. What are the key drivers of property prices?
2. How does price per sqft vary across cities and property types?
3. What is the relationship between area size and price (and how does it differ by city)?

## Quick Start
```bash
# optional venv
python -m venv .venv && . .venv/bin/activate   # Windows: .venv\Scripts\activate

# install
pip install -r requirements.txt

# run ETL
python scripts/etl_cli.py --config config.yaml

# notebooks
jupyter notebook jupyter_notebooks/01_eda_overview.ipynb

# optional summary
python scripts/make_report.py

# optional dashboard
python dash_app/app.py
```

## Structure
```
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── user-story.md
│   │   └── task.md
│   └── workflows/ci.yml
├── dash_app/
│   └── app.py
├── data/
│   ├── raw/
│   └── processed/
├── jupyter_notebooks/
│   ├── 01_eda_overview.ipynb
│   ├── 02_feature_views.ipynb
│   └── 03_insights_report.ipynb
├── reports/
│   ├── figures/
│   └── html/
├── scripts/
│   ├── etl_cli.py
│   └── make_report.py
├── src/
│   └── etl.py
├── config.yaml
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

*Prepared on 2025-11-12*
