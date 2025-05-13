# ---------------------------------------
# Importing Libraries
# ---------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

# ---------------------------------------
# Task 1: Load and Explore the Dataset
# ---------------------------------------
try:
    # Load the iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Dataset structure
    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    # No missing values in this dataset, so no cleaning needed
except Exception as e:
    print(f"Error loading dataset: {e}")

# ---------------------------------------
# Task 2: Basic Data Analysis
# ---------------------------------------
print("\nBasic statistics:")
print(df.describe())

# Group by species and compute mean
grouped = df.groupby("species").mean()
print("\nMean values per species:")
print(grouped)

# Interesting observation example:
print("\nObservation: Setosa has significantly shorter petals than Versicolor and Virginica.")

# ---------------------------------------
# Task 3: Data Visualization
# ---------------------------------------
sns.set(style="whitegrid")

# 1. Line Chart (not time-series but comparing average measurements)
grouped.T.plot(kind='line', marker='o')
plt.title("Average Measurements by Species")
plt.xlabel("Measurement Type")
plt.ylabel("Value (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()

# 2. Bar Chart
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram
plt.hist(df['sepal width (cm)'], bins=10, edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# ---------------------------------------
# Conclusion / Observations
# ---------------------------------------
"""
Findings:
- Setosa has the smallest petal length and width among all species.
- Virginica tends to have the largest petal measurements.
- There’s a strong positive correlation between sepal length and petal length.
- Sepal width has a normal-like distribution centered around 3 cm.

This basic analysis demonstrates the power of pandas and matplotlib for data exploration.
"""
