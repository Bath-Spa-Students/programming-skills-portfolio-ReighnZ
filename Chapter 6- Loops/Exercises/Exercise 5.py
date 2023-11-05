''' This code manages sandwich orders in a deli. It accounts for the situation where the deli has run out of pastrami sandwiches.
It removes all instances of "pastrami" from the sandwich orders list, ensuring no pastrami sandwiches are made.
Then, it processes the remaining orders and lists the finished sandwiches. '''

sandwich_orders = ["chicken", "pastrami", "beef", "pastrami", "tuna", "turkey", "pastrami"]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)