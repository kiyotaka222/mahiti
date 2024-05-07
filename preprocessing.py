import pandas as pd

# Reading CSV file into DataFrame
df = pd.read_csv("samp.csv")
print("Our dataset:")
print(df)

# Reading JSON file into DataFrame
data = pd.read_json("sample.json")
print(data)

# Filling missing values with 0
print("Dataset after filling NA values with 0:")
df2 = df.fillna(value=0)
print(df2)

# Dropping rows with any missing values
print("Dataset after dropping NA values:")
df.dropna(inplace=True)
print(df)