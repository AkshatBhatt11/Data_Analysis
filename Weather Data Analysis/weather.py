import pandas as pd

data = pd.read_csv("D:/Work/Data Analyst/Data/Weather Dataset.csv")

#print(data)

#print(data.head(10))

#print(data.shape)

#print(data.index)

#print(data.columns)

#print(data.dtypes)

#print(data['Weather'].unique())

#print(data.nunique())

#print(data.count())

#print(data['Weather'].value_counts())

#print(data.info)

#################################
#Q-1. Find all unique 'Wind Speed' values in the data.
#print(data.head(2))

#print(data.nunique())

#print(data['Wind Speed_km/h'].nunique())

#print(data['Wind Speed_km/h'].unique())
#################################
#Q-2. Find the number of times when the 'Weather is exactly clear'.

#print(data.Weather.value_counts())

#print(data[data.Weather == 'Clear'])

#print(data.groupby('Weather').get_group('Clear'))
#################################
#Q-3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.

#print(data[data['Wind Speed_km/h'] == 4])
#################################
#Q-4. Find out all the Null Values in the data.

#print(data.isnull().sum())

#print(data.notnull().sum())
#################################
#Q-5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

#print(data.rename(columns= {'Weather': 'Weather Condition'}))

#print(data.rename(columns= {'Weather': 'Weather Condition'}, inplace= True))
#################################
#Q-6. What is the mean 'Visibility'.

#print(data.Visibility_km.mean())
#################################
#Q-7. What is the Standard Deviation of 'Pressure' in this data?

#print(data.Press_kPa.std())
#################################
#Q-8. What is the Variance of 'Relative Humidity' in this data?

#print(data['Rel Hum_%'].var())
#################################
#Q-9. Find all instances when 'Snow' was recorded.

#print(data[data['Weather']  == 'Snow'])

#print(data[data['Weather'].str.contains('Snow')])
#################################
#Q-10. Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

#print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])
#################################
#Q-11. What is the Mean value of each column against each 'Weather Condition'.
#print(data.head(2))
########print(data.groupby('Weather').mean())
#################################
#Q-12. What is the Minimum & Maximum value of each column against each 'Weather Condition'.

#print(data.groupby('Weather').min().head(5))
#print(data.groupby('Weather').max().head(5))
#################################
#Q-13. Show all the Records where Weather Condition is Fog.

#print(data[data['Weather'] == 'Fog'])
#################################
#Q-14. Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
#print(data.head(5).all())
########print(data[(data['Weather'] == 'Clear') or (data['Visibility_km'] > 40)].head(5))
#################################
#Q-15. Find all instances when:
#A. 'Weather is Clear' and 'Relative Humidity is greater that 50'.
#B. 'Visibility is baove 40'.

########print([(data['Weather'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibilily_km'] > 40)])