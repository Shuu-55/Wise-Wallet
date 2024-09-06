import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv('C:\\Users\\H.P\\Documents\\Book1.csv')

# List of expenditure categories you want to create line charts for
expenditure_categories = ['Groceries', 'Household']

# Create a single figure for all line charts
plt.figure(figsize=(12, 6))

# Loop through each expenditure category and create a line chart
for category in expenditure_categories:
    plt.plot(data['Date'], data[category], marker='o', linestyle='-', label=category)

plt.xlabel('Date')
plt.ylabel('Expenditure')
plt.title('Line Chart')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()  # Add a legend to differentiate categories
plt.show()