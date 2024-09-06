import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\H.P\\Documents\\Book1.csv')

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%Y')

expenditure_categories = ['Grocery', 'Household', 'Bills']

# Calculate total expenditure for each category
category_totals = data.groupby('Category')['Amount'].sum()

plt.figure(figsize=(12, 6))

# Create a bar graph
category_totals.plot(kind='bar', color='skyblue')

plt.xlabel('Expenditure Category')
plt.ylabel('Total Expenditure')
plt.title('Bar Graph for Expenditure Categories')
plt.xticks(rotation=0)
plt.show()
