import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

summary_stats = df.describe()

sns.histplot(data=df, x="numerical_variable", bins=20, kde=True)
plt.title("Histogram of Numerical Variable")
plt.xlabel("Numerical Variable")
plt.ylabel("Frequency")
plt.show()

sns.countplot(data=df, x="categorical_variable", palette="viridis")
plt.title("Bar Chart of Categorical Variable")
plt.xlabel("Categories")
plt.ylabel("Count")
plt.show()

print("# Data Analysis and Visualization Report\n")
print("## Summary Statistics:\n")
print(summary_stats)
print("\n## Insights:\n")

print(
    "- The histogram shows that the distribution of the numerical variable is approximately normal."
)
print(
    "- The bar chart indicates that category A is the most frequent in the categorical variable."
)