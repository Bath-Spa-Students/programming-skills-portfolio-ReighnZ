''' The code contains a list of names representing individuals, and it uses a loop to generate personalized messages for each person.
Each message begins with "Hello" and addresses the person by their name, then adds "Just wanted to say hi" to each message.
The code prints these personalized messages for each individual in the list. '''

names = ["John", "Lloyd", "Khadijah", "Ifrah"]
for friend in names:
    message = f"Hello, {friend}! Hope you have a great day!"
    print(message)