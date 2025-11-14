import argparse, yaml
from pathlib import Path
import pandas as pd
from src.etl import extract, transform, load

def main(cfg_path: str):
    cfg = yaml.safe_load(Path(cfg_path).read_text())
    raw_path = Path(cfg['dataset']['path'])
    out_path = Path('data/processed/clean.csv')

    print(f'[ETL] Reading {raw_path}')
    df = extract(raw_path)

    date_col = cfg['dataset'].get('date_col')
    if date_col and date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    print('[ETL] Transforming...')
    df_clean = transform(df)
    print(f'[ETL] Saving → {out_path}')
    load(df_clean, out_path)
    print('[ETL] Done.')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--config', required=True)
    a = p.parse_args()
    main(a.config)
