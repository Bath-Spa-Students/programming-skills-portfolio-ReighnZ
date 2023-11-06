''' This code defines a function called 'make_shirt()' that prints information about a shirt's size and the message to be printed on it.
It can be called with different size and message values, either using positional or keyword arguments.
The code demonstrates two function calls, one with positional arguments and another with keyword arguments, each resulting in the function printing the provided size and message. '''

def make_shirt(size, message):
    print(f"Shirt size: {size}, Message: {message}")

make_shirt("Medium", "Hello!")

make_shirt(size="Large", message="Hi!")