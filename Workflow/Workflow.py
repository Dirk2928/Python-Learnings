# Create an empty shopping list
shopping_list = []

# Loop through each ingredient and required quantity
for ingredient, required_qty in recipe.items():
    # Check if we need more than what we have
    if required_qty > pantry_stock[ingredient]:
        # Add the ingredient to our shopping list
        shopping_list.append(ingredient)

# Display the shopping list
print("Shopping list:", shopping_list)

shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    # Calculate the amount needed for the party
    needed_amount = amount * scale_factor
    
    # Check if we need to buy this ingredient
    if ingredient not in pantry or needed_amount > pantry[ingredient]:
        shopping_list.append(ingredient)

print("Shopping list for your party:")
print(shopping_list)