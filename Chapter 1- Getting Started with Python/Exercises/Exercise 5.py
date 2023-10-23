''' The program requests the user to provide the radius of a circle, presenting the message "Enter the radius of the circle:".

User input is obtained through the input() function, which captures the user's response as a string.

To facilitate mathematical operations, the program converts the user's input (originally a string)
into a floating-point number using float().

The program computes the circle's area using the formula: area = π * radius^2, where π (pi) is approximately 3.14159265359.

The calculated area is presented to the user, along with the message "The area of the circle is:", followed by the computed value. '''

radius = float(input("Enter the radius of the circle: "))
area = 3.14159265359 * (radius ** 2)
print("The area of the circle is:", area)