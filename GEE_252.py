# ==============================
# Problem 1: Variables and Data Types
# ==============================
print("=== Problem 1 ===")

market_name = "Balogun Market"
num_traders = 5000
location_coords = (6.4541, 3.3947)
is_open_sundays = False

print("Market:", market_name, ", Type:", type(market_name))
print("Traders:", num_traders, ", Type:", type(num_traders))
print("Coordinates:", location_coords, ", Type:", type(location_coords))
print("Open Sundays:", is_open_sundays, ", Type:", type(is_open_sundays))

total_revenue = 25000000
average_revenue = total_revenue / num_traders
print("Average Daily Revenue per Trader:", average_revenue, "Naira")


# ==============================
# Problem 2: Lists and Basic Operations
# ==============================
print("\n=== Problem 2 ===")

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]

# Add Ivory Coast
host_countries.append("Ivory Coast")

# Insert Morocco at position 1
host_countries.insert(1, "Morocco")

# Remove Senegal
host_countries.remove("Senegal")

# Total number of countries
print("Total countries:", len(host_countries))

# Alphabetical order (without modifying original)
print("Alphabetical order:", sorted(host_countries))

# Every second country
print("Every second country:", host_countries[::2])


# ==============================
# Problem 3: Dictionaries
# ==============================
print("\n=== Problem 3 ===")

river_data = {
    "Nile": {"length_km": 6650, "countries": 11},
    "Congo": {"length_km": 4700, "countries": 9},
    "Niger": {"length_km": 4180, "countries": 5}
}

# Add Zambezi
river_data["Zambezi"] = {"length_km": 2574, "countries": 6}

# Update Niger countries
river_data["Niger"]["countries"] = 6

# Print river names
print("Rivers:", river_data.keys())

# Congo countries
print("Congo flows through:", river_data["Congo"]["countries"], "countries")

# Total length
total_length = 0
for river in river_data:
    total_length += river_data[river]["length_km"]

print("Total river length:", total_length, "km")


# ==============================
# Problem 4: Loops
# ==============================
print("\n=== Problem 4 ===")

# Part A: For loops

# Multiplication table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")

# Print letters in AFRICA
for letter in "AFRICA":
    print(letter)

# Sum of even numbers 1 to 50
sum_even = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i

print("Sum of even numbers:", sum_even)

# Part B: While loops

# Countdown from 20 to 1
count = 20
while count >= 1:
    print(count)
    count -= 1

# First number > 500 divisible by 3 and 7
num = 501
while True:
    if num % 3 == 0 and num % 7 == 0:
        print("First number > 500 divisible by 3 and 7:", num)
        break
    num += 1


# ==============================
# Problem 5: Conditional Statements
# ==============================
print("\n=== Problem 5 ===")

def classify_rainfall(mm):
    if mm > 300:
        return "Flood Risk"
    elif 200 <= mm <= 300:
        return "Heavy Rain"
    elif 100 <= mm <= 199:
        return "Moderate Rain"
    elif 1 <= mm <= 99:
        return "Light Rain"
    elif mm == 0:
        return "Dry"

# Test cases
tests = [350, 250, 150, 50, 0]

for t in tests:
    print(f"{t}mm:", classify_rainfall(t))


# ==============================
# Problem 6: Functions
# ==============================
print("\n=== Problem 6 ===")

# Part A
def calculate_exchange(amount, rate):
    return amount * rate

print("Exchange:", calculate_exchange(100, 1580))


# Part B
def format_price(amount, currency="NGN"):
    return f"{currency} {amount:,}"

print(format_price(5000))
print(format_price(200, "GHS"))


# Part C
def analyze_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    average = sum(scores) / len(scores)
    return lowest, highest, average

scores = [55, 72, 88, 61, 94, 47, 79]

low, high, avg = analyze_scores(scores)

print("Lowest:", low)
print("Highest:", high)
print("Average:", avg)1