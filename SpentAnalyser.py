def split_wallet_money(wallet_money, categories):

  category_amounts = {}
  for category in categories:
    category_amounts[category] = 0

  # Split the wallet money evenly among the categories.
  for i in range(len(categories)):
    for category in categories:
      category_amounts[category] += wallet_money / len(categories)

  # Round the amounts to the nearest integer.
  for category in categories:
    category_amounts[category] = int(round(category_amounts[category]))

  return category_amounts


def main():
  """The main function."""

  wallet_money = 1000
  categories = ["Food", "Transportation", "Housing", "Entertainment", "Other"]

  category_amounts = split_wallet_money(wallet_money, categories)

  # Track the spending over time.
  spending_history = []
  for month in range(1, 13):
    spending_history.append(category_amounts.copy())

  for month, category_amounts in enumerate(spending_history):
    print(f"Month {month}:")
    for category, amount in category_amounts.items():
      print(f"{category}: ${amount}")


if __name__ == "__main__":
  main()