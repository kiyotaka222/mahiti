import pandas as pd

data = pd.read_csv("data32.csv")
categorical_features = data.select_dtypes(include="object")
dummies = pd.get_dummies(categorical_features)
data = pd.concat([data, dummies], axis=1)
data.drop(categorical_features, axis=1, inplace=True)
data.to_csv("Output1.csv")