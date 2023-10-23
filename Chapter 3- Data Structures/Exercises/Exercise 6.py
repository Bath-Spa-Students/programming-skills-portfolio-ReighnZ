''' This code manages a guest list for a dinner, considers a change in the table size, and maintains a list with two invited guests.
It sends sorry messages to guests who can't attend and clears the list at the end. '''

guests = ["John", "Lloyd", "Khadijah"]

guest_cant_make_it = "Khadijah"
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

new_guest = "Ifrah"
guests.remove(guest_cant_make_it)
guests.append(new_guest)

print("I can invite only two people for dinner.\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

guests.clear()