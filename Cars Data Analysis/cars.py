import pandas as pd

car = pd.read_csv("D:/Work/Data Analyst/Project/Cars Data Analysis/Cars Dataset.csv")

pd.set_option('display.max_columns', None)

print(car.head(5))
print(car.shape)

#---Find all null values in dataset.

print(car.isnull().sum())

#---Fill all null values with mean of that column.

print(car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True))

print(car['Cylinders'] == car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True))

print(car.isnull().sum())

#---Check what are difference types of make are there in our dataset and count of each make in data

print(car['Make'].value_counts())

#---Show all records where Origin is asia or europe.

print(car[car['Origin'].isin(['Asia','Europe'])])

#---Remove all records (rows) where weigth is above 4000.

print(car[~(car['Weight'] > 4000)])

#---Increase all values of 'MPG_City' column by 3.

print(car['MPG_City'] == car['MPG_City'].apply(lambda x:x+3))