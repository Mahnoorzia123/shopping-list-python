# Create an empty list to store shopping items
Shopping_list = []

# Ask the user how many items they want to add
n = int(input("How many items do you want to add? "))

# Use a loop to take input for each item
for i in range(n):
    # Ask the user to enter each item one by one
    item = input(f"Enter item{i+1}: ")
    # Add (append) the item to the shopping list
    Shopping_list.append(item)

# Print the final shopping list
print("Your shopping list:", Shopping_list)