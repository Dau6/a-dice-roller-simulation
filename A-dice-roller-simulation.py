import random
from prettytable import PrettyTable

def roll_dice():
    random_number = random.uniform(0, 1)
    
    if random_number < 1/6:
        return 1
    elif random_number < 2/6:
        return 2
    elif random_number < 3/6:
        return 3
    elif random_number < 4/6:
        return 4
    elif random_number < 5/6:
        return 5
    else:
        return 6

def simulate_rolls(num_rolls):
    results = [roll_dice() for _ in range(num_rolls)]
    return results

def calculate_percentage(frequency, total_rolls):
    return (frequency / total_rolls) * 100

# Simulate rolling a six-sided die 1000 times
num_rolls = 1000
dice_rolls = simulate_rolls(num_rolls)

# Count face frequencies using if statements
face_frequencies = [0, 0, 0, 0, 0, 0]
for roll in dice_rolls:
    face_frequencies[roll - 1] += 1

# Create a table to display the results
table = PrettyTable()
table.field_names = ["Face", "Frequency", "Percentage"]

# Populate the table with results
total_percentage = 0
for face in range(1, 7):
    frequency = face_frequencies[face - 1]
    percentage = calculate_percentage(frequency, num_rolls)
    total_percentage += percentage
    table.add_row([face, frequency, f"{percentage:.2f}%"])

# Add a row for totals
table.add_row(["Total", sum(face_frequencies), f"{total_percentage:.2f}%"])

# Print the table
print(table)
