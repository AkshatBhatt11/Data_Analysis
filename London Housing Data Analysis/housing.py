import pandas as pd

data = pd.read_csv("D:/Work/Data Analyst/Project/London Housing Data Analysis/Housing Dataset.csv")

pd.set_option('display.max_columns', None)

print(data.count())

print(data.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(data.isnull())
plt.show()

#---1.Convert datatype of 'Date' column to Data-Time format.

data.date = pd.to_datetime(data.date)
print(data.dtypes)

#---2.Add new column 'Year' in dataframe, which contain years only.

data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
print(data.head(5))

#---3.Add new column 'Month' as 2nd column in dataframe, which contain months only.

data['date'] = pd.to_datetime(data['date'])
data.insert(2, 'month', data['date'].dt.month)
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year
print(data.head(5))

#---4.Remove column 'Year' and 'Month' from dataframe.

data.drop(['month','year'], axis=1, inplace=True)

#---5.Show all records where 'No of Crimes' is 0. And, how many such records are there?

print(data[data.no_of_crimes == 0])
print(len(data[data.no_of_crimes == 0]))

#---6.What is maximum & minimum 'Average_price' per year in england?

data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
print(data[data.area == 'england'])

print(data.groupby('year').average_price.max())
print(data.groupby('year').average_price.min())

#---7.What is maximum & minimum 'No of Crimes' recorded per area?

print(data.groupby('area').no_of_crimes.max())
print(data.groupby('area').no_of_crimes.max().sort_values(ascending=True))

#---8.Show total counts of records of each area, where average price is less than 100000.

print(data[data.average_price < 100000].area.value_counts())