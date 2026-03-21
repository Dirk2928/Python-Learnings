total_confirmations = 10
guest_count = 0

# Count confirmations using a while loop
while guest_count < total_confirmations:
    guest_count += 1
    print(guest_count, "guests so far!")

print("We have", guest_count, "guests coming!")

total_ingredients = 7
ingredients_checked = 0

# Set up the loop
while ingredients_checked < total_ingredients:
    # Increment the counter
    ingredients_checked += 1
    # Check if less than 4 ingredients reviewed
    if ingredients_checked < 4:
        print("More than half remaining")
    # Check if 6 or fewer ingredients reviewed
    elif ingredients_checked <= 6:
        print("Nearly finished checking")
    else:
        print("All ingredients verified!")

