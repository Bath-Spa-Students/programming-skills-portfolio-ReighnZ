''' This code uses a dictionary to connect river names with the countries they pass through.
It then employs loops to print sentences about each river and its corresponding country, lists the river names, and lists the countries separately.
This code demonstrates the effective use of dictionaries to manage related data and how to access and display that data using loops. '''

rivers = {
    "Nile": "Egypt",
    "Pasig River": "Philippines",
    "Shinano River": "Japan"
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers:")
for river in rivers.keys():
    print(river)

print("\nCountries:")
for country in rivers.values():
    print(country)