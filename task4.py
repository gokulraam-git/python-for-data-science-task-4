import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("retail_data.csv")

print(df.head())

print("\nStatistical Summary:")
print(df.describe())

total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

highest_profit = df.loc[df["Profit"].idxmax()]
print("\nHighest Profit Product:")
print(highest_profit)

print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

plt.figure(figsize=(7,5))
sns.barplot(x="Product", y="Sales", data=df)

plt.title("Product vs Sales")
plt.xticks(rotation=30)
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x="Sales", y="Profit", data=df)

plt.title("Sales vs Profit")
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True)

plt.title("Correlation Heatmap")
plt.show()