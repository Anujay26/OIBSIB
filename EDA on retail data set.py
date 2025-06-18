import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#DATA LOADING AND CLEANING
df = pd.read_csv("retail_sales_dataset.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

#DESCRIPTIVE STATISTICS
df.dropna(inplace=True)
print(df.describe())
print(df.mode().iloc[0])
print(df.duplicated().sum())
df=df.drop_duplicates()
mean_values = df[['Age','Quantity','Price per Unit','Total Amount']].mean()
print("Mean:\n", mean_values)
median_values = df[['Age','Quantity','Price per Unit','Total Amount']].median()
print("Median:\n", median_values)
mode_values = df[['Age','Quantity','Price per Unit','Total Amount']].mode()
print("Mode:\n", mode_values)
std_values = df[['Age','Quantity','Price per Unit','Total Amount']].std()
print("Standard Deviation:\n", std_values)

#TIME SERIES ANALYSIS
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
monthly_sales = df['Total Amount'].resample('M').sum()
monthly_sales.plot(figsize=(10, 5), title='Monthly Sales Trend')
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

#CUSTMER AND PRODUCT ANALYSIS
top_customers = df.groupby('Customer ID')['Total Amount'].sum().sort_values(ascending=False)
print(top_customers.head(10))
purchase_freq = df['Customer ID'].value_counts()
print(purchase_freq.head(10))

plt.figure(figsize=(8, 4))
sns.histplot(data=df, x='Age', bins=10, kde=False)
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.show()

gender_sales = df.groupby('Gender')['Total Amount'].sum()
gender_count = df['Gender'].value_counts()
print("Sales by Gender:\n", gender_sales)
print("Customer Count by Gender:\n", gender_count)
gender_sales.plot(kind='bar', title='Total Sales by Gender', color=['salmon', 'skyblue'])
plt.ylabel("Total Sales")
plt.show()

top_categories = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
print(top_categories)
qty_per_category = df.groupby('Product Category')['Quantity'].sum().sort_values(ascending=False)
print(qty_per_category)
avg_price_per_category = df.groupby('Product Category')['Price per Unit'].mean().sort_values(ascending=False)
print(avg_price_per_category)
top_categories.plot(kind='bar', title='Top Product Categories by Sales', color='teal')
plt.ylabel("Total Amount")
plt.xlabel("Product Category")
plt.xticks(rotation=45)
plt.show()



