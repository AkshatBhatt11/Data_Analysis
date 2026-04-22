import pandas as pd
import seaborn as ana
import matplotlib.pyplot as plt
from six import assertCountEqual

data = pd.read_excel("D:/Work/Data Analyst/Project/Sales Data Analysis/Sales Data Analysis.xlsx")

pd.set_option('display.max_columns', None)

print(data.head())
print(data.info())

print(data.drop(columns='Unnamed: 0', inplace=True))
#print(data.head())

print(data.loc[0])
data.columns = data.loc[0]
print(data.drop(0, inplace=True))
#print(data.head())

#print(data.Manager)
data['Manager'] = data['Manager'].str.strip().str.replace(r'\s+', ' ', regex=True)
print(data.Manager)

print(data.describe())
print(data[data.duplicated()])
print(data.drop_duplicates(inplace=True))
print(data[data['Order ID'].duplicated()])
print(data[data['Order ID'] == 10485])

#print(data.info())
data.Quantity = data.Quantity.astype(float)
print(data.info())
data.Quantity = data.Quantity.round()
print(data.Quantity)
data.Quantity = data.Quantity.astype(int)
print(data.Quantity)

data['Order ID'] = data['Order ID'].astype(int)
data['Price'] = data['Price'].astype(float)
print(data.info())

data.Date = pd.to_datetime(data.Date)
print(data.info())

#---Most preferred payment method?

print(data['Payment Method'].unique())
print(data['Payment Method'].value_counts(normalize=True)*100)
print(data['Payment Method'].value_counts().plot(kind='bar'))
plt.show()

#---Most selling product? -By Quantity -By Revenue

print(data.groupby('Product')['Quantity'].sum().sort_values(ascending=False))
most_quantity = data.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
most_quantity = most_quantity.reset_index()
print(type(most_quantity))
plt.figure(figsize=(9,4))
plt.bar(most_quantity['Product'],most_quantity['Quantity'])
plt.title('Most selling product')
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.show()

data['Revenue'] = data['Price'] * data['Quantity']
print(data.groupby('Product')['Revenue'].sum().sort_values(ascending=False))
most_revenue = data.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
most_revenue = most_revenue.reset_index()
print(most_revenue)
plt.bar(most_revenue['Product'],most_revenue['Revenue'])
plt.title('Most selling product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()

#---Which city had maximum revenue or Which manager earned maximum revenue.

print(data.City.unique())
print(data.groupby('City')['Revenue'].sum().sort_values(ascending=False))

print(data.Manager.unique())
print(data.groupby('Manager')['Revenue'].sum().sort_values(ascending=False))

#---Data wise revenue.

data.plot('Date','Revenue')
plt.show()

#---Average Revenue.

print(data['Revenue'].mean())

#---Average Revenue of November & December months.

data['Month'] = data['Date'].dt.month
November = data[data['Month'] == 11]
print(November.Revenue.mean())
December = data[data['Month'] == 12]
print(December.Revenue.mean())

#---Standard Devitation of Revenue and Quantity?

print(data['Quantity'].std())
print(data['Revenue'].std())

#---Variance of Revenue and Quantity?

print(data['Quantity'].var())
print(data['Revenue'].var())

#---Is revenue increasing or decreasing over time?

print(November['Revenue'].sum())
print(December['Revenue'].sum())

#---Average 'Quantity Sold' & 'Average Revenue' for each product?

print(data.groupby('Product')[['Quantity', 'Revenue']].agg({'Quantity':'mean', 'Revenue':'mean'}))