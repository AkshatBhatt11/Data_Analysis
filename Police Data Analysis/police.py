import pandas as pd

data = pd.read_csv("D:/Work/Data Analyst/Data/Police Dataset.csv")

pd.set_option('display.max_columns', None)

#print(data)

#---Remove column that only contain missing values
#print(data.isnull().sum())
#print(data.drop(columns='country_name', inplace=True))

#---For speeding, were Men or Women stopped more often?
#print(data[data.violation == 'Speeding'].driver_gender.value_counts())

#---Does gender affect who gets searched during a stop?
#print(data.search_conducted.value_counts())
#print(data.groupby('driver_gender').search_conducted.sum())

#---What is the mean stop_duration?
#data['stop_duration'] = data['stop_duration'].map({'0-15 Min' : 7.5, '16-30 Min': 24, '30+ Min': 45})
#print(data.head())
#print(data['stop_duration'].mean())

#---Compare age distributions for each violation
#print(data.groupby('violation').driver_age.describe())