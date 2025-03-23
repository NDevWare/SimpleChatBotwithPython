# Read the initial deposit
initial_deposit = int(input())

# Set the interest rate and the protected amount
interest_rate = 1.071
protected_amount = 700000

# Initialize variables
deposit = initial_deposit
years = 0

# Loop until the deposit exceeds the protected amount
while deposit <= protected_amount:
    # Increase the deposit by the interest rate
    deposit *= interest_rate
    # Increase the year count
    years += 1

# Print the number of years
print(years)
