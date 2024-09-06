import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv('C:\\Users\\H.P\\Documents\\Book1.csv')

# List of data columns you want to create pie charts for
data_columns = ['Groceries', 'Household']

# Create a single figure with subplots for each data column
fig, axes = plt.subplots(1, len(data_columns), figsize=(15, 6))

# Loop through each data column and create a pie chart in its respective subplot
for i, column in enumerate(data_columns):
    ax = axes[i]
    ax.pie(data[column], labels=data['Date'], autopct='%1.1f%%', startangle=140)
    ax.set_title(f'Pie Chart for {column}')

# Display all pie charts at the same time
plt.show()
