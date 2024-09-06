import pandas as pd
import matplotlib.pyplot as plt

# Load your spending data from a CSV file
data = pd.read_csv('Book1.csv')

# Specify the correct date format (dd-mm-yyyy)
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%Y')

# Calculate total spending over time
data['YearMonth'] = data['Date'].dt.to_period('D')
total_spending_over_time = data.groupby('YearMonth')['Amount'].sum()

# Convert the Period index to strings (e.g., '2023-11')
total_spending_over_time.index = total_spending_over_time.index.strftime('%d-%m')

# Plot a time series of total spending
plt.figure(figsize=(12, 6))
plt.plot(total_spending_over_time.index, total_spending_over_time.values, marker='o')
plt.title('Total Spending Over Time')
plt.xlabel('YearMonth')
plt.ylabel('Total Spending (₹)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Continue with the rest of your data analysis code

# Calculate spending by category
spending_by_category = data.groupby('Category')['Amount'].sum()

# Plot a pie chart of spending by category
plt.figure(figsize=(8, 8))
plt.pie(spending_by_category, labels=spending_by_category.index, autopct='%1.1f%%')
plt.title('Spending by Category')
plt.show()

# Analyze spending trends by category, month, or any other dimension you like

# Example: Monthly spending by category
monthly_spending_by_category = data.pivot_table(index='YearMonth', columns='Category', values='Amount', aggfunc='sum', fill_value=0)

# Plot a stacked bar chart
monthly_spending_by_category.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Monthly Spending by Category')
plt.xlabel('Year-Month')
plt.ylabel('Spending ($)')
plt.xticks(rotation=45)
plt.legend(title='Category')
plt.show()