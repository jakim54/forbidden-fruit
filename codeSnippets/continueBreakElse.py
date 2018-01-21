shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# continue example
for item in shoppingList:
    if item == 'spam':
        print("I am ignoring " + item)
        continue #continue, once finding the match, skips that, and continues

    print("Buy " + item) # this will print everything but spam due to continue

print("") # Spacer

# break example
for item in shoppingList:
    if item == 'spam':
        print("I broke out of the loop because it matched " + item)
        break
    print("Buy " + item)

print("") # Spacer

meal = ["egg", "bacon", "spam", "sausage"]
nasty_food_item = ''

for eachItem in meal:
    if item == 'spam':
        nasty_food_item = item
        break

else:
    print("I'll have a plate of that, then, please.")

if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it?")