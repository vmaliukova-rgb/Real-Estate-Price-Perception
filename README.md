#  Real Estate Price Analysis

This project is a analytical and machine-learning exercise  
The goal is to explore a housing price dataset, understand the main drivers of price variation, create visual summaries, and build a simple baseline regression model.


##  Dataset

The dataset contains information about residential properties, including:

- area  
- bedrooms  
- bathrooms  
- stories  
- parking  
- furnishing status  
- presence of air conditioning  
- price (target variable)

The data does not contain personal or identifiable information and is safe for  use.


##  Exploratory Data Analysis (EDA)

The EDA part includes:

- checking dataset shape, dtypes and missing values  
- summary statistics  
- distribution plots for numerical features  
- scatterplots (e.g., area vs price)  
- boxplots for categorical–numerical relationships  
- correlation heatmap  
- pairplot for selected variables  

Additionally, a sunburst was created to explore combinations of furnishing status, AC and parking, summarised by median property price.


##  Modelling

A simple **Linear Regression** model was built using numeric features:

- area  
- bedrooms  
- bathrooms  
- stories  
- parking  

Train–test split: 80/20  
Model evaluation: MAE and R²


### **Baseline model results**
- **MAE ≈ 915,000**  
- **R² ≈ 0.53**

The model explains a bit more than half of the variation in property prices, which is expected because not much variables used


###  **Model with Yeo–Johnson transformation**
- **MAE ≈ 1,119,000**  
- **R² ≈ 0.56**

The R² increased slightly, but the error became larger.  
Therefore, the transformed model is not better and the original linear model is sufficient as a simple baseline.


## takeaways

- Area, bedrooms and bathrooms show clear positive relationships with price.  
- Properties that are furnished and have AC + parking tend to cluster in higher-price segments.  
- The dataset lacks many factors that strongly influence house prices (location, year built, neighbourhood quality), which influences the quality of models




##Tools & Libraries

- Python  
- pandas  
- numpy  
- seaborn  
- matplotlib  
- plotly  
- scikit-learn  
- feature-engine  




