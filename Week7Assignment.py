# Task 1: Load and Explore the Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("✅ Dataset loaded successfully.")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")

# Display first few rows
print("\n🔍 First 5 rows:")
print(df.head())

# Check data types and missing values
print("\n📋 Data Types:")
print(df.dtypes)

print("\n🧼 Missing Values:")
print(df.isnull().sum())

# Clean dataset (no missing values in Iris, but here's how you'd handle it)
df.dropna(inplace=True)

# Task 2: Basic Data Analysis

print("\n📊 Basic Statistics:")
print(df.describe())

# Group by species and compute mean of each feature
grouped = df.groupby('species').mean()
print("\n📈 Mean values by species:")
print(grouped)

# Observations
"""
Findings:
- Setosa species has significantly smaller petal length and width.
- Versicolor and Virginica have overlapping sepal lengths but differ in petal dimensions.
"""

# Task 3: Data Visualization

# Set plot style
sns.set(style="whitegrid")

# 1. Line chart (simulated time-series using index)
plt.figure(figsize=(8, 5))
df['petal length (cm)'].plot(kind='line', title='Petal Length Over Samples')
plt.xlabel('Sample Index')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(8, 5))
grouped['petal length (cm)'].plot(kind='bar', color='skyblue', title='Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(8, 5))
df['sepal width (cm)'].plot(kind='hist', bins=20, color='lightgreen', title='Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.tight_layout()
plt.show()

# 4. Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()
