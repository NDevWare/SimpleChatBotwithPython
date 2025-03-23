# Function to convert miles to kilometers

def miles_to_kilometers(miles):
    miles_to_km = miles * 1.60934
    return round(miles_to_km, 2)

# Main program
if __name__ == "__main__":
    miles = float(input())
    result = miles_to_kilometers(miles)
    print(f"{result:.2f}")