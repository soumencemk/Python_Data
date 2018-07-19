import pandas as pd

data = pd.read_csv("data.csv")
# print(data)
# print(data[0:3]['salary'])
#print(data.loc[:, ['salary', 'name']])

#print(data.loc[[1, 3, 5], ['salary', 'name']])

for datum in data:
    print(datum)
