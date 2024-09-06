import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\H.P\\Documents\\Book1.csv')

expenditure_categories = ['Grocery', 'Household', 'Bills']

plt.figure(figsize=(12, 6))

# Loop through each expenditure category and create a line chart
for category in expenditure_categories:
    plt.plot(data['Date'], data[category], marker='o', linestyle='-', label=category)


total_expenditure = data[expenditure_categories].sum(axis=1)


plt.plot(data['Date'], total_expenditure, marker='o', linestyle='-', label='Total Expenditure', color='black')

plt.xlabel('Date')
plt.ylabel('Expenditure')
plt.title('Line Chart')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()  # Add a legend to differentiate categories
plt.show()
