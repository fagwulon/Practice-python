# This program just returns a normal comprehension.

# This is for list
prices = [4.00, 3.00, 5.00]
taxed_prices = [p * 1.10 for p in prices]
print(taxed_prices)
# The terminal outputs a new list with 10% tax added to each price.

# This is for set
messy_names = ['LATTE', 'Espresso', 'Latte', 'EsPresSO']
unique_clean = {name.lower() for name in messy_names}
print(unique_clean)
# The output displays {'latte', 'espresso'} with all duplicates removed.

# This is for dictionary.
stock = {"cups": 100, "lids": 150}
doubled_stocks = {item: count * 2 for item, count in stock.items()}
# Note: We use .items() on our source dictionary to extract both the keys and values simultaneously during iteration.
print(doubled_stocks)
# The output {'cups': 200, 'lids': 300}; the quantities are doubled


# This program doesn't use the list, set or dictioary comprehension to filter the values as usual
# It's a ternary operator, uses if-else conditions.
# So this conditions go in front of the for loop statement
sizes = ["Large", "Large", "Small", "Medium", "Small", "Tiny"]

# This prints a dictionary
size_package = {x: 'Premium' if x == 'Large' else 'Regular' for x in sizes}

# This prints a list for the comprehension

size_package1 = ['Premium' if x == 'Large' else 'Regular' for x in sizes]


# This prints for a set

size_package2 = {'Premium' if x == 'Large' else 'Regular' for x in sizes}

# For this one the output is just 2 values; ('Premium, 'Regular')
# As set doesn't allow duplicate value

print(size_package)
print(size_package1)
print(size_package2)
