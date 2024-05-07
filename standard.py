import pandas as pd
from sklearn.preprocessing import Normalizer, StandardScaler

print("printing few data")
df = pd.read_csv("SampleFile.csv")
print(df.head())

print("Normalization")
scaler = Normalizer()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_df.head())

print("Standardization")
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_df.head())