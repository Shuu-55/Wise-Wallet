import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv('C:\\Users\\H.P\\Documents\\Book1.csv')

# List of expenditure categories you want to create bar charts for
expenditure_categories = ['Groceries', 'Household']

# Create a single figure for all bar charts
plt.figure(figsize=(10, 6))

# Calculate the width of each bar
bar_width = 0.35

# Create an index for the x-axis labels (dates)
x = range(len(data['Date']))

# Loop through each expenditure category and create a bar chart
for i, category in enumerate(expenditure_categories):
    plt.bar(
        [pos + i * bar_width for pos in x],  # Shift the bars for each category
        data[category],
        width=bar_width,
        label=category,
    )

# Set the x-axis labels
plt.xlabel('Date')
plt.ylabel('Expenditure')
plt.title('Bar Chart')
plt.xticks([pos + (len(expenditure_categories) - 1) * bar_width / 2 for pos in x], data['Date'], rotation=45)
plt.legend()  # Add a legend to differentiate categories
plt.grid(axis='y')  # Add a grid to the y-axis (optional)
plt.tight_layout()  # Ensure labels and titles are not cut off
plt.show()
