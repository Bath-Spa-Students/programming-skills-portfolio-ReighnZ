''' This code starts with a list of places to visit and demonstrates various operations on this list.
It includes sorting the list in alphabetical and reverse alphabetical order using sorted(), reversing the list using reverse(), and sorting it in place using sort().
It confirms that the original list order is preserved when these operations are applied and shows the results of each operation. '''

places_to_visit = ["New York", "Tokyo", "Japan", "London", "South Korea"]

print("Original order:", places_to_visit)

print("Alphabetical order:", sorted(places_to_visit))

print("Original order:", places_to_visit)

print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

print("Original order:", places_to_visit)

places_to_visit.reverse()
print("Reversed order:", places_to_visit)

places_to_visit.reverse()
print("Original order:", places_to_visit)

places_to_visit.sort()
print("Alphabetical order:", places_to_visit)

places_to_visit.sort(reverse=True)
print("Reverse alphabetical order:", places_to_visit)