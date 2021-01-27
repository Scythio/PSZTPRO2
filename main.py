import pandas as pd

train_data = pd.read_csv("trainWineRed.csv",sep=';')
test_data = pd.read_csv("testWineRed.csv",sep=';')


average = sum(train_data["quality"]) / len(train_data["quality"])

print(average)