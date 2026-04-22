import pandas as pd

data = pd.read_csv("D:/Work/Data Analyst/Project/Covid-19 Data Analysis/Covid_19_dataset.csv")

pd.set_option('display.max_columns', None)

print(data)

print(data.count())

print(data.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(data.isnull())
plt.show()

#---Show number of confirmed, deaths and recovered cases in each region.

print(data.groupby('Region').sum().head(10))
print(data.groupby('Region')['Confirmed'].sum().sort_values(ascending= False).head(7))
print(data.groupby('Region')[['Confirmed', 'Recovered']].sum().sort_values('Confirmed' ,ascending= False).head(10))

#---Remove all records where confirmed cases is less than 10.

print(data[data.Confirmed < 10])
print(data[~(data.Confirmed < 10)])
data = data[~(data.Confirmed < 10)]
print(data)

#---In which region, maximum number of confirmed cases were recorded?

print(data.groupby('Region').Confirmed.sum().sort_values(ascending=False).head(7))

#---In which region, minimum number of deaths cases were recorded?

print(data.groupby('Region').Deaths.sum().sort_values(ascending=True).head(29))

#---How many confirmed, deaths & recovered cases were reported from india till 29 april 2020?

print(data['Confirmed','Deaths','Recovered'].Region == 'India'.sort_values(ascii()))
print(data[data.Region == 'India'])

#---Sort entire data wrt no of confirmed cases in ascending order.

print(data.sort_values(by = ['Confirmed'], ascending= True).head(5))

#---Sort entire data wrt no of recovered cases in descending order.

print(data.sort_values(by=['Recovered'], ascending= False))