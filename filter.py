import pandas as pd

df = pd.read_csv("samp.csv")

filtered_df = df[df["age"] > 25]

sorted_df = df.sort_values(by="age")

grouped_df = df.groupby("city").agg({"age": "mean"})

print("Filtered DataFrame:")
print(filtered_df)

print("Sorted DataFrame:")
print(sorted_df)

print("Grouped DataFrame:")
print(grouped_df)