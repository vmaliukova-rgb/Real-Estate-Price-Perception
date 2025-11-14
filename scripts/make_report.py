from pathlib import Path
import pandas as pd

TEMPLATE = """
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Real Estate — Insights Summary</title></head>
<body>
<h1>Real Estate — Insights Summary</h1>
<p>Auto-generated summary from the processed dataset.</p>
<ul>
  <li>Rows: {rows}</li>
  <li>Columns: {cols}</li>
</ul>
<h2>Numeric Columns (preview)</h2>
<pre>{desc}</pre>
</body>
</html>
"""

def main():
    clean = Path('data/processed/clean.csv')
    if not clean.exists():
        raise SystemExit('Run ETL first to produce data/processed/clean.csv')
    df = pd.read_csv(clean)
    html = TEMPLATE.format(rows=len(df), cols=df.shape[1], desc=df.describe().to_string())
    out = Path('reports/html/summary.html')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')
    print(f'Wrote {out}')

if __name__ == '__main__':
    main()
