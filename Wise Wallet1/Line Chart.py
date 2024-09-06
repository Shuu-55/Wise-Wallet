import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\H.P\\Documents\\Book1.csv')

data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%Y')

expenditure_categories = ['Grocery', 'Household', 'Bills']

plt.figure(figsize=(12, 6))

# Loop through each expenditure category and create a line chart
for category in expenditure_categories:
    plt.plot(data.loc[data['Category'] == category, 'Date'], data.loc[data['Category'] == category, 'Amount'],
             marker='o', linestyle='-', label=category)

plt.xlabel('Date')
plt.ylabel('Expenditure')
plt.title('Line Chart')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()  
plt.show()