import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic supply chain data
np.random.seed(42)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Price': np.random.randint(10, 200, 100),
    'Demand': np.random.randint(50, 500, 100),
    'Supply': np.random.randint(40, 450, 100)
}
df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Histogram of Prices
plt.figure(figsize=(10, 5))
sns.histplot(df['Price'], bins=15, kde=True, color='purple')
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Distribution of Product Prices")
plt.show()

# Heatmap of correlation between features
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Trend Analysis - Line plot of Demand and Supply over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Demand'], label='Demand', color='blue')
plt.plot(df['Date'], df['Supply'], label='Supply', color='red')
plt.xlabel("Date")
plt.ylabel("Quantity")
plt.title("Trend Analysis: Demand vs Supply Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.show()
