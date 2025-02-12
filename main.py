import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/results.csv')

data = data[data['Event']=='400M Men']

# print(data.sort_values('Result'))
print(data['Result'].describe())