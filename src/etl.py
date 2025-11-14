from __future__ import annotations
from pathlib import Path
import pandas as pd

def extract(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == '.csv':
        return pd.read_csv(path)
    elif path.suffix.lower() in {'.xlsx', '.xls'}:
        return pd.read_excel(path)
    else:
        raise ValueError(f'Unsupported file type: {path.suffix}')

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy().drop_duplicates()
    df.columns = [c.strip().replace('\xa0',' ').strip() for c in df.columns]
    df.columns = [c.replace(' ', '_').lower() for c in df.columns]

    for col in ['price','area_size','price_per_sqft','no._of_bedrooms','no._of_bathrooms']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    for col in df.columns:
        if df[col].dtype.kind in 'biufc':
            df[col].replace([float('inf'), float('-inf')], pd.NA, inplace=True)

    if 'price_per_sqft' not in df.columns and 'price' in df.columns and 'area_size' in df.columns:
        df['price_per_sqft'] = df['price'] / df['area_size']
    return df

def load(df: pd.DataFrame, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)
