import pandas as pd
import matplotlib.pyplot as plt

# Example Time Series Data (Replace with real data)
data = {
    "Month": pd.date_range(start="2023-01", periods=12, freq="M"),
    "Sales": [100, 120, 150, 170, 160, 180, 200, 220, 250, 270, 260, 280]
}

df = pd.DataFrame(data)

# Plot Trend Line
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Sales"], marker="o", linestyle="-", color="b", label="Sales Trend")

# Customize
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Trend Analysis")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Show Plot
plt.show()
