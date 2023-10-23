''' This code starts by inviting a list of initial guests to dinner.
It then acknowledges that one of the guests, Khadijah, can't attend and replaces her with a new guest, Ifrah.
Afterward, it sends out a second round of invitations to the updated list of guests, including the new invitee. '''

guests = ["John", "Lloyd", "Khadijah"]
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner. Please join us!")

guest_cant_make_it = "Khadijah"
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

new_guest = "Ifrah"
guests.remove(guest_cant_make_it)
guests.append(new_guest)

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner. Please join us!")