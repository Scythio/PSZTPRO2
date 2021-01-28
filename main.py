import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

train_data = pd.read_csv("trainWineRed.csv",sep=';')
test_data = pd.read_csv("testWineRed.csv",sep=';')


average = sum(train_data["quality"]) / len(train_data["quality"])

print(average)

wine_parameters = ["fixed acidity","volatile acidity","citric acid",
                   "residual sugar","chlorides","free sulfur dioxide",
                   "total sulfur dioxide","density","pH","sulphates","alcohol"]

Y = train_data.iloc[:,-1]
X = train_data.iloc[:,:-1]

Y = train_data.iloc[:,-1]
X = train_data.iloc[:,:-1]

# X=[]
# for wp in wine_parameters:
#     X.append(list(train_data[wp]))
# X = list(map(list, zip(*X)))

# print(X)

regressor = DecisionTreeRegressor(criterion="mse",min_samples_leaf=5)
regressor.fit(X, Y)

Y_pred = regressor.predict(X)
Y_pred = np.round(Y_pred,0)

print(Y_pred - Y)



def F(data):
    return d0

def calculate_residuum(data, model):
    return 0

def calculate_gamme():
    return 0

#initialization
d0 = average
M=10

for m in list(range(M)):
    print(m)















