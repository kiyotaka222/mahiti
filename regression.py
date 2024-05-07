import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([[7], [9], [11], [13], [15], [17], [19], [21], [23], [25]])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept:", model.intercept_[0])
print("Coefficient:", model.coef_[0][0])

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

plt.scatter(X_test, y_test, color="blue")
plt.plot(X_test, y_pred, color="red")
plt.title("Simple Linear Regression")
plt.xlabel("Independent Variable (X)")
plt.ylabel("Dependent Variable (y)")
plt.show()