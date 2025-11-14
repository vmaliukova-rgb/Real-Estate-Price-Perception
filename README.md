# Real Estate Price Perception 
This project is a  practice exercise based on the ML and Data Visualisation 
The goal was to explore a housing price dataset, create some visualisations, and build a simple regression model.
Main steps
Inspect the dataset
Basic EDA (distributions, scatterplots, boxplots, correlation heatmap, pairplot)
Sunburst charts to explore combinations of furnishing status, AC and parking
Simple Linear Regression model
Optional experiment with a Yeo-Johnson transformation
Model results
The baseline linear regression model gave:
MAE = 915k
R² = 0.53
So the model explains a bit more than half of the variation in house prices.
This is expected because it uses only a few features.
After applying a Yeo-Johnson transformation:
mAE = 1.12M
R² = 0.56
The R² increased slightly, but MAE became worse.
So the transformed model is not better overall, and the simple version is enough as a baseline.
Findings
Area, bedrooms and bathrooms all have a positive relation with price
Furnished homes with AC and parking tend to appear in higher price segments
Prices depend on many factors not included in this dataset, so the model remains simple
Tools used
Python, pandas, seaborn, matplotlib, plotly, scikit-learn, feature-engine
