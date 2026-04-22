import pandas as pd

data = pd.read_csv("D:/Work/Data Analyst/Data/Udemy Dataset.csv")

pd.set_option('display.max_columns', None)

#print(data.head())

#---What are all different subject for which Udemy is offering courses?
#print(data.subject.unique())

#---Which subject has maximum number of courses.
#print(data.subject.value_counts())

#---Show all courses which are Free of Cost.
#print(data[data.is_paid == False])

#---Show all courses which are Paid.
#print(data[data.is_paid == True])

#---Which are top selling courses?
#print(data.sort_values('num_subscribers', ascending=False))

#---Which are least selling courses?
#print(data.sort_values('num_subscribers'))

#---Show all courses of Graphic Design where price is below 100?
#data['price'] = data['price'].astype(int)
#print(data[(data.subject == "Graphic Design") & (data.price == '100')])

#---List out all courses that are related with 'Python'.
#print(data[data.course_title.str.contains('Python')])

#---What are courses that published in year 2015?
#data['published_timestamp'] = pd.to_datetime(data.published_timestamp)
#data['Year'] = data['published_timestamp'].dt.year
#print(data[data.Year == 2015])

#---What are Max. number of subscribes for each level of courses?
#print(data.groupby('level')['num_subscribers'].max())
#print(data.groupby('level').max())
