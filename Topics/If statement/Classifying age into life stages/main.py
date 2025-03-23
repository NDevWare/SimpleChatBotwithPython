# Read the user's age
age = int(input())

# Check the age and print the corresponding category
if age < 18:
    print('Minor')
if age >= 18 and age < 64:
    print('Adult')
if age >= 65:
    print('Senior')