''' This code determines a person's stage of life based on their age using an if-elif-else chain.
In this specific case, with an age of 20, it identifies the person as a teenager because the age falls within the range defined for that category.
The code does not evaluate the remaining conditions once it finds a matching one. '''

age = 20

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")