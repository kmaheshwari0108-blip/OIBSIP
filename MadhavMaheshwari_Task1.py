import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\kmahe\Downloads\Task1_Dataset.zip")           
print(df.head())

df.info()                                       #Understand the dataset
df.describe()
df.columns

df.isnull().sum()       # Check for missing values 

df.duplicated().sum()   # Check for duplicate values    

df.duplicated().sum()   # Check for duplicate values

print("Mean = " ,df['Total Amount'].mean())       # Calculate the mean of the 'Total Amount' column
print("Median = " ,df['Total Amount'].median())     # Calculate the median of the 'Total Amount' column
print("Mode = " ,df['Total Amount'].mode()[0])       # Calculate the mode of the 'Total Amount'   
print("Standard Deviation = " ,df['Total Amount'].std())        # Calculate the standard deviation of the 'Total Amount' column

total_sales = df['Total Amount'].sum()        # Calculate the total sales
print("Total Sales = ", total_sales)

avg_sales = df['Total Amount'].mean()        # Calculate the average sales
print("Average Sales = ", avg_sales)

productcategory = df.groupby('Product Category')['Total Amount'].sum()  # Calculate total sales for each product category
productcategory.plot(kind='bar')        # Visualize the total sales for each product category
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')

plt.show()

daily_sales = df.groupby('Date')['Total Amount'].sum()  # Calculate total sales for each date
daily_sales.head()

plt.figure(figsize=(12, 6))
daily_sales.plot(kind='line')        # Visualize the total sales over time
plt.title('Total Sales over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

df['Month_Name'] = pd.to_datetime(df['Date']).dt.month_name()
monthly_sales = df.groupby('Month_Name')['Total Amount'].sum()  # Calculate total sales for each month
monthly_sales.head()

monthly_sales.plot(kind='line',marker = 'o')        # Visualize the total sales for each month
plt.title('Total Sales by Month')
plt.xlabel('Month_Name')
plt.ylabel('Total Sales')
plt.show()

corr  = df.corr(numeric_only=True)        # Calculate the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')        # Visualize the correlation matrix
plt.title('Correlation Matrix')
plt.show()

gender_purchase = df.groupby('Gender')['Total Amount'].mean()  # Calculate total sales for each
print(gender_purchase)

gender_purchase.plot(kind='bar')        # Visualize the total
plt.title('Average Total Amount by Gender')
plt.show()

age_sales = df.groupby('Age')['Total Amount'].mean()  # Calculate total sales for each age group
age_sales.sort_values(ascending=False).head(10)



