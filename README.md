# Project-SIA
# Data Analysis Project: CO₂ Emissions in the European Union (1960–2023)

## Project Overview
This project investigates the key drivers of **CO₂ emissions** in the **European Union** between **1960 and 2023**. The study examines how **energy consumption, urbanization rate, and industrial production** affect **GDP per capita**, providing valuable insights for policymakers working on sustainable economic and environmental strategies.

## Installation
This project requires Python and a virtual environment setup to manage dependencies efficiently.

### **1. Setting Up a Virtual Environment (Linux/Windows WSL)**
If you are using a **Linux virtual machine on Windows (WSL)**, follow these steps:

#### **Update System Packages (Linux)**
```bash
sudo apt update && sudo apt upgrade -y
```

#### **Ensure Python and pip Are Installed**
```bash
sudo apt install python3 python3-pip python3-venv -y
```

#### **Create and Activate a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### **Install Required Dependencies**
```bash
pip install -r requirements.txt
```

For **Windows users (without WSL)**, replace `source venv/bin/activate` with:
```powershell
venv\Scripts\activate
```

### **2. Checking the Setup**
After installation, verify everything is working correctly:
- Check Python version:
  ```bash
  python --version
  ```
- Verify installed dependencies:
  ```bash
  pip list
  ```

## Dataset
The dataset consists of an **Excel file** containing historical records of:
- CO₂ emissions
- GDP per capita
- Urbanization rates
- Industrial production

Data is collected across **European Union** countries from **1960 to 2023**.

## Features and Methodology
### **Data Processing**
- Uses `pandas` for data cleaning and formatting.
- Handles missing values and performs necessary transformations.

### **Exploratory Data Analysis (EDA)**
- Uses `matplotlib` and `seaborn` for visualization.
- Identifies trends and correlations in emissions data.

### **Regression Modeling**
- Implements **linear regression** and **instrumental variable regression** using `statsmodels` and `linearmodels`.
- Examines the impact of energy consumption, industrial production, and urbanization on GDP per capita.

### **Statistical Transformations**
- Uses **quantile transformations** (`sklearn.preprocessing`) to normalize skewed data.

## Usage
### **1. Load the Dataset**
```python
import pandas as pd
df = pd.read_excel("data.xlsx")
df.head()
```

### **2. Perform Exploratory Data Analysis (EDA)**
```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(df)
plt.show()
```

### **3. Run Regression Models**
```python
import statsmodels.api as sm

X = df[["Energy_Consumption", "Urbanization", "Industrial_Production"]]
Y = df["CO2_Emissions"]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())
```

### **4. Interpret Results and Visualize Findings**
- Graphically represent emissions trends over time.
- Identify primary economic drivers of CO₂ emissions.
- Provide policy recommendations.

## Results and Insights
- **Key economic factors influencing CO₂ emissions** are identified.
- **Policy recommendations** are suggested based on empirical findings.
- **Graphs and visualizations** illustrate emission trends over time.

## Contributing
If you would like to contribute:
- Fork the repository.
- Create a feature branch.
- Submit a **pull request** with detailed explanations.

## License
This project is distributed under the **MIT License**, allowing free use, modification, and distribution.

