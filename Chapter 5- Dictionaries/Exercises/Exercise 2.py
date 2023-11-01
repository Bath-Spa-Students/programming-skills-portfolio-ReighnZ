''' This code creates a dictionary called 'programming_glossary' that contains programming terms as keys and their explanations as values.
It then uses a loop to go through each term and its definition in the dictionary and prints them in an organized format.
This code helps present programming concepts and their meanings clearly. '''

programming_glossary = {
    "Variable": "Stores data or information.",
    "Function": "A named block of code that can be reused.",
    "If Statement": "Executes code conditionally.",
    "Loop": "Repeats a set of instructions.",
    "List": "An ordered collection of items"
}

for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")