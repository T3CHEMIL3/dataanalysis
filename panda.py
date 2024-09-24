import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#creating a simple DataFrame
#data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        #City': ['New York', 'Paris', 'Berlin', 'London']}
#df = pd.DataFrame(data)

#print('DataFrame:\n', df)

df = pd.read_csv('vgsales.csv')
#print("First 5 rows of the dataset:\n", df.head())

#view summary statics
#print("Summary statistics:\n", df.describe)

#view column names
#print("column Names:", df.columns)


# filter rows where Rank is greater then 30
#filtered_df = df[df['Rank'] > 30]
#print("Rows where Rank > 30:\n", filtered_df)

#sorting by Name
sorted_df = df.sort_values(by='Name', ascending=False)
print("sorted by Name:\n", sorted_df)

#check for missing values
print("missing values:\n", df.isnull().sum())

#drop rows with missing values
df_cleaned = df.dropna()

#fill missing values with a specific value (e.g., mean or zero)
df_filled = df.fillna(0)


#plot a simple line chart
plt.plot(df['Rank'])
plt.title('Rank Plot')
plt.show()

#create a histogram of Rank column
plt.hist(def['Age'], bins=5)
