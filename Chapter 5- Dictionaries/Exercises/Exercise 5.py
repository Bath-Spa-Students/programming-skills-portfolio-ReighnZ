''' This code creates a list of dictionaries, each representing a pet and its owner.
The dictionaries store information about the type of animal ("kind") and the name of the owner ("owner"). The code then uses a for loop to iterate through the list, printing details about each pet, including its kind and the owner's name.
Information for each pet is separated by newline characters, ensuring a well-organized presentation of the data. '''

pet1 = {"kind": "Dog", "owner": "Anthony"}
pet2 = {"kind": "Cat", "owner": "David"}
pet3 = {"kind": "Rabbit", "owner": "Jess"}
pet4 = {"kind": "Hamster", "owner": "Sophia"}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner's name: {pet['owner']}")
    print()