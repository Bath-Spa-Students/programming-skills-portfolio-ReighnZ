''' This code defines a function called 'describe_city' that takes a city name and an optional country name (defaulting to "Philippines").
It prints a sentence stating the city's location in the specified or default country. The function is then called with different cities and, in some cases, a different country.
The output displays sentences indicating the cities' locations. '''

def describe_city(city, country="Philippines"):
    print(f"{city} is in {country}.")

describe_city("Manila")
describe_city("Tokyo", "Japan")
describe_city("New York", "USA")