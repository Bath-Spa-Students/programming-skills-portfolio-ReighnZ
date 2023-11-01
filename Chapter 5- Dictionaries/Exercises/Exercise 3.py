''' This code defines a dictionary named programming_glossary that stores programming terms and their meanings.
It then uses a for loop to iterate through the dictionary, printing each programming term followed by its definition.
The code demonstrates the use of dictionaries to organize information and showcases how to display this information in an organized manner using a loop. '''

programming_glossary = {
    "Variable": "Stores data or information.",
    "Function": "A named block of code that can be reused.",
    "If Statement": "Executes code conditionally.",
    "Loop": "Repeats a set of instructions.",
    "List": "An ordered collection of items.",
    "Print": "Displays text or values on the screen.",
    "Comment": "Explanatory text in your code for people.",
    "Dictionary": "A data structure that stores key-value pairs.",
    "Integer": "A whole number without a decimal point.",
    "String": "A sequence of characters or text.",
}

for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")