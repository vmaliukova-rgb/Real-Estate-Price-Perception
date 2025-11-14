# Real Estate Price Analysis

This project is a practice exercise based on the ML and Data Visualisation.  
The goal was to explore a housing price dataset, create some visualisations, and build a simple regression model.

# Dataset

The dataset contains information about residential properties, including:

area  
bedrooms  
bathrooms  
stories  
parking  
furnishing status  
presence of air conditioning  
price (target variable)

The data does not contain personal  information and is safe for educational use

##  Main steps

Loaded and inspected the dataset  
Basic EDA (distributions, scatterplots, boxplots, correlation heatmap, pairplot)  
Sunburst chart to explore combinations of furnishing status, AC and parking  
Simple Linear Regression model  
experiment with a Yeo-Johnson transformation  


##  Model results

### Baseline linear regression:
**MAE = 915k**  
  **R² = 0.53**

The model explains a bit more than half of the variation in house prices.  
This is expected because it uses only a few numeric features.


### After Yeo-Johnson transformation:
**MAE = 1.12M**  
 **R² = 0.56**

The R² increased slightly, but MAE became higher.  
So the transformed model is **not better overall**, and the simple version is enough as a baseline.


## Findings

Area, bedrooms and bathrooms all have a positive relation with price  
Furnished homes with AC and parking tend to appear in higher price segments  
Prices depend on many factors not included in this dataset, so the model stays simple  
 

##  Ethical Considerations
Data does not contain personal information; the regression model is used only for educational purpuse only. The dataset is limited, hence some bias may be present.

 ## Tools

Python  
pandas  
seaborn  
matplotlib  
plotly  
scikit-learn  
feature-engine  
