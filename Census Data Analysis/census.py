import pandas as pd

data = pd.read_csv("D:/Work/Data Analyst/Project/Census Data Analysis/Census Dataset.csv")

pd.set_option('display.max_columns', None)

print(data.head())

#---How will you hide indexes of dataframe.

print(data.to_string(index=False))

#---How can we set caption/heading on dataframe.

print('India Census Data')
print(data.head())

#---Show records related with districts - New Delhi, Lucknow, Jaipur.

print(data[data['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])])

#---Calculate state-wise: Total number of population | Total no of population with different religions.

print(data.groupby('State_name').Population.sum().sort_values())
Religion = ['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains']
print(data.groupby('State_name')[Religion].sum())

#---How many Male workers were there in Maharashtra state?

print(data[data.State_name == 'MAHARASHTRA'].Male_Workers.sum())

#---How to set column as index of dataframe?

print(data.set_index('District_code'))

#---Add Suffix to column names | Add Prefix to column names.

print(data.add_suffix('_ak'))
print(data.add_prefix('vk_'))