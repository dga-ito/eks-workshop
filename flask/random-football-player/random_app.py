import csv
import random


def get_random_menu():
    try:
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader) # Skip the header
            data = list(reader) # Convert iterator to list

        if not data:
            return "No data available"

        random_menu = random.choice(data) # Select one random menu

        # Use join to convert the list to a string and strip 
        # to remove leading/trailing whitespace
        final_random_menu = ' '.join(random_menu).strip()

        return final_random_menu
    
    except FileNotFoundError:
        return "The data file was not found"
    except Exception as e:
        return f"An error occurred: {e}"

print(get_random_menu)