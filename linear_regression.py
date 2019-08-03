import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


# x = np.array([5, 15, 25, 35, 45, 55,65,75,85,95,105]).reshape((-1, 1))
x = pd.read_csv('exported_data.csv', usecols = ["score"])
x = np.array(x)

y = np.array(pd.read_csv('exported_data.csv', usecols = ["len_title"]))

# y = np.array([5, 20, 14, 32, 22, 38,12,20,34,60,90])

# print(x)


model = LinearRegression().fit(x, y.reshape((-1, 1)))

r_sq = model.score(x, y)

print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

y_pred = model.predict(x)

print('predicted response:', y_pred, sep='\n')

plt.scatter(x, y,  color='black')
plt.plot(x, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())
plt.xlabel('Reddit score')
plt.ylabel('Length of meme text')
plt.show()

