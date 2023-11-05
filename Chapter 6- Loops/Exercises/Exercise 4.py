''' This code uses two lists, 'sandwich_orders' and 'finished_sandwiches', to simulate making sandwiches.
It iterates through 'sandwich_orders', processing each order and moving them to 'finished_sandwiches'.
After processing all orders, it prints the list of finished sandwiches. '''

sandwich_orders = ["chicken", "beef", "tuna", "turkey"]
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)