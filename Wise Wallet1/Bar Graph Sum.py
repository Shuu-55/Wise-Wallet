import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\H.P\\Desktop\\Wise Wallet\\Book1.csv')

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%Y')

expenditure_categories = ['Grocery', 'Household', 'Bills']

plt.figure(figsize=(10, 6))

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

total_expenditure = data[expenditure_categories].sum(axis=1)

plt.bar(
    [pos + len(expenditure_categories) * bar_width for pos in x],  # Shift the bars for the total
    total_expenditure,
    width=bar_width,
    label='Total Expenditure',
    color='black',
)

# Set the x-axis labels
plt.xlabel('Date')
plt.ylabel('Expenditure')
plt.title('Bar Chart')
plt.xticks(
    [pos + ((len(expenditure_categories) + 1) * bar_width / 2) for pos in x],  # Shift the labels for the total
    data['Date'],
    rotation=45,
)
plt.legend()  
plt.grid(axis='y')  
plt.tight_layout()  
plt.show()
