import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("D:/Work/Data Analyst/Project/Netflix Data Analysis/Netflix Dataset.csv")

pd.set_option('display.max_columns', None)

print(data.head()) #top 5 record

print(data.tail()) #botton 5 record

print(data.shape) #total row and column

print(data.size) #total element

print(data.columns) #print column names

print(data.dtypes) #print datatypes of column

print(data.info()) #info about data frame

#---Check any duplicate record and remove that duplicate record.

print(data[data.duplicated()])
print(data.drop_duplicates(inplace=True))

#---Check null value in column and show on heat-map.

print(data.isnull().sum())
sns.heatmap(data.isnull())
plt.show()

#---For 'House of Cards', what is show Id and who is Director of this show?

print(data[data['Title'].isin(['House of Cards'])])
print(data[data['Title'].str.contains('House of Cards')])

#---In which year highest number of TV shows & Movies were released? Show with Bar Graph.

#print(data.dtypes)
data['Release_Date'] = data['Release_Date'].str.strip()
data['Date_N'] = pd.to_datetime(data['Release_Date'], format='mixed', errors='coerce')
print(data['Date_N'].dt.year.value_counts())
data['Date_N'].dt.year.value_counts().plot(kind='bar')
plt.show()

#---How many Movies & TV Shows are in dataset? Show with Bar Graph.

print(data.groupby('Category').Category.count().plot(kind='bar'))
plt.show()

#---Show all Movies that were released in year 2000.

data['Year'] = data['Date_N'].dt.year
print(data[(data['Category'] == 'Movie') & (data['Year'] == 2020)])

#---Show only Titles of all TV Shows that were released in India only.

print(data[(data['Category'] == 'TV Show') & (data['Country'] == 'India')]['Title'])

#---Show Top 10 Directors, who gave highest number of TV Shows & Movies to Netflix?

print(data['Director'].value_counts().head(10))

#---Show all Records, where 'Category is Movie and Type is Comedies' or 'Country is United Kingdom'.

print(data[ (data['Category'] == 'Movie') & (data['Type'] == 'Comedies') | (data['Country'] == 'United Kingdom') ])

#---In how many movies/shows, Tom Cruise was cast?

print(data[(data['Cast'] == 'Tom Cruise')])
print(data[data['Cast'].str.contains('Tom Cruise')])

data_new = data.dropna()
print(data_new.head())
print(data_new[data_new['Cast'].str.contains('Tom Cruise')])

#---What are different Ratings defined by Netflix?

print(data['Rating'].unique())

#---How many Movies got 'TV-14' rating, in Canada?

print(data[ (data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada') ].shape)

#---How many TV Show got 'R' rating, after year 2018?

print(data[ (data['Category'] == 'TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018) ])

#---What is maximum duration of Movie/Show on Netflix?

print(data.Duration.unique())
data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand=True)
print(data['Minutes'].max())
print(data['Minutes'].min())

#---Which individual country has Highest No. of TV shows?

data_tvshow = data[data['Category'] == 'TV Show']
print(data_tvshow.Country.value_counts().head(1))

#---How can we sort dataset by Year?

print(data.sort_values('Year', ascending=False).head(5))

#---Find all Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' and Type is 'Kids TV'

print(data[ (data['Category'] == 'Movie') & (data['Type'] == 'Dramas') | (data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV") ].head(3))
