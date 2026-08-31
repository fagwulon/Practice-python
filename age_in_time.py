age = int(input("Enter age in years: "))

# Assumptions:
# 1 year = 12 months
# 1 month = 4 weeks
# 1 week = 7 days
# Therefore, 1 year = 52 weeks and 365 days

months = age * 12
weeks = age * 52
days = age * 365

print(f"\nYou are approximately:\n")
print(f"\nYou are {months} months old")
print(f"\nYou are {weeks} weeks old")
print(f"\nYou are {days} days old")