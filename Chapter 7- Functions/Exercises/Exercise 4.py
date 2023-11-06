''' This code defines a function called 'make_shirt()' that creates custom shirt descriptions.
The function accepts two parameters: 'size' and 'message', with default values of "large" and "I love Python," respectively.
It demonstrates creating shirts with different sizes and messages, allowing customization while providing default values if no specific arguments are given. '''

def make_shirt(size="large", message="I love Python"):
    print(f"Shirt size: {size}, Message: {message}")

make_shirt()
make_shirt("medium")
make_shirt("small", "Python is fun!")