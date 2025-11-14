import pandas as pd
from pathlib import Path
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

clean = Path('data/processed/clean.csv')
if clean.exists():
    df = pd.read_csv(clean)
else:
    df = pd.DataFrame({'City':['Sample']*3,'Area Size':[50,75,100],'Price':[100000,160000,230000]})

cities = sorted([c for c in df['City'].dropna().unique()]) if 'City' in df.columns else []
prop_types = sorted([c for c in df['Property Type'].dropna().unique()]) if 'Property Type' in df.columns else []

num_cols = df.select_dtypes(include='number').columns.tolist()
x = 'Area Size' if 'Area Size' in df.columns else (num_cols[0] if num_cols else None)
y = 'Price' if 'Price' in df.columns else (num_cols[1] if len(num_cols)>1 else None)

fig = px.scatter(df, x=x, y=y, color='City', trendline='ols') if x and y else px.scatter()

app.layout = html.Div(children=[
    html.H1(children='Real Estate Dashboard'),
    dcc.Dropdown(cities, id='city-dd', placeholder='Filter by City', multi=True),
    dcc.Dropdown(prop_types, id='type-dd', placeholder='Filter by Property Type', multi=True),
    dcc.Graph(id='scatter', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
