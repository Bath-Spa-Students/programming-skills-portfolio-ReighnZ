''' This code uses a loop to ask the user for their age continuously until they choose to exit by typing 'quit.'
It calculates the cost of a movie ticket based on their age, with free tickets for ages under 3, $10 tickets for ages between 3 and 12, and $15 tickets for ages 13 and older.
The program informs the user of the ticket price and continues the process until they decide to quit. '''

while True:
    age = input("Please enter your age (or type 'quit' to exit): ")
    
    if age == 'quit':
        break
    
    age = int(age)
    
    if age < 3:
        print("Your ticket is free.")
    elif age >= 3 and age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")