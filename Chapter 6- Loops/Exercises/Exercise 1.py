''' This code utilizes a while loop to enable the user to input pizza toppings. It continues to prompt the user for toppings until 'quit' is entered.
Each entered topping is acknowledged with a message confirming it will be added to the pizza.
After the user enters 'quit', the code displays the list of selected pizza toppings. '''

toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping == 'quit':
        break
    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)

print("Your pizza will have the following toppings:")
for topping in toppings:
    print(topping)