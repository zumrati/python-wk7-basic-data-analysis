import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Display first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check for missing values and data types
print("\nData Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset by filling missing values (if any)
# Example: Filling missing values with mean
df = df.fillna(df.mean())

# Task 2: Basic Data Analysis

# Display basic statistics for numerical columns
print("\nBasic Statistics of Numerical Columns:")
print(df.describe())

# Group by the species and compute the mean for each species
grouped_data = df.groupby('species').mean()
print("\nGrouped Data by Species (Mean of Numerical Columns):")
print(grouped_data)

# Task 3: Data Visualization

# Line chart: Plotting a trend over time (Example using a time-series if available)
# For Iris dataset, we don't have time-series data, but you can adjust this section based on your data.
# For this example, we'll skip the line chart because the Iris dataset doesn't contain time data.

# Bar chart: Compare average petal length across species
plt.figure(figsize=(8, 6))
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=0)
plt.show()

# Histogram: Distribution of petal length
plt.figure(figsize=(8, 6))
df['petal length (cm)'].hist(bins=20, color='lightgreen')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Relationship between sepal length and petal length
plt.figure(figsize=(8, 6))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], color='purple', label='Sepal vs Petal')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Customize plots: Adding labels, legends, and colors for clarity
# Example of customizing scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], color='blue', label='Sepal vs Petal')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()
