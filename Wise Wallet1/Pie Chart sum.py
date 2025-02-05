import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\H.P\\Documents\\Book1.csv')


data_columns = ['Grocery', 'Household', 'Bills']

fig, axes = plt.subplots(1, len(data_columns) + 1, figsize=(18, 6))

# Loop through each data column and create a pie chart in its respective subplot
for i, column in enumerate(data_columns):
    ax = axes[i]
    ax.pie(data[column], labels=data['Date'], autopct='%1.1f%%', startangle=140)
    ax.set_title(f'Pie Chart for {column}')

total_expenditure = data[data_columns].sum(axis=1)

# Create a pie chart for the total expenditure
ax_total = axes[-1]
ax_total.pie(total_expenditure, labels=data['Date'], autopct='%1.1f%%', startangle=140)
ax_total.set_title('Pie Chart for Total Expenditure')

plt.show()
