import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\H.P\\Documents\\Book1.csv')

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%Y')

expenditure_categories = ['Grocery', 'Household', 'Bills']

# Calculate total expenditure for each category
category_totals = data.groupby('Category')['Amount'].sum()

plt.figure(figsize=(12, 6))

# Create a pie chart
plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)

plt.title('Pie Chart for Expenditure Categories')
plt.show()

