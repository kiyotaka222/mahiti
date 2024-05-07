import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

model = PCA(n_components=2)
X_r = model.fit_transform(X)

df = pd.DataFrame(data=X_r, columns=["PC1", "PC2"])
df["target"] = y

# Plot the data
plt.figure()
colors = ["navy", "turquoise", "darkorange"]

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        df.loc[df["target"] == i, "PC1"],
        df.loc[df["target"] == i, "PC2"],
        color=color,
        lw=2,
        label=target_name,
    )

plt.title("PCA of IRIS dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()